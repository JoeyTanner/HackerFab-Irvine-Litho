#!/cygdrive/c/Python27/python
# ******************************************************************************
# 
#   Copyright (c) 2018 Texas Instruments
# 
# ******************************************************************************/
# 
#  This script acts as a interface to define a physical layer. The Command class
#  expects a class object that implements this interface for communication.
#  
# ******************************************************************************

from interface import Interface

class PhyType:
    USB = 0
    I2C = 1
    URT = 2
    SPI = 3

class PhysicalLayer(Interface):

    def get_name(self):
        pass

    def get_type(self):
        pass

    def enable_connection_print(self, enable):
        pass

    def connect(self, instance = 0):
        pass

    def disconnect(self):
        pass

    def send(self, byte_arr):
        pass

    def receive(self, read_len, timeout_in_sec = 2):
        pass
    
    def flush_received_data(self):
        pass




