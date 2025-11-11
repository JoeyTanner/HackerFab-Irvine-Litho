import time

from CommandScript.dlpc754x import *
from USBConnection import *

def main():
    def WriteCommand (WriteBytes, ProtocolData):
        USBWriteCommand (WriteBytes, ProtocolData)
        
    def ReadCommand(ReadByteCount, WriteBytes, ProtocolData):
        return USBReadCommand(ReadByteCount, WriteBytes, ProtocolData)
        
    # register the Read/Write Command in the Python library
    DLPC754Xinit(ReadCommand, WriteCommand)

    # USBConnect
    USBConnect()

    # ##### ##### ##### ##### Command call(s) start here ##### ##### ##### ##### 
    # switch to App mode for command processing
    Summary = WriteSwitchMode ( CmdSwitchTypeT.ToAppDirect )
    time.sleep(1.0)

    # Example of Read Command
    Summary, AppMode, ControllerConfig = ReadMode ( )
    print ("Read Mode; AppMode & ControllerConfig", AppMode, ControllerConfig)
    
    Summary, Version = ReadVersion ( )
    print ("Read Version; App & Api's maj, min, patch", Version.AppMajor, Version.AppMinor, Version.AppPatch, Version.ApiMajor, Version.ApiMinor, Version.ApiPatch)

    # Example of Write Command
    Summary, KeystoneEnabled = ReadEnableKeystone()
    print ("Enable Keystone ", KeystoneEnabled)

    Summary = WriteEnableKeystone (not KeystoneEnabled)

    Summary, KeystoneEnabled = ReadEnableKeystone()
    print ("Enable Keystone ", KeystoneEnabled)
    # ##### ##### ##### ##### Command call(s) end here ##### ##### ##### #####
    
    USBDisconnect()
if __name__ == "__main__" : main()


