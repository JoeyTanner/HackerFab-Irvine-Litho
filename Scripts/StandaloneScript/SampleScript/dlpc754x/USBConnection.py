from enum import Enum
from DriverScript.phy.usbhid import *

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
    RWCommand: RWCommandEnum
    InsertSequenceByte: bool
    SequenceNumber: int
    InsertByteLength: bool
    InsertChecksum: bool
    Checksum: int
    RequestACK: bool

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
    CommandHeader.InsertSequenceByte = False
    CommandHeader.InsertByteLength = False
    CommandHeader.InsertChecksum = False
    CommandHeader.RequestACK = False

    usbhid.connect()
    time.sleep(0.2)

def USBDisconnect():
    usbhid.disconnect()
    
def USBWriteCommand (WriteBytes, ProtocolData):
    CommandHeader.Destination = ProtocolData.CommandDestination
    CommandHeader.RWCommand = RWCommandEnum.WriteCommand
    WriteBuffer = GetHeaderAndFooterAppendedData(CommandHeader, WriteBytes)
    #print ("Write Command WriteBytes ", [hex(x) for x in WriteBuffer])
    usbhid.send(WriteBuffer)

def USBReadCommand(ReadByteCount, WriteBytes, ProtocolData):
    CommandHeader.Destination = ProtocolData.CommandDestination
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
    #print ("Input WriteBytes ",  [hex(x) for x in WriteBytes])
    
    Buffer.append(CommandHeaderSettings.Destination)
    Buffer[0] += CommandHeaderSettings.RWCommand.value

    if CommandHeaderSettings.RequestACK == True:
        Buffer[0] |= 0x40

    #print ("Destination ", CommandDestinationEnum(CommandHeaderSettings.Destination))
    OpcodeLength = CommadOpcodeByteCount[CommandDestinationEnum(CommandHeaderSettings.Destination)]
    DataBytesLength = len(WriteBytes)
    #print ("OpcodeLength ", OpcodeLength)
    for index in range(0, OpcodeLength):
        Buffer.append(WriteBytes[index])

    if CommandHeaderSettings.InsertSequenceByte == True:
        Buffer[0] |= 0x08
        Buffer.append(CommandHeaderSettings.SequenceNumber)

    if CommandHeaderSettings.InsertByteLength == True:
        Buffer[0] |= 0x10
        Length = DataBytesLength - OpcodeLength
        Buffer.append(Length & 0xFF)
        Buffer.append((Length)>> 8 & 0xFF)

    for index in range (OpcodeLength, len(WriteBytes)):
        Buffer.append(WriteBytes[index])

    if CommandHeaderSettings.InsertChecksum == True:
        Buffer[0] |= 0x20
        Buffer.append(CommandHeaderSettings.Checksum)

    #print ("Output Buffer ", [hex(x) for x in Buffer])
    return Buffer
