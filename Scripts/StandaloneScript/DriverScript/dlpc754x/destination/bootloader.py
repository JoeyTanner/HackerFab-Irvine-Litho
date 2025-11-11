#!/cygdrive/c/Python27/python
# ******************************************************************************
# 
#   Copyright (c) 2018 Texas Instruments
# 
# ******************************************************************************/
# 
#  Command support for the BOOTLOADER.
#  
# ******************************************************************************

import sys
import os
import array
from cStringIO import StringIO

from command_handler.core.core import *
import command_handler.core.utils as utils

############################### General classes ################################
class FlashId:
    def __init__(self, manf_id, dev_id):
        self.manf_id = manf_id
        self.dev_id = dev_id

    def __str__(self):
        msg = "  - Manufacturer ID = 0x{0:04X}\r\n" + \
              "  - Device ID       = 0x{1:016X}\r\n"
        return msg.format(self.manf_id, self.dev_id);

class FlashSectorInfo:

    class SectorGroup:
        def __init__(self, sector_size, num_sectors):
            self.sector_size = sector_size
            self.num_sectors = num_sectors

    class SectorInfo:
        def __init__(self, sector_base_address, sector_size):
            self.address = sector_base_address
            self.size = sector_size

        def __str__(self):
            fmt_str = "0x{0:08X}   {1:>5} bytes"
            return fmt_str.format(self.address, self.size)

    def __init__(self, sector_grp_arr):
        self.sectors = []
        addr = 0
        for i in xrange(0, len(sector_grp_arr)):
            size = sector_grp_arr[i].sector_size
            num_sectors = sector_grp_arr[i].num_sectors
            for j in xrange(0, num_sectors):
                sector = FlashSectorInfo.SectorInfo(addr, size)
                self.sectors.append(sector)
                addr += size

    def __str__(self):
        sect_info = StringIO()
        for sector in self.sectors:
            sect_info.write(str(sector) + "\r\n")
        return sect_info.getvalue()

class FlashChecksum:
    def __init__(self, simple, sumofsum):
        self.simple = simple
        self.sumofsum = sumofsum

    def __str__(self):
        return "0x{0:08X}{1:08X}".format(self.simple, self.sumofsum)


################################## Bootloader ##################################
class Bootloader:
    
    DESTINATION_VALUE = 1
    NUM_CMD_BYTES = 1

    def __init__(self, phy, use_seq, use_len, use_checksum):
        self.tx_header = TxHeader(Bootloader.DESTINATION_VALUE, Bootloader.NUM_CMD_BYTES, use_seq, use_len, use_checksum)
        self.phy = phy

    class CommandId:
        FLASH_ID = 0x20
        FLASH_SECTOR_INFO = 0x21
        FLASH_UNLOCK = 0x22
        FLASH_ERASE = 0x23
        FLASH_INIT_RW = 0x24
        FLASH_RW = 0x25
        FLASH_CHECKSUM = 0x26

    #################   BASIC COMMANDS  #######################################
    def cmd_get_flash_id(self):
        cmd = Command(Bootloader.CommandId.FLASH_ID, self.tx_header)
        response = cmd.read(self.phy, 10)

        if not utils.check_response_and_print_error(response, True, "Flash ID"):
            return None

        manf_id = response.get_int(2)
        dev_id_lsv = response.get_int(4)
        dev_id_msv = response.get_int(4)
        dev_id = dev_id_lsv | (dev_id_msv << 32)

        flash_id = FlashId(manf_id, dev_id)
        return flash_id

    def cmd_get_flash_sector_info(self):
        cmd = Command(Bootloader.CommandId.FLASH_SECTOR_INFO, self.tx_header)
        response = cmd.read(self.phy, 65535)

        if not utils.check_response_and_print_error(response, True, "Flash Sector Info"):
            return None

        sector_grp_arr = []
        addr = 0
        num_info = response.length / 6
        for i in xrange(0, num_info):
            size = response.get_int(4)
            num_sector = response.get_int(2)
            sector_grp = FlashSectorInfo.SectorGroup(size, num_sector)
            sector_grp_arr.append(sector_grp)

        flash_sector_info = FlashSectorInfo(sector_grp_arr)
        return flash_sector_info

    def cmd_set_flash_unlock(self, unlock):
        cmd = Command(Bootloader.CommandId.FLASH_UNLOCK, self.tx_header)
        if unlock:
           cmd.put_int(4, 0xF7A54027)
        else:
           cmd.put_int(4, 0x0)
        response = cmd.write(self.phy, True)

        if not utils.check_response_and_print_error(response, False, "Flash Unlock"):
            return False
        return True

    def cmd_get_flash_unlock(self):
        cmd = Command(Bootloader.CommandId.FLASH_UNLOCK, self.tx_header)
        response = cmd.read(self.phy, 1)

        if not utils.check_response_and_print_error(response, True, "Flash Unlock"):
            return None

        unlocked = response.get_int(1)
        return (unlocked == 1)

    def cmd_init_flash_read_write(self, flash_addr, size):
        cmd = Command(Bootloader.CommandId.FLASH_INIT_RW, self.tx_header)
        cmd.put_int(4, flash_addr)
        cmd.put_int(4, size)
        response = cmd.write(self.phy, True)
        if not utils.check_response_and_print_error(response, False, "Flash RW Init"):
            return False
        return True

    def cmd_flash_write(self, byte_arr, print_progress=False):
        """ 
        Ensure appropriate unlock, erase and init flash read write commands are called before this function.

        Returns:
            (int) - Num Bytes written
        """
        max_size = 512
        size = len(byte_arr)
        rem_bytes = size
        chunk_size = max_size
        start_index = 0
        while rem_bytes > 0:
            chunk_size = min(max_size, rem_bytes)

            cmd = Command(Bootloader.CommandId.FLASH_RW, self.tx_header, True)
            cmd.put_arr(byte_arr[start_index:start_index + chunk_size])
            response = cmd.write(self.phy, True, 5)
            if not utils.check_response_and_print_error(response, False, "Flash Write"):
                return size - rem_bytes

            if print_progress:
                sys.stdout.write("Programming {0}%...\r".format((size-rem_bytes)*100 // size))
                sys.stdout.flush()
            start_index += chunk_size
            rem_bytes -= chunk_size
            #print("rem = {0}".format(rem_bytes))
        return size

    def cmd_flash_read(self, size):
        read_data = []
        return_val = True

        while len(read_data) < size:
            cmd = Command(Bootloader.CommandId.FLASH_RW, self.tx_header)
            cmd.put_int(2, 50)
            response = cmd.read(self.phy, 65535, 5)
            if not utils.check_response_and_print_error(response, True, "Flash Read"):
                break
            read_data += response.get_arr(response.length)

        return read_data

    def cmd_flash_erase(self, sector_addr):
        """ Flash unlock shall be called before calling this function """
        cmd = Command(Bootloader.CommandId.FLASH_ERASE, self.tx_header)
        cmd.put_int(4, sector_addr)
        response = cmd.write(self.phy, True, 2)
        if not utils.check_response_and_print_error(response, False, "Flash Erase"):
            return False
        return True

    def cmd_get_flash_checksum(self, flash_addr, size):
        cmd = Command(Bootloader.CommandId.FLASH_CHECKSUM, self.tx_header)
        cmd.put_int(4, flash_addr)
        cmd.put_int(4, size)
        response = cmd.read(self.phy, 8, 5)
        if not utils.check_response_and_print_error(response, True, "Flash Checksum"):
            return 0
        
        simple_checksum = response.get_int(4)
        sum_of_sum_checksum = response.get_int(4)

        return FlashChecksum(simple_checksum, sum_of_sum_checksum)
