#!/cygdrive/c/Python27/python
# ******************************************************************************
# 
#   Copyright (c) 2018 Texas Instruments
# 
# ******************************************************************************/
# 
#  This script acts as a dummy physical layer interface for the command handler.
#  This is primarily used to test the command handler data packing, and does not
#  communicate with the projector.
#  
# ******************************************************************************

from __future__ import print_function
import sys

from interface import implements

import command_handler.core.utils as utils
from command_handler.core.physical_layer import *

class DummyPhy(implements(PhysicalLayer)):
    def __init__(self, phy_type = PhyType.USB):
        self.connected = False
        self.data = None
        self.unread_bytes = 0
        self.data_index = 0
        self.phy_type = phy_type
        self.print_event_msg = True
        
    def get_name(self):
        return "Dummy"

    def get_type(self):
        return self.phy_type

    def enable_connection_print(self, enable):
        self.print_event_msg = enable

    def connect(self, instance = 0):
        self.connected = True
        pass

    def disconnect(self):
        self.connected = False
        pass

    def send(self, byte_arr):
        if not self.connected:
            utils.print_error("ERROR: Not connected.")
            return False

        print("TX: {0}".format(map(lambda val: "{0:02X}h".format(val), byte_arr)))
        return True

    def receive(self, read_len, timeout_in_sec = 2):
        self.unread_bytes -= read_len
        returnval = self.data[self.data_index : self.data_index + read_len]
        self.data_index += read_len
        return returnval

    def flush_received_data(self):
        pass

    def set_read_data(self, data):
        self.data = data
        self.unread_bytes = len(data)
        self.data_index = 0
        print("RX: {0}".format(map(lambda val: "{0:02X}h".format(val), self.data)))

