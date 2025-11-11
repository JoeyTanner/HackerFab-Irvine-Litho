from enum import Enum

import sys, os.path
python_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(python_dir)
from third_party.command_handler.phy.usbhid import *

class RWCommandEnum(Enum):
    WriteCommand = 0x00
    ReadCommand = 0x80

class CommandDestinationEnum(Enum):
    Bootloader = 1
    ProjectorControl = 2
    RemoteFunctionCall = 3
    FormatterOnly = 4
    FormatterOnlyExtension = 5
    
class CommandHeaderStruct:
    Destination: CommandDestinationEnum
    OpcodeLength: int
    InsertByteLength: bool
    InsertChecksum: bool
    RequestACK: bool
    RWCommand: RWCommandEnum
    Checksum: int

global CommandHeader
CommandHeader = CommandHeaderStruct()

global usbhid
usbhid = USBHID(0x0451, 0x7540)

CommadOpcodeByteCount = {
    CommandDestinationEnum.Bootloader:1,
    CommandDestinationEnum.ProjectorControl:2,
    CommandDestinationEnum.RemoteFunctionCall:2,
    CommandDestinationEnum.FormatterOnly:1,
    CommandDestinationEnum.FormatterOnlyExtension:2
}

def USBConnect():
    # Default Header Settings for Read/Write Command
    CommandHeader.InsertByteLength = False
    CommandHeader.InsertChecksum = False
    CommandHeader.RequestACK = False

    usbhid.connect()
    time.sleep(0.2)

def USBDisconnect():
    usbhid.disconnect()
    
def USBWriteCommand (WriteBytes, ProtocolData):
    CommandHeader.Destination = ProtocolData.CommandDestination
    CommandHeader.OpcodeLength = ProtocolData.OpcodeLength
    CommandHeader.RWCommand = RWCommandEnum.WriteCommand
    WriteBuffer = GetHeaderAndFooterAppendedData(CommandHeader, WriteBytes)
    #print ("Write Command WriteBytes ", [hex(x) for x in WriteBuffer])
    usbhid.send(WriteBuffer)

def USBReadCommand(ReadByteCount, WriteBytes, ProtocolData):
    CommandHeader.Destination = ProtocolData.CommandDestination
    CommandHeader.OpcodeLength = ProtocolData.OpcodeLength
    CommandHeader.RWCommand = RWCommandEnum.ReadCommand
    if len(WriteBytes)!= 0:
        WriteBuffer = GetHeaderAndFooterAppendedData(CommandHeader, WriteBytes)
        #print ("Read Command WriteBytes ", [hex(x) for x in WriteBuffer])
        usbhid.send(WriteBuffer)

    # **********    TBD - fixed vs. variable length return data   **********
    # **********************************************************************
    time.sleep(1.0)
    ReadBytes = usbhid.receive(ReadByteCount+1)
    #print ("readbytes after receive ", [hex(x) for x in ReadBytes])
    ReadBytes.pop(0)
    usbhid.flush_received_data()
    return ReadBytes
    
def GetHeaderAndFooterAppendedData(CommandHeaderSettings, WriteBytes):
    Buffer = list()
    
    Buffer.append(CommandHeaderSettings.Destination)
    Buffer[0] += CommandHeaderSettings.RWCommand.value

    if CommandHeaderSettings.RequestACK == True:
        Buffer[0] |= 0x40

    if CommandHeaderSettings.OpcodeLength == 2:
        Buffer[0] |= 0x08
    for index in range(0, CommandHeaderSettings.OpcodeLength):
        Buffer.append(WriteBytes[index])

    DataBytesLength = len(WriteBytes)
    if CommandHeaderSettings.InsertByteLength == True:
        Buffer[0] |= 0x10
        Length = DataBytesLength - CommandHeaderSettings.OpcodeLength
        Buffer.append(Length & 0xFF)
        Buffer.append((Length)>> 8 & 0xFF)

    for index in range (CommandHeaderSettings.OpcodeLength, len(WriteBytes)):
        Buffer.append(WriteBytes[index])

    if CommandHeaderSettings.InsertChecksum == True:
        Buffer[0] |= 0x20
        Buffer.append(CommandHeaderSettings.Checksum)

    #print ("Output Buffer ", [hex(x) for x in Buffer])
    return Buffer
