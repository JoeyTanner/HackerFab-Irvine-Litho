#-------------------------------------------------------------------------------
# Copyright (c) 2023 Texas Instruments Incorporated - http://www.ti.com/
#-------------------------------------------------------------------------------
#
# NOTE: This file is auto generated from a command definition file.
#       Please do not modify the file directly.                    
#
# Command Spec Version : 0.1
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#   Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
#
#   Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the
#   distribution.
#
#   Neither the name of Texas Instruments Incorporated nor the names of
#   its contributors may be used to endorse or promote products derived
#   from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import struct
from enum import Enum

import sys, os.path
python_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(python_dir)
from api.packer import *

class DpStateT(Enum):
    Standby = 0
    DetectingExtSource = 1
    ExtSourceLocked = 2
    ConfigError = 3
    InternalSource = 4

class DpDisplaySourceT(Enum):
    External = 0
    Tpg = 1
    Splash = 2

class SeqOtfSequenceOperationModeT(Enum):
    NormalSeqOperation = 0
    Force1BitSeq = 1

class DispFeatureT(Enum):
    AnamorphicScaling = 0
    Keystone = 1
    Warping = 2

class SrcFpdFRangeT(Enum):
    SrcFpdFrange10MhzTo20Mhz = 0
    SrcFpdFrange20MhzTo30Mhz = 1
    SrcFpdFrange30MhzTo55Mhz = 2
    SrcFpdFrange55MhzTo100Mhz = 3
    SrcFpdFrange100MhzTo160Mhz = 4
    AutoSelect = 5

class SplashCompressionT(Enum):
    Uncompressed = 0
    Rle20 = 1

class Xpr4WayCommand(Enum):
    Fixeden = 0
    Dacgain = 1
    Sfdelay = 2
    Acttype = 3
    Outputsel = 4
    Clockwidth = 5
    Dacoffset = 6
    Ramplen = 7
    Segmentlen = 8
    Invpwma = 9
    Invpwmb = 10
    Sffilterval = 11
    Sfwatchdog = 12
    Fixedoutputval = 13
    Actforcestop = 14

class DlpIllumTypeT(Enum):
    Red = 0
    Green = 1
    Blue = 2
    Cyan = 3
    Magenta = 4
    Yellow = 5
    Spoke1 = 6
    Spoke2 = 7
    Spare1 = 8
    Spare2 = 9
    Spare3 = 10
    DlpLinkLeft = 11
    DlpLinkRight = 12
    DarkTime = 13

class TpgBorderColorT(Enum):
    White = 0
    Color = 1

class SrcFpdDataMapT(Enum):
    SrcFpd30BppRgbMode0 = 0
    SrcFpd30BppRgbMode1 = 1
    SrcFpd30BppRgbMode2 = 2
    SrcFpd24BppRgbMode0 = 3
    SrcFpd24BppRgbMode1 = 4
    SrcFpd30BppYcbCr444Mode0 = 5
    SrcFpd30BppYcbCr444Mode1 = 6
    SrcFpd30BppYcbCr444Mode2 = 7
    SrcFpd24BppYcbCr444Mode0 = 8
    SrcFpd24BppYcbCr444Mode1 = 9
    SrcFpd20BppYcbCr422Mode0 = 10
    SrcFpd20BppYcbCr422Mode1 = 11
    SrcFpd20BppYcbCr422Mode2 = 12
    SrcFpd16BppYcbCr422Mode0 = 13
    SrcFpd16BppYcbCr422Mode1 = 14

class DispfmtManualWarpTableUpdateModeCmdT(Enum):
    OverwriteMode = 0
    MergeMode = 1

class ActChannelT(Enum):
    ActChannel1 = 0
    ActChannel2 = 1

class DispBufferModeT(Enum):
    SingleBuffer = 0
    DoubleBuffer = 1
    RollingBuffer = 2

class DispXprEnableModeT(Enum):
    Auto = 0
    On = 1
    Off = 2

class CmdModeT(Enum):
    Bootloader = 0
    MainApplication = 1

class SysSourceTypeT(Enum):
    Srctype2D = 0
    Srctype3D = 1
    Srctype2Xpr = 2
    Srctype4Xpr = 3

class CmdAccessWidthT(Enum):
    Uint32 = 0
    Uint16 = 1
    Uint08 = 2

class Src3DlrGenerationT(Enum):
    SwGeneration = 0
    HwGeneration = 1

class CmdSwitchTypeT(Enum):
    ToBoot = 0
    ToAppViaReset = 1
    ToAppDirect = 2
    ToAppSecBoot = 3

class Tmp411TempSensorT(Enum):
    LocalTempSensor = 0
    RemoteTempSensor = 1

class SeqSequenceTypeT(Enum):
    MultiBitSequence = 0
    OneBitSequence = 1
    Unknown = 2

class DpHdrMode(Enum):
    Auto = 0
    Manual = 1

class SeqSyncModeT(Enum):
    SyncVrrMode = 0
    AsyncVrrMode = 1

class DispCurtainColorT(Enum):
    Black = 0
    Red = 1
    Green = 2
    Blue = 3
    Cyan = 4
    Magenta = 5
    Yellow = 6
    White = 7

class XprMdtVfilterModeT(Enum):
    MaxFilter = 0
    LowPassFilter = 1
    HybridFilter = 2

class WpcLedColorT(Enum):
    Red = 0
    Green = 1
    Blue = 2

class DispfmtManualWarpMapPointsTypeCmdT(Enum):
    EvenlySampledPointsByRowsAndColumns = 0
    UserDefinedAll32X18Points = 1

class HdrTransferFnT(Enum):
    TradGamSdr = 0
    TradGamHdr = 1
    Pq = 2
    Hlg = 3

class SeqRunningModeT(Enum):
    Synchronous = 0
    Asynchronous = 1

class I2CPortT(Enum):
    Port0 = 0
    Port1 = 1
    MaxPort = 2

class DdpHwBuildTypeT(Enum):
    Asic = 0
    EmuFe = 1
    EmuBe = 2
    EmuEnd2End = 3

class SrcDsiDataMapT(Enum):
    SrcDsi30BppRgb101010 = 0
    SrcDsi24BppRgb888 = 1
    SrcDsi18BppRgb666Config1 = 2
    SrcDsi18BppRgb666Config2 = 3
    SrcDsi16BppRgb565Config1 = 4
    SrcDsi16BppRgb565Config2 = 5
    SrcDsi16BppRgb565Config3 = 6
    SrcDsi20BppYcbCr422 = 7
    SrcDsi16BppYcbCr422 = 8

class Src3DFrameDominanceT(Enum):
    LeftFrameDominance = 0
    RightFrameDominance = 1

class SplashPixelFormatT(Enum):
    Rgb56516Bit = 0
    YcrCb42216Bit = 1
    Rgb88824Bit = 2

class FastXyShiftModeT(Enum):
    Disabled = 0
    Immediate = 1
    PreplannedShift = 2

class SrcFpdOperationModeT(Enum):
    SingleportA = 0
    SingleportB = 1
    DualportEvenAOddB = 2
    DualportOddAEvenB = 3

class Summary:
    Command: str
    CommInterface: str
    Successful: bool

class ProtocolData:
    CommandDestination: int
    OpcodeLength: int
    BytesRead: int

class MemoryArray:
     StartAddress: int                      # int
     AddressIncrement: int                  # int
     AccessWidth: CmdAccessWidthT
     NumberOfWords: int                     # int
     NumberOfBytesPerWord: int              # int
     Data: bytearray

class SystemStatus:
     CwSpinning: bool
     CwPhaselock: bool
     CwFreqlock: bool
     Lamplit: bool
     MemTstPassed: bool
     FrameRateConvEn: bool
     SeqPhaselock: bool
     SeqFreqlock: bool
     SeqSearch: bool
     ScpcalEnable: bool
     VicalEnable: bool
     BccalEnable: bool
     SequenceErr: bool
     PixclkOor: bool
     SyncvalStat: bool
     UartPort0CommErr: bool
     UartPort1CommErr: bool
     UartPort2CommErr: bool
     SspPort0CommErr: bool
     SspPort1CommErr: bool
     SspPort2CommErr: bool
     I2CPort0CommErr: bool
     I2CPort1CommErr: bool
     I2CPort2CommErr: bool
     DlpcInitErr: bool
     LampHwErr: bool
     LampPprftout: bool
     NoFreqBinErr: bool
     Dlpa3000CommErr: bool
     UmcRefreshBwUnderflowErr: bool
     DmdInitErr: bool
     DmdPwrDownErr: bool
     SrcdefNotpresent: bool
     SeqbinNotpresent: bool
     ProductConfigurationFailed: bool
     TemporalDitherMaskNotLoading: bool
     SeqselErr: bool
     EepromInitFail: bool

class WpcCalibrationData:
     ChromaticX: int                        # int
     ChromaticY: int                        # int
     LuminanceY: int                        # int
     RedSensorOutput: int                   # int
     GreenSensorOutput: int                 # int
     BlueSensorOutput: int                  # int
     DutyCycle: float

class KeystoneCorners:
     TopLeftX: int                          # int
     TopLeftY: int                          # int
     TopRightX: int                         # int
     TopRightY: int                         # int
     BottomLeftX: int                       # int
     BottomLeftY: int                       # int
     BottomRightX: int                      # int
     BottomRightY: int                      # int

class SourceTimingsAndErrors:
     PixelClockRate: int                    # int
     ActivePixelsPerLine: int               # int
     ActiveLinesPerFrame: int               # int
     FrameRate: int                         # int
     HSyncRate: int                         # int
     VerticalFrontPorch: int                # int
     VerticalBackPorch: int                 # int
     HorizFrontPorch: int                   # int
     HorizBackPorch: int                    # int
     TotalPixelsPerLine: int                # int
     TotalLinesPerFrame: int                # int
     InvalidAppl: bool
     InvalidAlpf: bool
     InvalidHorizontalBlanking: bool
     InvalidVerticalBlanking: bool
     InvalidHsyncWidth: bool
     InvalidVsyncWidth: bool
     InvalidClock: bool
     UnstableTppl: bool
     UnstableActiveArea: bool
     SystemMeasurementError: bool

class ColorDutyCycles:
     RedDutyCycle: float
     GreenDutyCycle: float
     BlueDutyCycle: float
     YellowDutyCycle: float
     CyanDutyCycle: float
     BlackDutyCycle: float

class HdrSourceConfiguration:
     Enable: bool
     TransferFunction: HdrTransferFnT
     MasterDisplayBlackLevel: float
     MasterDisplayWhiteLevel: float
     MasterDisplayColorGamutRedX: float
     MasterDisplayColorGamutRedY: float
     MasterDisplayColorGamutGreenX: float
     MasterDisplayColorGamutGreenY: float
     MasterDisplayColorGamutBlueX: float
     MasterDisplayColorGamutBlueY: float
     MasterDisplayColorGamutWhiteX: float
     MasterDisplayColorGamutWhiteY: float

class LedCurrents:
     Red1Level: int                         # int
     Green1Level: int                       # int
     Blue1Level: int                        # int
     IrRed2Level: int                       # int
     UvGreen2Level: int                     # int
     Blue2Level: int                        # int

class ImageCcaCoordinates:
     OrigCoordsRedX: float
     OrigCoordsRedY: float
     OrigCoordsRedLum: float
     OrigCoordsGreenX: float
     OrigCoordsGreenY: float
     OrigCoordsGreenLum: float
     OrigCoordsBlueX: float
     OrigCoordsBlueY: float
     OrigCoordsBlueLum: float
     OrigCoordsWhiteX: float
     OrigCoordsWhiteY: float
     OrigCoordsWhiteLum: float
     TargetCoordsRedX: float
     TargetCoordsRedY: float
     TargetCoordsRedGain: float
     TargetCoordsGreenX: float
     TargetCoordsGreenY: float
     TargetCoordsGreenGain: float
     TargetCoordsBlueX: float
     TargetCoordsBlueY: float
     TargetCoordsBlueGain: float
     TargetCoordsCyanX: float
     TargetCoordsCyanY: float
     TargetCoordsCyanGain: float
     TargetCoordsMagentaX: float
     TargetCoordsMagentaY: float
     TargetCoordsMagentaGain: float
     TargetCoordsYellowX: float
     TargetCoordsYellowY: float
     TargetCoordsYellowGain: float
     TargetCoordsWhiteX: float
     TargetCoordsWhiteY: float
     TargetCoordsWhiteGain: float

class ImageHsg:
     HsgRedGain: float
     HsgRedSaturation: float
     HsgRedHue: float
     HsgGreenGain: float
     HsgGreenSaturation: float
     HsgGreenHue: float
     HsgBlueGain: float
     HsgBlueSaturation: float
     HsgBlueHue: float
     HsgCyanGain: float
     HsgCyanSaturation: float
     HsgCyanHue: float
     HsgMagentaGain: float
     HsgMagentaSaturation: float
     HsgMagentaHue: float
     HsgYellowGain: float
     HsgYellowSaturation: float
     HsgYellowHue: float
     HsgWhiteRedGain: float
     HsgWhiteGreenGain: float
     HsgWhiteBlueGain: float

class DebugLogOptions:
     Sequence: bool
     Ite: bool
     Communication: bool
     ThreeD: bool
     MsgServers: bool
     Environment: bool
     Illum: bool
     System: bool
     Eeprom: bool
     Dpath: bool
     Usb: bool
     RtosMailbox: bool
     LogsOnUsb: bool

class SequenceDebugInformation:
     SequenceType: SeqSequenceTypeT
     SeqMode: SeqRunningModeT
     FrameRateBinIndex: int                 # int
     SequenceVectorOrderInfoIndex: int      # int
     Enabled: int                           # int
     DutyCycle: float
     ColorTime: int                         # int
     ColorCycles: int                       # int
     IllumDefIndex: int                     # int
     ColorTimeBinIndex: int                 # int
     MiniSequenceIndex: int                 # int
     CwaIndex: int                          # int
     BpdlutIndex: int                       # int
     BpdOffset: int                         # int
     NumberOfBitplanes: int                 # int

class I2CPassthrough:
     Port: I2CPortT
     Is7Bit: int                            # int
     HasSubaddr: int                        # int
     ClockRate: int                         # int
     DeviceAddress: int                     # int
     SubAddr: bytearray
     DataBytes: bytearray

class SmoothWarpTable:
     TopLeftX: int                          # int
     TopLeftY: int                          # int
     TopCenterX: int                        # int
     TopCenterY: int                        # int
     TopRightX: int                         # int
     TopRightY: int                         # int
     MidLeftX: int                          # int
     MidLeftY: int                          # int
     MidCenterX: int                        # int
     MidCenterY: int                        # int
     MidRightX: int                         # int
     MidRightY: int                         # int
     BotLeftX: int                          # int
     BotLeftY: int                          # int
     BotCenterX: int                        # int
     BotCenterY: int                        # int
     BotRightX: int                         # int
     BotRightY: int                         # int

_readcommand = None
_writecommand = None

def DLPC8430init(readcommandcb, writecommandcb):
    global _readcommand
    global _writecommand
    _readcommand = readcommandcb
    _writecommand = writecommandcb

    global Summary
    Summary.CommInterface = "DLPC8430"

    global PortocolData
    ProtocolData.CommandDestination = 0
    ProtocolData.OpcodeLength = 0
    ProtocolData.BytesRead = 0

def ReadMode():
    "This command returns whether the controller software being executed is the Bootloader or Main Application <br>"
    global Summary
    Summary.Command = "Read Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 1;
    try:
        writebytes=list(struct.pack('B',0))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        AppModeObj = getbits(2, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, CmdModeT(AppModeObj)

def ReadSoftwareVersion():
    "This command reads the main application software version residing in the controller. <br>"
    global Summary
    Summary.Command = "Read Software Version"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 1;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(3, writebytes, ProtocolData)
        Major = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        Minor = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        Patch = struct.unpack_from ('B', bytearray(readbytes), 2)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Major, Minor, Patch

def WriteSwitchMode(SwitchMode):
    "This command is used to switch between bootloader and application mode. <br>"
    global Summary
    Summary.Command = "Write Switch Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 1;
    try:
        writebytes=list(struct.pack('B',2))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',SwitchMode.value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadExtendedSoftwareVersion():
    "This command returns the Pre Release Info and Commit ID of software version residing in the controller. <br>"
    global Summary
    Summary.Command = "Read Extended Software Version"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 1;
    try:
        writebytes=list(struct.pack('B',4))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(10, writebytes, ProtocolData)
        PreReleaseName = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        PreReleaseVersion = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        TestBuildNumber = struct.unpack_from ('B', bytearray(readbytes), 2)[0]
        CommitId = str(bytearray(readbytes), encoding)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, PreReleaseName, PreReleaseVersion, TestBuildNumber, CommitId

def WriteMemory(Address,  Value):
    "This command attempts a direct write of the given 32-bit value to the given 32-bit memory address. The memory address is not verified whether it is valid to write to the location. <br>"
    global Summary
    Summary.Command = "Write Memory"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 1;
    try:
        writebytes=list(struct.pack('B',16))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('I',Address)))
        writebytes.extend(list(struct.pack('I',Value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadMemory(Address):
    "This command returns the 32-bit value stored at the given 32-bit memory address. <br>"
    global Summary
    Summary.Command = "Read Memory"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 1;
    try:
        writebytes=list(struct.pack('B',16))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('I',Address)))
        readbytes = _readcommand(4, writebytes, ProtocolData)
        Value = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Value

def WriteMemoryArray(MemoryArray):
    "Writes a stream of words into the RAM memory (DRAM or IRAM) starting from the address specified. Performs no checks as to whether the specified memory address given is valid or not. <br>"
    global Summary
    Summary.Command = "Write Memory Array"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 1;
    try:
        writebytes=list(struct.pack('B',17))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('I',MemoryArray.StartAddress)))
        packerinit()
        value = setbits(int(MemoryArray.AddressIncrement), 6, 0)
        value = setbits(MemoryArray.AccessWidth.value, 2, 6)
        writebytes.extend(list(struct.pack('B',value)))
        writebytes.extend(list(struct.pack('H',MemoryArray.NumberOfWords)))
        writebytes.extend(list(struct.pack('B',MemoryArray.NumberOfBytesPerWord)))
        writebytes.extend(list(MemoryArray.Data))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadMemoryArray(StartAddress,  AddressIncrement,  AccessWidth,  NumberOfWords,  NumberOfBytesPerWord):
    "Reads a stream of words from memory starting from the address specified. Performs no checks as to whether the specified memory address given is valid or not. <br>"
    global Summary
    Summary.Command = "Read Memory Array"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 1;
    try:
        writebytes=list(struct.pack('B',17))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('I',StartAddress)))
        packerinit()
        value = setbits(int(AddressIncrement), 6, 0)
        value = setbits(AccessWidth.value, 2, 6)
        writebytes.extend(list(struct.pack('B',value)))
        writebytes.extend(list(struct.pack('H',NumberOfWords)))
        writebytes.extend(list(struct.pack('B',NumberOfBytesPerWord)))
        readbytes = _readcommand(0, writebytes, ProtocolData)
        Data = bytearray(readbytes)[0, 1]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Data

def ReadControllerId():
    "This command returns the device ID for the controller(s). <br>"
    global Summary
    Summary.Command = "Read Controller Id"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',16))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        ControllerId = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ControllerId

def ReadDmdInfo():
    "Returns the dmd information. <br>"
    global Summary
    Summary.Command = "Read Dmd Info"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',17))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(16, writebytes, ProtocolData)
        FirstDmdDeviceId = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        FirstDmdFuseId = struct.unpack_from ('I', bytearray(readbytes), 4)[0]
        SecondDmdDeviceId = struct.unpack_from ('I', bytearray(readbytes), 8)[0]
        SecondDmdFuseId = struct.unpack_from ('I', bytearray(readbytes), 12)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, FirstDmdDeviceId, FirstDmdFuseId, SecondDmdDeviceId, SecondDmdFuseId

def ReadSystemStatus():
    "Command to read status information from DLP Controller. If status interrupt is enabled (configurable via default UI tool in DLP Composer), reading back this command will acknowledge/deactivate the interrupt pin until the next change in status. <br>"
    global Summary
    Summary.Command = "Read System Status"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',18))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(12, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        SystemStatus.CwSpinning = getbits(1, 0);
        SystemStatus.CwPhaselock = getbits(1, 1);
        SystemStatus.CwFreqlock = getbits(1, 2);
        SystemStatus.Lamplit = getbits(1, 3);
        SystemStatus.MemTstPassed = getbits(1, 4);
        SystemStatus.FrameRateConvEn = getbits(1, 10);
        SystemStatus.SeqPhaselock = getbits(1, 11);
        SystemStatus.SeqFreqlock = getbits(1, 12);
        SystemStatus.SeqSearch = getbits(1, 13);
        SystemStatus.ScpcalEnable = getbits(1, 29);
        SystemStatus.VicalEnable = getbits(1, 30);
        SystemStatus.BccalEnable = getbits(1, 31);
        readdata = struct.unpack_from ('I', bytearray(readbytes), 4)[0]
        packerinit(readdata)
        SystemStatus.SequenceErr = getbits(1, 0);
        SystemStatus.PixclkOor = getbits(1, 1);
        SystemStatus.SyncvalStat = getbits(1, 2);
        SystemStatus.UartPort0CommErr = getbits(1, 6);
        SystemStatus.UartPort1CommErr = getbits(1, 7);
        SystemStatus.UartPort2CommErr = getbits(1, 8);
        SystemStatus.SspPort0CommErr = getbits(1, 9);
        SystemStatus.SspPort1CommErr = getbits(1, 10);
        SystemStatus.SspPort2CommErr = getbits(1, 11);
        SystemStatus.I2CPort0CommErr = getbits(1, 12);
        SystemStatus.I2CPort1CommErr = getbits(1, 13);
        SystemStatus.I2CPort2CommErr = getbits(1, 14);
        SystemStatus.DlpcInitErr = getbits(1, 15);
        SystemStatus.LampHwErr = getbits(1, 16);
        SystemStatus.LampPprftout = getbits(1, 17);
        SystemStatus.NoFreqBinErr = getbits(1, 19);
        SystemStatus.Dlpa3000CommErr = getbits(1, 20);
        SystemStatus.UmcRefreshBwUnderflowErr = getbits(1, 21);
        SystemStatus.DmdInitErr = getbits(1, 22);
        SystemStatus.DmdPwrDownErr = getbits(1, 23);
        SystemStatus.SrcdefNotpresent = getbits(1, 24);
        SystemStatus.SeqbinNotpresent = getbits(1, 25);
        SystemStatus.ProductConfigurationFailed = getbits(1, 26);
        SystemStatus.TemporalDitherMaskNotLoading = getbits(1, 27);
        SystemStatus.SeqselErr = getbits(1, 28);
        readdata = struct.unpack_from ('I', bytearray(readbytes), 8)[0]
        packerinit(readdata)
        SystemStatus.EepromInitFail = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SystemStatus

def ReadFlashLayoutVersion():
    "Returns supported Layout revision numbers and hash for flash config and app config layout. <br>"
    global Summary
    Summary.Command = "Read Flash Layout Version"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',217))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(68, writebytes, ProtocolData)
        FlashCfgLayoutVersion = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        FlashCfgLayoutHash = str(bytearray(readbytes), encoding)
        AppCfgLayoutVersion = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        AppCfgLayoutHash = str(bytearray(readbytes), encoding)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, FlashCfgLayoutVersion, FlashCfgLayoutHash, AppCfgLayoutVersion, AppCfgLayoutHash

def WriteWpcCalibrationData(LedColor,  WpcCalibrationData):
    "Set the entire WPC sensor calibration data through this command. <br>"
    global Summary
    Summary.Command = "Write Wpc Calibration Data"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',178))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',LedColor.value)))
        writebytes.extend(list(struct.pack('H',WpcCalibrationData.ChromaticX)))
        writebytes.extend(list(struct.pack('H',WpcCalibrationData.ChromaticY)))
        writebytes.extend(list(struct.pack('I',WpcCalibrationData.LuminanceY)))
        writebytes.extend(list(struct.pack('I',WpcCalibrationData.RedSensorOutput)))
        writebytes.extend(list(struct.pack('I',WpcCalibrationData.GreenSensorOutput)))
        writebytes.extend(list(struct.pack('I',WpcCalibrationData.BlueSensorOutput)))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(WpcCalibrationData.DutyCycle,256)))))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadWpcCalibrationData(LedColor):
    "Gets WPC sensor calibration data through this command <br>"
    global Summary
    Summary.Command = "Read Wpc Calibration Data"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',178))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',LedColor.value)))
        readbytes = _readcommand(22, writebytes, ProtocolData)
        WpcCalibrationData.ChromaticX = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        WpcCalibrationData.ChromaticY = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        WpcCalibrationData.LuminanceY = struct.unpack_from ('I', bytearray(readbytes), 4)[0]
        WpcCalibrationData.RedSensorOutput = struct.unpack_from ('I', bytearray(readbytes), 8)[0]
        WpcCalibrationData.GreenSensorOutput = struct.unpack_from ('I', bytearray(readbytes), 12)[0]
        WpcCalibrationData.BlueSensorOutput = struct.unpack_from ('I', bytearray(readbytes), 16)[0]
        WpcCalibrationData.DutyCycle = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 20)[0], 256)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, WpcCalibrationData

def WriteXprCalibrationMode(Enable):
    "This command enables an image processing bypass mode for use during XPR calibration. This command causes the controller to bypass all image processing including XPR image processing and establishes a one-to-one correspondence between source image pixels and the mirrors on the DMD. This mode is useful for seeing clear splits between XPR subframes when performing XPR calibration. XPR calibration is needed to assure the mechanical actuator has optimal alignment when the system displays each spatially-shifted subframe image. <br>"
    global Summary
    Summary.Command = "Write Xpr Calibration Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',179))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(Enable), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteXprActuatorPosition(PositionNumber):
    "This command sets the position of the XPR mechanical actuator for calibration purposes. There are 24 possible mechanical positions. Use this command while performing XPR calibration using a TI-provided XPR calibration splash image. For this command to take effect, command Set XPR Calibration Mode must be set to enable. <br>"
    global Summary
    Summary.Command = "Write Xpr Actuator Position"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',180))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',PositionNumber)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadXprActuatorPosition():
    "This command sets the position of the XPR mechanical actuator for calibration purposes. There are 24 possible mechanical positions. Use this command while performing XPR calibration using a TI-provided XPR calibration splash image. For this command to take effect, command Set XPR Calibration Mode must be set to enable. <br>"
    global Summary
    Summary.Command = "Read Xpr Actuator Position"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',180))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        PositionNumber = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, PositionNumber

def WriteInputImageSize(PixelsPerLine,  LinesPerFrame):
    "This command sets the input image size. <br>"
    global Summary
    Summary.Command = "Write Input Image Size"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',32))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',PixelsPerLine)))
        writebytes.extend(list(struct.pack('H',LinesPerFrame)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadInputImageSize():
    "This command gets the input image size. <br>"
    global Summary
    Summary.Command = "Read Input Image Size"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',32))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        PixelsPerLine = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        LinesPerFrame = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, PixelsPerLine, LinesPerFrame

def WriteImageCrop(CaptureStartPixel,  CaptureStartLine,  PixelsPerLine,  LinesPerFrame):
    "This command specifies the cropping applied to input images prior to controller image processing <br>"
    global Summary
    Summary.Command = "Write Image Crop"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',33))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',CaptureStartPixel)))
        writebytes.extend(list(struct.pack('H',CaptureStartLine)))
        writebytes.extend(list(struct.pack('H',PixelsPerLine)))
        writebytes.extend(list(struct.pack('H',LinesPerFrame)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadImageCrop():
    "This command specifies the cropping applied to input images prior to controller image processing <br>"
    global Summary
    Summary.Command = "Read Image Crop"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',33))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(8, writebytes, ProtocolData)
        CaptureStartPixel = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        CaptureStartLine = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        PixelsPerLine = struct.unpack_from ('H', bytearray(readbytes), 4)[0]
        LinesPerFrame = struct.unpack_from ('H', bytearray(readbytes), 6)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, CaptureStartPixel, CaptureStartLine, PixelsPerLine, LinesPerFrame

def WriteDisplaySize(StartPixel,  StartLine,  PixelsPerLine,  LinesPerFrame):
    "This command specifies the size of the displayed image"
    global Summary
    Summary.Command = "Write Display Size"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',34))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',StartPixel)))
        writebytes.extend(list(struct.pack('H',StartLine)))
        writebytes.extend(list(struct.pack('H',PixelsPerLine)))
        writebytes.extend(list(struct.pack('H',LinesPerFrame)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDisplaySize():
    "This command specifies the size of the displayed image <br>"
    global Summary
    Summary.Command = "Read Display Size"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',34))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(8, writebytes, ProtocolData)
        StartPixel = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        StartLine = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        PixelsPerLine = struct.unpack_from ('H', bytearray(readbytes), 4)[0]
        LinesPerFrame = struct.unpack_from ('H', bytearray(readbytes), 6)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, StartPixel, StartLine, PixelsPerLine, LinesPerFrame

def WriteDisplayImageOrientation(Rotation,  LongAxisImageFlip,  ShortAxisImageFlip):
    "This command specifies the orientation of the image displayed on the DMD <br>"
    global Summary
    Summary.Command = "Write Display Image Orientation"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',35))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(Rotation), 1, 0)
        value = setbits(int(LongAxisImageFlip), 1, 1)
        value = setbits(int(ShortAxisImageFlip), 1, 2)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDisplayImageOrientation():
    "This command specifies the orientation of the image displayed on the DMD <br>"
    global Summary
    Summary.Command = "Read Display Image Orientation"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',35))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        Rotation = getbits(1, 0);
        LongAxisImageFlip = getbits(1, 1);
        ShortAxisImageFlip = getbits(1, 2);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Rotation, LongAxisImageFlip, ShortAxisImageFlip

def WriteDisplayCurtain(Curtain,  Color):
    "This command controls the image curtain displayed on the DMD <br>"
    global Summary
    Summary.Command = "Write Display Curtain"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',36))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(Curtain), 1, 0)
        value = setbits(Color.value, 3, 1)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDisplayCurtain():
    "This command controls the image curtain displayed on the DMD <br>"
    global Summary
    Summary.Command = "Read Display Curtain"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',36))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        Curtain = getbits(1, 0);
        ColorObj = getbits(3, 1);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Curtain, DispCurtainColorT(ColorObj)

def WriteImageFreeze(Freeze):
    "This command freezes the image whereby the last image received is displayed in every subsequent frame <br>"
    global Summary
    Summary.Command = "Write Image Freeze"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',37))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(Freeze), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadImageFreeze():
    "This command freezes the image whereby the last image received is displayed in every subsequent frame <br>"
    global Summary
    Summary.Command = "Read Image Freeze"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',37))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        Freeze = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Freeze

def WriteBorderColor(Color):
    "This command specifies the border color displayed on the DMD <br>"
    global Summary
    Summary.Command = "Write Border Color"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',38))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(Color.value, 3, 0)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadBorderColor():
    "This command specifies the border color displayed on the DMD <br>"
    global Summary
    Summary.Command = "Read Border Color"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',38))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        ColorObj = getbits(3, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DispCurtainColorT(ColorObj)

def WriteXprEnableMode(Mode):
    "Xpr Set Enable Mode <br>"
    global Summary
    Summary.Command = "Write Xpr Enable Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',39))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Mode.value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadXprEnableMode():
    "Xpr Get Enable Mode <br>"
    global Summary
    Summary.Command = "Read Xpr Enable Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',39))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        ModeObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DispXprEnableModeT(ModeObj)

def WriteDisplayFeaturesControl(Feature,  Enable):
    "Set DISP Feature Enable <br>"
    global Summary
    Summary.Command = "Write Display Features Control"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',40))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Feature.value)))
        packerinit()
        value = setbits(int(Enable), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDisplayFeaturesControl(Feature):
    "Get DISP Feature Enable <br>"
    global Summary
    Summary.Command = "Read Display Features Control"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',40))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Feature.value)))
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        Enable = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Enable

def WriteWarpFunctionControl(Enable,  EnableSmoothOperation):
    "LCW Set Enable/Disable <br>"
    global Summary
    Summary.Command = "Write Warp Function Control"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',41))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(Enable), 1, 0)
        value = setbits(int(EnableSmoothOperation), 1, 1)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadWarpFunctionControl():
    "LCW Get Enable/Disable <br>"
    global Summary
    Summary.Command = "Read Warp Function Control"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',41))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        Enable = getbits(1, 0);
        EnableSmoothOperation = getbits(1, 1);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Enable, EnableSmoothOperation

def WriteVrrSyncMode(SyncMode):
    "This command sets the VRR sync mode when images are being received on an external video port. <br>"
    global Summary
    Summary.Command = "Write Vrr Sync Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',48))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',SyncMode.value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadVrrSyncMode():
    "This command gets the VRR sync mode when images are being received on an external video port. <br>"
    global Summary
    Summary.Command = "Read Vrr Sync Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',48))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        SyncModeObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SeqSyncModeT(SyncModeObj)

def WriteKeystoneAngles(Pitch,  Yaw,  Roll):
    "Configures the Keystone correction when the pitch, yaw & roll for the corrected image are known. Keystone correction is used to remove the distortion caused when the projector is not orthogonal to the projection surface (screen). <br>"
    global Summary
    Summary.Command = "Write Keystone Angles"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',192))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(Pitch,256)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(Yaw,256)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(Roll,256)))))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadKeystoneAngles():
    "Returns the keystone configuration parameters currently set. <br>"
    global Summary
    Summary.Command = "Read Keystone Angles"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',192))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(6, writebytes, ProtocolData)
        Pitch = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 0)[0], 256)
        Yaw = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 2)[0], 256)
        Roll = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 4)[0], 256)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Pitch, Yaw, Roll

def WriteOpticalParameters(ThrowRatio,  VerticalOffset):
    "Configures the Optical Parameters for the Keystone correction when the Throw Ratio & the Vertical Offset for the projector are known. <br>"
    global Summary
    Summary.Command = "Write Optical Parameters"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',193))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ThrowRatio,256)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(VerticalOffset,256)))))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadOpticalParameters():
    "Returns the optical parameters currently set. <br>"
    global Summary
    Summary.Command = "Read Optical Parameters"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',193))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        ThrowRatio = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 0)[0], 256)
        VerticalOffset = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 2)[0], 256)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ThrowRatio, VerticalOffset

def WriteKeystoneCorners(KeystoneCorners):
    "Configures the 2D Keystone correction when the corners of the corrected image are known. Keystone correction is used to remove the distortion caused when the projector is not orthogonal to the projection surface (screen). For the effects to take place, the Keystone feature has to be enabled. Command CMD_EnableKeystone() should be called to enable the keystone feature. <br>"
    global Summary
    Summary.Command = "Write Keystone Corners"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',194))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',KeystoneCorners.TopLeftX)))
        writebytes.extend(list(struct.pack('H',KeystoneCorners.TopLeftY)))
        writebytes.extend(list(struct.pack('H',KeystoneCorners.TopRightX)))
        writebytes.extend(list(struct.pack('H',KeystoneCorners.TopRightY)))
        writebytes.extend(list(struct.pack('H',KeystoneCorners.BottomLeftX)))
        writebytes.extend(list(struct.pack('H',KeystoneCorners.BottomLeftY)))
        writebytes.extend(list(struct.pack('H',KeystoneCorners.BottomRightX)))
        writebytes.extend(list(struct.pack('H',KeystoneCorners.BottomRightY)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadKeystoneCorners():
    "Returns the keystone configuration parameters currently set. This command should be used when the keystone correction has been configured using the four corners of the corrected image. The keystone correction is observed only if the keystone feature is enabled, even if the parameters are configured correctly. <br>"
    global Summary
    Summary.Command = "Read Keystone Corners"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',194))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(16, writebytes, ProtocolData)
        KeystoneCorners.TopLeftX = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        KeystoneCorners.TopLeftY = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        KeystoneCorners.TopRightX = struct.unpack_from ('H', bytearray(readbytes), 4)[0]
        KeystoneCorners.TopRightY = struct.unpack_from ('H', bytearray(readbytes), 6)[0]
        KeystoneCorners.BottomLeftX = struct.unpack_from ('H', bytearray(readbytes), 8)[0]
        KeystoneCorners.BottomLeftY = struct.unpack_from ('H', bytearray(readbytes), 10)[0]
        KeystoneCorners.BottomRightX = struct.unpack_from ('H', bytearray(readbytes), 12)[0]
        KeystoneCorners.BottomRightY = struct.unpack_from ('H', bytearray(readbytes), 14)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, KeystoneCorners

def WriteFastXyShiftMode(Mode,  AutoClear):
    "This command specifies whether the Fast XY Shift feature uses Immediate Shift mode or Planned Shift mode <br>"
    global Summary
    Summary.Command = "Write Fast Xy Shift Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',240))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(Mode.value, 2, 0)
        value = setbits(int(AutoClear), 1, 7)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadFastXyShiftMode():
    "This command specifies whether the Fast XY Shift feature uses Immediate Shift mode or Planned Shift mode <br>"
    global Summary
    Summary.Command = "Read Fast Xy Shift Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',240))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        ModeObj = getbits(2, 0);
        AutoClear = getbits(1, 7);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, FastXyShiftModeT(ModeObj), AutoClear

def WriteXyShiftTimes(Times):
    "This command assigns the shift times for the Fast XY Shift feature when using Planned Shift mode <br>"
    global Summary
    Summary.Command = "Write Xy Shift Times"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',241))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(Times))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadXyShiftTimes():
    "This command assigns the shift times for the Fast XY Shift feature when using Planned Shift mode <br>"
    global Summary
    Summary.Command = "Read Xy Shift Times"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',241))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(32, writebytes, ProtocolData)
        Times = bytearray(readbytes)[0, 32]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Times

def WriteXyShiftPosition(X,  Y):
    "This SPI command sets the amount of x,y position shift to be applied when using the Fast XY Shift feature <br>"
    global Summary
    Summary.Command = "Write Xy Shift Position"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',242))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('b',X)))
        writebytes.extend(list(struct.pack('b',Y)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadXyShiftCurrentPosition():
    "This SPI command gets the amount of x,y position shift applied when using the Fast XY Shift feature <br>"
    global Summary
    Summary.Command = "Read Xy Shift Current Position"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',243))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(2, writebytes, ProtocolData)
        X = struct.unpack_from ('b', bytearray(readbytes), 0)[0]
        Y = struct.unpack_from ('b', bytearray(readbytes), 1)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, X, Y

def WriteCheckoutModeInternal(Enable):
    "This command specifies whether the Fast XY Shift debug mode is used <br>"
    global Summary
    Summary.Command = "Write Checkout Mode Internal"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',244))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(Enable), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadCheckoutModeInternal():
    "This command specifies whether the Fast XY Shift debug mode is used <br>"
    global Summary
    Summary.Command = "Read Checkout Mode Internal"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',244))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        Enable = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Enable

def WritePreplannedFifoInternal(Count,  Positions):
    "This command controls pre-planned FIFO used for debug mode. It is 2 byte aligned <br>"
    global Summary
    Summary.Command = "Write Preplanned Fifo Internal"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',245))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Count)))
        writebytes.extend(list(Positions))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadPreplannedFifoInternal():
    "This command controls pre-planned FIFO used for debug mode. It is 2 byte aligned <br>"
    global Summary
    Summary.Command = "Read Preplanned Fifo Internal"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',245))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(65, writebytes, ProtocolData)
        Count = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        Positions = bytearray(readbytes)[1, 65]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Count, Positions

def WriteXyMarginInternal(X,  Y):
    "This command controls the amount of x,y margin <br>"
    global Summary
    Summary.Command = "Write Xy Margin Internal"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',246))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',X)))
        writebytes.extend(list(struct.pack('B',Y)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadXyMarginInternal():
    "This command controls the amount of x,y margin <br>"
    global Summary
    Summary.Command = "Read Xy Margin Internal"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',246))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(2, writebytes, ProtocolData)
        X = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        Y = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, X, Y

def WriteInputSource(Source):
    "Displays the specified source. <br>"
    global Summary
    Summary.Command = "Write Input Source"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',5))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Source.value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadInputSource():
    "Returns the source which is currently being displayed. <br>"
    global Summary
    Summary.Command = "Read Input Source"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',5))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        SourceObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DpDisplaySourceT(SourceObj)

def ReadSystemSourceStatus():
    "Returns the status of video source in the system <br>"
    global Summary
    Summary.Command = "Read System Source Status"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',6))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        SystemStateObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DpStateT(SystemStateObj)

def ReadSourceTimingsAndErrors():
    "Returns the timings of the displayed Source and any errors detected in the timings <br>"
    global Summary
    Summary.Command = "Read Source Timings And Errors"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',7))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(28, writebytes, ProtocolData)
        SourceTimingsAndErrors.PixelClockRate = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        SourceTimingsAndErrors.ActivePixelsPerLine = struct.unpack_from ('H', bytearray(readbytes), 4)[0]
        SourceTimingsAndErrors.ActiveLinesPerFrame = struct.unpack_from ('H', bytearray(readbytes), 6)[0]
        SourceTimingsAndErrors.FrameRate = struct.unpack_from ('H', bytearray(readbytes), 8)[0]
        SourceTimingsAndErrors.HSyncRate = struct.unpack_from ('I', bytearray(readbytes), 10)[0]
        SourceTimingsAndErrors.VerticalFrontPorch = struct.unpack_from ('H', bytearray(readbytes), 14)[0]
        SourceTimingsAndErrors.VerticalBackPorch = struct.unpack_from ('H', bytearray(readbytes), 16)[0]
        SourceTimingsAndErrors.HorizFrontPorch = struct.unpack_from ('H', bytearray(readbytes), 18)[0]
        SourceTimingsAndErrors.HorizBackPorch = struct.unpack_from ('H', bytearray(readbytes), 20)[0]
        SourceTimingsAndErrors.TotalPixelsPerLine = struct.unpack_from ('H', bytearray(readbytes), 22)[0]
        SourceTimingsAndErrors.TotalLinesPerFrame = struct.unpack_from ('H', bytearray(readbytes), 24)[0]
        readdata = struct.unpack_from ('H', bytearray(readbytes), 26)[0]
        packerinit(readdata)
        SourceTimingsAndErrors.InvalidAppl = getbits(1, 0);
        SourceTimingsAndErrors.InvalidAlpf = getbits(1, 1);
        SourceTimingsAndErrors.InvalidHorizontalBlanking = getbits(1, 2);
        SourceTimingsAndErrors.InvalidVerticalBlanking = getbits(1, 3);
        SourceTimingsAndErrors.InvalidHsyncWidth = getbits(1, 4);
        SourceTimingsAndErrors.InvalidVsyncWidth = getbits(1, 5);
        SourceTimingsAndErrors.InvalidClock = getbits(1, 6);
        SourceTimingsAndErrors.UnstableTppl = getbits(1, 7);
        SourceTimingsAndErrors.UnstableActiveArea = getbits(1, 8);
        SourceTimingsAndErrors.SystemMeasurementError = getbits(1, 9);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SourceTimingsAndErrors

def WriteFpdConfiguration(OperationMode,  Datamap,  PixelClockFreqRange):
    "Configures the characteristics of the FPD source. <br>"
    global Summary
    Summary.Command = "Write Fpd Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',8))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',OperationMode.value)))
        writebytes.extend(list(struct.pack('B',Datamap.value)))
        writebytes.extend(list(struct.pack('B',PixelClockFreqRange.value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadFpdConfiguration():
    "Retruns the characteristics of the FPD source. <br>"
    global Summary
    Summary.Command = "Read Fpd Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',8))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(3, writebytes, ProtocolData)
        OperationModeObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        DatamapObj = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        PixelClockFreqRangeObj = struct.unpack_from ('B', bytearray(readbytes), 2)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SrcFpdOperationModeT(OperationModeObj), SrcFpdDataMapT(DatamapObj), SrcFpdFRangeT(PixelClockFreqRangeObj)

def WriteExternalSourceSyncPolarity(IsManualPolarityDetection,  IsVSyncActiveHigh,  IsHSyncActiveHigh):
    "Sets the input polarity detection mode for VSync and HSync signals for all external sources. Controller requires Sync signals to have active-high polarity. It can auto-detect and correct the polarity. User should choose Automatic mode to use this feature. This is the default mode. Otherwise, user can choose manual mode and provide the input polarities. The provided input polarities take effect only in manual mode. It will be used by hardware to correct the polarities. <br>"
    global Summary
    Summary.Command = "Write External Source Sync Polarity"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',9))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(IsManualPolarityDetection), 1, 0)
        value = setbits(int(IsVSyncActiveHigh), 1, 1)
        value = setbits(int(IsHSyncActiveHigh), 1, 2)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadExternalSourceSyncPolarity():
    "Gets the input polarity detection mode for VSync and HSync signals for all external sources. For Automatic Mode, it will return the polarities detected by the hardware as current VSync and HSync Polarity. For Manual Mode, it will return the polarities provided by the user. <br>"
    global Summary
    Summary.Command = "Read External Source Sync Polarity"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',9))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        IsManualPolarityDetection = getbits(1, 0);
        IsVSyncActiveHigh = getbits(1, 1);
        IsHSyncActiveHigh = getbits(1, 2);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, IsManualPolarityDetection, IsVSyncActiveHigh, IsHSyncActiveHigh

def WriteSystemLookIndex(LookIndex):
    "This command attempts a Write Look Select value by the user which will trigger to sequence selection. The value should be between 0 and 65535 <br>"
    global Summary
    Summary.Command = "Write System Look Index"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',13))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',LookIndex)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadSystemLookIndex():
    "This command returns current Look Index value for the Sequence selection. <br>"
    global Summary
    Summary.Command = "Read System Look Index"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',13))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(2, writebytes, ProtocolData)
        LookIndex = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, LookIndex

def WriteColorDutyCycles(ColorDutyCycles):
    "This command defines duty cycles for illumination light colors and for an optional dark time at the end of frames. Values in the 8.8 fixed point format. <br>"
    global Summary
    Summary.Command = "Write Color Duty Cycles"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',14))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('I',int(convertfloattofixed(ColorDutyCycles.RedDutyCycle,8388608)))))
        writebytes.extend(list(struct.pack('I',int(convertfloattofixed(ColorDutyCycles.GreenDutyCycle,8388608)))))
        writebytes.extend(list(struct.pack('I',int(convertfloattofixed(ColorDutyCycles.BlueDutyCycle,8388608)))))
        writebytes.extend(list(struct.pack('I',int(convertfloattofixed(ColorDutyCycles.YellowDutyCycle,8388608)))))
        writebytes.extend(list(struct.pack('I',int(convertfloattofixed(ColorDutyCycles.CyanDutyCycle,8388608)))))
        writebytes.extend(list(struct.pack('I',int(convertfloattofixed(ColorDutyCycles.BlackDutyCycle,8388608)))))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadColorDutyCycles():
    "This command defines duty cycles for illumination light colors and for an optional dark time at the end of frames. Values in the 8.8 fixed point format. <br>"
    global Summary
    Summary.Command = "Read Color Duty Cycles"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',14))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(24, writebytes, ProtocolData)
        ColorDutyCycles.RedDutyCycle = convertfixedtofloat(struct.unpack_from ('I', bytearray(readbytes), 0)[0], 8388608)
        ColorDutyCycles.GreenDutyCycle = convertfixedtofloat(struct.unpack_from ('I', bytearray(readbytes), 4)[0], 8388608)
        ColorDutyCycles.BlueDutyCycle = convertfixedtofloat(struct.unpack_from ('I', bytearray(readbytes), 8)[0], 8388608)
        ColorDutyCycles.YellowDutyCycle = convertfixedtofloat(struct.unpack_from ('I', bytearray(readbytes), 12)[0], 8388608)
        ColorDutyCycles.CyanDutyCycle = convertfixedtofloat(struct.unpack_from ('I', bytearray(readbytes), 16)[0], 8388608)
        ColorDutyCycles.BlackDutyCycle = convertfixedtofloat(struct.unpack_from ('I', bytearray(readbytes), 20)[0], 8388608)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ColorDutyCycles

def WriteTpgVrr(Enable,  MinFrameRate,  MaxFrameRate,  FrameRateStepSize,  NumFramesBetweenUpdate):
    "This command configures and enables the internal TPG functionality of the controller to simulate a variable refresh rate. <br>"
    global Summary
    Summary.Command = "Write Tpg Vrr"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',15))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Enable)))
        writebytes.extend(list(struct.pack('H',MinFrameRate)))
        writebytes.extend(list(struct.pack('H',MaxFrameRate)))
        writebytes.extend(list(struct.pack('B',FrameRateStepSize)))
        writebytes.extend(list(struct.pack('B',NumFramesBetweenUpdate)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadTpgVrr():
    "<br>"
    global Summary
    Summary.Command = "Read Tpg Vrr"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',15))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(7, writebytes, ProtocolData)
        Enable = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        MinFrameRate = struct.unpack_from ('H', bytearray(readbytes), 1)[0]
        MaxFrameRate = struct.unpack_from ('H', bytearray(readbytes), 3)[0]
        FrameRateStepSize = struct.unpack_from ('B', bytearray(readbytes), 5)[0]
        NumFramesBetweenUpdate = struct.unpack_from ('B', bytearray(readbytes), 6)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Enable, MinFrameRate, MaxFrameRate, FrameRateStepSize, NumFramesBetweenUpdate

def ReadFrameBufferMode():
    "This command gets the frame buffer mode <br>"
    global Summary
    Summary.Command = "Read Frame Buffer Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',21))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        ModeObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DispBufferModeT(ModeObj)

def WriteDsiConfiguration(DsiDataMapFormat,  SourcePixelsPerLine,  SourceLinesPerFrame):
    "Configures the characteristics of the DSI source. <br>"
    global Summary
    Summary.Command = "Write Dsi Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',22))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',DsiDataMapFormat.value)))
        writebytes.extend(list(struct.pack('H',SourcePixelsPerLine)))
        writebytes.extend(list(struct.pack('H',SourceLinesPerFrame)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDsiConfiguration():
    "Retruns the characteristics of the DSI source. <br>"
    global Summary
    Summary.Command = "Read Dsi Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',22))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(5, writebytes, ProtocolData)
        DsiDataMapFormatObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        SourcePixelsPerLine = struct.unpack_from ('H', bytearray(readbytes), 1)[0]
        SourceLinesPerFrame = struct.unpack_from ('H', bytearray(readbytes), 3)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SrcDsiDataMapT(DsiDataMapFormatObj), SourcePixelsPerLine, SourceLinesPerFrame

def WriteEnableThreeD(Enable3D,  DominantFrame,  ThreeDlrGenerationMode):
    "This command enable the 3D image handling and sync functionality in the controller. <br><br>"
    global Summary
    Summary.Command = "Write Enable Three D"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',23))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(Enable3D), 1, 0)
        value = setbits(DominantFrame.value, 2, 1)
        value = setbits(ThreeDlrGenerationMode.value, 2, 3)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadEnableThreeD():
    "This command reflect the current state of 3D image handling in the controller. <br>"
    global Summary
    Summary.Command = "Read Enable Three D"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',23))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        Enable3D = getbits(1, 0);
        DominantFrameObj = getbits(2, 1);
        ThreeDlrGenerationModeObj = getbits(2, 3);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Enable3D, Src3DFrameDominanceT(DominantFrameObj), Src3DlrGenerationT(ThreeDlrGenerationModeObj)

def WriteSplashScreenSelect(Index):
    "Sets splash image from the index provided. <br>"
    global Summary
    Summary.Command = "Write Splash Screen Select"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',96))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Index)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadSplashScreenSelect():
    "Gets splash image index. <br>"
    global Summary
    Summary.Command = "Read Splash Screen Select"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',96))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        Index = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Index

def WriteExecuteSplashScreen():
    "Loads splash image. <br>@retval PASS Successful"
    global Summary
    Summary.Command = "Write Execute Splash Screen"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',97))
        ProtocolData.OpcodeLength = 1;
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadSplashScreenHeader(Index):
    "Gets splash image header info from the index. <br>"
    global Summary
    Summary.Command = "Read Splash Screen Header"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',98))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Index)))
        readbytes = _readcommand(6, writebytes, ProtocolData)
        HorzRes = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        VertRes = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        PixelFormatObj = struct.unpack_from ('B', bytearray(readbytes), 4)[0]
        CompressionTypeObj = struct.unpack_from ('B', bytearray(readbytes), 5)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, HorzRes, VertRes, SplashPixelFormatT(PixelFormatObj), SplashCompressionT(CompressionTypeObj)

def WriteWpcEnable(Enable):
    "Enable/Disbale the WPC algorithm. WPC calibration data should be set before calling this command. <br>"
    global Summary
    Summary.Command = "Write Wpc Enable"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',99))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(Enable), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadWpcEnable():
    "Gets the enable status of WPC algorithm. <br>"
    global Summary
    Summary.Command = "Read Wpc Enable"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',99))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        Enable = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Enable

def ReadWpcCalcDutyCycle():
    "Gets calculated Duty Cycle for current Target Color Point. WPC should be enabled before calling this command. <br>"
    global Summary
    Summary.Command = "Read Wpc Calc Duty Cycle"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',100))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(6, writebytes, ProtocolData)
        RedDutyCycle = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 0)[0], 256)
        GreenDutyCycle = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 2)[0], 256)
        BlueDutyCycle = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 4)[0], 256)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, RedDutyCycle, GreenDutyCycle, BlueDutyCycle

def ReadWpcTargetColorPoint():
    "Gets the currently active target color point for WPC <br>"
    global Summary
    Summary.Command = "Read Wpc Target Color Point"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',101))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        X = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 0)[0], 65536)
        Y = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 2)[0], 65536)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, X, Y

def ReadWpcSensorOutput():
    "Returns output of Integrating Sensor for Red, Blue and Green. command."
    global Summary
    Summary.Command = "Read Wpc Sensor Output"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',102))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(12, writebytes, ProtocolData)
        Red = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        Green = struct.unpack_from ('I', bytearray(readbytes), 4)[0]
        Blue = struct.unpack_from ('I', bytearray(readbytes), 8)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Red, Green, Blue

def WriteHdrMode(HdrMode):
    "<br>"
    global Summary
    Summary.Command = "Write Hdr Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',160))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',HdrMode.value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadHdrMode():
    "<br>"
    global Summary
    Summary.Command = "Read Hdr Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',160))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        HdrModeObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DpHdrMode(HdrModeObj)

def WriteHdrSourceConfiguration(HdrSourceConfiguration):
    "<br>HDR maps wider brightness and color range of HDR sources to projector brightness and color range. The mapping requires multiple source groups and system groups define the HDR source and projection device properties respectively. This command sets the source properties and based on this information nearest source group is selected for mapping. <br>"
    global Summary
    Summary.Command = "Write Hdr Source Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',162))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(HdrSourceConfiguration.Enable), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        writebytes.extend(list(struct.pack('B',HdrSourceConfiguration.TransferFunction.value)))
        writebytes.extend(list(struct.pack('I',int(convertfloattofixed(HdrSourceConfiguration.MasterDisplayBlackLevel,65536)))))
        writebytes.extend(list(struct.pack('I',int(convertfloattofixed(HdrSourceConfiguration.MasterDisplayWhiteLevel,65536)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(HdrSourceConfiguration.MasterDisplayColorGamutRedX,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(HdrSourceConfiguration.MasterDisplayColorGamutRedY,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(HdrSourceConfiguration.MasterDisplayColorGamutGreenX,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(HdrSourceConfiguration.MasterDisplayColorGamutGreenY,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(HdrSourceConfiguration.MasterDisplayColorGamutBlueX,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(HdrSourceConfiguration.MasterDisplayColorGamutBlueY,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(HdrSourceConfiguration.MasterDisplayColorGamutWhiteX,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(HdrSourceConfiguration.MasterDisplayColorGamutWhiteY,32768)))))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadHdrSourceConfiguration():
    "<br>Includes the metadata information. <br>"
    global Summary
    Summary.Command = "Read Hdr Source Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',162))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(26, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        HdrSourceConfiguration.Enable = getbits(1, 0);
        HdrSourceConfiguration.TransferFunction = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        HdrSourceConfiguration.MasterDisplayBlackLevel = convertfixedtofloat(struct.unpack_from ('I', bytearray(readbytes), 2)[0], 65536)
        HdrSourceConfiguration.MasterDisplayWhiteLevel = convertfixedtofloat(struct.unpack_from ('I', bytearray(readbytes), 6)[0], 65536)
        HdrSourceConfiguration.MasterDisplayColorGamutRedX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 10)[0], 32768)
        HdrSourceConfiguration.MasterDisplayColorGamutRedY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 12)[0], 32768)
        HdrSourceConfiguration.MasterDisplayColorGamutGreenX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 14)[0], 32768)
        HdrSourceConfiguration.MasterDisplayColorGamutGreenY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 16)[0], 32768)
        HdrSourceConfiguration.MasterDisplayColorGamutBlueX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 18)[0], 32768)
        HdrSourceConfiguration.MasterDisplayColorGamutBlueY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 20)[0], 32768)
        HdrSourceConfiguration.MasterDisplayColorGamutWhiteX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 22)[0], 32768)
        HdrSourceConfiguration.MasterDisplayColorGamutWhiteY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 24)[0], 32768)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, HdrSourceConfiguration

def WriteHdrStrengthSetting(HdrStrength):
    "<br>Sets HDR strength which adjusts the electro-optical transfer function that is applied on the input HDR video signal. HDR strength can vary with the ambient brightness level.HDR strength is not applicable for HLG transfer function set by HDR source configuration. <br>"
    global Summary
    Summary.Command = "Write Hdr Strength Setting"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',163))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',HdrStrength)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadHdrStrengthSetting():
    "<br>"
    global Summary
    Summary.Command = "Read Hdr Strength Setting"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',163))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        HdrStrength = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, HdrStrength

def WriteSystemBrightnessRangeSetting(MinBrightness,  MaxBrightness):
    "<br>Sets the system brightness range in nits. These are used in determining the appropriate EOTF and OOTF function to be applied on the HDR source. This need to set only for HDR functionality. <br>"
    global Summary
    Summary.Command = "Write System Brightness Range Setting"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',164))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('I',int(convertfloattofixed(MinBrightness,65536)))))
        writebytes.extend(list(struct.pack('I',int(convertfloattofixed(MaxBrightness,65536)))))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadSystemBrightnessRangeSetting():
    "<br>"
    global Summary
    Summary.Command = "Read System Brightness Range Setting"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',164))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(8, writebytes, ProtocolData)
        MinBrightness = convertfixedtofloat(struct.unpack_from ('I', bytearray(readbytes), 0)[0], 65536)
        MaxBrightness = convertfixedtofloat(struct.unpack_from ('I', bytearray(readbytes), 4)[0], 65536)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, MinBrightness, MaxBrightness

def WriteLedEnable(Red,  Green,  Blue,  Ir,  Uv):
    "This command enables or disables the individual LEDs. If Dual LED drivers are present in the system, this command will enable or disable them together. For example, Enabling Red LED will enable both the Red LEDs present in the system. <br><br>"
    global Summary
    Summary.Command = "Write Led Enable"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',94))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(Red), 1, 0)
        value = setbits(int(Green), 1, 1)
        value = setbits(int(Blue), 1, 2)
        value = setbits(int(Ir), 1, 3)
        value = setbits(int(Uv), 1, 4)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadLedEnable():
    "This command returns if the LEDs are enabled or disabled. In dual driver system, both LEDs are enabled or disabled together and so the status returned by this command should be considered as the status of both LEDs (if present). <br><br>"
    global Summary
    Summary.Command = "Read Led Enable"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',94))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        Red = getbits(1, 0);
        Green = getbits(1, 1);
        Blue = getbits(1, 2);
        Ir = getbits(1, 3);
        Uv = getbits(1, 4);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Red, Green, Blue, Ir, Uv

def WriteLedCurrents(LedCurrents):
    "This command sets the drive levels for each LED. The drive levels are set only if the LED Channel is valid. Otherwise, the level setting is ignored. The drive levels are limited by the max and min levels specified for each channel in the system. For a dual RGB LED system, the drive level for each LED can be independently configured. <br>"
    global Summary
    Summary.Command = "Write Led Currents"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',95))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',LedCurrents.Red1Level)))
        writebytes.extend(list(struct.pack('H',LedCurrents.Green1Level)))
        writebytes.extend(list(struct.pack('H',LedCurrents.Blue1Level)))
        writebytes.extend(list(struct.pack('H',LedCurrents.IrRed2Level)))
        writebytes.extend(list(struct.pack('H',LedCurrents.UvGreen2Level)))
        writebytes.extend(list(struct.pack('H',LedCurrents.Blue2Level)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadLedCurrents():
    "This command gets the drive levels for each LED. For a dual RGB LED system, the drive level for each LED is returned . <br><br>"
    global Summary
    Summary.Command = "Read Led Currents"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',95))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(12, writebytes, ProtocolData)
        LedCurrents.Red1Level = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        LedCurrents.Green1Level = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        LedCurrents.Blue1Level = struct.unpack_from ('H', bytearray(readbytes), 4)[0]
        LedCurrents.IrRed2Level = struct.unpack_from ('H', bytearray(readbytes), 6)[0]
        LedCurrents.UvGreen2Level = struct.unpack_from ('H', bytearray(readbytes), 8)[0]
        LedCurrents.Blue2Level = struct.unpack_from ('H', bytearray(readbytes), 10)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, LedCurrents

def WriteImageCcaCoordinates(ImageCcaCoordinates):
    "This Command allows independent adjustment of the primary, secondary and white coordinates. This call will override any CCA settings performed by prior calls. <br>"
    global Summary
    Summary.Command = "Write Image Cca Coordinates"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',42))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.OrigCoordsRedX,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.OrigCoordsRedY,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.OrigCoordsRedLum,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.OrigCoordsGreenX,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.OrigCoordsGreenY,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.OrigCoordsGreenLum,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.OrigCoordsBlueX,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.OrigCoordsBlueY,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.OrigCoordsBlueLum,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.OrigCoordsWhiteX,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.OrigCoordsWhiteY,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.OrigCoordsWhiteLum,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.TargetCoordsRedX,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.TargetCoordsRedY,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.TargetCoordsRedGain,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.TargetCoordsGreenX,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.TargetCoordsGreenY,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.TargetCoordsGreenGain,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.TargetCoordsBlueX,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.TargetCoordsBlueY,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.TargetCoordsBlueGain,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.TargetCoordsCyanX,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.TargetCoordsCyanY,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.TargetCoordsCyanGain,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.TargetCoordsMagentaX,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.TargetCoordsMagentaY,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.TargetCoordsMagentaGain,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.TargetCoordsYellowX,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.TargetCoordsYellowY,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.TargetCoordsYellowGain,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.TargetCoordsWhiteX,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.TargetCoordsWhiteY,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.TargetCoordsWhiteGain,32768)))))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadImageCcaCoordinates():
    "Returns the current color coordinate configuration. <br>"
    global Summary
    Summary.Command = "Read Image Cca Coordinates"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',42))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(66, writebytes, ProtocolData)
        ImageCcaCoordinates.OrigCoordsRedX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 0)[0], 32768)
        ImageCcaCoordinates.OrigCoordsRedY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 2)[0], 32768)
        ImageCcaCoordinates.OrigCoordsRedLum = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 4)[0], 32768)
        ImageCcaCoordinates.OrigCoordsGreenX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 6)[0], 32768)
        ImageCcaCoordinates.OrigCoordsGreenY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 8)[0], 32768)
        ImageCcaCoordinates.OrigCoordsGreenLum = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 10)[0], 32768)
        ImageCcaCoordinates.OrigCoordsBlueX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 12)[0], 32768)
        ImageCcaCoordinates.OrigCoordsBlueY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 14)[0], 32768)
        ImageCcaCoordinates.OrigCoordsBlueLum = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 16)[0], 32768)
        ImageCcaCoordinates.OrigCoordsWhiteX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 18)[0], 32768)
        ImageCcaCoordinates.OrigCoordsWhiteY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 20)[0], 32768)
        ImageCcaCoordinates.OrigCoordsWhiteLum = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 22)[0], 32768)
        ImageCcaCoordinates.TargetCoordsRedX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 24)[0], 32768)
        ImageCcaCoordinates.TargetCoordsRedY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 26)[0], 32768)
        ImageCcaCoordinates.TargetCoordsRedGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 28)[0], 32768)
        ImageCcaCoordinates.TargetCoordsGreenX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 30)[0], 32768)
        ImageCcaCoordinates.TargetCoordsGreenY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 32)[0], 32768)
        ImageCcaCoordinates.TargetCoordsGreenGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 34)[0], 32768)
        ImageCcaCoordinates.TargetCoordsBlueX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 36)[0], 32768)
        ImageCcaCoordinates.TargetCoordsBlueY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 38)[0], 32768)
        ImageCcaCoordinates.TargetCoordsBlueGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 40)[0], 32768)
        ImageCcaCoordinates.TargetCoordsCyanX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 42)[0], 32768)
        ImageCcaCoordinates.TargetCoordsCyanY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 44)[0], 32768)
        ImageCcaCoordinates.TargetCoordsCyanGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 46)[0], 32768)
        ImageCcaCoordinates.TargetCoordsMagentaX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 48)[0], 32768)
        ImageCcaCoordinates.TargetCoordsMagentaY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 50)[0], 32768)
        ImageCcaCoordinates.TargetCoordsMagentaGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 52)[0], 32768)
        ImageCcaCoordinates.TargetCoordsYellowX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 54)[0], 32768)
        ImageCcaCoordinates.TargetCoordsYellowY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 56)[0], 32768)
        ImageCcaCoordinates.TargetCoordsYellowGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 58)[0], 32768)
        ImageCcaCoordinates.TargetCoordsWhiteX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 60)[0], 32768)
        ImageCcaCoordinates.TargetCoordsWhiteY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 62)[0], 32768)
        ImageCcaCoordinates.TargetCoordsWhiteGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 64)[0], 32768)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ImageCcaCoordinates

def WriteImageHsg(ImageHsg):
    "This command applies the given hue, saturation and gain values for all colors. It does not affect colors having a gain of zero. <br>Note: This call will override any CCA settings performed by prior calls. <br>"
    global Summary
    Summary.Command = "Write Image Hsg"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',43))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageHsg.HsgRedGain,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageHsg.HsgRedSaturation,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageHsg.HsgRedHue,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageHsg.HsgGreenGain,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageHsg.HsgGreenSaturation,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageHsg.HsgGreenHue,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageHsg.HsgBlueGain,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageHsg.HsgBlueSaturation,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageHsg.HsgBlueHue,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageHsg.HsgCyanGain,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageHsg.HsgCyanSaturation,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageHsg.HsgCyanHue,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageHsg.HsgMagentaGain,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageHsg.HsgMagentaSaturation,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageHsg.HsgMagentaHue,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageHsg.HsgYellowGain,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageHsg.HsgYellowSaturation,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageHsg.HsgYellowHue,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageHsg.HsgWhiteRedGain,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageHsg.HsgWhiteGreenGain,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageHsg.HsgWhiteBlueGain,16384)))))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadImageHsg():
    "This command returns the currently applied hue, saturation and gain values for all the colors. If gain for a color is zero then the HSG is not applied on the color. <br>"
    global Summary
    Summary.Command = "Read Image Hsg"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',43))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(42, writebytes, ProtocolData)
        ImageHsg.HsgRedGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 0)[0], 16384)
        ImageHsg.HsgRedSaturation = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 2)[0], 16384)
        ImageHsg.HsgRedHue = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 4)[0], 16384)
        ImageHsg.HsgGreenGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 6)[0], 16384)
        ImageHsg.HsgGreenSaturation = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 8)[0], 16384)
        ImageHsg.HsgGreenHue = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 10)[0], 16384)
        ImageHsg.HsgBlueGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 12)[0], 16384)
        ImageHsg.HsgBlueSaturation = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 14)[0], 16384)
        ImageHsg.HsgBlueHue = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 16)[0], 16384)
        ImageHsg.HsgCyanGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 18)[0], 16384)
        ImageHsg.HsgCyanSaturation = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 20)[0], 16384)
        ImageHsg.HsgCyanHue = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 22)[0], 16384)
        ImageHsg.HsgMagentaGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 24)[0], 16384)
        ImageHsg.HsgMagentaSaturation = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 26)[0], 16384)
        ImageHsg.HsgMagentaHue = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 28)[0], 16384)
        ImageHsg.HsgYellowGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 30)[0], 16384)
        ImageHsg.HsgYellowSaturation = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 32)[0], 16384)
        ImageHsg.HsgYellowHue = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 34)[0], 16384)
        ImageHsg.HsgWhiteRedGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 36)[0], 16384)
        ImageHsg.HsgWhiteGreenGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 38)[0], 16384)
        ImageHsg.HsgWhiteBlueGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 40)[0], 16384)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ImageHsg

def WriteGeneralDelayCommand(DelayInMilliseconds):
    "<br>This command tells the controller to wait for a delay period before executing the next command. <br>"
    global Summary
    Summary.Command = "Write General Delay Command"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',60))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('I',DelayInMilliseconds)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteImagePixelBrightness(Brightness):
    "Sets the Image Brightness by adding an offset to pixel values. The offset added to Red, Green and Blue is same. For YCbCr images, brightness setting is applied after it is converted to RGB <br>"
    global Summary
    Summary.Command = "Write Image Pixel Brightness"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',64))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('h',Brightness)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadImagePixelBrightness():
    "Gets the currently applied Image Brightness value (offset applied to pixel values). The offset added to Red, Green and Blue is same. Brightness is applied on YCbCr images after converting it to RGB. <br>"
    global Summary
    Summary.Command = "Read Image Pixel Brightness"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',64))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(2, writebytes, ProtocolData)
        Brightness = struct.unpack_from ('h', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Brightness

def WriteImagePixelContrast(Contrast):
    "Sets the Image Contrast by providing a multiplicative gain to pixel values. The gain is same for Red, Green and Blue. For YCbCr images, contrast setting is applied after it is converted to RGB <br>"
    global Summary
    Summary.Command = "Write Image Pixel Contrast"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',65))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Contrast)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadImagePixelContrast():
    "Gets the currently applied Image Contrast value (Gain multiplied to pixel values). The gain is same for Red, Green and Blue. Contrast is applied on YCbCr images after converting it to RGB. <br>"
    global Summary
    Summary.Command = "Read Image Pixel Contrast"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',65))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        Contrast = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Contrast

def WriteDegammaTable(TableIndex):
    "Sets the index of the De-Gamma Table to be loaded into the system from Flash. This table will be used to perform de-gamma operation on the input data. It is 0-indexed (Starts from 0). Maximum value can be 254. A value of 255 would disable de-gamma operations. <br>"
    global Summary
    Summary.Command = "Write Degamma Table"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',66))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',TableIndex)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDegammaTable():
    "Gets the index of the De-Gamma Table currently loaded into the system. This Table is used to perform de-gamma operation on the input data. It is 0-indexed (Starts from 0). A value of 0xff means no De-gamma table is loaded <br>"
    global Summary
    Summary.Command = "Read Degamma Table"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',66))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        TableIndex = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, TableIndex

def WriteImageSharpness(Sharpness):
    "Set image sharpness value. <br>"
    global Summary
    Summary.Command = "Write Image Sharpness"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',67))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Sharpness)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadImageSharpness():
    "Return image sharpness value. <br>"
    global Summary
    Summary.Command = "Read Image Sharpness"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',67))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        Sharpness = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Sharpness

def WriteXprActuatorWaveformControlParameter(XprCommand,  AwcChannel,  Data):
    "<br>This command configure/setup Actuator Waveform Control(AWC) block. Here, AWCx can be AWC 0 or 1. Bytes 2-5 contains the XPR command data as mentioned in Byte 0. Byte 1 contains AWC channel number, possible values are 0 or 1.<BR><BR> <br>**Fixed Output Enable** : Configures Actuator in fixed output mode.<BR> Byte    2: 0x00 - Disable 0x01 - Enable  <BR> Bytes 3-5: Reserved must be set to 0x000000<BR><BR> <br>**Gain** : Set Waveform Generator DAC/PWM Gain.<BR> Byte    2: Range 0 - 255 format u1.7 (0 to 1.9921875) <BR> Bytes 3-5: Reserved must be set to 0x000000<BR><BR> <br>**Subframe delay** : Subframe delay Bytes 2-5; Range 0 - 262143 and lsb = 133.333ns  <BR><BR> <br>**Actuator Type (READ ONLY)** : Actuator type <BR> Byte    2: <BR>0x00 - NONE <BR> 0x01 - Optotune (XPR-25 Model) <BR> 0x80 - TI Actuator Interface (EEPROM) <BR> 0x81 - TI Actuator Interface (MCU) <BR> Bytes 3-5: Reserved must be set to 0x000000<BR><BR> <br>**Output Enable/Disable** : Actuator output enable/disable <BR> Byte    2: 0x00 - Disable 0x01 - Enable  <BR> Bytes 3-5: Reserved must be set to 0x000000<BR><BR> Note: Both AWC0 and AWC1 disabled/enabled together <BR> <br>**Clock Width** : Defines the high and low width for the output clock (the clock period will be 2*(ClkWidth+1)) <BR> 0 = 1 (Clock period is two clocks); lsb = 8.33ns <BR> Bytes 2-5 : ClkWidth <BR> Example: ClkWidth = 0; will generate clock of 2*(0+1)*8.33 = 16.66ns <BR><BR> <br>**Offset** : DAC/PWM Output Offset <BR> Byte    2: Range -128 - +127 format S7 (-128 to +127) <BR> Bytes 3-5: Reserved must be set to 0x000000<BR><BR> <br>**Number of Segments** : Defines number of segments <BR> Byte    2: Range 2 - 255<BR> Bytes 3-5: Reserved must be set to 0x000000<BR><BR> <br>**Segments Length** : Defines size of the segments <BR> Bytes 2-3: Range 19 - 4095<BR> Bytes 4-5: Reserved must be set to 0x0000<BR><BR> <br>**Invert PWM A** : Applicable when AWC is configured to PWM type instead of DAC <BR> Byte    2: 0x00 - No inversion <BR> 0x01 - Inverted  <BR> Bytes 3-5: Reserved must be set to 0x000000<BR><BR> <br>**Invert PWM B** : Applicable when AWC is configured to PWM type instead of DAC <BR> Byte    2: 0x00 - No inversion 0x01 - Inverted  <BR> Bytes 3-5: Reserved must be set to 0x000000<BR><BR> <br>**Subframe Filter Value** : Sets Subframe Filter Value - defines the minimum time between Subframe edges. Edges closer than the set value will be filtered out <BR> Byte    2: 0 = Filter disabled, >0 = Filter time will be Val x 60us, Range: 0 - 255 <BR> Bytes 3-5: Reserved must be set to 0x000000<BR><BR> <br>**Subframe Watch Dog** : Defines the maximum time between Subframe edges; if timer expires, then the WG will automatically output the Fixed Output value, and the normal output will resume on the next subframe edge.<BR> Bytes 2-3: 0 = Subframe watchdog disabled, >0 = Watchdog time will be Time x 60us, Range: Range: 0 - 1023 <BR> Bytes 4-5: Reserved must be set to 0x0000<BR><BR> <br>**Fixed Output Value** : Defines the value to be output on DAC/PWM when fixed output mode is selected.<BR> Byte    2: Value to be output on DAC/PWM, Range -128 to 127 Bytes 3-5: Reserved must be set to 0x000000<BR><BR> <br>**Note** : To use **Subframe Filter Value** and **Subframe Watch Dog** care must be taken to set a value which aproximately 10% more than 2x of the operating frequency. <BR> For example - 4K @ 60Hz, the value can be set as (1/(60*2))*1.10*10^6 = 9166us. <br>"
    global Summary
    Summary.Command = "Write Xpr Actuator Waveform Control Parameter"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',XprCommand.value)))
        writebytes.extend(list(struct.pack('B',AwcChannel.value)))
        writebytes.extend(list(struct.pack('I',Data)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadXprActuatorWaveformControlParameter(XprCommand,  AwcChannel):
    "<br>This command gets the parameter set to the AWC waveform generator.<BR> **Note** : This command is supposed to be used only during the normal operating mode and not during the standby state. <br>"
    global Summary
    Summary.Command = "Read Xpr Actuator Waveform Control Parameter"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',XprCommand.value)))
        writebytes.extend(list(struct.pack('B',AwcChannel.value)))
        readbytes = _readcommand(4, writebytes, ProtocolData)
        Data = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Data

def WriteThreeDDebugControl(EnableRegPrint,  EnableVpsRegWrite):
    ""
    global Summary
    Summary.Command = "Write Three D Debug Control"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',182))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(EnableRegPrint), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(int(EnableVpsRegWrite), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadThreeDDebugControl():
    ""
    global Summary
    Summary.Command = "Read Three D Debug Control"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',182))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(2, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        EnableRegPrint = getbits(1, 0);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        packerinit(readdata)
        EnableVpsRegWrite = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, EnableRegPrint, EnableVpsRegWrite

def WriteWpcTargetManualMode(Enable):
    "Sets/Resets the manual mode for speciying WPC target color point at run-time. When manual mode is set, all target color points specified in the project will be ignored. Software will set only the user specified target color point until the manual mode is reset using this same command. <br>"
    global Summary
    Summary.Command = "Write Wpc Target Manual Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',183))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(Enable), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadWpcTargetManualMode():
    "Gets whether the manual mode for speciying WPC target color point at run-time is active. <br>"
    global Summary
    Summary.Command = "Read Wpc Target Manual Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',183))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        Enable = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Enable

def WriteWpcManualTargetColorPoint(X,  Y):
    "Sets the target color point which will be used in Manual Mode <br>"
    global Summary
    Summary.Command = "Write Wpc Manual Target Color Point"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',184))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(X,65536)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(Y,65536)))))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadWpcManualTargetColorPoint():
    "Gets the target color point set for Manual Mode <br>"
    global Summary
    Summary.Command = "Read Wpc Manual Target Color Point"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',184))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        X = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 0)[0], 65536)
        Y = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 2)[0], 65536)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, X, Y

def WriteDebugLogOptions(DebugLogOptions):
    "Set enable mask for debug messages. The mask identifies the sources of debug messages which are to be enabled for printing at the debug port. The mask bit corresponding to the source has to be set to enable it. <br>"
    global Summary
    Summary.Command = "Write Debug Log Options"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',224))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(DebugLogOptions.Sequence), 1, 19)
        value = setbits(int(DebugLogOptions.Ite), 1, 20)
        value = setbits(int(DebugLogOptions.Communication), 1, 21)
        value = setbits(int(DebugLogOptions.ThreeD), 1, 22)
        value = setbits(int(DebugLogOptions.MsgServers), 1, 23)
        value = setbits(int(DebugLogOptions.Environment), 1, 24)
        value = setbits(int(DebugLogOptions.Illum), 1, 25)
        value = setbits(int(DebugLogOptions.System), 1, 26)
        value = setbits(int(DebugLogOptions.Eeprom), 1, 27)
        value = setbits(int(DebugLogOptions.Dpath), 1, 28)
        value = setbits(int(DebugLogOptions.Usb), 1, 29)
        value = setbits(int(DebugLogOptions.RtosMailbox), 1, 30)
        writebytes.extend(list(struct.pack('L',value)))
        packerinit()
        value = setbits(int(DebugLogOptions.LogsOnUsb), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDebugLogOptions():
    "Retrieves the current debug message mask. The mask decides which sources of debug messages are enabled. A value of 1 in the mask bit corresponding to a source means that the source is enabled. <br>"
    global Summary
    Summary.Command = "Read Debug Log Options"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',224))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(5, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        DebugLogOptions.Sequence = getbits(1, 19);
        DebugLogOptions.Ite = getbits(1, 20);
        DebugLogOptions.Communication = getbits(1, 21);
        DebugLogOptions.ThreeD = getbits(1, 22);
        DebugLogOptions.MsgServers = getbits(1, 23);
        DebugLogOptions.Environment = getbits(1, 24);
        DebugLogOptions.Illum = getbits(1, 25);
        DebugLogOptions.System = getbits(1, 26);
        DebugLogOptions.Eeprom = getbits(1, 27);
        DebugLogOptions.Dpath = getbits(1, 28);
        DebugLogOptions.Usb = getbits(1, 29);
        DebugLogOptions.RtosMailbox = getbits(1, 30);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 4)[0]
        packerinit(readdata)
        DebugLogOptions.LogsOnUsb = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DebugLogOptions

def WriteDlpa3005Register(Index,  RegisterAddress,  RegisterValue):
    "Command that writes specified value to the specified register address. Refer to DLPA30005 datasheet for register descriptions. http://www.ti.com/lit/gpn/dlpa3005."
    global Summary
    Summary.Command = "Write Dlpa 3005 Register"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',227))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Index)))
        writebytes.extend(list(struct.pack('B',RegisterAddress)))
        writebytes.extend(list(struct.pack('B',RegisterValue)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDlpa3005Register(Index,  RegisterAddress):
    "Returns specified register value from DLPA3005. Refer to DLPA30005 datasheet for register descriptions. http://www.ti.com/lit/gpn/dlpa3005."
    global Summary
    Summary.Command = "Read Dlpa 3005 Register"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',227))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Index)))
        writebytes.extend(list(struct.pack('B',RegisterAddress)))
        readbytes = _readcommand(1, writebytes, ProtocolData)
        RegisterValue = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, RegisterValue

def ReadEmuBuildInfo():
    "Returns the current build number and type for Emulation platform"
    global Summary
    Summary.Command = "Read Emu Build Info"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',228))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(3, writebytes, ProtocolData)
        BuildNumber = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        BuildTypeObj = struct.unpack_from ('B', bytearray(readbytes), 2)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, BuildNumber, DdpHwBuildTypeT(BuildTypeObj)

def ReadSequenceDebugInformation(SegmentType):
    "Obtains sequence selection information for the selected segment type. <br>"
    global Summary
    Summary.Command = "Read Sequence Debug Information"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',229))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',SegmentType.value)))
        readbytes = _readcommand(48, writebytes, ProtocolData)
        SequenceDebugInformation.SequenceType = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        SequenceDebugInformation.SeqMode = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        SequenceDebugInformation.FrameRateBinIndex = struct.unpack_from ('I', bytearray(readbytes), 2)[0]
        SequenceDebugInformation.SequenceVectorOrderInfoIndex = struct.unpack_from ('I', bytearray(readbytes), 6)[0]
        SequenceDebugInformation.Enabled = struct.unpack_from ('B', bytearray(readbytes), 10)[0]
        SequenceDebugInformation.DutyCycle = convertfixedtofloat(struct.unpack_from ('I', bytearray(readbytes), 11)[0], 256)
        SequenceDebugInformation.ColorTime = struct.unpack_from ('I', bytearray(readbytes), 15)[0]
        SequenceDebugInformation.ColorCycles = struct.unpack_from ('I', bytearray(readbytes), 19)[0]
        SequenceDebugInformation.IllumDefIndex = struct.unpack_from ('I', bytearray(readbytes), 23)[0]
        SequenceDebugInformation.ColorTimeBinIndex = struct.unpack_from ('I', bytearray(readbytes), 27)[0]
        SequenceDebugInformation.MiniSequenceIndex = struct.unpack_from ('I', bytearray(readbytes), 31)[0]
        SequenceDebugInformation.CwaIndex = struct.unpack_from ('B', bytearray(readbytes), 35)[0]
        SequenceDebugInformation.BpdlutIndex = struct.unpack_from ('I', bytearray(readbytes), 36)[0]
        SequenceDebugInformation.BpdOffset = struct.unpack_from ('I', bytearray(readbytes), 40)[0]
        SequenceDebugInformation.NumberOfBitplanes = struct.unpack_from ('I', bytearray(readbytes), 44)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SequenceDebugInformation

def WriteSequenceOperationMode(SequenceMode):
    ""
    global Summary
    Summary.Command = "Write Sequence Operation Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',230))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',SequenceMode.value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadSequenceOperationMode():
    ""
    global Summary
    Summary.Command = "Read Sequence Operation Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',230))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        SequenceModeObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SeqOtfSequenceOperationModeT(SequenceModeObj)

def WriteIvfEnableMode(IvfEnable):
    "Ivf Set Enable Mode <br>"
    global Summary
    Summary.Command = "Write Ivf Enable Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',231))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(IvfEnable), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadIvfEnableMode():
    "Ivf Get Enable Mode <br>"
    global Summary
    Summary.Command = "Read Ivf Enable Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',231))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        IvfEnable = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, IvfEnable

def WriteMdtOptions(MdtEnable,  Mdt3DEnable,  MdtTemporalDialationEnable,  MdtVfilterMode,  MdtNoiseCoreThresold):
    "Set Mdt Options <br>"
    global Summary
    Summary.Command = "Write Mdt Options"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',232))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(MdtEnable), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(int(Mdt3DEnable), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(int(MdtTemporalDialationEnable), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        writebytes.extend(list(struct.pack('B',MdtVfilterMode.value)))
        writebytes.extend(list(struct.pack('B',MdtNoiseCoreThresold)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadMdtOptions():
    "Get Mdt options <br>"
    global Summary
    Summary.Command = "Read Mdt Options"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',232))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(5, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        MdtEnable = getbits(1, 0);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        packerinit(readdata)
        Mdt3DEnable = getbits(1, 0);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 2)[0]
        packerinit(readdata)
        MdtTemporalDialationEnable = getbits(1, 0);
        MdtVfilterModeObj = struct.unpack_from ('B', bytearray(readbytes), 3)[0]
        MdtNoiseCoreThresold = struct.unpack_from ('B', bytearray(readbytes), 4)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, MdtEnable, Mdt3DEnable, MdtTemporalDialationEnable, XprMdtVfilterModeT(MdtVfilterModeObj), MdtNoiseCoreThresold

def WriteXprFrcSubframe(XprFrcSubframe0,  XprFrcSubframe1,  XprFrcSubframe2,  XprFrcSubframe3):
    "Set Xpr Subframes map in FRC <br>"
    global Summary
    Summary.Command = "Write Xpr Frc Subframe"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',233))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',XprFrcSubframe0)))
        writebytes.extend(list(struct.pack('B',XprFrcSubframe1)))
        writebytes.extend(list(struct.pack('B',XprFrcSubframe2)))
        writebytes.extend(list(struct.pack('B',XprFrcSubframe3)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadXprFrcSubframe():
    "Get Xpr Subframe map in FRC <br>"
    global Summary
    Summary.Command = "Read Xpr Frc Subframe"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',233))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        XprFrcSubframe0 = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        XprFrcSubframe1 = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        XprFrcSubframe2 = struct.unpack_from ('B', bytearray(readbytes), 2)[0]
        XprFrcSubframe3 = struct.unpack_from ('B', bytearray(readbytes), 3)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, XprFrcSubframe0, XprFrcSubframe1, XprFrcSubframe2, XprFrcSubframe3

def WriteSingleXprFrcSubframeToAll(Subframe):
    "Map all subframes to a single subframes <br>"
    global Summary
    Summary.Command = "Write Single Xpr Frc Subframe To All"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',234))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Subframe)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteDtlDpfBypassMode(DtlDpfBypassEnable):
    "Set Bypass DTL and DPF processing <br>"
    global Summary
    Summary.Command = "Write Dtl Dpf Bypass Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',235))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(DtlDpfBypassEnable), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDtlDpfBypassMode():
    "Get Bypass DTL and DPF processing <br>"
    global Summary
    Summary.Command = "Read Dtl Dpf Bypass Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',235))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        DtlDpfBypassEnable = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DtlDpfBypassEnable

def ReadSequenceSourceSelect():
    "Returns the source select for sequence selection <br>"
    global Summary
    Summary.Command = "Read Sequence Source Select"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',236))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        SourceObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SysSourceTypeT(SourceObj)

def WriteI2CPassthrough(I2CPassthrough):
    "Writes data to specified I2C device address. <br>"
    global Summary
    Summary.Command = "Write I 2 C Passthrough"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',103))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',I2CPassthrough.Port.value)))
        writebytes.extend(list(struct.pack('B',I2CPassthrough.Is7Bit)))
        writebytes.extend(list(struct.pack('B',I2CPassthrough.HasSubaddr)))
        writebytes.extend(list(struct.pack('I',I2CPassthrough.ClockRate)))
        writebytes.extend(list(struct.pack('H',I2CPassthrough.DeviceAddress)))
        if I2CPassthrough.HasSubaddr:
            writebytes.extend(list(I2CPassthrough.SubAddr))
        writebytes.extend(list(I2CPassthrough.DataBytes))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadI2CPassthrough(Port,  Is7Bit,  HasSubaddr,  ClockRate,  DeviceAddress,  ByteCount,  SubAddr):
    "Reads data from specified I2C device address. <br>"
    global Summary
    Summary.Command = "Read I 2 C Passthrough"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',103))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Port.value)))
        writebytes.extend(list(struct.pack('B',Is7Bit)))
        writebytes.extend(list(struct.pack('B',HasSubaddr)))
        writebytes.extend(list(struct.pack('I',ClockRate)))
        writebytes.extend(list(struct.pack('H',DeviceAddress)))
        writebytes.extend(list(struct.pack('H',ByteCount)))
        if HasSubaddr:
            writebytes.extend(list(SubAddr))
        readbytes = _readcommand(ByteCount, writebytes, ProtocolData)
        DataBytes = bytearray(readbytes)[0, 1]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DataBytes

def ReadTmp411Temperature(TempSensorType):
    "This command applicable only if TMP411A temperature sensor is installed in the system. <br>"
    global Summary
    Summary.Command = "Read Tmp 411 Temperature"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',105))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',TempSensorType.value)))
        readbytes = _readcommand(2, writebytes, ProtocolData)
        Temperature = struct.unpack_from ('h', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Temperature

def WriteTpgTimings(Index):
    "Validates & sets frame rate, active resolution & blankings for current test pattern. <br>"
    global Summary
    Summary.Command = "Write Tpg Timings"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',80))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',Index)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadTpgTimings():
    "Returns the index & sets frame rate, active resolution & blankings for current test pattern. <br>"
    global Summary
    Summary.Command = "Read Tpg Timings"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',80))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(2, writebytes, ProtocolData)
        Index = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Index

def WriteTpgFrameRate(FrameRate):
    "Sets frame rate in Hz for current test pattern. <br>"
    global Summary
    Summary.Command = "Write Tpg Frame Rate"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',81))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',FrameRate)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadTpgFrameRate():
    "Returns frame rate in Hz for current test pattern. <br>"
    global Summary
    Summary.Command = "Read Tpg Frame Rate"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',81))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(2, writebytes, ProtocolData)
        FrameRate = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, FrameRate

def WriteTpgBorder(BorderColor,  BorderWidth):
    "Sets Border Settings for TPG test patterns. <br>"
    global Summary
    Summary.Command = "Write Tpg Border"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',83))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',BorderColor.value)))
        writebytes.extend(list(struct.pack('H',BorderWidth)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadTpgBorder():
    "Gets Border Settings for TPG test patterns. <br>"
    global Summary
    Summary.Command = "Read Tpg Border"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',83))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(3, writebytes, ProtocolData)
        BorderColorObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        BorderWidth = struct.unpack_from ('H', bytearray(readbytes), 1)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, TpgBorderColorT(BorderColorObj), BorderWidth

def WriteTpgSolidField(Red,  Green,  Blue):
    "Sets color for solid field test pattern <br>"
    global Summary
    Summary.Command = "Write Tpg Solid Field"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',84))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',Red)))
        writebytes.extend(list(struct.pack('H',Green)))
        writebytes.extend(list(struct.pack('H',Blue)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadTpgSolidField():
    "Returns color for current solid field set by test patter generator. If Solid field is not enabled via TPG, 0 is returned for each color <br>"
    global Summary
    Summary.Command = "Read Tpg Solid Field"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',84))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(6, writebytes, ProtocolData)
        Red = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        Green = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        Blue = struct.unpack_from ('H', bytearray(readbytes), 4)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Red, Green, Blue

def WriteManualWarpControlPoints(ControlPointsDefinedByArray,  HorizontalCtrlPoints,  VerticalCtrlPoints):
    "This command sets up the user defined control points of the warp map that shall be applied on top of the keystone correction, anamorphic scaling and other warp dependent feature settings if they are enabled. <br>The warping map table loaded by the manual warp table write command is used as a two dimensional array with dimension which is defined based on the first argument of this command: - TRUE  = (NumHorzCtrlPoints x NumVertCtrlPoints) - FALSE = (32 x 18) <br>The points in the map should lie within the display area defined by display image size command. Any points lying outside the display area shall get cropped. <br>"
    global Summary
    Summary.Command = "Write Manual Warp Control Points"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',208))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',ControlPointsDefinedByArray.value)))
        ********** Invalid Write Data Field Type - DLPComposer.Commands.Spec.ArrayType;
        ********** Invalid Write Data Field Type - DLPComposer.Commands.Spec.ArrayType;
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadManualWarpControlPoints():
    "This command gets up the user defined warping map control points. <br>"
    global Summary
    Summary.Command = "Read Manual Warp Control Points"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',208))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        ControlPointsDefinedByArrayObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        ********** Invalid Write Data Field Type - DLPComposer.Commands.Spec.ArrayType;
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DispfmtManualWarpMapPointsTypeCmdT(ControlPointsDefinedByArrayObj), CtrlPoints

def WriteManualWarpTable(WarpTableIndex,  WarpPoints):
    "This command writes to the warp map table that can be enabled using the [[#cat-general_operation/apply_manual_warping_write]] command. N warp map points (that does not exceed the command packet size) can be loaded at a time to anywhere within the table. Maximum number of points that can be set using this command is 32 in the horizontal direction and 18 in the vertical direction. Overall max 576 points. The number of points set by this command should match the number of control points specified using [[#cat-general_operation/manual_warp_control_points_write]] command. <br>"
    global Summary
    Summary.Command = "Write Manual Warp Table"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',209))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',WarpTableIndex)))
        ********** Invalid Write Data Field Type - DLPComposer.Commands.Spec.ArrayType;
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadManualWarpTable(WarpTableIndex,  NumEntries):
    "This command reads from the warp map table already loaded using [[#cat-general_operation/manual_warp_table_write]] command. N warp map points (that does not exceed the command packet size) can be read at a time from anywhere within the table. Maximum table size is 1952. <br>"
    global Summary
    Summary.Command = "Read Manual Warp Table"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',209))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',WarpTableIndex)))
        writebytes.extend(list(struct.pack('H',NumEntries)))
        readbytes = _readcommand(0, writebytes, ProtocolData)
        ********** Invalid Write Data Field Type - DLPComposer.Commands.Spec.ArrayType;
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, WarpPoints

def WriteApplyManualWarping(WarpEnabled):
    "This command applies the manual warping control points and map table to the HW defined by [[#cat-general_operation/manual_warp_control_points_write]] and [[#cat-general_operation/manual_warp_table_write]] respectively. <br><br>"
    global Summary
    Summary.Command = "Write Apply Manual Warping"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',210))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(WarpEnabled), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadApplyManualWarping():
    "This command returns if manual warping is enabled or disabled. <br>"
    global Summary
    Summary.Command = "Read Apply Manual Warping"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',210))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        WarpEnabled = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, WarpEnabled

def WriteSmoothWarpTable(SmoothWarpTable):
    "This command sets up the user defined 3x3 warping map that creates a parameteric smooth curve. To disable this feature use ConfigureWarpMap command. <br>"
    global Summary
    Summary.Command = "Write Smooth Warp Table"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',211))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',SmoothWarpTable.TopLeftX)))
        writebytes.extend(list(struct.pack('H',SmoothWarpTable.TopLeftY)))
        writebytes.extend(list(struct.pack('H',SmoothWarpTable.TopCenterX)))
        writebytes.extend(list(struct.pack('H',SmoothWarpTable.TopCenterY)))
        writebytes.extend(list(struct.pack('H',SmoothWarpTable.TopRightX)))
        writebytes.extend(list(struct.pack('H',SmoothWarpTable.TopRightY)))
        writebytes.extend(list(struct.pack('H',SmoothWarpTable.MidLeftX)))
        writebytes.extend(list(struct.pack('H',SmoothWarpTable.MidLeftY)))
        writebytes.extend(list(struct.pack('H',SmoothWarpTable.MidCenterX)))
        writebytes.extend(list(struct.pack('H',SmoothWarpTable.MidCenterY)))
        writebytes.extend(list(struct.pack('H',SmoothWarpTable.MidRightX)))
        writebytes.extend(list(struct.pack('H',SmoothWarpTable.MidRightY)))
        writebytes.extend(list(struct.pack('H',SmoothWarpTable.BotLeftX)))
        writebytes.extend(list(struct.pack('H',SmoothWarpTable.BotLeftY)))
        writebytes.extend(list(struct.pack('H',SmoothWarpTable.BotCenterX)))
        writebytes.extend(list(struct.pack('H',SmoothWarpTable.BotCenterY)))
        writebytes.extend(list(struct.pack('H',SmoothWarpTable.BotRightX)))
        writebytes.extend(list(struct.pack('H',SmoothWarpTable.BotRightY)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadSmoothWarpTable():
    "This command returns the user defined 3x3 warping map points <br>"
    global Summary
    Summary.Command = "Read Smooth Warp Table"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',211))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(36, writebytes, ProtocolData)
        SmoothWarpTable.TopLeftX = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        SmoothWarpTable.TopLeftY = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        SmoothWarpTable.TopCenterX = struct.unpack_from ('H', bytearray(readbytes), 4)[0]
        SmoothWarpTable.TopCenterY = struct.unpack_from ('H', bytearray(readbytes), 6)[0]
        SmoothWarpTable.TopRightX = struct.unpack_from ('H', bytearray(readbytes), 8)[0]
        SmoothWarpTable.TopRightY = struct.unpack_from ('H', bytearray(readbytes), 10)[0]
        SmoothWarpTable.MidLeftX = struct.unpack_from ('H', bytearray(readbytes), 12)[0]
        SmoothWarpTable.MidLeftY = struct.unpack_from ('H', bytearray(readbytes), 14)[0]
        SmoothWarpTable.MidCenterX = struct.unpack_from ('H', bytearray(readbytes), 16)[0]
        SmoothWarpTable.MidCenterY = struct.unpack_from ('H', bytearray(readbytes), 18)[0]
        SmoothWarpTable.MidRightX = struct.unpack_from ('H', bytearray(readbytes), 20)[0]
        SmoothWarpTable.MidRightY = struct.unpack_from ('H', bytearray(readbytes), 22)[0]
        SmoothWarpTable.BotLeftX = struct.unpack_from ('H', bytearray(readbytes), 24)[0]
        SmoothWarpTable.BotLeftY = struct.unpack_from ('H', bytearray(readbytes), 26)[0]
        SmoothWarpTable.BotCenterX = struct.unpack_from ('H', bytearray(readbytes), 28)[0]
        SmoothWarpTable.BotCenterY = struct.unpack_from ('H', bytearray(readbytes), 30)[0]
        SmoothWarpTable.BotRightX = struct.unpack_from ('H', bytearray(readbytes), 32)[0]
        SmoothWarpTable.BotRightY = struct.unpack_from ('H', bytearray(readbytes), 34)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SmoothWarpTable

def WriteManualWarpTableUpdateMode(Mode):
    "This command sets Manula Warp Table write Mode <br>"
    global Summary
    Summary.Command = "Write Manual Warp Table Update Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',212))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Mode.value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadManualWarpTableUpdateMode():
    "This command returns if manual warping is enabled or disabled. <br>"
    global Summary
    Summary.Command = "Read Manual Warp Table Update Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',212))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        ModeObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DispfmtManualWarpTableUpdateModeCmdT(ModeObj)

