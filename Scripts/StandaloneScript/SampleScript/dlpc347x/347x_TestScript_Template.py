import struct
import time

from enum import Enum

from CommandScript.dlpc347x import *
from DriverScript.cypress import *

def main():
    with Cypress(0x36) as dev, LightCrafterDisplay(dev) as lcd:
    
        protocoldata = ProtocolData()
        
        def WriteCommand (writebytes, protocoldata):
            # print ("Write Command writebytes ", [hex(x) for x in writebytes])
            
            # check protocoldata.CommandDestination for destination to send command
            # print ("Destination ", protocoldata.CommandDestination)

            dev.write(writebytes)

        def ReadCommand(readbytecount, writebytes, protocoldata):
            # print ("Read Command writebytes ", [hex(x) for x in writebytes])
            
            # check protocoldata.CommandDestination for destination to send command
            # print ("Destination ", protocoldata.CommandDestination)
            
            # TBD - need utility to read and also return the actual number of bytes read
            #       then update protocoldata.BytesRead before return the data read back

            readbytes = dev.read(readbytecount, writebytes)
            # print ("readbytes ", [hex(x) for x in readbytes])

            return readbytes
            
        # register the Read/Write Command in the Python library
        DLPC347Xinit(ReadCommand, WriteCommand)

        # ##### ##### Command call(s) start here ##### #####
        # Example of Read Command
        Summary, PatchVersion, MinorVersion, MajorVersion = ReadFlashBuildVersion()
        print ("Flash Build Version ", PatchVersion, MinorVersion, MajorVersion)
        
        Summary, CurrentOperatingMode = ReadOperatingModeSelect()
        print ("Operating Mode ", CurrentOperatingMode)

        # Example of Write/Read Command
        Summary = WriteKeystoneProjectionPitchAngle(15.0)
        Summary, PitchAngle = ReadKeystoneProjectionPitchAngle()
        print ("Keystone PitchAngle ", PitchAngle)

        # Example of Write Command
        Summary = WriteOperatingModeSelect(OperatingMode.SensInternalPattern)
        Summary = WriteInternalPatternControl(PatternControl.Start, 255)
        time.sleep(5)
        Summary = WriteInternalPatternControl(PatternControl.Stop, 0)

if __name__ == "__main__" : main()


