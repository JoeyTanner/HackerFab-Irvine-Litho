import clr
clr.AddReference('DLPComposer.IO')
from DLPComposer.IO.DLPC34xx import I2CCommandInterface
clr.AddReference('DLPComposer.Commands.DLPC343x.XPR')
from DLPComposer.Commands.DLPC343x.XPR import *
clr.AddReference('DLPComposer.IO.Communications')
from DLPComposer.IO.Communications import DLPC343xXPRCommunicationManager as CommunicationManager
clr.AddReference('DLPComposer.Registers')
from DLPComposer.IO import RegisterBase

def _get_i2c_interface(dev_instance):
    available_i2c_interfaces = I2CCommandInterface.GetAvailableInterfaces()
    if available_i2c_interfaces.Count < (dev_instance + 1):
        return None

    i2c_interface = available_i2c_interfaces[dev_instance]
    i2c_interface.Timeout = 500
    return i2c_interface

def i2c_connect(dev_instance = 0, gpio_handshake = False, slave_adress = 0x36):
    i2c_interface = _get_i2c_interface(dev_instance)
    if i2c_interface == None:
        return False

    i2c_interface.SlaveAddress = slave_adress
    i2c_interface.RequestAccessViaGpio = gpio_handshake
    i2c_interface.Connect()
    Command.CommInterface = i2c_interface

    if RegisterBase.CommunicationManager == None:
        RegisterBase.CommunicationManager = CommunicationManager("")
    
    return i2c_interface.IsConnected

def request_i2c_access(dev_instance = 0):
    i2c_interface = _get_i2c_interface(dev_instance)
    i2c_interface.RequestAccessViaGpio = True
    if i2c_interface != None:
        i2c_interface.RequestAccess()
        return True
    return False

def relinquish_i2c_access(dev_instance = 0):
    i2c_interface = _get_i2c_interface(dev_instance)
    i2c_interface.RequestAccessViaGpio = True
    if i2c_interface != None:
        i2c_interface.RelinquishAccess()
        return True
    return False

__all__ = ['i2c_connect', 'request_i2c_access', 'relinquish_i2c_access']