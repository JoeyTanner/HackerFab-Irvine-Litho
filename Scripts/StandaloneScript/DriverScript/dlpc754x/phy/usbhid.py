#!/cygdrive/c/Python27/python
# ******************************************************************************
#
#   Copyright (c) 2018 Texas Instruments
#
# ******************************************************************************/
#
#  This script acts as the physical layer implementation to communicate over
#  USB HID. This uses the 3rd party python package pywinusb.
#
#  See more details in the readme file to see how to install, and which
#  version to use etc of all 3rd party python packages.
#
# ******************************************************************************

import re
import sys
import time

from interface import implements
import pywinusb.hid as hid

import DriverScript.core.utils as utils
from DriverScript.core.physical_layer import *

class USBHID(implements(PhysicalLayer)):
    def __init__(self, vendor_id, product_id):
        self.vendor_id = vendor_id
        self.product_id = product_id
        self.device = None
        self.all_devices = None
        self.out_report = None
        self.print_event_msg = False
        self._identify()

    @staticmethod
    def get_device_str(device):
        return ("{0}: {1} [vID=0x{2:04X}, pID=0x{3:04X}, v=0x{4:04X}]"
                .format(device.vendor_name, device.product_name, device.vendor_id, device.product_id, device.version_number))

    def _print_all_matching_devices(self):
        utils.print_and_flush("Identified Devices:\r\n")
        i = 0
        for device in self.all_devices:
            device_str = USBHID.get_device_str(device)
            utils.print_and_flush("{0} - {1}\r\n".format(i, device_str))
            i = i + 1

    def _identify(self):
    # usually you'll find and open the target device, here we'll browse for the current connected devices
        self.all_devices = hid.HidDeviceFilter(vendor_id = self.vendor_id, product_id = self.product_id).get_devices()

        if not self.all_devices:
            raise ValueError("ERROR: Can't find target device (vendor_id = 0x{0:04X}, product_id = 0x{1:04X})."
                    .format(self.vendor_id, self.product_id))
        else:
            if utils.is_debug():
                self._print_all_matching_devices()

    def _identify_output_report(self):
        """ Identifies the output report to use to send data """
        # This function being private assumes the device is connected.
        output_reports = self.device.find_output_reports()
        if len(output_reports) > 0:
            self.out_report = output_reports[0]

    def get_name(self):
        return "USBHID"

    def get_type(self):
        return PhyType.USB

    def enable_connection_print(self, enable):
        self.print_event_msg = enable

    def connect(self, instance = 0):
        if self.device != None and self.device.is_opened():
            utils.print_error("ERROR: Following device is already connected. Disconnect before attempting to connect "
                    + "again.\r\n{0}".format(self.device))
            return False

        if not self.all_devices:
            utils.print_error("ERROR: Can't find target device (vendor_id = 0x{0:04X}, product_id = 0x{1:04X})."
                    .format(self.vendor_id, self.product_id))
            return False

        if instance == 0 and len(self.all_devices) == 1:
            self.device = self.all_devices[0]
        else:
            # Python re-orders the interfaces (device[0] may not be the first interface)
            # To identify the correct interface number of a given instance use the MI_0, MI_1 ...
            # string available in the instance_id
            for device in self.all_devices:
                #print(device.instance_id)
                inst_match = re.match(r'.*MI_([0-9]+)\\.*',device.instance_id)
                if inst_match and int(inst_match.group(1)) == instance:
                    self.device = device
                    break
            else:
                utils.print_error("ERROR: Invalid instance {0} provided. Choose a number less than {1}"
                            .format(instance, len(self.all_devices)))
                return False

        try:
            self.device.open()
            if self.print_event_msg or utils.is_debug():
                utils.print_and_flush("Opened {0}\r\n".format(USBHID.get_device_str(self.device)))

            # Identify the output report to which to send data
            self._identify_output_report()
            if self.out_report == None:
                utils.print_error("ERROR: No Output reports found. Sending data will not be supported.")

            self.device.set_raw_data_handler(USBHID._rx_handler)
            self.flush_received_data()

            return True
        except:
            utils.print_error("ERROR: Failed to open {0}\r\nException:\r\n{1}"
                    .format(USBHID.get_device_str(self.device), sys.exc_info()[0]))
            return False

    def disconnect(self):
        if self.device != None and self.device.is_opened():
            self.device.close()
            if self.print_event_msg or utils.is_debug():
                utils.print_and_flush("Closed {0}\r\n".format(USBHID.get_device_str(self.device)))

    def print_reports(self):
        if self.device == None or not self.device.is_opened():
            utils.print_error("ERROR: No device connected")
            return

        for report in self.device.find_output_reports():
            utils.debug_print("{0}\r\n".format(report))

    def send(self, byte_arr):
        if self.device == None or not self.device.is_opened():
            utils.print_error("ERROR: No device connected")
            return False

        if self.out_report == None:
            utils.print_error("ERROR: Output report not found. Cannot send data")
            return False

        # TODO : To be updated to support multiple out reports and choose the right report
        # based on the size of data packet

        # Extend the data into report size and split into multiple packets if data size is larger.
        report_len = 65
        rem_bytes = len(byte_arr)
        start_index = 0
        while rem_bytes > 0:
            size = min(rem_bytes, report_len - 1)
            raw_data = []
            raw_data.append(self.out_report.report_id)
            raw_data[1:] = byte_arr[start_index:start_index + size]
            raw_len = len(raw_data)
            if raw_len < report_len:
                raw_data[raw_len: report_len] = [0x00]*(report_len - raw_len)
            utils.debug_print("USBHID TX [{0}]: {1}".format(len(raw_data), map(lambda val: "{0:02X}h".format(val), raw_data)))
            self.out_report.send(raw_data)
            rem_bytes -= size
            start_index += size
        return True

    def receive(self, read_len, timeout_in_sec = 2):
        if self.device == None or not self.device.is_opened():
            utils.print_error("ERROR: No device connected")
            return False

            utils.debug_print("read_len = {0}, unread_bytes = {1}".format(read_len, USBHID.unread_bytes))

        # Wait till we have enough data
        i = 0
        start_time = time.time()
        while read_len > USBHID.unread_bytes:
            i += 1
            if i % 10 == 0:
                utils.debug_print("Waiting for {0} more bytes...".format(read_len - USBHID.unread_bytes))
            if timeout_in_sec != 0 and (time.time() - start_time) >= timeout_in_sec:
                utils.print_error("ERROR: Timed out waiting for bytes.")
                return None

            # Sleep 10 ms
            time.sleep (10 / 1000.0)

        # This means we have enough bytes to return from our already received data
        USBHID.unread_bytes -= read_len
        returnval = USBHID.data[self.data_index : self.data_index + read_len]
        self.data_index += read_len
        return returnval

    def flush_received_data(self):
        USBHID.data = []
        self.data_index = 0
        USBHID.unread_bytes = 0

    @staticmethod
    def _rx_handler(data):
        utils.debug_print("USBHID RX: [{0}]: {1}".format(len(data) - 1, map(lambda val: "{0:02X}h".format(val), data[1:])))

        # Each time data is recived, remove the 1st byte which indicates the report descriptor ID
        USBHID.data += data[1:]
        USBHID.unread_bytes += len(data) - 1

