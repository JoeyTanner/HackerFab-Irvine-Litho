#!/cygdrive/c/Python27/python
# ******************************************************************************
# 
#   Copyright (c) 2018 Texas Instruments
# 
# ******************************************************************************/
# 
#  This script stores various helper utilities for other code to use.
#  
# ******************************************************************************


from __future__ import print_function
import sys
import string

import DriverScript.core.core as core

_debug = False
_error_count = 0

def print_error(*args, **kwargs):
    """ Call this to print a message to STDERR"""
    print(*args, file=sys.stderr, **kwargs)
    sys.stderr.flush()

def enable_debug(enable):
    global _debug
    _debug = enable

def is_debug():
    global _debug
    return _debug

def print_and_flush(*args, **kwargs):
    sys.stdout.write(*args, **kwargs)
    sys.stdout.flush()

def debug_print(*args, **kwargs):
    global _debug
    if _debug:
        print(*args, **kwargs)
        sys.stdout.flush()

def reset_error_count():
    global _error_count
    _error_count = 0

def get_error_count():
    global _error_count
    return _error_count

def check_response_and_print_error(response, is_read_cmd, cmd_name):
    global _error_count

    cmd_type = "Write"
    if is_read_cmd:
        cmd_type = "Read"
    
    if response == False:
        print_error("ERROR: {0} {1} failed.".format(cmd_type, cmd_name))
        _error_count += 1
        return False
        
    if response == True:
        return True

    if response.header == None:
        print_error("ERROR: {0} {1} failed. Response packet is None ".format(cmd_type, cmd_name))
        _error_count += 1
        return False

    if response.header.nack:
        print_error("ERROR: {0} {1} failed with error code : {2} ({3})"
                        .format(cmd_type, cmd_name, core.Command.ErrorCodeStr[response.error_code], response.error_code))
        _error_count += 1
        return False

    if not response.checksum_valid:
        error_str = "ERROR: {0} {1} failed due to checksum mismatch.\r\n" + \
                    "       Received checksum = 0x{2:02X}\r\n" + \
                    "       Computed checksum = 0x{3:02X}"
        print_error(error_str.format(cmd_type, cmd_name, response.checksum, response.computed_checksum))
        _error_count += 1
        return False

    return True

def byte_array_to_hex_str(byte_arr):
    return "[{0}]: {1}".format(len(byte_arr), map(lambda val: "{0:02X}h".format(val), byte_arr))
        

def print_in_bin_notation(byte_arr, start_addr = 0, group_size = 2):
    addr_fmt = "{0:08x}: "
    data_fmt = ""
    if group_size == 1:
        single_fmt = "{{{0}:02x}} "
        for i in xrange(1, 17):
            data_fmt += single_fmt.format(i)
    elif group_size == 4:
        single_fmt = "{{{0}:02x}}{{{1}:02x}}{{{2}:02x}}{{{3}:03x}} "
        for i in xrange(1, 17, 4):
            data_fmt += single_fmt.format(i, i+1, i+2, i+3)
    else: # all other options default to group size 2
        group_size = 2
        single_fmt = "{{{0}:02x}}{{{1}:02x}} "
        for i in xrange(1, 17, 2):
            data_fmt += single_fmt.format(i, i+1)

    fmt_str = addr_fmt + data_fmt + " {17}"
    i = 0
    rem_len = len(byte_arr)
    addr = start_addr
    while rem_len >= 16:
        char_str = ""
        for j in xrange(0, 16):
            if (chr(byte_arr[i + j]) in string.printable) and not (chr(byte_arr[i + j]) in string.whitespace):
                char_str += "{0:c}".format(byte_arr[i+j])
            else:
                char_str += "."
        print(fmt_str.format(addr, 
            byte_arr[i],
            byte_arr[i + 1],
            byte_arr[i + 2],
            byte_arr[i + 3],
            byte_arr[i + 4],
            byte_arr[i + 5],
            byte_arr[i + 6],
            byte_arr[i + 7],
            byte_arr[i + 8],
            byte_arr[i + 9],
            byte_arr[i + 10],
            byte_arr[i + 11],
            byte_arr[i + 12],
            byte_arr[i + 13],
            byte_arr[i + 14],
            byte_arr[i + 15], char_str))

        i += 16
        rem_len -= 16
        addr += 16

    if i < len(byte_arr):
        last_line = addr_fmt.format(addr)
        char_str = ""
        while i < len(byte_arr):
            data_str = "{0:02x}".format(byte_arr[i])
            if (chr(byte_arr[i]) in string.printable) and not (chr(byte_arr[i]) in string.whitespace):
                char_str += "{0:c}".format(byte_arr[i])
            else:
                char_str += "."
            i += 1
            last_line += data_str
            if group_size == 1 or (group_size == 2 and (i % 2 == 0)) or (i % 4 == 0):
                last_line += " "
        
        # Now print the line
        print("{0:51}{1}".format(last_line, char_str))



    

