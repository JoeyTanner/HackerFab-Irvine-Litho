#!/cygdrive/c/Python27/python
# ******************************************************************************
# 
#   Copyright (c) 2018 - 2019 Texas Instruments
# 
# ******************************************************************************/
# 
#  Command support for the Shared commands that are available in Bootloader
#  and application SW.
#  
# ******************************************************************************

import sys
import os
import array
from cStringIO import StringIO

from command_handler.core.core import *
import command_handler.core.utils as utils

############################### General classes ################################
class AppMode:
    def __init__(self, mode_byte):
        self.is_bootloader = mode_byte & 0x1 == 0
        self.is_application = mode_byte & 0x1 == 1
        self.is_dual_controller = mode_byte & 0x2 != 0
        self.is_formatter_only = mode_byte & 0x4 != 0

    def __str__(self):
        str1 = ""
        str2 = "Bootloader"
        if self.is_dual_controller:
            str1 = "Dual Controller " 
        if self.is_application:
            str2 = "Main Application"
            if self.is_formatter_only:
                str2 = "Formatter Only Application"
        return "{0} {1}".format(str1, str2).strip()

class AppVersion:
    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __str__(self):
        #return "v0x{0:02X}.0x{1:02X}.0x{2:04X}".format(self.major, self.minor, self.patch)
        return "v{0}.{1}.{2}".format(self.major, self.minor, self.patch)


################################## Shared App ##################################
class SharedApp:
    
    DESTINATION_VALUE = 1
    NUM_CMD_BYTES = 1

    def __init__(self, phy, use_seq, use_len, use_checksum):
        self.tx_header = TxHeader(SharedApp.DESTINATION_VALUE, SharedApp.NUM_CMD_BYTES, use_seq, use_len, use_checksum)
        self.phy = phy

    class CommandId:
        APP_MODE = 0x00
        APP_VER = 0x01
        SWITCH_MODE = 0x02
        MEMORY = 0x10
        MEMORY_ARR = 0x11

    #################   BASIC COMMANDS  #######################################
    def cmd_get_app_mode(self):
        cmd = Command(SharedApp.CommandId.APP_MODE, self.tx_header)
        response = cmd.read(self.phy, 1)

        if not utils.check_response_and_print_error(response, True, "Application Mode"):
            return None

        mode_val = response.get_int(1)
        app_mode = AppMode(mode_val)
        return app_mode

    def cmd_switch_mode(self, mode_to_switch_to):
        cmd = Command(SharedApp.CommandId.SWITCH_MODE, self.tx_header)
        cmd.put_int(1, mode_to_switch_to)
        cmd.write(self.phy, False)
        time.sleep(10)
        return True

    def cmd_memory(self, address, value = None):
        cmd = Command(SharedApp.CommandId.MEMORY, self.tx_header)
        cmd.put_int(4, address)
        if value is None:
            response = cmd.read(self.phy, 4)
            if not utils.check_response_and_print_error(response, True, "Memory read"):
                return None
            value = response.get_int(4)
        else:
            cmd.put_int(4, value)
            cmd.write(self.phy, False)
        return value

    def cmd_memory_array(self, start_address, auto_increment, bytes_per_word, data = None):
        chunk_words = 480/bytes_per_word
        if not isinstance(data, list):
            num_words = data
            rem_words = num_words
            data = []
            while rem_words > 0:
                cmd = Command(SharedApp.CommandId.MEMORY_ARR, self.tx_header)
                cmd.put_int(4, start_address)
                cmd.put_int(1, auto_increment)
                numwords = min(chunk_words, rem_words)
                cmd.put_int(2, numwords)
                cmd.put_int(1, bytes_per_word)
                response = cmd.read(self.phy, 65535)
                if not utils.check_response_and_print_error(response, True, "Memory Read Array"):
                    break
                #print 'recieved {0} bytes'.format(response.length)
                for i in range(0, response.length/bytes_per_word):
                    data.append(response.get_int(bytes_per_word))
                rem_words -= response.length/bytes_per_word
                if auto_increment:
                    start_address = start_address + numwords * bytes_per_word
        
            return data
            
        else:
            num_words = len(data)
            rem_words = num_words
            start_index = 0
            while rem_words > 0:
                cmd = Command(SharedApp.CommandId.MEMORY_ARR, self.tx_header)
                cmd.put_int(4, start_address)
                cmd.put_int(1, auto_increment)
                numwords = min(chunk_words, rem_words)
                cmd.put_int(2, numwords)
                cmd.put_int(1, bytes_per_word)
                for value in data[start_index:start_index+numwords]:
                    cmd.put_int(bytes_per_word, value)

                response = cmd.write(self.phy, 65535)
                if not utils.check_response_and_print_error(response, True, "Memory Write Array"):
                    return (num_words - rem_words)
                rem_words -= numwords
                start_index += chunk_words
                if auto_increment:
                    start_address = start_address + numwords * bytes_per_word
                
            return num_words
        
    def cmd_get_version(self):
        cmd = Command(SharedApp.CommandId.APP_VER, self.tx_header)
        response = cmd.read(self.phy, 4)

        if not utils.check_response_and_print_error(response, True, "Application Version"):
            return None

        major = response.get_int(1)
        minor = response.get_int(1)
        patch = response.get_int(2)
        version = AppVersion(major, minor, patch)
        return version

