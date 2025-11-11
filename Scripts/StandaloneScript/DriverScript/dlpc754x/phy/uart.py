#!/cygdrive/c/Python27/python
# ******************************************************************************
#
#   Copyright (c) 2018 Texas Instruments
#
# ******************************************************************************/
#
#  This script acts as the physical layer implementation to communicate over
#  DeVaSys USB to I2C.
#
#  See more details in the readme file to see how to install, and which
#  version to use etc of all 3rd party SW.
#
#  This module uses ctypes to implement an interface to the DeVaSys I2C
#  DLL/driver. The original python code was taken from DLPC230 GUI tool python
#  script code base and was adapted to match the command handler implementation.
#
# ******************************************************************************
import sys
import time
import serial

from interface import implements

import command_handler.core.utils as utils
from command_handler.core.physical_layer import *

class URT(implements(PhysicalLayer)):
	def __init__(self, port, baudrate=115200, timeout=2, rtscts=False):
		self.ser = serial.Serial()
		self.ser.port = port
		self.ser.baudrate = baudrate
		self.ser.timeout = timeout
                self.ser.rtscts = rtscts
		
	def get_name(self): 
		return "UART" 
		
	def get_type(self):
		return PhyType.URT
		
	def enable_connection_print(self, enable):
		self.print_event_msg = enable
		
	def flush_received_data(self):
		pass
		
	def connect(self, instance = 0):
		try:
			self.ser.open()
		except Exception, e:
			print( str(e))
		
		if self.ser.isOpen():
			try:
				#Discarding all the elements in the buffer
				self.ser.reset_input_buffer()
				self.ser.reset_output_buffer()
			except Exception,e1:
				print("error communicating...:" + str(e1))
				self.ser.close()
				exit()
		else:
			print("can't open serial port ")
			exit()
			
		return True
		
	def disconnect(self):
		if self.ser.isOpen():
			self.ser.close()
			exit()
			
		else:
			print("can't open serial port ")
			exit()
			
		return True
			
	def send(self, byte_arr):
		if self.ser.isOpen():
                    buffer_len = 32
                    rem_bytes = len(byte_arr)
                    start_index = 0
                    while rem_bytes > 0:
                        size = min(rem_bytes, buffer_len-1)
                        raw_data = []
                        raw_data[0:] = byte_arr[start_index:start_index + size]
                        raw_len = len(raw_data)
                        self.ser.write(raw_data)
                        rem_bytes -= size
                        start_index += size
		else:
			print("can't open serial port ")
			exit()
			
		return True
		
	def receive(self, read_len, timeout_in_sec = 2):
		self.ser.timeout = timeout_in_sec
                #utils.print_and_flush("Read_len = {0}...".format(read_len))
		if self.ser.isOpen():
			data = self.ser.read(read_len)
                        if len(data) != 0:
			    data = [(ord(c)) for c in data]
                            #utils.print_and_flush(utils.byte_array_to_hex_str(data) + "\r\n")
			    return data
                        else:
                            return None
		else:
			print("can't open serial port ")
			exit()
