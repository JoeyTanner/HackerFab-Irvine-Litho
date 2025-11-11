#!/cygdrive/c/Python27/python
# ******************************************************************************
#
#   Copyright (c) 2019 Texas Instruments
#
# ******************************************************************************/
#
#  This script is the core implementation of the unified command protocol. The
#  various classes in this script allows for easily creating a command with
#  proper bytes, transmit it over a physical layer and receive the response
#  data. It also allows for easy unpacking of the response data read from
#  the system.
#
#  See details of new protocol here:
#  https://confluence.itg.ti.com/display/DDP75SW/Command+Protocols
#
#  See documentation and sample usage of these test scripts here:
#  TODO LAZ 2018/01/06 Add confluence page for scripts
#
# ******************************************************************************

import sys
import time

from DriverScript.core.physical_layer import PhyType
import DriverScript.core.utils as utils

class TxHeader:

    def __init__(self, destination, num_cmd_bytes, use_seq, use_len, use_checksum):
        self.destination = destination & 0x7
        self.use_seq = use_seq
        self.use_len = use_len
        self.use_checksum = use_checksum

        self.num_cmd_bytes = num_cmd_bytes
        self.byte = self.destination
        if self.use_seq:
            self.byte |= 1 << 3
        if self.use_len:
            self.byte |= 1 << 4
        if self.use_checksum:
            self.byte |= 1 << 5

        self.set_seq_range(1, 0xFF)
        self.set_seq_auto_increment(True)

    def set_seq_range(self, start, end):
        self.seq_start = start
        self.seq_end = end
        self.seq_num = start

    def set_seq_auto_increment(self, enable):
        self.seq_auto = enable

    def get_next_seq(self):
        seq_num = self.seq_num
        self.seq_num += 1
        if self.seq_num > self.seq_end:
            self.seq_num = self.seq_start
        return seq_num

class RxHeader:
    
    SHORT_STATUS_BUSY = 0x80
    SHORT_STATUS_FREE = 0x00

    def __init__(self, header_byte):
        self.header_byte = header_byte
        self.destination = header_byte & 0x7
        self.seq_present = (header_byte >> 3) & 1
        self.len_present = (header_byte >> 4) & 1
        self.checksum_present = (header_byte >> 5) & 1
        self.nack = (header_byte >> 6) & 1

        # Check if the response header is of type short status
        self.is_short_status_header = (self.header_byte == RxHeader.SHORT_STATUS_BUSY 
                                        or self.header_byte == RxHeader.SHORT_STATUS_FREE)

    def __str__(self):
        if self.is_short_status_header:
            return "Rx Header 0x{0:02X} - Short Status".format(self.header_byte)
        else:
            fmt_str = "Rx Header 0x{0:02X}\r\n" + \
                      "  - Destination  = {1}\r\n" + \
                      "  - Seq Present  = {2}\r\n" + \
                      "  - Len Present  = {3}\r\n" + \
                      "  - Cksm Present = {4}\r\n" + \
                      "  - Nack         = {5}"
            return fmt_str.format(self.header_byte, self.destination, self.seq_present, self.len_present,
                                     self.checksum_present, self.nack)

class Response:
    def __init__(self, raw_data, nack=False):
        self.raw_data = raw_data

        self.header = None
        self.seq_num = None
        self.length = None
        self.error_code = None
        self.checksum = None
        self.computed_checksum = None
        self.checksum_valid = False

        self._data_index = None
        self._num_data_rem = 0
        self.nack = nack

        if raw_data != None and len(raw_data) != 0:
            self._analyze()

    def __str__(self):
        fmt_str =  "dest = {0}\r\n" + \
                   "seq  = {1}\r\n" + \
                   "len  = {2}\r\n" + \
                   "err  = {3}\r\n"
        return fmt_str.format(self.header.destination, self.seq_num, self.length, self.error_code)


    def _analyze(self):
        raw_len = len(self.raw_data)
        self.header = RxHeader(self.raw_data[0])
        i = 1
        if self.header.seq_present and i < raw_len:
            self.seq_num = self.raw_data[i]
            i += 1
        if self.header.len_present and (i + 1) < raw_len:
            self.length = self.raw_data[i] | (self.raw_data[i+1] << 8)
            i += 2
        else:
            self.length = raw_len - i - self.header.checksum_present

        self._data_index = i
        self._num_data_rem = self.length

        if self.header.nack and i < raw_len:
            self.error_code = self.raw_data[i]

        if self.header.checksum_present:
            self.checksum = self.raw_data[self._data_index + self.length]
            self.computed_checksum = Command.compute_checksum(self.raw_data)
            self.checksum_valid = (self.checksum == self.computed_checksum)
        else:
            self.checksum_valid = True

    def get_arr(self, size):
        if self._num_data_rem < size:
            return [0xdeadbeef]*size

        if size == 0:
            return None

        arr = self.raw_data[self._data_index:self._data_index + size]
        self._data_index += size
        self._num_data_rem -= size
        return arr

    def get_int(self, size):
        if self._num_data_rem < size:
            return 0xdeadbeef

        if size == 0 or size > 4:
            return 0xbeefdead

        data = 0
        if size >= 1:
            data = self.raw_data[self._data_index]
            self._data_index += 1
        if size >= 2:
            data |= self.raw_data[self._data_index] << 8
            self._data_index += 1
        if size >= 3:
            data |= self.raw_data[self._data_index] << 16
            self._data_index += 1
        if size >= 4:
            data |= self.raw_data[self._data_index] << 24
            self._data_index += 1

        self._num_data_rem -= size
        return data

class Command:

    ErrorCodeStr = [ "UNKNOWN_ERROR", 
                     "INVALID_DESTINATION",
                     "INVALID_COMMAND",
                     "INVALID_LENGTH",
                     "NOT_ENOUGH_STORAGE",
                     "LENGTH_INFO_MISSING",
                     "CHECKSUM_MISMATCH",
                     "TIMEOUT",
                     "READ_NOT_SUPPORTED",
                     "WRITE_NOT_SUPPORTED",
                     "EXECUTION_FAILED",
                     "INVALID_RESPONSE_LENGTH",
                     "BUFFER_FULL" ]

    def __init__(self, cmd_id, tx_header, var_len = False, seq_num = 0):
        self.cmd_id = cmd_id
        self.tx_header = tx_header
        self.var_len = var_len
        self.data_bytes = []
        self.byte_arr = []
        self.seq_num = seq_num

    def _prepare_data(self, is_read_cmd, reply_req):
        # Complete Header byte
        self.byte_arr.append(self.tx_header.byte)
        if is_read_cmd:
            self.byte_arr[0] |= 1 << 7
        if reply_req:
            self.byte_arr[0] |= 1 << 6
        if self.var_len:
            self.byte_arr[0] |= 1 << 4

        # command byte
        if self.tx_header.num_cmd_bytes >= 1:
            self.byte_arr.append(self.cmd_id & 0xFF)
        if self.tx_header.num_cmd_bytes == 2:
            self.byte_arr.append((self.cmd_id >> 8) & 0xFF)

        # Sequence byte - Use either from header (auto_incr) or use the provided value
        if self.tx_header.use_seq:
            if self.tx_header.seq_auto:
                self.seq_num = self.tx_header.get_next_seq()
            self.byte_arr.append(self.seq_num)

        # Length
        if self.tx_header.use_len or self.var_len:
            length = len(self.data_bytes)
            self.byte_arr.append(length & 0xFF)
            self.byte_arr.append((length >> 8) & 0xFF)

        # Pack data
        self.byte_arr += self.data_bytes

        # Checksum
        if self.tx_header.use_checksum:
            checksum = Command.compute_checksum(self.byte_arr)
            self.byte_arr.append(checksum)

    def _phy_send(self, phy, byte_arr):
        # For I2C, before sending do a short status read to see if the device is free
        if phy.get_type() == PhyType.I2C:
            timeout = 2
            start_time = time.time()
            while True:
                resp_arr = self._phy_receive(phy, 1, 2, True)
                if isinstance(resp_arr, bool) or resp_arr[0] == RxHeader.SHORT_STATUS_FREE:
                    break
                if timeout != 0 and (time.time() - start_time) >= timeout:
                    utils.print_error("ERROR: Timed out waiting for slave to be free to send next command.")
                    break

        utils.debug_print("{0} TX {1}".format(phy.get_name(), utils.byte_array_to_hex_str(byte_arr)))
        return phy.send(byte_arr)

    def _phy_receive(self, phy, count, timeout, clean_short_status = False):
        byte_arr = phy.receive(count, timeout)
        if not isinstance(byte_arr, bool) and byte_arr != None:
            #Print . instead of short status
            if clean_short_status and count == 1 and byte_arr[0] == RxHeader.SHORT_STATUS_BUSY:
                utils.debug_print(".", end="")
            elif clean_short_status and count == 1 and byte_arr[0] == RxHeader.SHORT_STATUS_FREE:
                utils.debug_print("-", end="")
            else:
                utils.debug_print("{0} RX {1}".format(phy.get_name(), utils.byte_array_to_hex_str(byte_arr)))
        return byte_arr

    def _read_helper(self, phy, read_data_len, reply_timeout_in_sec):

        #reply_timeout_in_sec = 0
        start_time = time.time()
        while True:
            #phy.flush_received_data()
            # read header byte.
            resp_bytes = self._phy_receive(phy, 1, reply_timeout_in_sec, True)
            if isinstance(resp_bytes, bool) or resp_bytes == None:
                return False
        
            rx_header = RxHeader(resp_bytes[0])
            if not rx_header.is_short_status_header:
                # Check if destination matches the command destination
                if self.tx_header.destination != rx_header.destination:
                    utils.print_error(
                       "ERROR: Destination value in response header 0x{0:X} is different from transmitted header value 0x{1:X}."
                            .format(rx_header.destination, self.tx_header.destination))
                    return False
                else:
                    # All good. We are ready to proceed
                    break

            if reply_timeout_in_sec != 0 and (time.time() - start_time) >= reply_timeout_in_sec:
                utils.print_error("ERROR: Timed out waiting for bytes.")
                return False
        
        # If we are expecting seq in response, read it to match the sequence number
        if self.tx_header.use_seq:
            # Read the seq bytes first
            seq_byte = self._phy_receive(phy, 1, reply_timeout_in_sec)
            if seq_byte == None:
                return False
        
            resp_bytes += seq_byte
        
            # Check if we sent sequence, and if sequence is present in response.
            if not rx_header.seq_present:
                utils.print_error("ERROR: Expected Sequence byte in response, but not found.")
                return False
            else:
                # Sequence number 0 is obtained if an error occurred in command handler before even reading seq byte.
                # This condition is allowed.
                if self.seq_num != seq_byte[0] and seq_byte[0] != 0x00:
                    utils.print_error(
                        "ERROR: Received Sequence number 0x{0:02X} does not match with Expected Sequence number 0x{1:02X}"
                            .format(seq_byte[0], self.seq_num))
                    return False
        
        num_bytes_to_read = 0
        length = read_data_len
        if rx_header.nack:
            length = 1

        # identify if length is provided with the header. If so, read only that much data
        if rx_header.len_present:
            num_bytes_to_read += 2
            resp_bytes += self._phy_receive(phy, num_bytes_to_read, reply_timeout_in_sec)
            if resp_bytes == None:
               return False
            # reset as we have read the computed number of bytes
            num_bytes_to_read = 0
            length = (resp_bytes[-1] << 8) | resp_bytes[-2]
            if length != read_data_len and read_data_len != 65535:
                utils.print_error("WARNING: Number of data bytes expected {0} does not match received {1}"
                        .format(read_data_len, length))
        elif read_data_len == 65535:
            # The user expected a variable response, but length is not present as per header.
            # This is an error condition and we cannot continue.
            # Check first if this is because of NACK
            if not rx_header.nack:
                utils.print_error(
                    "ERROR: Length for variable response command 0x{0:X} is not included per the received header 0x{1:02X}"
                            .format(self.cmd_id, rx_header.header_byte))
                return False

        num_bytes_to_read += length
        if rx_header.checksum_present:
            num_bytes_to_read += 1

        if num_bytes_to_read != 0:
            resp_bytes += self._phy_receive(phy, num_bytes_to_read, reply_timeout_in_sec)
            if resp_bytes == None:
               return False

        response_pkt = Response(resp_bytes, rx_header.nack)
        return response_pkt

    def write(self, phy, reply_req = False, reply_timeout_in_sec = 500,retries = 4):
        self._prepare_data(False, reply_req)
        utils.debug_print("\r\n\r\nCOMMAND = 0x{0:X} [Write]".format(self.cmd_id))
        utils.debug_print("REPLY_REQ = {0}".format(reply_req))
        if reply_req:
            phy.flush_received_data()
            for i in range(1,retries+1):
                if self._phy_send(phy, self.byte_arr):
                    response = self._read_helper(phy, 0, reply_timeout_in_sec)
                    if response != False:
                        return response
                else:
                    return False
        else:
            return self._phy_send(phy, self.byte_arr)

    def read(self, phy, read_data_len, reply_timeout_in_sec = 2,retries = 4):
        self._prepare_data(True, False)
        phy.flush_received_data()
        utils.debug_print("\r\n\r\nCOMMAND = 0x{0:X} [Read]".format(self.cmd_id))
        for i in range(1,retries+1):
            if self._phy_send(phy, self.byte_arr):
                response = self._read_helper(phy, read_data_len, reply_timeout_in_sec)
                if response != False:
                    return response
            else:
                print('send failed')
                return False

    def put_int(self, size, value):
        if size < 1 or size > 4:
            utils.print_error("ERROR: Invalid size {0} mentioned for put_int(). Data not added to payload".format(size))
        if size >= 1:
            self.data_bytes.append(value & 0xFF)
        if size >= 2:
            self.data_bytes.append((value >> 8) & 0xFF)
        if size >= 3:
            self.data_bytes.append((value >> 16) & 0xFF)
        if size >= 4:
            self.data_bytes.append((value >> 24) & 0xFF)

    def put_arr(self, byte_arr):
        self.data_bytes += byte_arr

    @staticmethod
    def send_raw(self, phy, byte_arr, num_bytes_to_return):
        phy.flush_received_data()
        self._phy_send(phy, byte_arr)

        if num_bytes_to_return == 0:
            return None
        else:
            return self._phy_receive(phy, num_bytes_to_return)

    @staticmethod
    def compute_checksum(byte_arr):
        # TODO LAZ 2018/01/06 To be implemented
        return 0

