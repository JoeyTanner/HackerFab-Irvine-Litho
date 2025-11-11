#!/cygdrive/c/Python27/python
# ******************************************************************************
# 
#   Copyright (c) 2019 Texas Instruments
# 
# ******************************************************************************/
# 
#  Command support for the BOOTLOADER.
#  
# ******************************************************************************

import sys
import time
import os
import array
from cStringIO import StringIO
import re


from command_handler.core.core import *
import command_handler.core.utils as utils
from command_handler.destination.bootloader import *
from command_handler.destination.sharedapp import *
from command_handler.destination.projector_control import *
from command_handler.phy.cypress import *

class ProgramMode:
    BOOTLOADER = 0x00
    APPLICATION = 0x01

class SectorData:
    def __init__(self, sector_info, flash_cksum = None):
        self.info = sector_info
        self.flash_cksum = flash_cksum
        self.file_data = None

    def set_file_data(self, file_data):
        self.file_data = file_data
        self.file_cksum = self._compute_checksum()
    
    def _compute_checksum(self):
        simple = 0;
	sumofsum = 0;
        num_bytes = len(self.file_data)
        for i in xrange(0, num_bytes):
            simple = (simple + self.file_data[i]) & 0xFFFFFFFF
            sumofsum = (sumofsum + simple) & 0xFFFFFFFF
        # Account for partial sector write
        while num_bytes < self.info.size:
            simple = (simple + 0xFF) & 0xFFFFFFFF
            sumofsum = (sumofsum + simple) & 0xFFFFFFFF
            num_bytes += 1
        return FlashChecksum(simple, sumofsum)

    def __str__(self):
        return str(self.info)
            
class Projector:

    FLASH_TABLE_SIGNATURE = [0xF7, 0xA5, 0x47, 0xAB, 0x7E, 0x51, 0x62, 0xA7]

    def __init__(self, phy, use_seq, use_len, use_checksum):
        self.phy = phy
        self.use_seq = use_seq
        self.use_len = use_len
        self.use_checksum = use_checksum

        # initialize all destination classes
        self.bl = Bootloader(self.phy, self.use_seq, self.use_len, self.use_checksum)
        self.sa = SharedApp(self.phy, self.use_seq, self.use_len, self.use_checksum)
        self.pc = ProjectorControl(self.phy, self.use_seq, self.use_len, self.use_checksum)

    def _init_program_mode(self):

        cypress_connected = False
        # First read mode to see which application we are in.
        self.initial_mode = mode = self.sa.cmd_get_app_mode()
        print("Current mode {0}".format(mode))
        if self.initial_mode == None or not self.initial_mode.is_bootloader:
            if self._cy_hold_boot(True):
                cypress_connected = True
                mode = self.sa.cmd_get_app_mode()
            else:
                utils.print_and_flush("Switching to BOOTLOADER via shared command...\r\n")
                if self.sa.cmd_switch_mode(ProgramMode.BOOTLOADER):
                    elapsed = 0
                    start_time = time.time()
                    while elapsed < 20:
                        elapsed = time.time() - start_time
                        mode = self.sa.cmd_get_app_mode()
                        if mode is not None and mode.is_bootloader:
                            break

        if not mode.is_bootloader:
            utils.print_error("ERROR: Switching to BOOTLOADER mode failed.\r\n")
            return False, cypress_connected

        self.flash_id = self.bl.cmd_get_flash_id()
        sector_info = self.bl.cmd_get_flash_sector_info()
        self.sector_data = []
        for sector in sector_info.sectors:
            self.sector_data.append(SectorData(sector, None))
            #utils.print_and_flush("{0}\r\n".format(sector))

        return True, cypress_connected

    def _end_program_mode(self, cypress_connected):
        if self.initial_mode.is_bootloader:
            return True
        
        if cypress_connected:
            self._cy_hold_boot(False)
        mode = self.sa.cmd_get_app_mode()
        if mode == None:
            utils.print_error("ERROR: Reading mode after reset failed")
            return False
        # if we are still in bootloader, that means boot hold flag is active.
        if mode.is_bootloader:
            return self.sa.cmd_switch_mode(ProgramMode.APPLICATION)

        return True

    def _cy_hold_boot(self, hold):
        # Check if cypress is connected
        try:
            cy = Cypress()
            if cy.connect():
                if hold:
                    utils.print_and_flush("Switching to BOOTLOADER via GPIO...\r\n")
                # set the gpio boot hold line
                cy.gpio([6], [hold == False])
                # now modulate power good and posense for asic reset
                # power down and then power up:
                cy.gpio([2, 5], [0, 0])
                cy.gpio([2, 5], [1, 1])
                time.sleep(0.5)
                return True
            else:
                utils.print_error("ERROR: Cypress is not connected 1")
                return False
        except Exception as e:
            utils.print_error("ERROR: Cypress is not connected: {0}".format(e))
            return False

    def _program_flash(self, sectors, partial = True):
        if partial:
            # read the sector wise checksum information from flash, but only till end of file
            for sector in sectors:
                sector.flash_cksum = self.bl.cmd_get_flash_checksum(sector.info.address, sector.info.size)

        # Choose only the sectors marked for download

        sectors = [item for item in sectors if item.file_data != None
                                                and (item.flash_cksum == None 
                                                    or item.flash_cksum.simple != item.file_cksum.simple 
                                                    or item.flash_cksum.sumofsum != item.file_cksum.sumofsum)]
        download_size = sum([len(item.file_data) for item in sectors])

        # Download identified sectors
        num_sectors = len(sectors)
        if num_sectors == 0:
            utils.print_and_flush("No sectors changed. Flash sectors up to date.\r\n")
            return True
        else:
            utils.print_and_flush("No of sectors to download = {0}\r\n".format(num_sectors))
            utils.print_and_flush("Total download size = {0} bytes\r\n".format(download_size))
        
        """
        utils.print_and_flush("Sectors to download\r\n")
        for i in xrange(0, num_sectors):
            sector = sectors[i]
            utils.print_and_flush("{0}  {1}  {2}\r\n".format(sector.info, sector.flash_cksum, sector.file_cksum))
        return True
        """
        
        size = 0
        # unlock flash
        self.bl.cmd_set_flash_unlock(True)
        for i in xrange(0, num_sectors):
            sector = sectors[i]
            sector_str = "0x{0:08X}".format(sector.info.address)
            utils.print_and_flush("Updating sector {0}...\r\n".format(sector_str))
            self.bl.cmd_flash_erase(sector.info.address)

            # set the flash address and size
            self.bl.cmd_init_flash_read_write(sector.info.address, len(sector.file_data))
            size += self.bl.cmd_flash_write(sector.file_data, True)

            checksum = self.bl.cmd_get_flash_checksum(sector.info.address, sector.info.size)
            if checksum.simple != sector.file_cksum.simple or checksum.sumofsum != sector.file_cksum.sumofsum:
                utils.print_error("ERROR: Programming failed for sector {0} - Checksum error {1}  {2}.".format(sector_str, checksum, sector.file_cksum))
                return False

        utils.print_and_flush("Programmed {0} bytes\r\n".format(size))
        return True

    def program_flash_binary(self, download_file, partial=True, skip_boot_size_kb=128):
        """
        Programs a flash binary to the connected system by sending all appropriate commands.
        """
        
        returnval, cypress_connected = self._init_program_mode()
        if returnval == False:
            return False

        # Break the file into sectors so that we can split and compute the sector wise checksum
        with open(download_file, 'rb') as df:
            file_data = bytearray(df.read())
        
        file_size = len(file_data)
        # skip boot sectors if set to do so.
        # Also skip sectors larger than the file size
        boot_end_address = skip_boot_size_kb * 1024
        sectors_involved = [item for item in self.sector_data if item.info.address >= boot_end_address
                                                            and item.info.address <= file_size]
        for sector in sectors_involved:
            start_addr = sector.info.address
            end_addr = start_addr + sector.info.size
            sector.set_file_data(file_data[start_addr:end_addr])
        
        if self._program_flash(sectors_involved, partial) != True:
            return False

        return self._end_program_mode(cypress_connected)

    def program_app_binary(self, download_file, partial=True, flash_table_addr=0x20000, app_addr=0x25000):
        """
        Programs given application binary to the connected system by sending all appropriate commands.
        """

        returnval, cypress_connected = self._init_program_mode()
        if returnval == False:
            return False

        # Break the file into sectors so that we can split and compute the sector wise checksum
        with open(download_file, 'rb') as df:
            file_data = bytearray(df.read())
        
        file_size = len(file_data)
        # Merge flash signature and file to a single binary starting at flash table addr
        merged_data = Projector.FLASH_TABLE_SIGNATURE 
        merged_data += [0xFF] * (app_addr - flash_table_addr - len(Projector.FLASH_TABLE_SIGNATURE)) 
        merged_data += file_data

        # identify the sector which has flash_table_addr
        flash_table_sector = None 
        prev_sector = self.sector_data[0]
        for i in xrange(1, len(self.sector_data)):
            if self.sector_data[i].info.address > flash_table_addr:
                flash_table_sector = prev_sector
                break
            prev_sector = self.sector_data[i]

        # extend the data to start at the identified flash table sector
        if flash_table_sector.info.address != flash_table_addr:
            merged_data = ([0xFF] * flash_table_addr - flash_table_sector.info.address) + merged_data

        end_addr = flash_table_sector.info.address + len(merged_data)
        sectors_involved = [item for item in self.sector_data if item.info.address >= flash_table_sector.info.address
                                                            and item.info.address < end_addr]
        for sector in sectors_involved:
            start_addr = sector.info.address - flash_table_sector.info.address
            end_addr = start_addr + sector.info.size
            sector.set_file_data(merged_data[start_addr:end_addr])
        
        if self._program_flash(sectors_involved, partial) != True:
            return False

        return self._end_program_mode(cypress_connected)

    def get_emulation_fw_version(self):
        """
        Returns emulation firmware version in Major, Minor
        """

        value = 0
        # First read the application mode
        app_mode = self.sa.cmd_get_app_mode()
        value = self.sa.cmd_memory(0x4000D010)

        major = (value >> 8) & 0xFFFF
        minor = value & 0xFF
        build_type = (value >> 28) & 0xF

        return major, minor, build_type
