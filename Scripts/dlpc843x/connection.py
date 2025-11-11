import clr
clr.AddReference('DLPComposer.IO')
from DLPComposer.IO import CommunicationPort, RegisterBase
from DLPComposer.IO.DLPC754x import USBBulkCommandInterface, I2CCommandInterface, TestRegisterCommunicationInterface
clr.AddReference('DLPComposer.Commands.DLPC843x')
from DLPComposer.Commands.DLPC843x import *
clr.AddReference('DLPComposer.Commands.Library')
from DLPComposer.Commands.Library.DLPC843x import Command as LibraryCommand
clr.AddReference('DLPComposer.IO.Communications')
from DLPComposer.IO.Communications import DLPC843xCommunicationManager as CommunicationManager
from dlpc843x.registers import *

def _connect(comm_interface, apply_settings = True):
    if apply_settings:
        comm_interface.CommandHeader.InsertByteLength = True
        comm_interface.CommandHeader.InsertChecksum = False
        comm_interface.CommandHeader.RequestACK = True
        comm_interface.Timeout = 2000
    
    comm_interface.Connect()
    Command.CommInterface = comm_interface
    LibraryCommand.CommInterface = comm_interface
    
    if RegisterBase.CommunicationManager == None:
        RegisterBase.CommunicationManager = CommunicationManager(CommunicationPort.Command)
    
    return comm_interface.IsConnected

def _disconnect():
    if Command.CommInterface != None:
        Command.CommInterface.Disconnect()
        Command.CommInterface = None

def usb_connect(vid=0x451, pid=0x8430):
    _disconnect()
    available_usb_interfaces = USBBulkCommandInterface.GetAvailableInterfaces()
    for interface in available_usb_interfaces:
        if interface.VID == vid and interface.PID == pid:
            return _connect(interface)
    return False

def i2c_connect(dev_instance = 0):
    _disconnect()
    available_i2c_interfaces = I2CCommandInterface.GetAvailableInterfaces()
    if len(available_i2c_interfaces) < (dev_instance + 1):
        return False
    
    i2c_interface = available_i2c_interfaces[dev_instance]
    return _connect(i2c_interface)

def test_connect():
    _disconnect()
    return _connect(TestRegisterCommunicationInterface(), False)

__all__ = ['usb_connect', 'i2c_connect', 'test_connect']
