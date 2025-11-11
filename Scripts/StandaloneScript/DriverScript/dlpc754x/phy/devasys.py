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
from ctypes import c_ubyte, c_ushort, c_int, c_char, c_ulong, c_long
from ctypes import c_void_p, c_char_p
from ctypes import Structure, windll, POINTER, byref, create_string_buffer
from time import sleep

from interface import implements

from command_handler.core.physical_layer import *
import command_handler.core.utils as utils

MAX_MESSAGE_SIZE = 1088
PROPERTY_I2C_CHAN1_CLK_LO = 26

def _clocks_from_speed(speed_in_khz):
    """ converts a speed in KHz to a clock divisor,
        according to the DeVaSys method """
    if speed_in_khz > 0:
        divisor = int((48000.0 / speed_in_khz / 3.0) + 0.5)
        if 0 < divisor <= 256:
            return (-divisor) & 0xFF
    raise ValueError("Speed is not supported")


def _speed_from_clocks(clocks):
    """ converts a clock divisor to a speed in KHz,
        according to the DeVaSys method """
    divisor = (~clocks & 0xFF) + 1
    return 48000.0 / divisor / 3.0


class DeVaSysError(Exception):
    """ custom errors raised by the DeVaSys class will be of this type """
    pass


class DeVaSys(implements(PhysicalLayer)):
    """ instantiate this class to access a devasys device, which can perform
        i2c input/output, or read/write GPIO signals on the board.

        Example:

        with DeVaSys(0x36) as dev:
            dev.write([0xD2])
            patch, minor, major = unpack('HBB', buffer(bytearray(dev.read(4))))
            print "ASIC Software Version: %d.%d.%d" % (major, minor, patch)

        Constructs DeVaSys object with I2C slave address of attached device,
        0x36 in this example.  Then writes a 1 byte command (0xD2), and then
        reads 4 bytes, which is decoded as an unsigned short, and two unsigned
        chars ('HBB').

    """

    class DevInfo(Structure):
        """ used to pass to devasys dll functions """
        _fields_ = [("by_instance", c_ubyte),
                    ("serial_id",   c_char * 9)]

    class I2CTransaction(Structure):
        """ used to pass to devasys dll functions """
        _fields_ = [("by_trans_type",  c_ubyte),
                    ("by_slv_devaddr", c_ubyte),
                    ("w_memory_addr",  c_ushort),
                    ("w_count",        c_ushort),
                    ("data",           c_ubyte * MAX_MESSAGE_SIZE)]

    def __init__(self, slave=0x34):
        """ construct a DeVaSys object """
        self.dll = None
        self.device = None
        self.slave = slave
        self.instance = 0
        self.firmware_version = None
        self.print_event_msg = True

        self._identify()

    def _identify(self):
        count = self.GetDeviceCount()
        if count == 0:
            utils.print_error("ERROR: Could not find any DeVaSys device.")

        if utils.is_debug():
            for i in xrange(0, count):
                serial = self.GetDeviceInfo(i)
                utils.print_and_flush("{0} - DeVaSys SN: {1}\r\n".format(i, serial))

    def get_name(self):
        return "DeVaSys"

    def get_type(self):
        return PhyType.I2C

    def enable_connection_print(self, enable):
        self.print_event_msg = enable

    def connect(self, instance = 0):
        if instance >= self.GetDeviceCount():
            utils.print_error("ERROR: Opening DeVaSys instance {0} failed.".format(instance))
            return False

        self.instance = instance
        self._open()
        if self.device is None:
            utils.print_error("ERROR: Opening DeVaSys instance {0} failed.".format(instance))
            return False

        if self.print_event_msg or utils.is_debug():
            utils.debug_print("Opened DeVaSys SN: {0}\r\n".format(self.GetDeviceInfo(self.instance)))
        return True

    def disconnect(self):
        self._close()
        if self.print_event_msg or utils.is_debug():
            utils.debug_print("Closed DeVaSys SN: {0}\r\n".format(self.GetDeviceInfo(self.instance)))

    def send(self, byte_arr):
        try:
            self._write(byte_arr)
        except DeVaSysError as e:
            utils.print_error("ERROR: {0}".format(e))
            # Do a reset to see if we can recover
            utils.debug_print("Resetting DeVaSys device...")
            self.reset()

            # we will not re-attempt the command as we are not sure what the command was 
            # and if there is any after effect of running it twice.
            # Return false to indicate that the command failed.
            return False
        return True

    def receive(self, read_len, timeout_in_sec = 2):
        #utils.debug_print("read_len = {0}".format(read_len))
        try:
            data = self._read(read_len)
        except DeVaSysError as e:
            utils.print_error("ERROR: {0}".format(e))
            # Do a reset to see if we can recover
            utils.debug_print("Resetting DeVaSys device...")
            self.reset()

            # we will not re-attempt the command as we are not sure what the command was 
            # and if there is any after effect of running it twice.
            # Return false to indicate that the command failed.
            return False
        return data

    def flush_received_data(self):
	pass

    def __enter__(self):
        """ called when using python with statement:
                with DeVaSys(0x36) as dev:
                    # do something
            After the with statement, __exit__ is called to close the device
        """
        self._open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """ called after using python with statement """
        self._close()
        return False

    def _open(self):
        """ open devasys if not opened, yet.  opens by serial-id if
            instance is given as a string, else assumes instance is 0-n
        """
        if self.device is None:
            if type(self.instance) is str:
                self.device = self.OpenDeviceBySerialId(self.instance)
            else:
                self.device = self.OpenDeviceInstance(self.instance)

    def _close(self):
        """ close devasys device if opened """
        if self.device is not None:
            self.CloseDeviceInstance(self.device)
            self.device = None
            self.firmware_version = None

    def _read(self, numbytes, sendbytes=None, slave=None):
        """ read from devasys device, optionally writing 'sendbytes' before
            reading. the slave address given at construction can be overridden
            using the 'slave' parameter.  returns a list of bytes read.
        :type sendbytes: bytearray, list of bytes
        :param numbytes:
        :param sendbytes:
        :param slave:
        """
        if self.device is None:
            raise ValueError("Device not open (call open() or with DeVaSys())")
        if sendbytes is not None:
            self.write(sendbytes, slave=slave)
        return self.ReadI2c(self.device, slave or self.slave, numbytes)

    def _write(self, sendbytes, slave=None):
        """ write 'sendbytes' to the devasys device.  the slave address given
            at constructions can be overridden using the 'slave' parameter
        """
        if self.device is None:
            raise ValueError("ERROR: Not connected to any DeVaSys device");
        return self.WriteI2c(self.device, slave or self.slave, sendbytes)

    def get_speed(self):
        """ return the current I2C bus speed in KHz used by devasys """
        if self.device is None:
            raise ValueError("Device not open (call open() or with DeVaSys())")
        self._check_min_versions("getting speed", 0x0304, 0x0300, 0x0500)
        clocks = self.GetProperty(self.device, PROPERTY_I2C_CHAN1_CLK_LO)
        return _speed_from_clocks(clocks)

    def set_speed(self, speed_in_khz):
        """ set the current I2C bus speed in KHz used by devasys """
        if self.device is None:
            raise ValueError("Device not open (call open() or with DeVaSys())")
        self._check_min_versions("setting speed", 0x0304, 0x0300, 0x0500)
        clocks = _clocks_from_speed(speed_in_khz)
        self.SetProperty(self.device, PROPERTY_I2C_CHAN1_CLK_LO, clocks)
        # a reset is required for speed to take effect
        self.reset(4)
        utils.debug_print("Speed set to {0} KHz".format(self.get_speed))

    def reset(self, sleep_time=7):
        """ resets the devasys when it has a hard error
            this is just like unplugging and replugging the devasys device
        """
        if self.device is None:
            raise ValueError("Device not open (call open() or with DeVaSys())")
        self._check_min_versions("reset", 0x0304, 0x0300)
        self.SetVendorRequest(self.device, 0xE4, 0x0000, 0x0400, 0, None)
        self._close()
        sleep(sleep_time)
        self._open()

    def _check_min_versions(self, feature, dll, driver, firmware=None):
        """ check the dll, driver, and optionally firmware versions of the
            devasys device """
        dll_version = self.GetDllVersion()
        driver_version = self.GetDriverVersion()
        errstr = "DeVaSys DLL version too old for %s feature (need %x, have %x)"
        if dll_version < dll:
            raise DeVaSysError(errstr % (feature, dll, dll_version))
        if driver_version < driver:
            raise DeVaSysError(errstr % (feature, driver, driver_version))
        # cache firmware version so we don't have to keep accessing device
        if firmware is not None:
            if self.firmware_version is None:
                self.firmware_version = self.GetFirmwareVersion(self.device)
            if self.firmware_version < firmware:
                raise DeVaSysError(errstr % (feature, firmware,
                                             self.firmware_version))

    def unload(self):
        """ close and 'unload' the devasys dll """
        self._close()
        self.dll = None

    def load(self):
        """ load and define the functions in the devasys dll """
        self.dll = windll.usbi2cio

        self.dll.DAPI_GetDllVersion.argtypes = []
        self.dll.DAPI_GetDllVersion.restype = c_ushort

        self.dll.DAPI_GetDriverVersion.argtypes = []
        self.dll.DAPI_GetDriverVersion.restype = c_ushort

        self.dll.DAPI_GetFirmwareVersion.argtypes = [c_ulong, POINTER(c_ushort)]
        self.dll.DAPI_GetFirmwareVersion.restype = c_int

        self.dll.DAPI_OpenDeviceInstance.argtypes = [c_char_p, c_ubyte]
        self.dll.DAPI_OpenDeviceInstance.restype = c_void_p

        self.dll.DAPI_CloseDeviceInstance.argtypes = [c_void_p]
        self.dll.DAPI_CloseDeviceInstance.restype = c_int

        self.dll.DAPI_DetectDevice.argtypes = [c_void_p]
        self.dll.DAPI_DetectDevice.restype = c_int

        self.dll.DAPI_GetDeviceCount.argtypes = [c_char_p]
        self.dll.DAPI_GetDeviceCount.restype = c_ubyte

        self.dll.DAPI_GetDeviceInfo.argtypes = [c_char_p, POINTER(self.DevInfo)]
        self.dll.DAPI_GetDeviceInfo.restype = c_ubyte

        self.dll.DAPI_OpenDeviceBySerialId.argtypes = [c_char_p, c_char_p]
        self.dll.DAPI_OpenDeviceBySerialId.restype = c_void_p

        self.dll.DAPI_GetSerialId.argtypes = [c_void_p, c_char_p]
        self.dll.DAPI_GetSerialId.restype = c_int

        self.dll.DAPI_ReadI2c.argtypes = [c_void_p,
                                          POINTER(self.I2CTransaction)]
        self.dll.DAPI_ReadI2c.restype = c_long

        self.dll.DAPI_WriteI2c.argtypes = [c_void_p,
                                           POINTER(self.I2CTransaction)]
        self.dll.DAPI_WriteI2c.restype = c_long

        self.dll.DAPI_SetProperty.argtypes = [c_void_p, c_ubyte, c_ubyte]
        self.dll.DAPI_SetProperty.restype = c_int

        self.dll.DAPI_GetProperty.argtypes = [c_void_p, POINTER(c_ubyte),
                                              c_ubyte]
        self.dll.DAPI_GetProperty.restype = c_int

        self.dll.DAPI_ConfigIoPorts.argtypes = [c_void_p, c_ulong]
        self.dll.DAPI_ConfigIoPorts.restype = c_int

        self.dll.DAPI_GetIoConfig.argtypes = [c_void_p, POINTER(c_ulong)]
        self.dll.DAPI_GetIoConfig.restype = c_int

        self.dll.DAPI_ReadIoPorts.argtypes = [c_void_p, POINTER(c_ulong)]
        self.dll.DAPI_ReadIoPorts.restype = c_int

        self.dll.DAPI_WriteIoPorts.argtypes = [c_void_p, c_ulong, c_ulong]
        self.dll.DAPI_WriteIoPorts.restype = c_int

        self.dll.DAPI_ReadDebugBuffer.argtypes = [c_char_p, c_void_p, c_long]
        self.dll.DAPI_ReadDebugBuffer.restype = c_long

        self.dll.DAPI_GetLastFirmwareError.argtypes = [c_void_p,
                                                       POINTER(c_ulong)]
        self.dll.DAPI_GetLastFirmwareError.restype = c_int

        self.dll.DAPI_SetVendorRequest.argtypes = [c_void_p, c_ubyte, c_ushort,
                                                   c_ushort, c_ushort, c_char_p]
        self.dll.DAPI_SetVendorRequest.restype = c_int

        self.dll.DAPI_GetVendorRequest.argtypes = [c_void_p, c_char_p, c_ubyte,
                                                   c_ushort, c_ushort, c_ushort]
        self.dll.DAPI_GetVendorRequest.restype = c_int

    def GetDllVersion(self):
        """ simple wrapper for DAPI_GetDllVersion """
        if self.dll is None:
            self.load()
        return self.dll.DAPI_GetDllVersion()

    def GetDriverVersion(self):
        """ simple wrapper for DAPI_GetDriverVersion """
        if self.dll is None:
            self.load()
        return self.dll.DAPI_GetDriverVersion()

    def GetFirmwareVersion(self, device):
        """ simple wrapper for DAPI_GetFirmwareVersion """
        fwversion = c_ushort(0)
        result = self.dll.DAPI_GetFirmwareVersion(device, byref(fwversion))
        if not result:
            raise ValueError("DeVaSys GetFirmwareVersion failed, "
                             "is device handle valid?")
        return fwversion.value

    def OpenDeviceInstance(self, instance):
        """ simple wrapper for DAPI_OpenDeviceInstance """
        if self.dll is None:
            self.load()
        return self.dll.DAPI_OpenDeviceInstance("UsbI2cIo", instance)

    def CloseDeviceInstance(self, device):
        """ simple wrapper for DAPI_CloseDeviceInstance """
        return self.dll.DAPI_CloseDeviceInstance(device)

    def DetectDevice(self, device):
        """ simple wrapper for DAPI_DetectDevice """
        return self.dll.DAPI_DetectDevice(device)

    def GetDeviceCount(self):
        """ simple wrapper for DAPI_GetDeviceCount """
        if self.dll is None:
            self.load()
        return self.dll.DAPI_GetDeviceCount("UsbI2cIo")

    def GetDeviceInfo(self, instance):
        """ simple wrapper for DAPI_GetDeviceInfo """
        if self.dll is None:
            self.load()
        info = self.DevInfo()
        info.by_instance = instance
        if self.dll.DAPI_GetDeviceInfo("UsbI2cIo", byref(info)):
            return info.serial_id
        return None

    def OpenDeviceBySerialId(self, serial_id):
        """ simple wrapper for DAPI_OpenDeviceBySerialId """
        if self.dll is None:
            self.load()
        return self.dll.DAPI_OpenDeviceBySerialId("UsbI2cIo", serial_id)

    def GetSerialId(self, device):
        """ simple wrapper for DAPI_GetSerialId """
        buff = create_string_buffer(9)
        if self.dll.DAPI_GetSerialId(device, buff):
            return buff.value
        return None

    def ReadI2c(self, device, slave_addr, bytes_to_read=MAX_MESSAGE_SIZE):
        """ simple wrapper for DAPI_ReadI2c """
        if bytes_to_read > MAX_MESSAGE_SIZE:
            raise ValueError("Bytes to read {0} exceeds MAX_MESSAGE_SIZE".format(bytes_to_read))
        i2cxact = self.I2CTransaction()
        i2cxact.by_trans_type = 0
        i2cxact.by_slv_devaddr = slave_addr | 1
        i2cxact.w_count = bytes_to_read
        bytes_read = self.dll.DAPI_ReadI2c(device, byref(i2cxact))
        if bytes_read < 0:
            raise DeVaSysError("DeVaSys ReadI2C failed: " + hex(bytes_read))
        #utils.debug_print("DEBUG: Bytes read = {0}\r\ndata = {1}".format(bytes_read, utils.byte_array_to_hex_str(i2cxact.data)))
        return i2cxact.data[:bytes_read]

    def WriteI2c(self, device, slave_addr, sendbytes):
        """ simple wrapper for DAPI_WriteI2c """
        if len(sendbytes) > MAX_MESSAGE_SIZE:
            raise ValueError("Size of message {0} exceeds MAX_MESSAGE_SIZE".format(len(sendbytes)))
        i2cxact = self.I2CTransaction()
        i2cxact.by_trans_type = 0
        i2cxact.by_slv_devaddr = slave_addr
        i2cxact.w_count = len(sendbytes)
        for i, value in enumerate(sendbytes):
            i2cxact.data[i] = value
        if self.dll.DAPI_WriteI2c(device, byref(i2cxact)) < 0:
            raise DeVaSysError("DeVaSys WriteI2C failed")

    def SetProperty(self, device, index, value):
        """ simple wrapper for DAPI_SetProperty """
        return self.dll.DAPI_SetProperty(device, index, value)

    def GetProperty(self, device, index):
        """ simple wrapper for DAPI_GetProperty """
        value = c_ubyte(0)
        if self.dll.DAPI_GetProperty(device, byref(value), index):
            return value.value
        return None

    def ConfigIoPorts(self, device, config):
        """ simple wrapper for DAPI_ConfigIoPorts """
        return self.dll.DAPI_ConfigIoPorts(device, config)

    def GetIoConfig(self, device):
        """ simple wrapper for DAPI_GetIoConfig """
        config = c_ulong(0)
        if self.dll.DAPI_GetIoConfig(device, byref(config)):
            return config.value
        return None

    def ReadIoPorts(self, device):
        """ simple wrapper for DAPI_ReadIoPorts """
        ioports = c_ulong(0)
        if self.dll.DAPI_ReadIoPorts(device, byref(ioports)):
            return ioports.value
        return None

    def WriteIoPorts(self, device, value, mask):
        """ simple wrapper for DAPI_WriteIoPorts """
        return self.dll.DAPI_WriteIoPorts(device, value, mask)

    def ReadDebugBuffer(self, device):
        """ simple wrapper for DAPI_ReadDebugBuffer """
        buff = create_string_buffer(64)
        length = self.dll.DAPI_ReadDebugBuffer(buff, device, 64)
        return buff[:length]

    def GetLastFirmwareError(self, device):
        """ simple wrapper for DAPI_GetLastFirmwareError """
        errorcode = c_ulong(0)
        if self.dll.DAPI_GetLastFirmwareError(device, byref(errorcode)):
            return errorcode.value
        return None

    def GetVendorRequest(self, device, data, by_request,
                         value, index, length):
        """ simple wrapper for DAPI_GetVendorRequest """
        return self.dll.DAPI_GetVendorRequest(device, data, by_request, value,
                                              index, length)

    def SetVendorRequest(self, device, by_request, value,
                         index, length, data):
        """ simple wrapper for DAPI_SetVendorRequest """
        return self.dll.DAPI_SetVendorRequest(device, by_request, value, index,
                                              length, data)
