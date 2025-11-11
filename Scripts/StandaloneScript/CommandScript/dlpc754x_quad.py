#-------------------------------------------------------------------------------
# Copyright (c) 2024 Texas Instruments Incorporated - http://www.ti.com/
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

class DdpProductConfigFailCauseT(Enum):
    InvalidController = 0
    InvalidDmd = 1
    InvalidDmdProjectdata = 2
    PadUsedInEcdSystem = 3
    InvalidPadConfiguration = 4

class UrtFifoTriggerLevelT(Enum):
    OneEighthFull = 0
    OneFourthFull = 1
    OneHalfFull = 2
    ThreeFourthsFull = 3
    SevenEighthsFull = 4

class UrtRxDataSourceT(Enum):
    Rxd = 0
    Lampstat = 1

class I2CPortT(Enum):
    Port0 = 0
    Port1 = 1
    Port2 = 2
    MaxPort = 3

class CmdSwitchTypeT(Enum):
    ToBoot = 0
    ToAppViaReset = 1
    ToAppDirect = 2

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

class UrtPortT(Enum):
    Port0 = 0
    Port1 = 1
    Port2 = 2

class FpgaSrcCscTablesT(Enum):
    TableBt601YuvVideodecoder = 1
    TableFullrangeYuv1 = 2
    TableBt601OffsetYuv = 4
    TableFullrangeYuv = 5
    TableBt709OffsetYuv = 6
    TableSmpte240M = 7
    TableBt2020 = 8

class TpgLineColorT(Enum):
    Red = 0
    Green = 1
    Blue = 2

class UrtParityT(Enum):
    _None = 0
    Even = 1
    Odd = 2

class FpgaTestPatternT(Enum):
    Lut = 0
    Checkerboard = 4
    Hramp = 5
    Vramp = 6
    Hlines = 7
    Vlines = 8
    GridLines = 9
    GridDiag = 10
    Cross = 11
    SolidField = 12
    ColorBars = 13
    MultColorHorzRamp = 14
    FixedStepHorzRamp = 15
    DiamondDiagLines = 16

class TpgColorT(Enum):
    Black = 0
    Red = 1
    Green = 2
    Blue = 4
    Yellow = 3
    Magenta = 5
    Cyan = 6
    White = 7

class PowerstateEnum(Enum):
    Reset = 0
    Standby = 1
    Active = 2
    Cooling = 3
    Warming = 4

class CmdControllerConfigT(Enum):
    Single = 0
    Multiple = 1

class CmdAccessWidthT(Enum):
    Uint32 = 0
    Uint16 = 1
    Uint08 = 2

class Pwmport(Enum):
    Out0 = 0
    Out1 = 1
    Out2 = 2
    Ledr = 3
    Ledg = 4
    Ledb = 5
    Ledir = 6
    Leduv = 7
    Cw0 = 8
    Cw1 = 9
    Cw2 = 10
    In0 = 11
    In1 = 12
    NotUsed = 13
    MaxPort = 14

class PwmIncounter(Enum):
    Incount0 = 0
    Incount1 = 1

class HdrTransferFnT(Enum):
    TradGamSdr = 0
    TradGamHdr = 1
    Pq = 2
    Hlg = 3

class CmdProjectionModes(Enum):
    DispExternal = 0
    TestPattern = 1
    SolidField = 2
    Splash = 3
    Curtain = 4

class DbPixelWeightT(Enum):
    DbWeight0 = 0
    DbWeight25 = 1
    DbWeight50 = 2
    DbWeight75 = 3

class CmdFlashUpdateT(Enum):
    Lock = 0
    Unlock = 4154802215

class UrtFlowControlT(Enum):
    Off = 0
    Hw = 1

class FpgaTpgHorzRampStepT(Enum):
    FpgaTpgHorzrampStep1By16 = 1
    FpgaTpgHorzrampStep1By8 = 2
    FpgaTpgHorzrampStep1By4 = 4
    FpgaTpgHorzrampStep1By2 = 8
    FpgaTpgHorzrampStep1By1 = 16

class DispBackgroundColorT(Enum):
    Black = 0
    DitherBlack = 1
    White = 2
    Green = 3
    Red = 4
    Blue = 5
    Yellow = 6
    Cyan = 7
    Magenta = 8
    C1 = 9
    C2 = 10

class UrtDataBitsT(Enum):
    UrtDatbits5 = 0
    UrtDatbits6 = 1
    UrtDatbits7 = 2
    UrtDatbits8 = 3

class UrtStopBitsT(Enum):
    UrtStpbits1 = 0
    UrtStpbits2 = 1

class FpgaTpgVertRampStepT(Enum):
    FpgaTpgVertrampStep1By16 = 1
    FpgaTpgVertrampStep1By8 = 2
    FpgaTpgVertrampStep1By4 = 4
    FpgaTpgVertrampStep1By2 = 8
    FpgaTpgVertrampStep1By1 = 16

class FpgaVx1IpStateT(Enum):
    Shutdown = 0
    CdrTraining = 1
    AlnTraining = 2
    Normal = 3

class FpgaSourcePixelFormatT(Enum):
    Rgb = 0
    Yuv444 = 1
    Yuv422 = 2

class TpgHorzRampStepT(Enum):
    TpgHorzrampStep0P5 = 1
    TpgHorzrampStep1P0 = 2
    TpgHorzrampStep2P0 = 3
    TpgHorzrampStep0P25 = 5

class UrtBaudRateT(Enum):
    UrtBaud1200 = 0
    UrtBaud2400 = 1
    UrtBaud4800 = 2
    UrtBaud9600 = 3
    UrtBaud14400 = 4
    UrtBaud19200 = 5
    UrtBaud38400 = 6
    UrtBaud57600 = 7
    UrtBaud115200 = 8
    UrtBaud230400 = 9
    UrtBaud460800 = 10
    UrtBaud921600 = 11

class FlChipSelectT(Enum):
    Cs0 = 0
    Cs1 = 1
    Cs2 = 2

class ImgSpccPointIndexT(Enum):
    Row0Col0 = 0
    Row0Col1 = 1
    Row0Col2 = 2
    Row0Col3 = 3
    Row0Col4 = 4
    Row1Col0 = 5
    Row1Col1 = 6
    Row1Col2 = 7
    Row1Col3 = 8
    Row1Col4 = 9
    Row2Col0 = 10
    Row2Col1 = 11
    Row2Col2 = 12
    Row2Col3 = 13
    Row2Col4 = 14

class FrameFrcModeT(Enum):
    Fixed = 0
    Sync1X = 1
    Sync2X = 2
    Sync3X = 3
    Sync4X = 4
    Sync6X = 5
    Sync8X = 6
    Sync10X = 7

class FpgaDataMapModeT(Enum):
    Mode0 = 0
    Mode1 = 1
    Mode2 = 2
    Mode3 = 3
    Mode4 = 4
    Mode5 = 5
    ModeNone = 6

class UrtRxDataPolarityT(Enum):
    Noninv = 0
    Inv = 1

class CmdModeT(Enum):
    Bootloader = 0
    MainApplication = 1
    MainApplicationTrueGlobal = 2

class Summary:
    Command: str
    CommInterface: str
    Successful: bool

class ProtocolData:
    CommandDestination: int
    OpcodeLength: int
    BytesRead: int

class Version:
     AppMajor: int                          # int
     AppMinor: int                          # int
     AppPatch: int                          # int
     PreReleaseName: str
     PreReleaseVersion: int                 # int
     TestBuildNumber: int                   # int
     ApiMajor: int                          # int
     ApiMinor: int                          # int
     ApiPatch: int                          # int
     ApiPreReleaseName: str
     ApiPreReleaseVersion: int              # int
     ApiTestBuildNumber: int                # int
     FpgaBuildNumber: int                   # int
     FpgaBuildEcoId: int                    # int
     FpgaMajor: int                         # int
     FpgaMinor: int                         # int

class SectorInfo:
     SectorSize: int                        # int
     NumSectors: int                        # int

class MemoryArray:
     StartAddress: int                      # int
     AddressIncrement: int                  # int
     AccessWidth: CmdAccessWidthT
     NumberOfWords: int                     # int
     NumberOfBytesPerWord: int              # int
     Data: bytearray

class SystemStatus:
     MemTstPassed: bool
     FrameRateConvEn: bool
     SeqPhaselock: bool
     SeqFreqlock: bool
     SeqSearch: bool
     ScpcalEnable: bool
     VicalEnable: bool
     BccalEnable: bool

class SystemErrorStatus:
     SequenceErr: bool
     PixclkOor: bool
     SyncvalStat: bool
     FpgaInitErr: bool
     FpgaCommErr: bool
     FpgaConfigErr: bool
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
     NoFreqBinErr: bool
     Dlpa3000CommErr: bool
     UmcRefreshBwUnderflowErr: bool
     DmdInitErr: bool
     DmdPwrDownErr: bool
     SrcdefNotpresent: bool
     SeqbinNotpresent: bool
     ProductConfigurationFailed: bool
     TemporalDitherMaskNotLoading: bool
     MultiControllerSyncError: bool
     MultiControllerSeqSyncError: bool
     HubInitFailed: bool
     EepromInitFail: bool
     FpgaOverTemperature: bool

class EepromDataPresent:
     ColorwheelLampDataPresent: bool
     SsiCalibrationDataPresent: bool
     AdcCalibrationDataPresent: bool
     WpcSensorCalibrationDataPresent: bool
     WpcBrightnessTableDataPresent: bool
     XprCalibrationDataPresent: bool
     XprWaveformCalibrationDataPresent: bool
     EdgeBlendDataPresent: bool
     SurfaceCorrectionDataPresent: bool

class EepromInvalidate:
     InvalidateSettings: bool
     InvalidateColorwheelLampData: bool
     InvalidateSsiCalibrationData: bool
     InvalidateAdcCalibrationData: bool
     InvalidateWpcSensorCalibrationData: bool
     InvalidateWpcBrightnessTableData: bool
     InvalidateXprCalibrationData: bool
     InvalidateXprWaveformCalibrationData: bool
     InvalidateEdgeBlendData: bool
     InvalidateSurfaceCorrectionData: bool

class SsiDutyCycleIndex:
     NumberOfDutyCycles: int                # int
     CurrentDutyCycleIndex: int             # int
     CurrentRedDutyCycle: float
     CurrentGreenDutyCycle: float
     CurrentBlueDutyCycle: float
     CurrentYellowDutyCycle: float
     CurrentCyanDutyCycle: float
     CurrentMagentaDutyCycle: float
     CurrentWhiteDutyCycle: float

class DebugMessageMask:
     Comm: bool
     ThreeD: bool
     MessageService: bool
     I2C: bool
     ClosedCaptioning: bool
     DdcCi: bool
     Gui: bool
     Environment: bool
     Illumination: bool
     System: bool
     Eeprom: bool
     Datapath: bool
     Autolock: bool
     ProjectorCtl: bool
     Peripheral: bool
     Ir: bool
     Usb: bool
     Mailbox: bool

class Resource:
     TasksHighCount: int                    # int
     EventsHighCount: int                   # int
     GroupEventsHighCount: int              # int
     MailboxHighCount: int                  # int
     MemoryPoolsHighCount: int              # int
     SemaphoreHighCount: int                # int
     TasksCurrentCount: int                 # int
     EventsCurrentCount: int                # int
     GrpEventsCurrentCount: int             # int
     MailboxCurrentCount: int               # int
     MemoryPoolsCurrentCount: int           # int
     SemaphoreCurrentCount: int             # int

class SeqMultiasicSyncError:
     Seqnum: bool
     Lampbin: bool
     Syslook: bool
     Srcdef: bool
     Freq: bool
     Ssiconfig: bool
     Seqset: bool
     Hdrsrcgrp: bool
     Sysgrp: bool
     Bnmlut: bool
     Cwperiod: bool

class KeystoneCorners:
     TopLeftX: int                          # int
     TopLeftY: int                          # int
     TopRightX: int                         # int
     TopRightY: int                         # int
     BottomLeftX: int                       # int
     BottomLeftY: int                       # int
     BottomRightX: int                      # int
     BottomRightY: int                      # int

class Vx1SourceConfig:
     FrameRate: float
     ActiveResolutionWidth: int             # int
     ActiveResolutionHeight: int            # int
     FSyncEdgePol: int                      # int
     VsyncEdgePol: int                      # int
     HsyncEdgePol: int                      # int
     DataEnEdgePol: int                     # int
     PixelFormat: FpgaSourcePixelFormatT
     DataMapMode: FpgaDataMapModeT
     ColorSpaceConvCoeffsIndex0: int        # int
     ColorSpaceConvCoeffsIndex1: int        # int
     ColorSpaceConvCoeffsIndex2: int        # int
     ColorSpaceConvCoeffsIndex3: int        # int
     ColorSpaceConvCoeffsIndex4: int        # int
     ColorSpaceConvCoeffsIndex5: int        # int
     ColorSpaceConvCoeffsIndex6: int        # int
     ColorSpaceConvCoeffsIndex7: int        # int
     ColorSpaceConvCoeffsIndex8: int        # int
     IsOffsetBinary: bool
     ChannelAOffset: int                    # int
     ChannelBOffset: int                    # int
     ChannelCOffset: int                    # int

class SsiDriveLevels:
     DriveLevelRed: int                     # int
     DriveLevelGreen: int                   # int
     DriveLevelBlue: int                    # int
     DriveLevelC1: int                      # int
     DriveLevelC2: int                      # int
     DriveLevelSense: int                   # int

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
     OrigCoordsC1X: float
     OrigCoordsC1Y: float
     OrigCoordsC1Lum: float
     OrigCoordsC2X: float
     OrigCoordsC2Y: float
     OrigCoordsC2Lum: float
     OrigCoordsDraAX: float
     OrigCoordsDraAY: float
     OrigCoordsDraALum: float
     OrigCoordsDraBX: float
     OrigCoordsDraBY: float
     OrigCoordsDraBLum: float
     OrigCoordsDraCX: float
     OrigCoordsDraCY: float
     OrigCoordsDraCLum: float
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

class HdrSourceConfiguration:
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

class ImagePointHsg:
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

class PccCoefficientsDirect:
     PccRedR: float
     PccRedG: float
     PccRedB: float
     PccGreenR: float
     PccGreenG: float
     PccGreenB: float
     PccBlueR: float
     PccBlueG: float
     PccBlueB: float
     PccCyanR: float
     PccCyanG: float
     PccCyanB: float
     PccMagentaR: float
     PccMagentaG: float
     PccMagentaB: float
     PccYellowR: float
     PccYellowG: float
     PccYellowB: float
     PccWhiteR: float
     PccWhiteG: float
     PccWhiteB: float

class I2CPassthrough:
     Port: I2CPortT
     Is7Bit: int                            # int
     HasSubaddr: int                        # int
     ClockRate: int                         # int
     DeviceAddress: int                     # int
     SubAddr: bytearray
     DataBytes: bytearray

class UartConfiguration:
     Enable: bool
     BaudRate: UrtBaudRateT
     DataBits: UrtDataBitsT
     StopBits: UrtStopBitsT
     Parity: UrtParityT
     FlowControl: UrtFlowControlT
     RxTrigLevel: UrtFifoTriggerLevelT
     TxTrigLevel: UrtFifoTriggerLevelT
     RxDataPolarity: UrtRxDataPolarityT
     RxDataSource: UrtRxDataSourceT

class TpgHorizontalLines:
     Width: int                             # int
     Space: int                             # int
     LineColorRed: int                      # int
     LineColorGreen: int                    # int
     LineColorBlue: int                     # int
     BackgroundColorRed: int                # int
     BackgroundColorGreen: int              # int
     BackgroundColorBlue: int               # int

class TpgVerticalLines:
     Width: int                             # int
     Space: int                             # int
     LineColorRed: int                      # int
     LineColorGreen: int                    # int
     LineColorBlue: int                     # int
     BackgroundColorRed: int                # int
     BackgroundColorGreen: int              # int
     BackgroundColorBlue: int               # int

class TpgDiagonalLines:
     LineColorRed: int                      # int
     LineColorGreen: int                    # int
     LineColorBlue: int                     # int
     BackgroundColorRed: int                # int
     BackgroundColorGreen: int              # int
     BackgroundColorBlue: int               # int

class TpgGridLines:
     HorizontalWidth: int                   # int
     HorizontalSpace: int                   # int
     VerticalWidth: int                     # int
     VerticalSpace: int                     # int
     LineColorRed: int                      # int
     LineColorGreen: int                    # int
     LineColorBlue: int                     # int
     BackgroundColorRed: int                # int
     BackgroundColorGreen: int              # int
     BackgroundColorBlue: int               # int

class TpgFixedRamp:
     StartIntensity: int                    # int
     RampStepWidth: int                     # int
     RampStepInc: int                       # int
     BackgroundColorRed: int                # int
     BackgroundColorGreen: int              # int
     BackgroundColorBlue: int               # int
     RampColor: TpgColorT

class TpgDiamondDiagLines:
     ForwardLineStartColor: TpgLineColorT
     BackwardLineColor: TpgLineColorT
     BackgroundColorRed: int                # int
     BackgroundColorGreen: int              # int
     BackgroundColorBlue: int               # int
     DoubleLineMode: bool
     Distance: int                          # int

class TpgCheckerboard:
     Width: int                             # int
     Height: int                            # int
     TopLeftCheckerColorRed: int            # int
     TopLeftCheckerColorGreen: int          # int
     TopLeftCheckerColorBlue: int           # int
     NextCheckerColorRed: int               # int
     NextCheckerColorGreen: int             # int
     NextCheckerColorBlue: int              # int

class TpgCrossPattern:
     CoordinateX: int                       # int
     CoordinateY: int                       # int
     LineColorRed: int                      # int
     LineColorGreen: int                    # int
     LineColorBlue: int                     # int
     BackgroundColorRed: int                # int
     BackgroundColorGreen: int              # int
     BackgroundColorBlue: int               # int

_readcommand = None
_writecommand = None

def DLPC754X_QUADinit(readcommandcb, writecommandcb):
    global _readcommand
    global _writecommand
    _readcommand = readcommandcb
    _writecommand = writecommandcb

    global Summary
    Summary.CommInterface = "DLPC754X_QUAD"

    global PortocolData
    ProtocolData.CommandDestination = 0
    ProtocolData.OpcodeLength = 0
    ProtocolData.BytesRead = 0

def ReadMode():
    "This command returns whether we are in Bootloader or in Main Application."
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
        AppModeObj = getbits(1, 0);
        ControllerConfigObj = getbits(1, 1);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, CmdModeT(AppModeObj), CmdControllerConfigT(ControllerConfigObj)

def ReadVersion():
    "This command returns the version of the currently active Application and the version of the underlying API library. The currently active application can be queried using [[#t-mode_read]] command."
    global Summary
    Summary.Command = "Read Version"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 1;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(19, writebytes, ProtocolData)
        Version.AppMajor = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        Version.AppMinor = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        Version.AppPatch = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        Version.PreReleaseName = str(bytearray(readbytes), encoding)
        Version.PreReleaseVersion = struct.unpack_from ('B', bytearray(readbytes), 4)[0]
        Version.TestBuildNumber = struct.unpack_from ('B', bytearray(readbytes), 5)[0]
        Version.ApiMajor = struct.unpack_from ('B', bytearray(readbytes), 6)[0]
        Version.ApiMinor = struct.unpack_from ('B', bytearray(readbytes), 7)[0]
        Version.ApiPatch = struct.unpack_from ('H', bytearray(readbytes), 8)[0]
        Version.ApiPreReleaseName = str(bytearray(readbytes), encoding)
        Version.ApiPreReleaseVersion = struct.unpack_from ('B', bytearray(readbytes), 10)[0]
        Version.ApiTestBuildNumber = struct.unpack_from ('B', bytearray(readbytes), 11)[0]
        Version.FpgaBuildNumber = struct.unpack_from ('H', bytearray(readbytes), 12)[0]
        Version.FpgaBuildEcoId = struct.unpack_from ('B', bytearray(readbytes), 14)[0]
        Version.FpgaMajor = struct.unpack_from ('B', bytearray(readbytes), 15)[0]
        Version.FpgaMinor = struct.unpack_from ('B', bytearray(readbytes), 16)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Version

def WriteSwitchMode(SwitchMode):
    "This command is used to switch between bootloader and application mode."
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

def ReadBootHoldReason():
    "Returns the code that specifies the reason for being in bootloader mode."
    global Summary
    Summary.Command = "Read Boot Hold Reason"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 1;
    try:
        writebytes=list(struct.pack('B',18))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        ReasonCode = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ReasonCode

def ReadFlashInfo(ChipSelect):
    "This command returns the flash device and manufacturer IDs. Only CFI compliant flash devices are supported. The system can have multiple flash devices. The command returns the info for the flash present at the given chip select."
    global Summary
    Summary.Command = "Read Flash Info"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 1;
    try:
        writebytes=list(struct.pack('B',32))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',ChipSelect.value)))
        readbytes = _readcommand(15, writebytes, ProtocolData)
        ManfId = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        DevId = struct.unpack_from ('Q', bytearray(readbytes), 2)[0]
        DevSize = struct.unpack_from ('I', bytearray(readbytes), 10)[0]
        ********** Invalid Write Data Field Type - DLPComposer.Commands.Spec.ArrayType;
        readdata = struct.unpack_from ('B', bytearray(readbytes), 14)[0]
        packerinit(readdata)
        AvailableForProgramming = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ManfId, DevId, DevSize, SectorInfo, AvailableForProgramming

def ReadGetProgrammableFlashSectorInformation():
    "This command returns the flash sector information read from CFI compliant flash devices. If the flash is non-CFI compliant, this command will fail. The sectors returned by this command are the only ones available for programming a flash image. The system is designed such that the flash image is in a contiguous memory space. If a system has multiple flash parts, then the software checks the size of the flash at ChipSelect 0. If this is equal to the maximum supported size (32MB), then a flash device at ChipSelect 1 (if present) will also be supported for flash programming. Similarly, if the size of flash devices at both ChipSelect 0 and 1 are 32MB, then a flash device at ChipSelect 2 (if present) will be supported for flash programming as well. The command appends the sector information for each part, which is supported for flash programming, and provides them as output."
    global Summary
    Summary.Command = "Read Get Programmable Flash Sector Information"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 1;
    try:
        writebytes=list(struct.pack('B',33))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(0, writebytes, ProtocolData)
        ********** Invalid Write Data Field Type - DLPComposer.Commands.Spec.ArrayType;
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SectorInfo

def WriteUnlockFlashForUpdate(Unlock):
    "This command unlocks the flash update operation (Download, Erase). By default the flash update operations are locked. This is to prevent accidental modification of flash contents. To unlock, the pre-defined key shall be send as the unlock code. Calling this command with any other parameter will lock the flash update commands."
    global Summary
    Summary.Command = "Write Unlock Flash For Update"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 1;
    try:
        writebytes=list(struct.pack('B',34))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',Unlock.value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadUnlockFlashForUpdate():
    "This command returns whether the flash is in unlocked state."
    global Summary
    Summary.Command = "Read Unlock Flash For Update"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 1;
    try:
        writebytes=list(struct.pack('B',34))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        IsUnlocked = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, IsUnlocked

def WriteEraseSector(SectorAddress):
    "This command erases the sector of the flash where the given address falls in. This command is a flash update command, and requires flash operations to be unlocked using [[#t-unlock_flash_for_update_write]] command. The sector address shall be specified as an offset from flash start address. For example in a flash device where all sectors are 64KB of size, sector addresses shall be specified as follows:- <br> Sector 0 = 0 <br> Sector 1 = 0x10000 <br> Sector 2 = 0x20000 <br> and so on... <br>"
    global Summary
    Summary.Command = "Write Erase Sector"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 1;
    try:
        writebytes=list(struct.pack('B',35))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('I',SectorAddress)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteInitializeFlashReadWriteSettings(StartAddress,  NumBytes):
    "This command initializes flash read/write operation. This command shall be called before a [[#t-flash_write_command]] command is sent. Note: For Flash Write, the Address and download size set up shall both be even.__"
    global Summary
    Summary.Command = "Write Initialize Flash Read Write Settings"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 1;
    try:
        writebytes=list(struct.pack('B',36))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('I',StartAddress)))
        writebytes.extend(list(struct.pack('I',NumBytes)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteFlashWrite(Data):
    "This command is used to program data to flash. This command shall be called only after setting the start address and size using the [[#t-initialize_flash_read_write_settings_write]] command. This command is a flash update command, and requires flash operations to be unlocked using [[#t-unlock_flash_for_update_write]] command. <BR> Flash write commands can be chained till the initialized number of bytes are programmed. The bootloader will auto-increment the address and size for each command. Only the initialized number of bytes will be programmed even if more data is provided. <BR> __It is important to send only even number of bytes per flash write command to ensure all bytes are written. This is done so that all flash writes are optimized as per the multi-word write supported by the flash device.__ This command supports variable sized payload."
    global Summary
    Summary.Command = "Write Flash Write"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 1;
    try:
        writebytes=list(struct.pack('B',37))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(Data))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadFlashWrite(NumBytesToRead):
    "This command is used to read data from flash. This command shall be called only after setting the start address and size using the [[#t-initialize_flash_read_write_settings_write]] command. <BR> Flash read commands can be chained till the initialized number of bytes are returned. The bootloader will auto-increment the address and size for each command. Only the initialized number of bytes will be returned. Calling the function after returning requested data will return in command failure. This command supports variable sized response."
    global Summary
    Summary.Command = "Read Flash Write"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 1;
    try:
        writebytes=list(struct.pack('B',37))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',NumBytesToRead)))
        readbytes = _readcommand(0, writebytes, ProtocolData)
        Data = bytearray(readbytes)[0, 1]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Data

def ReadChecksum(StartAddress,  NumBytes):
    "This command computes and returns the checksum starting at the given address for the specified number of bytes. Checksum is calculated as below:- <BR> uint32 SimpleChecksum = 0; <BR> uint32 SumofSumChecksum = 0; <BR> uint08 *Addr = (uint08 *) StartAddress; <BR> <BR> while (NumBytes--) <BR> { <BR> SimpleChecksum += *Addr++; <BR> SumofSumChecksum += SimpleChecksum; <BR> } <BR>"
    global Summary
    Summary.Command = "Read Checksum"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 1;
    try:
        writebytes=list(struct.pack('B',38))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('I',StartAddress)))
        writebytes.extend(list(struct.pack('I',NumBytes)))
        readbytes = _readcommand(8, writebytes, ProtocolData)
        SimpleChecksum = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        SumofSumChecksum = struct.unpack_from ('I', bytearray(readbytes), 4)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SimpleChecksum, SumofSumChecksum

def WriteResetFlash(ChipSelect):
    "This command resets the Flash device connected to the given chipselect. Any partial commands given gets reset and the flash is put in read mode."
    global Summary
    Summary.Command = "Write Reset Flash"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 1;
    try:
        writebytes=list(struct.pack('B',39))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',ChipSelect.value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteMemory(Address,  Value):
    "This command attempts a direct write of the given 32-bit value to the given 32-bit memory address. The memory address is not verified whether it is valid to write to the location."
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
    "This command returns the 32-bit value stored at the given 32-bit memory address."
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
    "Writes a stream of words into the RAM memory (DRAM or IRAM) starting from the address specified. Performs no checks as to whether the specified memory address given is valid or not."
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
    "Reads a stream of words from memory starting from the address specified. Performs no checks as to whether the specified memory address given is valid or not."
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

def ReadControllerInfo():
    "Returns DLP Controller Information."
    global Summary
    Summary.Command = "Read Controller Info"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',0))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(13, writebytes, ProtocolData)
        ControllerId = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        ControllerName = str(bytearray(readbytes), encoding)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ControllerId, ControllerName

def ReadDmdInfo():
    "Returns the dmd information."
    global Summary
    Summary.Command = "Read Dmd Info"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(34, writebytes, ProtocolData)
        DmdId = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        FuseId = struct.unpack_from ('I', bytearray(readbytes), 4)[0]
        FuseBitString = str(bytearray(readbytes), encoding)
        DmdName = str(bytearray(readbytes), encoding)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DmdId, FuseId, FuseBitString, DmdName

def ReadDmdResolution():
    "Returns the DMD width and height in number of pixels and lines respectively."
    global Summary
    Summary.Command = "Read Dmd Resolution"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',2))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        Width = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        Height = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Width, Height

def ReadFlashVersion():
    "Returns version number that uniquely identifies the flash image."
    global Summary
    Summary.Command = "Read Flash Version"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',3))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(3, writebytes, ProtocolData)
        FlashVersionMajor = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        FlashVersionMinor = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        FlashVersionSubminor = struct.unpack_from ('B', bytearray(readbytes), 2)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, FlashVersionMajor, FlashVersionMinor, FlashVersionSubminor

def ReadFlashLayoutVersion():
    "Returns supported Layout revision numbers and hash for flash config and app config layout."
    global Summary
    Summary.Command = "Read Flash Layout Version"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',4))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(68, writebytes, ProtocolData)
        FlashConfigLayoutVersion = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        FlashConfigLayoutHash = str(bytearray(readbytes), encoding)
        ApplicationConfigLayoutVersion = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        ApplicationConfigLayoutHash = str(bytearray(readbytes), encoding)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, FlashConfigLayoutVersion, FlashConfigLayoutHash, ApplicationConfigLayoutVersion, ApplicationConfigLayoutHash

def ReadProductConfigurationFailureCause():
    "Use this command to get the cause of product configuration failure if Product Configuration Failed is set in system status command."
    global Summary
    Summary.Command = "Read Product Configuration Failure Cause"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',5))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        ProductConfigFailCauseObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DdpProductConfigFailCauseT(ProductConfigFailCauseObj)

def ReadSystemStatus():
    "Command to read status information from DLP Controller. If status interrupt is enabled (configurable via default UI tool in DLP Composer), reading back this command will acknowledge/deactivate the interrupt pin until the next change in status."
    global Summary
    Summary.Command = "Read System Status"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',6))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        SystemStatus.MemTstPassed = getbits(1, 4);
        SystemStatus.FrameRateConvEn = getbits(1, 10);
        SystemStatus.SeqPhaselock = getbits(1, 11);
        SystemStatus.SeqFreqlock = getbits(1, 12);
        SystemStatus.SeqSearch = getbits(1, 13);
        SystemStatus.ScpcalEnable = getbits(1, 29);
        SystemStatus.VicalEnable = getbits(1, 30);
        SystemStatus.BccalEnable = getbits(1, 31);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SystemStatus

def ReadSystemErrorStatus():
    "Command to read status information from DLP Controller. If status interrupt is enabled (configurable via default UI tool in DLP Composer), reading back this command will acknowledge/deactivate the interrupt pin until the next change in status."
    global Summary
    Summary.Command = "Read System Error Status"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',7))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(8, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        SystemErrorStatus.SequenceErr = getbits(1, 0);
        SystemErrorStatus.PixclkOor = getbits(1, 1);
        SystemErrorStatus.SyncvalStat = getbits(1, 2);
        SystemErrorStatus.FpgaInitErr = getbits(1, 3);
        SystemErrorStatus.FpgaCommErr = getbits(1, 4);
        SystemErrorStatus.FpgaConfigErr = getbits(1, 5);
        SystemErrorStatus.UartPort0CommErr = getbits(1, 6);
        SystemErrorStatus.UartPort1CommErr = getbits(1, 7);
        SystemErrorStatus.UartPort2CommErr = getbits(1, 8);
        SystemErrorStatus.SspPort0CommErr = getbits(1, 9);
        SystemErrorStatus.SspPort1CommErr = getbits(1, 10);
        SystemErrorStatus.SspPort2CommErr = getbits(1, 11);
        SystemErrorStatus.I2CPort0CommErr = getbits(1, 12);
        SystemErrorStatus.I2CPort1CommErr = getbits(1, 13);
        SystemErrorStatus.I2CPort2CommErr = getbits(1, 14);
        SystemErrorStatus.DlpcInitErr = getbits(1, 15);
        SystemErrorStatus.NoFreqBinErr = getbits(1, 19);
        SystemErrorStatus.Dlpa3000CommErr = getbits(1, 20);
        SystemErrorStatus.UmcRefreshBwUnderflowErr = getbits(1, 21);
        SystemErrorStatus.DmdInitErr = getbits(1, 22);
        SystemErrorStatus.DmdPwrDownErr = getbits(1, 23);
        SystemErrorStatus.SrcdefNotpresent = getbits(1, 24);
        SystemErrorStatus.SeqbinNotpresent = getbits(1, 25);
        SystemErrorStatus.ProductConfigurationFailed = getbits(1, 26);
        SystemErrorStatus.TemporalDitherMaskNotLoading = getbits(1, 27);
        SystemErrorStatus.MultiControllerSyncError = getbits(1, 28);
        SystemErrorStatus.MultiControllerSeqSyncError = getbits(1, 29);
        SystemErrorStatus.HubInitFailed = getbits(1, 30);
        readdata = struct.unpack_from ('I', bytearray(readbytes), 4)[0]
        packerinit(readdata)
        SystemErrorStatus.EepromInitFail = getbits(1, 0);
        SystemErrorStatus.FpgaOverTemperature = getbits(1, 1);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SystemErrorStatus

def ReadEepromDataPresent():
    "Reports which of the calibration data blocks are present in EEPROM. Use this command before sending EEPROM Invalidate command (0x0A)."
    global Summary
    Summary.Command = "Read Eeprom Data Present"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',8))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(2, writebytes, ProtocolData)
        readdata = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        EepromDataPresent.ColorwheelLampDataPresent = getbits(1, 0);
        EepromDataPresent.SsiCalibrationDataPresent = getbits(1, 1);
        EepromDataPresent.AdcCalibrationDataPresent = getbits(1, 2);
        EepromDataPresent.WpcSensorCalibrationDataPresent = getbits(1, 3);
        EepromDataPresent.WpcBrightnessTableDataPresent = getbits(1, 4);
        EepromDataPresent.XprCalibrationDataPresent = getbits(1, 5);
        EepromDataPresent.XprWaveformCalibrationDataPresent = getbits(1, 6);
        EepromDataPresent.EdgeBlendDataPresent = getbits(1, 7);
        EepromDataPresent.SurfaceCorrectionDataPresent = getbits(1, 8);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, EepromDataPresent

def WriteGeneralDelayCommand(DelayInMilliseconds):
    "On receipt of this command controller wait for specified period before executing the next command. This command to be used in Auto Initialization batchfile configuration. Use this command to insert delay between execution of two commands."
    global Summary
    Summary.Command = "Write General Delay Command"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',9))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('I',DelayInMilliseconds)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteEepromInvalidate(EepromInvalidate):
    "Invalidates the user settings portion of EEPROM data or calibration portion of EEPROM data or both as per input arguments and restarts the system. If none of the settings or calibration data is selected, then the command does nothing. Note: Chose valid flags as returned in [[#cat-administrative/eeprom_data_present_read]] command."
    global Summary
    Summary.Command = "Write Eeprom Invalidate"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',10))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(EepromInvalidate.InvalidateSettings), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(int(EepromInvalidate.InvalidateColorwheelLampData), 1, 0)
        value = setbits(int(EepromInvalidate.InvalidateSsiCalibrationData), 1, 1)
        value = setbits(int(EepromInvalidate.InvalidateAdcCalibrationData), 1, 2)
        value = setbits(int(EepromInvalidate.InvalidateWpcSensorCalibrationData), 1, 3)
        value = setbits(int(EepromInvalidate.InvalidateWpcBrightnessTableData), 1, 4)
        value = setbits(int(EepromInvalidate.InvalidateXprCalibrationData), 1, 5)
        value = setbits(int(EepromInvalidate.InvalidateXprWaveformCalibrationData), 1, 6)
        value = setbits(int(EepromInvalidate.InvalidateEdgeBlendData), 1, 7)
        value = setbits(int(EepromInvalidate.InvalidateSurfaceCorrectionData), 1, 8)
        writebytes.extend(list(struct.pack('I',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteXprCalibPatternDisplay():
    "This command loads a pre-defined XPR Calibration pattern as a splash image and displays it on the screen. A 64x64 pattern is repeated over a 7680x4320 display area."
    global Summary
    Summary.Command = "Write Xpr Calib Pattern Display"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',179))
        ProtocolData.OpcodeLength = 1;
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteXpr4WayOrientation(XprOrientationNumber):
    "This command sets the orientation number of the actuator position There are 24 possible options 0 - 23; use this commmand while performing XPR calibration using TI provided XPR calibration splash image."
    global Summary
    Summary.Command = "Write Xpr 4 Way Orientation"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',180))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',XprOrientationNumber)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadXpr4WayOrientation():
    "This command retrieves the last set orientation number or the subframe order"
    global Summary
    Summary.Command = "Read Xpr 4 Way Orientation"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',180))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        XprOrientationNumber = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, XprOrientationNumber

def WriteXprActuatorWaveformControlParameter(XprCommand,  AwcChannel,  Data):
    "This command configure/setup Actuator Waveform Control(AWC) block. Here, AWCx can be AWC 0 or 1. Bytes 2-5 contains the XPR command data as mentioned in Byte 0. Byte 1 contains AWC channel number, possible values are 0 or 1.<BR><BR> **Fixed Output Enable** : Configures Actuator in fixed output mode.<BR> Byte    2: 0x00 - Disable 0x01 - Enable  <BR> Bytes 3-5: Reserved must be set to 0x000000<BR><BR> **Gain** : Set Waveform Generator DAC/PWM Gain.<BR> Byte    2: Range 0 - 255 format u1.7 (0 to 1.9921875) <BR> Bytes 3-5: Reserved must be set to 0x000000<BR><BR> **Subframe delay** : Subframe delay Bytes 2-5; Range 0 - 262143 and lsb = 133.333ns  <BR><BR> **Actuator Type (READ ONLY)** : Actuator type <BR> Byte    2: <BR>0x00 - NONE <BR> 0x01 - Optotune (XPR-25 Model) <BR> 0x80 - TI Actuator Interface (EEPROM) <BR> 0x81 - TI Actuator Interface (MCU) <BR> Bytes 3-5: Reserved must be set to 0x000000<BR><BR> **Output Enable/Disable** : Actuator output enable/disable <BR> Byte    2: 0x00 - Disable 0x01 - Enable  <BR> Bytes 3-5: Reserved must be set to 0x000000<BR><BR> Note: Both AWC0 and AWC1 disabled/enabled together <BR> **Clock Width** : Defines the high and low width for the output clock (the clock period will be 2*(ClkWidth+1)) <BR> 0 = 1 (Clock period is two clocks); lsb = 8.33ns <BR> Bytes 2-5 : ClkWidth <BR> Example: ClkWidth = 0; will generate clock of 2*(0+1)*8.33 = 16.66ns <BR><BR> **Offset** : DAC/PWM Output Offset <BR> Byte    2: Range -128 - +127 format S7 (-128 to +127) <BR> Bytes 3-5: Reserved must be set to 0x000000<BR><BR> **Number of Segments** : Defines number of segments <BR> Byte    2: Range 2 - 255<BR> Bytes 3-5: Reserved must be set to 0x000000<BR><BR> **Segments Length** : Defines size of the segments <BR> Bytes 2-3: Range 19 - 4095<BR> Bytes 4-5: Reserved must be set to 0x0000<BR><BR> **Invert PWM A** : Applicable when AWC is configured to PWM type instead of DAC <BR> Byte    2: 0x00 - No inversion <BR> 0x01 - Inverted  <BR> Bytes 3-5: Reserved must be set to 0x000000<BR><BR> **Invert PWM B** : Applicable when AWC is configured to PWM type instead of DAC <BR> Byte    2: 0x00 - No inversion 0x01 - Inverted  <BR> Bytes 3-5: Reserved must be set to 0x000000<BR><BR> **Subframe Filter Value** : Sets Subframe Filter Value - defines the minimum time between Subframe edges. Edges closer than the set value will be filtered out <BR> Byte    2: 0 = Filter disabled, >0 = Filter time will be Val x 60us, Range: 0 - 255 <BR> Bytes 3-5: Reserved must be set to 0x000000<BR><BR> **Subframe Watch Dog** : Defines the maximum time between Subframe edges; if timer expires, then the WG will automatically output the Fixed Output value, and the normal output will resume on the next subframe edge.<BR> Bytes 2-3: 0 = Subframe watchdog disabled, >0 = Watchdog time will be Time x 60us, Range: Range: 0 - 1023 <BR> Bytes 4-5: Reserved must be set to 0x0000<BR><BR> **Fixed Output Value** : Defines the value to be output on DAC/PWM when fixed output mode is selected.<BR> Byte    2: Value to be output on DAC/PWM, Range -128 to 127 Bytes 3-5: Reserved must be set to 0x000000<BR><BR> **Note** : To use **Subframe Filter Value** and **Subframe Watch Dog** care must be taken to set a value which aproximately 10% more than 2x of the operating frequency. <BR> For example - 4K @ 60Hz, the value can be set as (1/(60*2))*1.10*10^6 = 9166us."
    global Summary
    Summary.Command = "Write Xpr Actuator Waveform Control Parameter"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',XprCommand.value)))
        writebytes.extend(list(struct.pack('B',AwcChannel)))
        writebytes.extend(list(struct.pack('I',Data)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadXprActuatorWaveformControlParameter(XprCommand,  AwcChannel):
    "This command gets the parameter set to the AWC waveform generator.<BR> **Note** : This command is supposed to be used only during the normal operating mode and not during the standby state."
    global Summary
    Summary.Command = "Read Xpr Actuator Waveform Control Parameter"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',XprCommand.value)))
        writebytes.extend(list(struct.pack('B',AwcChannel)))
        readbytes = _readcommand(4, writebytes, ProtocolData)
        Data = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Data

def WriteDbAperturePosition(Position):
    "This command controls how far open or closed the aperture should be over the light source. The aperture position is adjusted every frame based on the current scene brightness. Note: This function should only be used during calibration and only when the DynamicBlack(tm) II algorithm is disabled."
    global Summary
    Summary.Command = "Write Db Aperture Position"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',183))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',Position)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDbAperturePosition():
    "This command gives how far open or closed the aperture is over the light source. The aperture position is adjusted every frame based on the current scene brightness. Note: This function should only be used during calibration and only when the DynamicBlack(tm) II algorithm is disabled."
    global Summary
    Summary.Command = "Read Db Aperture Position"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',183))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(2, writebytes, ProtocolData)
        Position = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Position

def WriteDbApertureMinMax(AptMin,  AptMax):
    "This command controls the minimum and maximum aperture positions. The minimum command typically corresponds to the aperture position for the aperture to be fully closed, while the maximum command typically corresponds to the aperture position for the aperture to be fully open. However, the polarity of these may change depending on the aperture hardware used."
    global Summary
    Summary.Command = "Write Db Aperture Min Max"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',184))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',AptMin)))
        writebytes.extend(list(struct.pack('H',AptMax)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDbApertureMinMax():
    "This command gets the minimum and maximum aperture positions. The minimum command typically corresponds to the aperture position for the aperture to be fully closed, while the maximum command typically corresponds to the aperture position for the aperture to be fully open. However, the polarity of these may change depending on the aperture hardware used."
    global Summary
    Summary.Command = "Read Db Aperture Min Max"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',184))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        AptMin = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        AptMax = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, AptMin, AptMax

def WriteDbManualMode(Enable):
    "This command enables the DynamicBlack(tm) II Manual Mode of operation. It is intended to be used as a test command. The DB software algorithm will be disabled, and the user can set manual gain values using DB set gain command."
    global Summary
    Summary.Command = "Write Db Manual Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',185))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Enable)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDbManualMode():
    "This command enables the DynamicBlack(tm) II Manual Mode of operation. It is intended to be used as a test command. The DB software algorithm will be disabled, and the user can set manual gain values using DB set gain command."
    global Summary
    Summary.Command = "Read Db Manual Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',185))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        Enable = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Enable

def WriteDbBorderConfiguration(Top,  Bottom,  Left,  Right):
    "This command configures area of the DynamicBlack(tm) II border region for the border exclusion function. The border exclusion function allows the user to reduce the letterbox (black border) effect on a primarily bright image where letterbox area reduces the overall scene brightness for the algorithm. It also helps the algorithm better handle images with bright subtitles where the subtitles increase the overall scene brightness. This command will also be used in a multi-ASIC configuration to exclude any image overlap required for other image processing algorithms."
    global Summary
    Summary.Command = "Write Db Border Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',187))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',Top)))
        writebytes.extend(list(struct.pack('H',Bottom)))
        writebytes.extend(list(struct.pack('H',Left)))
        writebytes.extend(list(struct.pack('H',Right)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDbBorderConfiguration():
    "This Command returns the border region area for the DynamicBlack(tm) II border exclusion function."
    global Summary
    Summary.Command = "Read Db Border Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',187))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(8, writebytes, ProtocolData)
        Top = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        Bottom = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        Left = struct.unpack_from ('H', bytearray(readbytes), 4)[0]
        Right = struct.unpack_from ('H', bytearray(readbytes), 6)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Top, Bottom, Left, Right

def WriteDbBorderWeight(BorderWeight):
    ""
    global Summary
    Summary.Command = "Write Db Border Weight"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',188))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',BorderWeight.value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDbBorderWeight():
    "Sets weight value of the DynamicBlack(tm) II border region for the border exclusion function"
    global Summary
    Summary.Command = "Read Db Border Weight"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',188))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        BorderWeightObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DbPixelWeightT(BorderWeightObj)

def WriteDbClipPixels(ClipPixels):
    "This command returns currently configured number of steps to allow the DynamicBlack(tm) II aperture to move."
    global Summary
    Summary.Command = "Write Db Clip Pixels"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',189))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',ClipPixels)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDbClipPixels():
    "This command returns the currently selected number of pixels that can be clipped."
    global Summary
    Summary.Command = "Read Db Clip Pixels"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',189))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(2, writebytes, ProtocolData)
        ClipPixels = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ClipPixels

def WriteDbGain(DbGain):
    "This command controls the DynamicBlack(tm) II gain value. Typical value range is 1.0 to 8.0. Manual Mode needs to be enabled to set the gain as it will override the gain value that is calculated every frame."
    global Summary
    Summary.Command = "Write Db Gain"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',190))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(DbGain,4096)))))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDbGain():
    "This command gets the DynamicBlack(tm) II gain value. Typical value range is 1.0 to 8.0"
    global Summary
    Summary.Command = "Read Db Gain"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',190))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(2, writebytes, ProtocolData)
        DbGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 0)[0], 4096)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DbGain

def WriteDbNumSteps(Steps):
    "This command sets the number of steps to allow the DynamicBlack(tm) II aperture to move. This allows the number of steps to be adjusted dynamically so that the results can be visually compared."
    global Summary
    Summary.Command = "Write Db Num Steps"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',191))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',Steps)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDbNumSteps():
    "This command returns currently configured number of steps to allow the DynamicBlack(tm) II aperture to move."
    global Summary
    Summary.Command = "Read Db Num Steps"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',191))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(2, writebytes, ProtocolData)
        Steps = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Steps

def WriteDbApertureSpeed(Speed):
    "This command specifies the number of positions that the DynamicBlack(tm) aperture can move in one frame."
    global Summary
    Summary.Command = "Write Db Aperture Speed"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',192))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',Speed)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDbApertureSpeed():
    "This command returns the number of positions that the DynamicBlack(tm) II aperture can move in one frame."
    global Summary
    Summary.Command = "Read Db Aperture Speed"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',192))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(2, writebytes, ProtocolData)
        Speed = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Speed

def WriteDbStrength(Strength):
    "This function controls the DynamicBlack(tm) II strength. A higher strength value will cause DynamicBlack(tm) II to be more aggressive in closing the aperture for a given scene brightness. The aperture min and max positions have to be set prior to calling this function. The aperture movement strength range is 0 to 3, with a recommended value of 2."
    global Summary
    Summary.Command = "Write Db Strength"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',193))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Strength)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDbStrength():
    "This function returns the DynamicBlack(tm) II strength setting."
    global Summary
    Summary.Command = "Read Db Strength"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',193))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        Strength = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Strength

def ReadDbHistogram():
    "This command returns the start address of the DynamicBlack(tm) II (DB) histogram data. The histogram contains scene brightness data from the previous frame. The DB histogram contains 34 bins measuring non-overlapping intensity ranges in the displayed image. The value of each bin equals the number of pixels within the bin's intensity range. Each pixel's intensity is calculated as the maximum of its red, green, and blue values. In other words, pixel intensity = MAX( R, G, B ). Each pixel has a format of unsigned 8.8, making 16 bit values. Bins 32 and 33 are special bins that represent pixels that have values of exactly zero and only fractional values respectively. This function can be used independently of aperture control for image improvement in dark scenes."
    global Summary
    Summary.Command = "Read Db Histogram"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',194))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(136, writebytes, ProtocolData)
        HistPtr = bytearray(readbytes)[0, 136]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, HistPtr

def ReadDbCurrentApertPos():
    "This function returns the current aperture position.  This position indicates how far open or closed the aperture is over the light source. The aperture position is adjusted every frame based on the current scene brightness."
    global Summary
    Summary.Command = "Read Db Current Apert Pos"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',195))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        Position = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Position

def WriteSsiDutyCycleIndex(Index):
    "Select Duty Cycle index for SSI"
    global Summary
    Summary.Command = "Write Ssi Duty Cycle Index"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',207))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',Index)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadSsiDutyCycleIndex():
    "Get Details of selected Duty Cycles and number of duty cycles available in current system look"
    global Summary
    Summary.Command = "Read Ssi Duty Cycle Index"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',207))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(18, writebytes, ProtocolData)
        SsiDutyCycleIndex.NumberOfDutyCycles = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        SsiDutyCycleIndex.CurrentDutyCycleIndex = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        SsiDutyCycleIndex.CurrentRedDutyCycle = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 4)[0], 256)
        SsiDutyCycleIndex.CurrentGreenDutyCycle = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 6)[0], 256)
        SsiDutyCycleIndex.CurrentBlueDutyCycle = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 8)[0], 256)
        SsiDutyCycleIndex.CurrentYellowDutyCycle = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 10)[0], 256)
        SsiDutyCycleIndex.CurrentCyanDutyCycle = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 12)[0], 256)
        SsiDutyCycleIndex.CurrentMagentaDutyCycle = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 14)[0], 256)
        SsiDutyCycleIndex.CurrentWhiteDutyCycle = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 16)[0], 256)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SsiDutyCycleIndex

def WriteEnableXprCalibrationMode(Enable):
    "This command sets the system in bypass mode. Setting the system in  bypass mode disables any image processing to establish one to one correspondence between pixels on input source image and display image. Desirable for seeing clear splits of XPR subframes. There is no exit from calibration mode. Please restart the system."
    global Summary
    Summary.Command = "Write Enable Xpr Calibration Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',209))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Enable)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadEnableXprCalibrationMode():
    "This command gets the state of XPR calibration mode. Whether enabled or not."
    global Summary
    Summary.Command = "Read Enable Xpr Calibration Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',209))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        Enable = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Enable

def WriteDebugMessageMask(DebugMessageMask):
    "Set enable mask for debug messages. The mask identifies the sources of debug messages which are to be enabled for printing at the UART debug port. The mask bit corresponding to the source has to be set to enable it."
    global Summary
    Summary.Command = "Write Debug Message Mask"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',224))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(DebugMessageMask.Comm), 1, 11)
        value = setbits(int(DebugMessageMask.ThreeD), 1, 13)
        value = setbits(int(DebugMessageMask.MessageService), 1, 14)
        value = setbits(int(DebugMessageMask.I2C), 1, 15)
        value = setbits(int(DebugMessageMask.ClosedCaptioning), 1, 17)
        value = setbits(int(DebugMessageMask.DdcCi), 1, 18)
        value = setbits(int(DebugMessageMask.Gui), 1, 19)
        value = setbits(int(DebugMessageMask.Environment), 1, 20)
        value = setbits(int(DebugMessageMask.Illumination), 1, 21)
        value = setbits(int(DebugMessageMask.System), 1, 22)
        value = setbits(int(DebugMessageMask.Eeprom), 1, 23)
        value = setbits(int(DebugMessageMask.Datapath), 1, 24)
        value = setbits(int(DebugMessageMask.Autolock), 1, 25)
        value = setbits(int(DebugMessageMask.ProjectorCtl), 1, 26)
        value = setbits(int(DebugMessageMask.Peripheral), 1, 27)
        value = setbits(int(DebugMessageMask.Ir), 1, 28)
        value = setbits(int(DebugMessageMask.Usb), 1, 29)
        value = setbits(int(DebugMessageMask.Mailbox), 1, 30)
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDebugMessageMask():
    "Retrieves the current debug message mask. The mask decides which sources of debug messages are enabled. A value of 1 in the mask bit corresponding to a source means that the source is enabled."
    global Summary
    Summary.Command = "Read Debug Message Mask"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',224))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        DebugMessageMask.Comm = getbits(1, 11);
        DebugMessageMask.ThreeD = getbits(1, 13);
        DebugMessageMask.MessageService = getbits(1, 14);
        DebugMessageMask.I2C = getbits(1, 15);
        DebugMessageMask.ClosedCaptioning = getbits(1, 17);
        DebugMessageMask.DdcCi = getbits(1, 18);
        DebugMessageMask.Gui = getbits(1, 19);
        DebugMessageMask.Environment = getbits(1, 20);
        DebugMessageMask.Illumination = getbits(1, 21);
        DebugMessageMask.System = getbits(1, 22);
        DebugMessageMask.Eeprom = getbits(1, 23);
        DebugMessageMask.Datapath = getbits(1, 24);
        DebugMessageMask.Autolock = getbits(1, 25);
        DebugMessageMask.ProjectorCtl = getbits(1, 26);
        DebugMessageMask.Peripheral = getbits(1, 27);
        DebugMessageMask.Ir = getbits(1, 28);
        DebugMessageMask.Usb = getbits(1, 29);
        DebugMessageMask.Mailbox = getbits(1, 30);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DebugMessageMask

def WriteEepromMemory(Index,  Size,  Pwd,  Data):
    "Writes data to EEPROM connected to the controller. <BR> The EEPROM holds settings and calibration data. The primary purpose of this function is for the user to write to areas of EEPROM outside of the settings and calibration data. If user wants to overwrite settings/calibration data, the password sent with the command should match the expected password. This is a protection mechanism to prevent accidental overwrite of settings/calibration data."
    global Summary
    Summary.Command = "Write Eeprom Memory"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',226))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',Index)))
        writebytes.extend(list(struct.pack('H',Size)))
        writebytes.extend(list(struct.pack('I',Pwd)))
        if Size:
            writebytes.extend(list(Data))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadEepromMemory(Index,  Size):
    "This function reads data from EEPROM connected to the Controller which has settings and calibration data."
    global Summary
    Summary.Command = "Read Eeprom Memory"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',226))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',Index)))
        writebytes.extend(list(struct.pack('H',Size)))
        readbytes = _readcommand(Size, writebytes, ProtocolData)
        Data = bytearray(readbytes)[0, 1]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Data

def WriteTiActuatorInterfaceDebug(TiActQueryType,  TiActAddr,  TiActNumData):
    "Command used to query actuator related information for debugging purpose. Use this command to retrieve information when actuator not running or system is in standby state.<BR>"
    global Summary
    Summary.Command = "Write Ti Actuator Interface Debug"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',228))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',TiActQueryType)))
        writebytes.extend(list(struct.pack('H',TiActAddr)))
        writebytes.extend(list(struct.pack('H',TiActNumData)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadTiActuatorInterfaceDebug():
    "Command returns queried data as per the settings made in the set command"
    global Summary
    Summary.Command = "Read Ti Actuator Interface Debug"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',228))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(32, writebytes, ProtocolData)
        ActuatorData = bytearray(readbytes)[0, 32]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ActuatorData

def ReadVsyncPeriod():
    "Returns the latest VSync period measurement"
    global Summary
    Summary.Command = "Read Vsync Period"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',229))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        FramePeriod = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, FramePeriod

def ReadDmdPower():
    "Returns DMD power enable state"
    global Summary
    Summary.Command = "Read Dmd Power"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',232))
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

def WriteDmdPark(Park):
    "Parks/Unparks DMD"
    global Summary
    Summary.Command = "Write Dmd Park"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',233))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(Park), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDmdPark():
    "Returns 1 if DMD is Parked, else returns 0"
    global Summary
    Summary.Command = "Read Dmd Park"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',233))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        Park = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Park

def ReadIntStack():
    ""
    global Summary
    Summary.Command = "Read Int Stack"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',240))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(12, writebytes, ProtocolData)
        StackSize = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        StackUsed = struct.unpack_from ('I', bytearray(readbytes), 4)[0]
        StackFree = struct.unpack_from ('I', bytearray(readbytes), 8)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, StackSize, StackUsed, StackFree

def WritePrintAllTaskInformation():
    "Prints, on UART, Information of all tasks defined/created with RTOS. @retval PASS Successful"
    global Summary
    Summary.Command = "Write Print All Task Information"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',241))
        ProtocolData.OpcodeLength = 1;
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadResource():
    "Gives the maximum RTOS resource usage by the application."
    global Summary
    Summary.Command = "Read Resource"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',242))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(12, writebytes, ProtocolData)
        Resource.TasksHighCount = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        Resource.EventsHighCount = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        Resource.GroupEventsHighCount = struct.unpack_from ('B', bytearray(readbytes), 2)[0]
        Resource.MailboxHighCount = struct.unpack_from ('B', bytearray(readbytes), 3)[0]
        Resource.MemoryPoolsHighCount = struct.unpack_from ('B', bytearray(readbytes), 4)[0]
        Resource.SemaphoreHighCount = struct.unpack_from ('B', bytearray(readbytes), 5)[0]
        Resource.TasksCurrentCount = struct.unpack_from ('B', bytearray(readbytes), 6)[0]
        Resource.EventsCurrentCount = struct.unpack_from ('B', bytearray(readbytes), 7)[0]
        Resource.GrpEventsCurrentCount = struct.unpack_from ('B', bytearray(readbytes), 8)[0]
        Resource.MailboxCurrentCount = struct.unpack_from ('B', bytearray(readbytes), 9)[0]
        Resource.MemoryPoolsCurrentCount = struct.unpack_from ('B', bytearray(readbytes), 10)[0]
        Resource.SemaphoreCurrentCount = struct.unpack_from ('B', bytearray(readbytes), 11)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Resource

def ReadSeqMultiasicSyncError():
    "Indicates if any key parameters mismatch between the primary controler and any of the secondary controllers. This command must be addressed to any of the secondary controllers in a multi-controller system. Reading this command from primary will always retun all flags as 0. Any flag set below means the corresponding variable does not match between primary and the secondary that was queried. These flags get updated every frame. So user will see only the status updated in the preceding frame."
    global Summary
    Summary.Command = "Read Seq Multiasic Sync Error"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',245))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        SeqMultiasicSyncError.Seqnum = getbits(1, 2);
        SeqMultiasicSyncError.Lampbin = getbits(1, 3);
        SeqMultiasicSyncError.Syslook = getbits(1, 4);
        SeqMultiasicSyncError.Srcdef = getbits(1, 5);
        SeqMultiasicSyncError.Freq = getbits(1, 6);
        SeqMultiasicSyncError.Ssiconfig = getbits(1, 7);
        SeqMultiasicSyncError.Seqset = getbits(1, 8);
        SeqMultiasicSyncError.Hdrsrcgrp = getbits(1, 9);
        SeqMultiasicSyncError.Sysgrp = getbits(1, 10);
        SeqMultiasicSyncError.Bnmlut = getbits(1, 11);
        SeqMultiasicSyncError.Cwperiod = getbits(1, 12);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SeqMultiasicSyncError

def ReadWarpDecimationFactors():
    ""
    global Summary
    Summary.Command = "Read Warp Decimation Factors"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',250))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(8, writebytes, ProtocolData)
        HorzScaleFactor = convertfixedtofloat(struct.unpack_from ('I', bytearray(readbytes), 0)[0], 65536)
        VertScaleFactor = convertfixedtofloat(struct.unpack_from ('I', bytearray(readbytes), 4)[0], 65536)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, HorzScaleFactor, VertScaleFactor

def ReadEepromFreeAreaOffset():
    "This function idicates the EEPROM address offset which corresponds to the start of free area."
    global Summary
    Summary.Command = "Read Eeprom Free Area Offset"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',255))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(2, writebytes, ProtocolData)
        FreeAreaOffset = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, FreeAreaOffset

def ReadFpgaVx1ReceiverStatus():
    "This command returns the FPGA Vx1 receiver status and should be checked after FPGA Vx1 receiver is enabled."
    global Summary
    Summary.Command = "Read Fpga Vx 1 Receiver Status"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',113))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(5, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        HotPlugDetectActiveLow = getbits(1, 0);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        packerinit(readdata)
        LockActiveLow = getbits(1, 0);
        IpStateObj = struct.unpack_from ('B', bytearray(readbytes), 2)[0]
        readdata = struct.unpack_from ('B', bytearray(readbytes), 3)[0]
        packerinit(readdata)
        ArstzCqActiveLow = getbits(1, 0);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 4)[0]
        packerinit(readdata)
        ArstzLsqActiveLow = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, HotPlugDetectActiveLow, LockActiveLow, FpgaVx1IpStateT(IpStateObj), ArstzCqActiveLow, ArstzLsqActiveLow

def WritePower():
    "This commands toggles current power mode from standby to active or from active to power down. The Standby state corresponds to Low Power Mode."
    global Summary
    Summary.Command = "Write Power"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',16))
        ProtocolData.OpcodeLength = 1;
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadPower():
    "Returns current system power state."
    global Summary
    Summary.Command = "Read Power"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',16))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        PowerStateObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, PowerstateEnum(PowerStateObj)

def WriteDisplay(Source):
    "Displays the specified source."
    global Summary
    Summary.Command = "Write Display"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',17))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Source.value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDisplay():
    "Returns the source which is currently being displayed."
    global Summary
    Summary.Command = "Read Display"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',17))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        SourceObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, CmdProjectionModes(SourceObj)

def WriteSystemLook(System):
    "This command sets the current system look. System looks shall be designed and configured via DLP Composer tool. System look determines the current group of sequences and color points to be loaded. This command also initiates the source definition change that corresponds to new look index."
    global Summary
    Summary.Command = "Write System Look"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',19))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',System)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadSystemLook():
    "This command gets the current system look."
    global Summary
    Summary.Command = "Read System Look"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',19))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(2, writebytes, ProtocolData)
        System = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, System

def WriteTpgBorderEnable(Enable):
    "Draws a border around the test pattern of 1 pixel wide and color same as that of foreground color of the pattern.<BR> **Note** : 1. To be used only when the Display is set as Test Pattern. <BR> 2. Not supported for ASIC generated test patterns : Solid Field, Color Bars, Multi Color Horizontal Ramp, Fixed Step Horizontal Ramp, Diamond Diagonal Lines <BR> 3. Border color is same as foreground color of the pattern which is mapped to following parameter for each pattern : <BR> Checkerboard : Top Left checker color <BR> Horizontal Ramp : Ramp Color <BR> Vertical Ramp: Ramp Color <BR> Horizontal Lines : Line Color <BR> Vertical Lines : Line Color <BR> Grid Square : Line Color <BR> Grid diagonal : Line Color <BR> Cross : Line Color <BR>"
    global Summary
    Summary.Command = "Write Tpg Border Enable"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',21))
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

def ReadTpgBorderEnable():
    "Draws a border around the test pattern of 1 pixel wide and color same as that of foreground color of the pattern.<BR> **Note** : 1. To be used only when the Display is set as Test Pattern. <BR> 2. Not supported for ASIC generated test patterns : Solid Field, Color Bars, Multi Color Horizontal Ramp, Fixed Step Horizontal Ramp, Diamond Diagonal Lines <BR> 3. Border color is same as foreground color of the pattern which is mapped to following parameter for each pattern : <BR> Checkerboard : Top Left checker color <BR> Horizontal Ramp : Ramp Color <BR> Vertical Ramp: Ramp Color <BR> Horizontal Lines : Line Color <BR> Vertical Lines : Line Color <BR> Grid Square : Line Color <BR> Grid diagonal : Line Color <BR> Cross : Line Color <BR>"
    global Summary
    Summary.Command = "Read Tpg Border Enable"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',21))
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

def WriteTpgFrameRate(FrameRate):
    "Sets frame rate in Hz for current test pattern."
    global Summary
    Summary.Command = "Write Tpg Frame Rate"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',23))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',FrameRate)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadTpgFrameRate():
    "Returns frame rate in Hz for current test pattern."
    global Summary
    Summary.Command = "Read Tpg Frame Rate"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',23))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        FrameRate = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, FrameRate

def WriteSfgColor(Red,  Green,  Blue):
    "Configures the solid color to be displayed when display is set to solid field generator (SFG). This command only sets the SFG color and does NOT display it. In order to display the SFG, Display needs to be set with SFG as source(Use [[#cat-general_operation/display_write]] command)."
    global Summary
    Summary.Command = "Write Sfg Color"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',24))
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

def ReadSfgColor():
    "Returns the solid color which is programmed to be displayed when display is set to SFG."
    global Summary
    Summary.Command = "Read Sfg Color"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',24))
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

def WriteCurtainColor(Color):
    "Command to set the color to be  used in curtain mode. Use [[#cat-general_operation/display_write]] command to switch to curtain mode."
    global Summary
    Summary.Command = "Write Curtain Color"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',26))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Color.value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadCurtainColor():
    "Command that returns the color used in curtain mode."
    global Summary
    Summary.Command = "Read Curtain Color"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',26))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        ColorObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DispBackgroundColorT(ColorObj)

def WriteSplashLoadImage(Index):
    "Sets the index of the splash image to be loaded and displayed. If already in Splash mode the requested splash image is displayed."
    global Summary
    Summary.Command = "Write Splash Load Image"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',27))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Index)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadSplashLoadImage():
    "Gets the index of the splash image to be loaded and displayed."
    global Summary
    Summary.Command = "Read Splash Load Image"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',27))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        Index = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Index

def WriteEnableImageFlip(VertFlip,  HorzFlip):
    "Flips the data output to the display vertically or horizontally. This feature is provided to support ceiling mount and rear projection use cases.."
    global Summary
    Summary.Command = "Write Enable Image Flip"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',28))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(VertFlip), 1, 0)
        value = setbits(int(HorzFlip), 1, 1)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadEnableImageFlip():
    "Returns whether image flipping is enabled or not."
    global Summary
    Summary.Command = "Read Enable Image Flip"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',28))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        VertFlip = getbits(1, 0);
        HorzFlip = getbits(1, 1);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, VertFlip, HorzFlip

def WriteEnableFreeze(Freeze):
    "It enables or disables display freeze which freezes the current frame being displayed on the screen. Caution : Set Curtain or any operation that requires curtain will override Freeze and frozen image on the wall will be lost. The following operations require curtain (and will override Freeze): <BR> Source Type Switch (Standard - XPR - 3D) <BR> Source Type Switch (interlaced - non-interlaced) <BR> Switch to Splash Display <BR> Splash Capture <BR> Low Latency Mode Switch <BR> Source Relocking <BR> Switch to Stand-By/Low-Power mode"
    global Summary
    Summary.Command = "Write Enable Freeze"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',29))
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

def ReadEnableFreeze():
    "Returns whether the current display is frozen or not."
    global Summary
    Summary.Command = "Read Enable Freeze"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',29))
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

def WriteKeystoneAngles(Pitch,  Yaw):
    "Configures the Keystone correction when the pitch, yaw, throw ratio and vertical offset of corrected image are known. Keystone correction is used to remove the distortion caused when the projector is not orthogonal to the projection surface (screen). Keystone feature will be automatically enabled when this command is executed."
    global Summary
    Summary.Command = "Write Keystone Angles"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',30))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(Pitch,256)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(Yaw,256)))))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadKeystoneAngles():
    "Returns the keystone configuration parameters currently set."
    global Summary
    Summary.Command = "Read Keystone Angles"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',30))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        Pitch = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 0)[0], 256)
        Yaw = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 2)[0], 256)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Pitch, Yaw

def WriteKeystoneConfigOverride(ThrowRatio,  VerticalOffset):
    ""
    global Summary
    Summary.Command = "Write Keystone Config Override"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',31))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ThrowRatio,256)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(VerticalOffset,256)))))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadKeystoneConfigOverride():
    ""
    global Summary
    Summary.Command = "Read Keystone Config Override"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',31))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        ThrowRatio = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 0)[0], 256)
        VerticalOffset = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 2)[0], 256)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ThrowRatio, VerticalOffset

def ReadFrameRateParms():
    "Returns current Input Frame Rate, Output Frame rate anf FRC mode"
    global Summary
    Summary.Command = "Read Frame Rate Parms"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',35))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(9, writebytes, ProtocolData)
        InputFrameRate = convertfixedtofloat(struct.unpack_from ('I', bytearray(readbytes), 0)[0], 65536)
        OutputFrameRate = convertfixedtofloat(struct.unpack_from ('I', bytearray(readbytes), 4)[0], 65536)
        FrcModeObj = struct.unpack_from ('B', bytearray(readbytes), 8)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, InputFrameRate, OutputFrameRate, FrameFrcModeT(FrcModeObj)

def WriteKeystoneCorners(KeystoneCorners):
    "Configures the 2D Keystone correction when the corners of the corrected image are known. Keystone correction is used to remove the distortion caused when the projector is not orthogonal to the projection surface (screen). For the effects to take place, the Keystone feature has to be enabled."
    global Summary
    Summary.Command = "Write Keystone Corners"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',36))
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
    "Returns the keystone configuration parameters currently set. This command should be used when the keystone correction has been configured using the four corners of the corrected image. The keystone correction is observed only if the keystone feature is enabled, even if the parameters are configured correctly."
    global Summary
    Summary.Command = "Read Keystone Corners"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',36))
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

def WriteVx1SourceConfig(Vx1SourceConfig):
    "Sets the FPGA Vx1 RX Config"
    global Summary
    Summary.Command = "Write Vx 1 Source Config"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',39))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(Vx1SourceConfig.FrameRate,256)))))
        writebytes.extend(list(struct.pack('H',Vx1SourceConfig.ActiveResolutionWidth)))
        writebytes.extend(list(struct.pack('H',Vx1SourceConfig.ActiveResolutionHeight)))
        writebytes.extend(list(struct.pack('B',Vx1SourceConfig.FSyncEdgePol)))
        writebytes.extend(list(struct.pack('B',Vx1SourceConfig.VsyncEdgePol)))
        writebytes.extend(list(struct.pack('B',Vx1SourceConfig.HsyncEdgePol)))
        writebytes.extend(list(struct.pack('B',Vx1SourceConfig.DataEnEdgePol)))
        writebytes.extend(list(struct.pack('B',Vx1SourceConfig.PixelFormat.value)))
        writebytes.extend(list(struct.pack('B',Vx1SourceConfig.DataMapMode.value)))
        writebytes.extend(list(struct.pack('H',Vx1SourceConfig.ColorSpaceConvCoeffsIndex0)))
        writebytes.extend(list(struct.pack('H',Vx1SourceConfig.ColorSpaceConvCoeffsIndex1)))
        writebytes.extend(list(struct.pack('H',Vx1SourceConfig.ColorSpaceConvCoeffsIndex2)))
        writebytes.extend(list(struct.pack('H',Vx1SourceConfig.ColorSpaceConvCoeffsIndex3)))
        writebytes.extend(list(struct.pack('H',Vx1SourceConfig.ColorSpaceConvCoeffsIndex4)))
        writebytes.extend(list(struct.pack('H',Vx1SourceConfig.ColorSpaceConvCoeffsIndex5)))
        writebytes.extend(list(struct.pack('H',Vx1SourceConfig.ColorSpaceConvCoeffsIndex6)))
        writebytes.extend(list(struct.pack('H',Vx1SourceConfig.ColorSpaceConvCoeffsIndex7)))
        writebytes.extend(list(struct.pack('H',Vx1SourceConfig.ColorSpaceConvCoeffsIndex8)))
        packerinit()
        value = setbits(int(Vx1SourceConfig.IsOffsetBinary), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        writebytes.extend(list(struct.pack('H',Vx1SourceConfig.ChannelAOffset)))
        writebytes.extend(list(struct.pack('H',Vx1SourceConfig.ChannelBOffset)))
        writebytes.extend(list(struct.pack('H',Vx1SourceConfig.ChannelCOffset)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadVx1SourceConfig():
    "Sets the FPGA Vx1 RX Config"
    global Summary
    Summary.Command = "Read Vx 1 Source Config"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',39))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(37, writebytes, ProtocolData)
        Vx1SourceConfig.FrameRate = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 0)[0], 256)
        Vx1SourceConfig.ActiveResolutionWidth = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        Vx1SourceConfig.ActiveResolutionHeight = struct.unpack_from ('H', bytearray(readbytes), 4)[0]
        Vx1SourceConfig.FSyncEdgePol = struct.unpack_from ('B', bytearray(readbytes), 6)[0]
        Vx1SourceConfig.VsyncEdgePol = struct.unpack_from ('B', bytearray(readbytes), 7)[0]
        Vx1SourceConfig.HsyncEdgePol = struct.unpack_from ('B', bytearray(readbytes), 8)[0]
        Vx1SourceConfig.DataEnEdgePol = struct.unpack_from ('B', bytearray(readbytes), 9)[0]
        Vx1SourceConfig.PixelFormat = struct.unpack_from ('B', bytearray(readbytes), 10)[0]
        Vx1SourceConfig.DataMapMode = struct.unpack_from ('B', bytearray(readbytes), 11)[0]
        Vx1SourceConfig.ColorSpaceConvCoeffsIndex0 = struct.unpack_from ('H', bytearray(readbytes), 12)[0]
        Vx1SourceConfig.ColorSpaceConvCoeffsIndex1 = struct.unpack_from ('H', bytearray(readbytes), 14)[0]
        Vx1SourceConfig.ColorSpaceConvCoeffsIndex2 = struct.unpack_from ('H', bytearray(readbytes), 16)[0]
        Vx1SourceConfig.ColorSpaceConvCoeffsIndex3 = struct.unpack_from ('H', bytearray(readbytes), 18)[0]
        Vx1SourceConfig.ColorSpaceConvCoeffsIndex4 = struct.unpack_from ('H', bytearray(readbytes), 20)[0]
        Vx1SourceConfig.ColorSpaceConvCoeffsIndex5 = struct.unpack_from ('H', bytearray(readbytes), 22)[0]
        Vx1SourceConfig.ColorSpaceConvCoeffsIndex6 = struct.unpack_from ('H', bytearray(readbytes), 24)[0]
        Vx1SourceConfig.ColorSpaceConvCoeffsIndex7 = struct.unpack_from ('H', bytearray(readbytes), 26)[0]
        Vx1SourceConfig.ColorSpaceConvCoeffsIndex8 = struct.unpack_from ('H', bytearray(readbytes), 28)[0]
        readdata = struct.unpack_from ('B', bytearray(readbytes), 30)[0]
        packerinit(readdata)
        Vx1SourceConfig.IsOffsetBinary = getbits(1, 0);
        Vx1SourceConfig.ChannelAOffset = struct.unpack_from ('H', bytearray(readbytes), 31)[0]
        Vx1SourceConfig.ChannelBOffset = struct.unpack_from ('H', bytearray(readbytes), 33)[0]
        Vx1SourceConfig.ChannelCOffset = struct.unpack_from ('H', bytearray(readbytes), 35)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Vx1SourceConfig

def WriteInvalidWarpMapError(DecimationFactorLessThanHalf,  ProjectionGeometryViolated,  WarpHardwareLimitation,  WarpInterpolationOutOfRangeDueToInsufficientBlankings):
    "Invalid warp map error"
    global Summary
    Summary.Command = "Write Invalid Warp Map Error"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',40))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(DecimationFactorLessThanHalf), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(int(ProjectionGeometryViolated), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(int(WarpHardwareLimitation), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(int(WarpInterpolationOutOfRangeDueToInsufficientBlankings), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadInvalidWarpMapError():
    "Invalid warp map error"
    global Summary
    Summary.Command = "Read Invalid Warp Map Error"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',40))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        DecimationFactorLessThanHalf = getbits(1, 0);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        packerinit(readdata)
        ProjectionGeometryViolated = getbits(1, 0);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 2)[0]
        packerinit(readdata)
        WarpHardwareLimitation = getbits(1, 0);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 3)[0]
        packerinit(readdata)
        WarpInterpolationOutOfRangeDueToInsufficientBlankings = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DecimationFactorLessThanHalf, ProjectionGeometryViolated, WarpHardwareLimitation, WarpInterpolationOutOfRangeDueToInsufficientBlankings

def WriteIlluminationEnable(Enable):
    "Enables or Disables the illumination system. Additionally, For Systems with color wheel: - Illumination will be turned on only if the system has indicated that the color wheel is spinning This interlock is necessary to avoid burning the coatings off the glass For Lamp Based Systems with Lamp Strike Reset Enabled: - Only Illumination Disable is supported during run time To Enable illumination again, system should be powered down and then powered up again This is necessary to protect DMD from EMI generated during lamp strike event"
    global Summary
    Summary.Command = "Write Illumination Enable"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',128))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Enable)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadIlluminationEnable():
    "Gets the enable state of lamp/SSI illumination."
    global Summary
    Summary.Command = "Read Illumination Enable"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',128))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        Enable = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Enable

def WriteSsiDriveLevels(PwmGroup,  SsiDriveLevels):
    "Sets the drive current of all the channels of the SSI based illumination. Appicable for DLPA3000 or PWM based LED drivers Command should not be used if Dynamic Black or White Point Correction is enabled"
    global Summary
    Summary.Command = "Write Ssi Drive Levels"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',130))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',PwmGroup)))
        writebytes.extend(list(struct.pack('H',SsiDriveLevels.DriveLevelRed)))
        writebytes.extend(list(struct.pack('H',SsiDriveLevels.DriveLevelGreen)))
        writebytes.extend(list(struct.pack('H',SsiDriveLevels.DriveLevelBlue)))
        writebytes.extend(list(struct.pack('H',SsiDriveLevels.DriveLevelC1)))
        writebytes.extend(list(struct.pack('H',SsiDriveLevels.DriveLevelC2)))
        writebytes.extend(list(struct.pack('H',SsiDriveLevels.DriveLevelSense)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadSsiDriveLevels(PwmGroup):
    "Gets the drive current of all the channels of the SSI based illumination.  Appicable for DLPA3000 or PWM based LED drivers"
    global Summary
    Summary.Command = "Read Ssi Drive Levels"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',130))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',PwmGroup)))
        readbytes = _readcommand(12, writebytes, ProtocolData)
        SsiDriveLevels.DriveLevelRed = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        SsiDriveLevels.DriveLevelGreen = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        SsiDriveLevels.DriveLevelBlue = struct.unpack_from ('H', bytearray(readbytes), 4)[0]
        SsiDriveLevels.DriveLevelC1 = struct.unpack_from ('H', bytearray(readbytes), 6)[0]
        SsiDriveLevels.DriveLevelC2 = struct.unpack_from ('H', bytearray(readbytes), 8)[0]
        SsiDriveLevels.DriveLevelSense = struct.unpack_from ('H', bytearray(readbytes), 10)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SsiDriveLevels

def WriteImageAlgorithmEnable(GammaCorrectionEnableBit,  ColorCoordinateAdjustmentEnableBit,  BrilliantColorEnableBit,  DynamicBlackEnableBit,  HdrEnableBit):
    "Sets enable flag for all Image Algorithms.<BR> 0 = Disable <BR> 1 = Enable  <BR> **Gamma Correction** : <BR> This function enables/disables the Gamma Correction function which implements the removal of gamma transfer function applied at the source, via table lookup process called de-gamma. When enabled, perform de-gamma translation of the 10-bit RGB input to the common 12-bit floating point (S0M8E4) RGB output. When disabled, the full 10 bits of each data input to the Gamma Correction function are zero padded and MSB-aligned to 12-bits and passed through unmodified.<BR> **Color Coordinate Adjustment** : <BR> This function enables/disables the Spatially Adaptive Seven Primaries Color Correction Function Enable. When Disable forces 3x3 CSC (Color Space Conversion) with identity. <BR> **Brilliant Color** : <BR> This function enables/disables the BrilliantColor technology, Brilliant Color uses up to five colors, instead of just the three primary colors, red, green and blue, to improve color accuracy and brightens of secondary colors. This results in a new level of color performance that increases the brightness of the colors. <BR> **Dynamic Black** : <BR> Dynamic Black (DB) is an algorithm that reduces the amount of light reaching the projection path by means of LED output power through current control and compensates for reduced light by gaining up the RGB signals. <BR> **HDR** : <BR> High Dynamic Range (HDR) is an algorithm that maps wider brightness and color range of HDR source to the projector display range. HDR is affected by several factors such as illimuniation characterstics, duty cycle distribution and current running sequence. A valid HDR source should be set by HDR_SetHdrSourceConfiguration() before enabling HDR processing.<BR> Note: **Chroma Transient Improvement** is applicable to Analog SDTV sources only. DLPC654x controller doesn't support Analog sources. Even if enabled on DLPC65x controller, there is no changes in the displayed image when enabled."
    global Summary
    Summary.Command = "Write Image Algorithm Enable"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',64))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(GammaCorrectionEnableBit), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(int(ColorCoordinateAdjustmentEnableBit), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(int(BrilliantColorEnableBit), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(int(DynamicBlackEnableBit), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(int(HdrEnableBit), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadImageAlgorithmEnable():
    "Returns enable flag for all Image Algorithms <BR> '0' - Disabled or algorithm feature not available. <BR> '1' - Enabled"
    global Summary
    Summary.Command = "Read Image Algorithm Enable"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',64))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(5, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        GammaCorrectionEnableBit = getbits(1, 0);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        packerinit(readdata)
        ColorCoordinateAdjustmentEnableBit = getbits(1, 0);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 2)[0]
        packerinit(readdata)
        BrilliantColorEnableBit = getbits(1, 0);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 3)[0]
        packerinit(readdata)
        DynamicBlackEnableBit = getbits(1, 0);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 4)[0]
        packerinit(readdata)
        HdrEnableBit = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, GammaCorrectionEnableBit, ColorCoordinateAdjustmentEnableBit, BrilliantColorEnableBit, DynamicBlackEnableBit, HdrEnableBit

def WriteImageBrightness(BrightnessAdjustment):
    "The brightness control provides the ability to add or subtract a fixed bias from each of the input channels.  This may be used to remove any inherent offsets and/or adjust the brightness level. The brightness coefficients are signed, 11-bit (s8.2), 2's complement values between -256 and 255.75, inclusive.  Brightness Control is used after color space conversion."
    global Summary
    Summary.Command = "Write Image Brightness"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',65))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(BrightnessAdjustment,4)))))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadImageBrightness():
    "Returns Image Brightness Level."
    global Summary
    Summary.Command = "Read Image Brightness"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',65))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(2, writebytes, ProtocolData)
        BrightnessAdjustment = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 0)[0], 4)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, BrightnessAdjustment

def WriteImageContrast(Contrast):
    "Sets Image Contrast in percentage. Each contrast byte controls the gain applied to the input image data for a given data channel.  The contrast gain has a range from 0 to 200 (0% to 200%) with 100 (100%) being nominal (default)."
    global Summary
    Summary.Command = "Write Image Contrast"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',66))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',Contrast)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadImageContrast():
    "Returns Image Contrast in percentage."
    global Summary
    Summary.Command = "Read Image Contrast"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',66))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(2, writebytes, ProtocolData)
        Contrast = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Contrast

def WriteImageHueAndColorControl(HueAdjustmentAngle,  ColorControlGain):
    "Sets Image Hue Adjustment angle in degrees and Color Control Gain in percentage."
    global Summary
    Summary.Command = "Write Image Hue And Color Control"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',67))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('b',HueAdjustmentAngle)))
        writebytes.extend(list(struct.pack('H',ColorControlGain)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadImageHueAndColorControl():
    "Returns Image Hue Adjustment angle in degrees and Color Control Gain in percentage."
    global Summary
    Summary.Command = "Read Image Hue And Color Control"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',67))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(3, writebytes, ProtocolData)
        HueAdjustmentAngle = struct.unpack_from ('b', bytearray(readbytes), 0)[0]
        ColorControlGain = struct.unpack_from ('H', bytearray(readbytes), 1)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, HueAdjustmentAngle, ColorControlGain

def WriteImageSharpness(Sharpness):
    "Configures the sharpness filter.  A value of 0 is the least sharp (smoothest), while a value of 31 is the sharpest. This filter is in the back end of the data path, so both video and graphics are affected. TI recommends that the sharpness filters be disabled (sharpness=16) for graphics sources."
    global Summary
    Summary.Command = "Write Image Sharpness"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',68))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Sharpness)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadImageSharpness():
    "Returns the current sharpness value"
    global Summary
    Summary.Command = "Read Image Sharpness"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',68))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        Sharpness = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Sharpness

def WriteImageRgbOffset(Red,  Green,  Blue):
    "This command is used to add RGB offsets in 2's complement s9.0 format"
    global Summary
    Summary.Command = "Write Image Rgb Offset"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',69))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('h',Red)))
        writebytes.extend(list(struct.pack('h',Green)))
        writebytes.extend(list(struct.pack('h',Blue)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadImageRgbOffset():
    "Returns Red, Green and Blue channel offset settings in 2's complement s9.0 format."
    global Summary
    Summary.Command = "Read Image Rgb Offset"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',69))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(6, writebytes, ProtocolData)
        Red = struct.unpack_from ('h', bytearray(readbytes), 0)[0]
        Green = struct.unpack_from ('h', bytearray(readbytes), 2)[0]
        Blue = struct.unpack_from ('h', bytearray(readbytes), 4)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Red, Green, Blue

def WriteImageRgbGain(RedGain,  GreenGain,  BlueGain):
    "Adjusts individual R, G and B gains of the source image. Gain is specified as a percentage from 0% - 200%, with 100% being nominal (no gain change).  0% will zero out the channel. This function adjusts R, G and B gains by altering the Color Space Converter (CSC) coefficients. This function is only applicable to RGB sources."
    global Summary
    Summary.Command = "Write Image Rgb Gain"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',70))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',RedGain)))
        writebytes.extend(list(struct.pack('H',GreenGain)))
        writebytes.extend(list(struct.pack('H',BlueGain)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadImageRgbGain():
    "Returns gain setting for Red, Green and Blue color channels in percentage."
    global Summary
    Summary.Command = "Read Image Rgb Gain"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',70))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(6, writebytes, ProtocolData)
        RedGain = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        GreenGain = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        BlueGain = struct.unpack_from ('H', bytearray(readbytes), 4)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, RedGain, GreenGain, BlueGain

def WriteCscTable(Index):
    "Sets the Color Space Conversion Matrix with one of the CSC tables stored in flash."
    global Summary
    Summary.Command = "Write Csc Table"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',71))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Index.value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadCscTable():
    "Gets the index of the Color Space Conversion Matrix that is currently cofigured for use."
    global Summary
    Summary.Command = "Read Csc Table"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',71))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        IndexObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, FpgaSrcCscTablesT(IndexObj)

def WriteImageCcaCoordinates(ImageCcaCoordinates):
    "This Command allows independent adjustment of the primary, secondary and white coordinates. This call will override any CCA settings performed by prior calls."
    global Summary
    Summary.Command = "Write Image Cca Coordinates"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',72))
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
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.OrigCoordsC1X,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.OrigCoordsC1Y,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.OrigCoordsC1Lum,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.OrigCoordsC2X,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.OrigCoordsC2Y,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.OrigCoordsC2Lum,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.OrigCoordsDraAX,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.OrigCoordsDraAY,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.OrigCoordsDraALum,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.OrigCoordsDraBX,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.OrigCoordsDraBY,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.OrigCoordsDraBLum,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.OrigCoordsDraCX,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.OrigCoordsDraCY,32768)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImageCcaCoordinates.OrigCoordsDraCLum,32768)))))
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
    "Returns the current color coordinate configuration."
    global Summary
    Summary.Command = "Read Image Cca Coordinates"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',72))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(96, writebytes, ProtocolData)
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
        ImageCcaCoordinates.OrigCoordsC1X = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 24)[0], 32768)
        ImageCcaCoordinates.OrigCoordsC1Y = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 26)[0], 32768)
        ImageCcaCoordinates.OrigCoordsC1Lum = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 28)[0], 32768)
        ImageCcaCoordinates.OrigCoordsC2X = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 30)[0], 32768)
        ImageCcaCoordinates.OrigCoordsC2Y = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 32)[0], 32768)
        ImageCcaCoordinates.OrigCoordsC2Lum = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 34)[0], 32768)
        ImageCcaCoordinates.OrigCoordsDraAX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 36)[0], 32768)
        ImageCcaCoordinates.OrigCoordsDraAY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 38)[0], 32768)
        ImageCcaCoordinates.OrigCoordsDraALum = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 40)[0], 32768)
        ImageCcaCoordinates.OrigCoordsDraBX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 42)[0], 32768)
        ImageCcaCoordinates.OrigCoordsDraBY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 44)[0], 32768)
        ImageCcaCoordinates.OrigCoordsDraBLum = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 46)[0], 32768)
        ImageCcaCoordinates.OrigCoordsDraCX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 48)[0], 32768)
        ImageCcaCoordinates.OrigCoordsDraCY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 50)[0], 32768)
        ImageCcaCoordinates.OrigCoordsDraCLum = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 52)[0], 32768)
        ImageCcaCoordinates.TargetCoordsRedX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 54)[0], 32768)
        ImageCcaCoordinates.TargetCoordsRedY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 56)[0], 32768)
        ImageCcaCoordinates.TargetCoordsRedGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 58)[0], 32768)
        ImageCcaCoordinates.TargetCoordsGreenX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 60)[0], 32768)
        ImageCcaCoordinates.TargetCoordsGreenY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 62)[0], 32768)
        ImageCcaCoordinates.TargetCoordsGreenGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 64)[0], 32768)
        ImageCcaCoordinates.TargetCoordsBlueX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 66)[0], 32768)
        ImageCcaCoordinates.TargetCoordsBlueY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 68)[0], 32768)
        ImageCcaCoordinates.TargetCoordsBlueGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 70)[0], 32768)
        ImageCcaCoordinates.TargetCoordsCyanX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 72)[0], 32768)
        ImageCcaCoordinates.TargetCoordsCyanY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 74)[0], 32768)
        ImageCcaCoordinates.TargetCoordsCyanGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 76)[0], 32768)
        ImageCcaCoordinates.TargetCoordsMagentaX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 78)[0], 32768)
        ImageCcaCoordinates.TargetCoordsMagentaY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 80)[0], 32768)
        ImageCcaCoordinates.TargetCoordsMagentaGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 82)[0], 32768)
        ImageCcaCoordinates.TargetCoordsYellowX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 84)[0], 32768)
        ImageCcaCoordinates.TargetCoordsYellowY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 86)[0], 32768)
        ImageCcaCoordinates.TargetCoordsYellowGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 88)[0], 32768)
        ImageCcaCoordinates.TargetCoordsWhiteX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 90)[0], 32768)
        ImageCcaCoordinates.TargetCoordsWhiteY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 92)[0], 32768)
        ImageCcaCoordinates.TargetCoordsWhiteGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 94)[0], 32768)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ImageCcaCoordinates

def WriteImageHsg(ImageHsg):
    "This command applies the given hue, saturation and gain values for all colors. It does not affect colors having a gain of zero. Note: This call will override any CCA settings performed by prior calls."
    global Summary
    Summary.Command = "Write Image Hsg"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',73))
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
    "This command returns the currently applied hue, saturation and gain values for all the colors. If gain for a color is zero then the HSG is not applied on the color."
    global Summary
    Summary.Command = "Read Image Hsg"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',73))
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

def WriteImageGammaLut(GammaLutNumber):
    "This command loads the specified gamma look-up table into memory from flash. A single load is accomplished by loading data for red, green and blue look-up tables. Use DLP Composer(tm) to create new gamma tables or modify existing gamma tables."
    global Summary
    Summary.Command = "Write Image Gamma Lut"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',74))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',GammaLutNumber)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadImageGammaLut():
    "Returns the table number of the gamma look-up table currently loaded in memory."
    global Summary
    Summary.Command = "Read Image Gamma Lut"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',74))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        GammaLutNumber = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, GammaLutNumber

def WriteImageGammaCurveShift(RedShift,  GreenShift,  BlueShift,  AllColorShift):
    "Used to specify the shifts in the gamma curve of Red, Green and Blue. A left shift is a positive offset and a right shift is a negative offset. The effective brightness is increased with a left shift and decreased with a right shift."
    global Summary
    Summary.Command = "Write Image Gamma Curve Shift"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',75))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('b',RedShift)))
        writebytes.extend(list(struct.pack('b',GreenShift)))
        writebytes.extend(list(struct.pack('b',BlueShift)))
        writebytes.extend(list(struct.pack('b',AllColorShift)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadImageGammaCurveShift():
    "Returns Image Gamma Shift for red, green and blue as well as shift to be broadcasted to all colors"
    global Summary
    Summary.Command = "Read Image Gamma Curve Shift"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',75))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        RedShift = struct.unpack_from ('b', bytearray(readbytes), 0)[0]
        GreenShift = struct.unpack_from ('b', bytearray(readbytes), 1)[0]
        BlueShift = struct.unpack_from ('b', bytearray(readbytes), 2)[0]
        AllColorShift = struct.unpack_from ('b', bytearray(readbytes), 3)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, RedShift, GreenShift, BlueShift, AllColorShift

def WriteImgWhitePeakingFactor(WhitePeakingVal):
    ""
    global Summary
    Summary.Command = "Write Img White Peaking Factor"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',76))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',WhitePeakingVal)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadImgWhitePeakingFactor():
    ""
    global Summary
    Summary.Command = "Read Img White Peaking Factor"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',76))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        WhitePeakingVal = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, WhitePeakingVal

def WriteXprFilterStrengthCommand(Strength):
    ""
    global Summary
    Summary.Command = "Write Xpr Filter Strength Command"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',77))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Strength)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadXprFilterStrengthCommand():
    ""
    global Summary
    Summary.Command = "Read Xpr Filter Strength Command"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',77))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        Strength = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Strength

def WriteHdrSourceConfiguration(HdrSourceConfiguration):
    "HDR maps wider brightness and color range of HDR sources to projector brightness and color range. The mapping requires multiple source groups and system groups define the HDR source and projection device properties respectively. This command sets the source properties and based on this information nearest source group is selected for mapping."
    global Summary
    Summary.Command = "Write Hdr Source Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',78))
        ProtocolData.OpcodeLength = 1;
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
    "Includes the metadata information."
    global Summary
    Summary.Command = "Read Hdr Source Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',78))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(25, writebytes, ProtocolData)
        HdrSourceConfiguration.TransferFunction = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        HdrSourceConfiguration.MasterDisplayBlackLevel = convertfixedtofloat(struct.unpack_from ('I', bytearray(readbytes), 1)[0], 65536)
        HdrSourceConfiguration.MasterDisplayWhiteLevel = convertfixedtofloat(struct.unpack_from ('I', bytearray(readbytes), 5)[0], 65536)
        HdrSourceConfiguration.MasterDisplayColorGamutRedX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 9)[0], 32768)
        HdrSourceConfiguration.MasterDisplayColorGamutRedY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 11)[0], 32768)
        HdrSourceConfiguration.MasterDisplayColorGamutGreenX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 13)[0], 32768)
        HdrSourceConfiguration.MasterDisplayColorGamutGreenY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 15)[0], 32768)
        HdrSourceConfiguration.MasterDisplayColorGamutBlueX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 17)[0], 32768)
        HdrSourceConfiguration.MasterDisplayColorGamutBlueY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 19)[0], 32768)
        HdrSourceConfiguration.MasterDisplayColorGamutWhiteX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 21)[0], 32768)
        HdrSourceConfiguration.MasterDisplayColorGamutWhiteY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 23)[0], 32768)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, HdrSourceConfiguration

def WriteHdrStrengthSetting(HdrStrength):
    "Sets HDR strength which adjusts the electro-optical transfer function that is applied on the input HDR video signal. HDR strength can vary with the ambient brightness level.HDR strength is not applicable for HLG transfer function set by HDR source configuration."
    global Summary
    Summary.Command = "Write Hdr Strength Setting"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',79))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',HdrStrength)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadHdrStrengthSetting():
    ""
    global Summary
    Summary.Command = "Read Hdr Strength Setting"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',79))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        HdrStrength = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, HdrStrength

def WriteSystemBrightnessRangeSetting(MinBrightness,  MaxBrightness):
    "Sets the system brightness range in nits. These are used in determining the appropriate EOTF and OOTF function to be applied on the HDR source. This need to set only for HDR functionality."
    global Summary
    Summary.Command = "Write System Brightness Range Setting"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',80))
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
    ""
    global Summary
    Summary.Command = "Read System Brightness Range Setting"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',80))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(8, writebytes, ProtocolData)
        MinBrightness = convertfixedtofloat(struct.unpack_from ('I', bytearray(readbytes), 0)[0], 65536)
        MaxBrightness = convertfixedtofloat(struct.unpack_from ('I', bytearray(readbytes), 4)[0], 65536)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, MinBrightness, MaxBrightness

def WriteImageColorProfile(ColorProfile):
    "Sets pre-configured Gamma table index and HSG settings as stored in the flash image."
    global Summary
    Summary.Command = "Write Image Color Profile"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',81))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',ColorProfile)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteImagePointHsg(Point,  ImagePointHsg):
    "This command applies the given hue, saturation and gain values for all colors, for a specified sample point. Point is a number 0-15 corresponding to one of the the 5 x 3 PCC sample points in raster scan order. It does not affect colors having a gain of zero. Note: This call will override any CCA settings performed by prior calls."
    global Summary
    Summary.Command = "Write Image Point Hsg"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',82))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Point.value)))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImagePointHsg.HsgRedGain,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImagePointHsg.HsgRedSaturation,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImagePointHsg.HsgRedHue,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImagePointHsg.HsgGreenGain,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImagePointHsg.HsgGreenSaturation,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImagePointHsg.HsgGreenHue,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImagePointHsg.HsgBlueGain,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImagePointHsg.HsgBlueSaturation,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImagePointHsg.HsgBlueHue,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImagePointHsg.HsgCyanGain,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImagePointHsg.HsgCyanSaturation,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImagePointHsg.HsgCyanHue,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImagePointHsg.HsgMagentaGain,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImagePointHsg.HsgMagentaSaturation,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImagePointHsg.HsgMagentaHue,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImagePointHsg.HsgYellowGain,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImagePointHsg.HsgYellowSaturation,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImagePointHsg.HsgYellowHue,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImagePointHsg.HsgWhiteRedGain,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImagePointHsg.HsgWhiteGreenGain,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(ImagePointHsg.HsgWhiteBlueGain,16384)))))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadImagePointHsg(Point):
    "This command returns the currently applied hue, saturation and gain values for all the colors, for a specified sample point. Point is a number 0-15 corresponding to one of the the 5 x 3 PCC sample points in raster scan order. If gain for a color is zero then the HSG is not applied on the color."
    global Summary
    Summary.Command = "Read Image Point Hsg"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',82))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Point.value)))
        readbytes = _readcommand(42, writebytes, ProtocolData)
        ImagePointHsg.HsgRedGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 0)[0], 16384)
        ImagePointHsg.HsgRedSaturation = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 2)[0], 16384)
        ImagePointHsg.HsgRedHue = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 4)[0], 16384)
        ImagePointHsg.HsgGreenGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 6)[0], 16384)
        ImagePointHsg.HsgGreenSaturation = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 8)[0], 16384)
        ImagePointHsg.HsgGreenHue = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 10)[0], 16384)
        ImagePointHsg.HsgBlueGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 12)[0], 16384)
        ImagePointHsg.HsgBlueSaturation = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 14)[0], 16384)
        ImagePointHsg.HsgBlueHue = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 16)[0], 16384)
        ImagePointHsg.HsgCyanGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 18)[0], 16384)
        ImagePointHsg.HsgCyanSaturation = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 20)[0], 16384)
        ImagePointHsg.HsgCyanHue = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 22)[0], 16384)
        ImagePointHsg.HsgMagentaGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 24)[0], 16384)
        ImagePointHsg.HsgMagentaSaturation = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 26)[0], 16384)
        ImagePointHsg.HsgMagentaHue = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 28)[0], 16384)
        ImagePointHsg.HsgYellowGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 30)[0], 16384)
        ImagePointHsg.HsgYellowSaturation = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 32)[0], 16384)
        ImagePointHsg.HsgYellowHue = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 34)[0], 16384)
        ImagePointHsg.HsgWhiteRedGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 36)[0], 16384)
        ImagePointHsg.HsgWhiteGreenGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 38)[0], 16384)
        ImagePointHsg.HsgWhiteBlueGain = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 40)[0], 16384)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ImagePointHsg

def WritePccCoefficientsDirect(Point,  PccCoefficientsDirect):
    "This command applies raw PCC Coefficients for all colors through direct access, for a specified sample point. Point is a number 0-15 corresponding to one of the the 5 x 3 PCC sample points in raster scan order. Note: This call will override any CCA settings performed by prior calls."
    global Summary
    Summary.Command = "Write Pcc Coefficients Direct"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',84))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Point.value)))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(PccCoefficientsDirect.PccRedR,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(PccCoefficientsDirect.PccRedG,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(PccCoefficientsDirect.PccRedB,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(PccCoefficientsDirect.PccGreenR,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(PccCoefficientsDirect.PccGreenG,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(PccCoefficientsDirect.PccGreenB,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(PccCoefficientsDirect.PccBlueR,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(PccCoefficientsDirect.PccBlueG,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(PccCoefficientsDirect.PccBlueB,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(PccCoefficientsDirect.PccCyanR,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(PccCoefficientsDirect.PccCyanG,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(PccCoefficientsDirect.PccCyanB,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(PccCoefficientsDirect.PccMagentaR,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(PccCoefficientsDirect.PccMagentaG,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(PccCoefficientsDirect.PccMagentaB,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(PccCoefficientsDirect.PccYellowR,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(PccCoefficientsDirect.PccYellowG,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(PccCoefficientsDirect.PccYellowB,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(PccCoefficientsDirect.PccWhiteR,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(PccCoefficientsDirect.PccWhiteG,16384)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(PccCoefficientsDirect.PccWhiteB,16384)))))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadPccCoefficientsDirect(Point):
    "This command gets raw PCC Coefficients for all colors through direct access, for a specified sample point. Point is a number 0-15 corresponding to one of the the 5 x 3 PCC sample points in raster scan order. Note: This call will override any CCA settings performed by prior calls."
    global Summary
    Summary.Command = "Read Pcc Coefficients Direct"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',84))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Point.value)))
        readbytes = _readcommand(42, writebytes, ProtocolData)
        PccCoefficientsDirect.PccRedR = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 0)[0], 16384)
        PccCoefficientsDirect.PccRedG = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 2)[0], 16384)
        PccCoefficientsDirect.PccRedB = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 4)[0], 16384)
        PccCoefficientsDirect.PccGreenR = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 6)[0], 16384)
        PccCoefficientsDirect.PccGreenG = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 8)[0], 16384)
        PccCoefficientsDirect.PccGreenB = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 10)[0], 16384)
        PccCoefficientsDirect.PccBlueR = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 12)[0], 16384)
        PccCoefficientsDirect.PccBlueG = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 14)[0], 16384)
        PccCoefficientsDirect.PccBlueB = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 16)[0], 16384)
        PccCoefficientsDirect.PccCyanR = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 18)[0], 16384)
        PccCoefficientsDirect.PccCyanG = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 20)[0], 16384)
        PccCoefficientsDirect.PccCyanB = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 22)[0], 16384)
        PccCoefficientsDirect.PccMagentaR = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 24)[0], 16384)
        PccCoefficientsDirect.PccMagentaG = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 26)[0], 16384)
        PccCoefficientsDirect.PccMagentaB = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 28)[0], 16384)
        PccCoefficientsDirect.PccYellowR = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 30)[0], 16384)
        PccCoefficientsDirect.PccYellowG = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 32)[0], 16384)
        PccCoefficientsDirect.PccYellowB = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 34)[0], 16384)
        PccCoefficientsDirect.PccWhiteR = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 36)[0], 16384)
        PccCoefficientsDirect.PccWhiteG = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 38)[0], 16384)
        PccCoefficientsDirect.PccWhiteB = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 40)[0], 16384)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, PccCoefficientsDirect

def WriteGpioPinConfig(PinNumber,  Output,  LogicVal,  OpenDrain):
    "Programs the direction, logic value and open drain characteristics of a single general purpose I/O pin."
    global Summary
    Summary.Command = "Write Gpio Pin Config"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',96))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',PinNumber)))
        packerinit()
        value = setbits(int(Output), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(int(LogicVal), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(int(OpenDrain), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadGpioPinConfig(PinNumber):
    "Returns the direction, logic value and open drain configuration for a single general purpose I/O pin."
    global Summary
    Summary.Command = "Read Gpio Pin Config"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',96))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',PinNumber)))
        readbytes = _readcommand(3, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        Output = getbits(1, 0);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        packerinit(readdata)
        LogicVal = getbits(1, 0);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 2)[0]
        packerinit(readdata)
        OpenDrain = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Output, LogicVal, OpenDrain

def WriteGpioPin(PinNumber,  LogicVal):
    "Sets the output logic value for the specified GPIO Pin."
    global Summary
    Summary.Command = "Write Gpio Pin"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',97))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',PinNumber)))
        packerinit()
        value = setbits(int(LogicVal), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadGpioPin(PinNumber):
    "Returns the logic value for the specified GPIO pin."
    global Summary
    Summary.Command = "Read Gpio Pin"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',97))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',PinNumber)))
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        LogicVal = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, LogicVal

def WriteGenPurpseClockEnable(Clk,  Enabled,  Freq):
    ""
    global Summary
    Summary.Command = "Write Gen Purpse Clock Enable"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',99))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Clk)))
        writebytes.extend(list(struct.pack('B',Enabled)))
        writebytes.extend(list(struct.pack('I',Freq)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadGenPurpseClockEnable(Clk):
    ""
    global Summary
    Summary.Command = "Read Gen Purpse Clock Enable"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',99))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Clk)))
        readbytes = _readcommand(1, writebytes, ProtocolData)
        IsEnabled = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, IsEnabled

def ReadGenPurpseClockFrequency(Clk):
    ""
    global Summary
    Summary.Command = "Read Gen Purpse Clock Frequency"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',100))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Clk)))
        readbytes = _readcommand(4, writebytes, ProtocolData)
        Freq = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Freq

def WritePwmOutputConfiguration(Port,  Frequency,  DutyCycle,  OutputEnabled):
    "Sets the Dutycycle and frequency for the specified PWM port. It also enables or disables the port."
    global Summary
    Summary.Command = "Write Pwm Output Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',101))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Port.value)))
        writebytes.extend(list(struct.pack('I',Frequency)))
        writebytes.extend(list(struct.pack('B',DutyCycle)))
        packerinit()
        value = setbits(int(OutputEnabled), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadPwmOutputConfiguration(Port):
    "Gets the Dutycycle and frequency for the specified PWM port. It also returns whether the port is currently enabled or disabled."
    global Summary
    Summary.Command = "Read Pwm Output Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',101))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Port.value)))
        readbytes = _readcommand(6, writebytes, ProtocolData)
        Frequency = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        DutyCycle = struct.unpack_from ('B', bytearray(readbytes), 4)[0]
        readdata = struct.unpack_from ('B', bytearray(readbytes), 5)[0]
        packerinit(readdata)
        OutputEnabledBit = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Frequency, DutyCycle, OutputEnabledBit

def WritePwmInputConfiguration(Port,  SampleRate,  InCounterEnabled):
    "Sets the sample rate, dutycycle, high pulse width and low pulse width of the specified PWM incounter port. It also enables or disables the port."
    global Summary
    Summary.Command = "Write Pwm Input Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',102))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Port.value)))
        writebytes.extend(list(struct.pack('I',SampleRate)))
        writebytes.extend(list(struct.pack('B',InCounterEnabled)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadPwmInputConfiguration(Port):
    "Gets the sample rate, dutycycle, high pulse width and low pulse width of the specified PWM incounter port. It also returns whether the port is currently enabled or disabled."
    global Summary
    Summary.Command = "Read Pwm Input Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',102))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Port.value)))
        readbytes = _readcommand(10, writebytes, ProtocolData)
        SampleRate = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        InCounterEnabled = struct.unpack_from ('B', bytearray(readbytes), 4)[0]
        HighPulseWidth = struct.unpack_from ('H', bytearray(readbytes), 5)[0]
        LowPulseWidth = struct.unpack_from ('H', bytearray(readbytes), 7)[0]
        DutyCycle = struct.unpack_from ('B', bytearray(readbytes), 9)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SampleRate, InCounterEnabled, HighPulseWidth, LowPulseWidth, DutyCycle

def WriteI2CPassthrough(I2CPassthrough):
    "Writes data to specified I2C device address."
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
    "Reads data from specified I2C device address."
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

def ReadDmdTemperature():
    "This command applicable only if TMP411A temperature sensor is installed in the system."
    global Summary
    Summary.Command = "Read Dmd Temperature"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',105))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(2, writebytes, ProtocolData)
        Temperature = struct.unpack_from ('h', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Temperature

def ReadFpgaTemperature():
    "Retuns temperature values read by FPGA temperature sensor IP."
    global Summary
    Summary.Command = "Read Fpga Temperature"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',106))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(2, writebytes, ProtocolData)
        CurrentTemp = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 0)[0], 4)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, CurrentTemp

def WriteEepromLockState(LockState):
    "Sets the lock state of EEPROM. When lock is set, all writes to EEPROM settings and/or calibration data from application software will not be actually written to the EEPROM. The locked mode is to be used only in factory where user wants to play around with various settings without actually recording them in the EEPROM. In normal use mode, the lock is not supposed to be set."
    global Summary
    Summary.Command = "Write Eeprom Lock State"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',108))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',LockState)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadEepromLockState():
    "Gets the lock state of EEPROM."
    global Summary
    Summary.Command = "Read Eeprom Lock State"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',108))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        LockState = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, LockState

def WriteUartConfiguration(Port,  UartConfiguration):
    "Initializes all programmable parameters for the specified UART port."
    global Summary
    Summary.Command = "Write Uart Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',109))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Port.value)))
        packerinit()
        value = setbits(int(UartConfiguration.Enable), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        writebytes.extend(list(struct.pack('B',UartConfiguration.BaudRate.value)))
        writebytes.extend(list(struct.pack('B',UartConfiguration.DataBits.value)))
        writebytes.extend(list(struct.pack('B',UartConfiguration.StopBits.value)))
        writebytes.extend(list(struct.pack('B',UartConfiguration.Parity.value)))
        writebytes.extend(list(struct.pack('B',UartConfiguration.FlowControl.value)))
        writebytes.extend(list(struct.pack('B',UartConfiguration.RxTrigLevel.value)))
        writebytes.extend(list(struct.pack('B',UartConfiguration.TxTrigLevel.value)))
        writebytes.extend(list(struct.pack('B',UartConfiguration.RxDataPolarity.value)))
        writebytes.extend(list(struct.pack('B',UartConfiguration.RxDataSource.value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadUartConfiguration(Port):
    "Gets current configuration for the specified UART port."
    global Summary
    Summary.Command = "Read Uart Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',109))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Port.value)))
        readbytes = _readcommand(10, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        UartConfiguration.Enable = getbits(1, 0);
        UartConfiguration.BaudRate = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        UartConfiguration.DataBits = struct.unpack_from ('B', bytearray(readbytes), 2)[0]
        UartConfiguration.StopBits = struct.unpack_from ('B', bytearray(readbytes), 3)[0]
        UartConfiguration.Parity = struct.unpack_from ('B', bytearray(readbytes), 4)[0]
        UartConfiguration.FlowControl = struct.unpack_from ('B', bytearray(readbytes), 5)[0]
        UartConfiguration.RxTrigLevel = struct.unpack_from ('B', bytearray(readbytes), 6)[0]
        UartConfiguration.TxTrigLevel = struct.unpack_from ('B', bytearray(readbytes), 7)[0]
        UartConfiguration.RxDataPolarity = struct.unpack_from ('B', bytearray(readbytes), 8)[0]
        UartConfiguration.RxDataSource = struct.unpack_from ('B', bytearray(readbytes), 9)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, UartConfiguration

def ReadTpgPatternType():
    "Returns the current test pattern type being generated by Test Pattern Generator"
    global Summary
    Summary.Command = "Read Tpg Pattern Type"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',160))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        PatternTypeObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, FpgaTestPatternT(PatternTypeObj)

def ReadTpgPixelClkFreq():
    "Used to get the TPG clock frquency in Hertz. If External Clock is enabled function shall return external clock frequency otherwise shall return the internal reference clock selected to meet the pattern resolution and frame rate."
    global Summary
    Summary.Command = "Read Tpg Pixel Clk Freq"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',161))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        PixelClockFrequency = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, PixelClockFrequency

def WriteTpgSolidField(SolidColorRed,  SolidColorGreen,  SolidColorBlue):
    "Sets color for solid field test pattern"
    global Summary
    Summary.Command = "Write Tpg Solid Field"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',162))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',SolidColorRed)))
        writebytes.extend(list(struct.pack('H',SolidColorGreen)))
        writebytes.extend(list(struct.pack('H',SolidColorBlue)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadTpgSolidField():
    "Returns color for current solid field set by test patter generator. If Solid field is not enabled via TPG, 0 is returned for each color"
    global Summary
    Summary.Command = "Read Tpg Solid Field"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',162))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(6, writebytes, ProtocolData)
        SolidColorRed = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        SolidColorGreen = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        SolidColorBlue = struct.unpack_from ('H', bytearray(readbytes), 4)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SolidColorRed, SolidColorGreen, SolidColorBlue

def WriteTpgRampHorizontal(RampStep,  RampColor):
    "Sets the test pattern generator to produce a horizontal ramp with the specified step size. Only R/G/B/Y/C/M/W colors are Supported. For others, Use Color Ramp The ramp starts with intensity zero, depending on step speed reaches the maximum intensity if possible. If full intensity is acheived, the remaining pixels are white To start with some other intensity, use Fixed Ramp"
    global Summary
    Summary.Command = "Write Tpg Ramp Horizontal"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',163))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',RampStep.value)))
        writebytes.extend(list(struct.pack('B',RampColor.value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadTpgRampHorizontal():
    "Returns Horizontal Color Ramp's 'Stepping speed' and color. Only R/G/B/Y/C/M/W colors Supported."
    global Summary
    Summary.Command = "Read Tpg Ramp Horizontal"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',163))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(2, writebytes, ProtocolData)
        RampStepObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        RampColorObj = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, FpgaTpgHorzRampStepT(RampStepObj), TpgColorT(RampColorObj)

def WriteTpgRampVertical(RampStep,  RampColor):
    "sets the test pattern generator to produce a vertical ramp with the specified step size. Only R/G/B/Y/C/M/W Supported The ramp starts with intensity zero, depending on step speed reaches the maximum intensity if possible. If full intensity is acheived, the remaining pixels are white"
    global Summary
    Summary.Command = "Write Tpg Ramp Vertical"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',164))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',RampStep.value)))
        writebytes.extend(list(struct.pack('B',RampColor.value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadTpgRampVertical():
    "Returns Vertical Color Ramp's 'Stepping speed' and color. Only R/G/B/Y/C/M/W Supported"
    global Summary
    Summary.Command = "Read Tpg Ramp Vertical"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',164))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(2, writebytes, ProtocolData)
        RampStepObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        RampColorObj = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, FpgaTpgVertRampStepT(RampStepObj), TpgColorT(RampColorObj)

def WriteTpgHorizontalLines(TpgHorizontalLines):
    "Sets the test pattern generator to produce horizontal lines."
    global Summary
    Summary.Command = "Write Tpg Horizontal Lines"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',165))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',TpgHorizontalLines.Width)))
        writebytes.extend(list(struct.pack('H',TpgHorizontalLines.Space)))
        writebytes.extend(list(struct.pack('H',TpgHorizontalLines.LineColorRed)))
        writebytes.extend(list(struct.pack('H',TpgHorizontalLines.LineColorGreen)))
        writebytes.extend(list(struct.pack('H',TpgHorizontalLines.LineColorBlue)))
        writebytes.extend(list(struct.pack('H',TpgHorizontalLines.BackgroundColorRed)))
        writebytes.extend(list(struct.pack('H',TpgHorizontalLines.BackgroundColorGreen)))
        writebytes.extend(list(struct.pack('H',TpgHorizontalLines.BackgroundColorBlue)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadTpgHorizontalLines():
    "Gets current configuration for Horizontal Line Test Pattern"
    global Summary
    Summary.Command = "Read Tpg Horizontal Lines"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',165))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(16, writebytes, ProtocolData)
        TpgHorizontalLines.Width = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        TpgHorizontalLines.Space = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        TpgHorizontalLines.LineColorRed = struct.unpack_from ('H', bytearray(readbytes), 4)[0]
        TpgHorizontalLines.LineColorGreen = struct.unpack_from ('H', bytearray(readbytes), 6)[0]
        TpgHorizontalLines.LineColorBlue = struct.unpack_from ('H', bytearray(readbytes), 8)[0]
        TpgHorizontalLines.BackgroundColorRed = struct.unpack_from ('H', bytearray(readbytes), 10)[0]
        TpgHorizontalLines.BackgroundColorGreen = struct.unpack_from ('H', bytearray(readbytes), 12)[0]
        TpgHorizontalLines.BackgroundColorBlue = struct.unpack_from ('H', bytearray(readbytes), 14)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, TpgHorizontalLines

def WriteTpgVerticalLines(TpgVerticalLines):
    "Sets the test pattern generator to produce vertical lines. The sum of horizontal spacing and the horizontal width must be less than or equal to 100 pixels."
    global Summary
    Summary.Command = "Write Tpg Vertical Lines"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',166))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',TpgVerticalLines.Width)))
        writebytes.extend(list(struct.pack('H',TpgVerticalLines.Space)))
        writebytes.extend(list(struct.pack('H',TpgVerticalLines.LineColorRed)))
        writebytes.extend(list(struct.pack('H',TpgVerticalLines.LineColorGreen)))
        writebytes.extend(list(struct.pack('H',TpgVerticalLines.LineColorBlue)))
        writebytes.extend(list(struct.pack('H',TpgVerticalLines.BackgroundColorRed)))
        writebytes.extend(list(struct.pack('H',TpgVerticalLines.BackgroundColorGreen)))
        writebytes.extend(list(struct.pack('H',TpgVerticalLines.BackgroundColorBlue)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadTpgVerticalLines():
    "Gets current configuration for Vertical Line Test Pattern"
    global Summary
    Summary.Command = "Read Tpg Vertical Lines"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',166))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(16, writebytes, ProtocolData)
        TpgVerticalLines.Width = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        TpgVerticalLines.Space = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        TpgVerticalLines.LineColorRed = struct.unpack_from ('H', bytearray(readbytes), 4)[0]
        TpgVerticalLines.LineColorGreen = struct.unpack_from ('H', bytearray(readbytes), 6)[0]
        TpgVerticalLines.LineColorBlue = struct.unpack_from ('H', bytearray(readbytes), 8)[0]
        TpgVerticalLines.BackgroundColorRed = struct.unpack_from ('H', bytearray(readbytes), 10)[0]
        TpgVerticalLines.BackgroundColorGreen = struct.unpack_from ('H', bytearray(readbytes), 12)[0]
        TpgVerticalLines.BackgroundColorBlue = struct.unpack_from ('H', bytearray(readbytes), 14)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, TpgVerticalLines

def WriteTpgDiagonalLines(TpgDiagonalLines):
    "Sets current configuration for Diagonal Line Test Pattern"
    global Summary
    Summary.Command = "Write Tpg Diagonal Lines"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',167))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',TpgDiagonalLines.LineColorRed)))
        writebytes.extend(list(struct.pack('H',TpgDiagonalLines.LineColorGreen)))
        writebytes.extend(list(struct.pack('H',TpgDiagonalLines.LineColorBlue)))
        writebytes.extend(list(struct.pack('H',TpgDiagonalLines.BackgroundColorRed)))
        writebytes.extend(list(struct.pack('H',TpgDiagonalLines.BackgroundColorGreen)))
        writebytes.extend(list(struct.pack('H',TpgDiagonalLines.BackgroundColorBlue)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadTpgDiagonalLines():
    "Gets current configuration for Diagonal Line Test Pattern"
    global Summary
    Summary.Command = "Read Tpg Diagonal Lines"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',167))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(12, writebytes, ProtocolData)
        TpgDiagonalLines.LineColorRed = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        TpgDiagonalLines.LineColorGreen = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        TpgDiagonalLines.LineColorBlue = struct.unpack_from ('H', bytearray(readbytes), 4)[0]
        TpgDiagonalLines.BackgroundColorRed = struct.unpack_from ('H', bytearray(readbytes), 6)[0]
        TpgDiagonalLines.BackgroundColorGreen = struct.unpack_from ('H', bytearray(readbytes), 8)[0]
        TpgDiagonalLines.BackgroundColorBlue = struct.unpack_from ('H', bytearray(readbytes), 10)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, TpgDiagonalLines

def WriteTpgGridLines(TpgGridLines):
    "Sets current configuration for Grid Lines Test Pattern. The sum of horizontal spacing and the horizontal width must be less than or equal to 100 pixels."
    global Summary
    Summary.Command = "Write Tpg Grid Lines"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',168))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',TpgGridLines.HorizontalWidth)))
        writebytes.extend(list(struct.pack('H',TpgGridLines.HorizontalSpace)))
        writebytes.extend(list(struct.pack('H',TpgGridLines.VerticalWidth)))
        writebytes.extend(list(struct.pack('H',TpgGridLines.VerticalSpace)))
        writebytes.extend(list(struct.pack('H',TpgGridLines.LineColorRed)))
        writebytes.extend(list(struct.pack('H',TpgGridLines.LineColorGreen)))
        writebytes.extend(list(struct.pack('H',TpgGridLines.LineColorBlue)))
        writebytes.extend(list(struct.pack('H',TpgGridLines.BackgroundColorRed)))
        writebytes.extend(list(struct.pack('H',TpgGridLines.BackgroundColorGreen)))
        writebytes.extend(list(struct.pack('H',TpgGridLines.BackgroundColorBlue)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadTpgGridLines():
    "Gets current configuration for Grid Lines Test Pattern."
    global Summary
    Summary.Command = "Read Tpg Grid Lines"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',168))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(20, writebytes, ProtocolData)
        TpgGridLines.HorizontalWidth = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        TpgGridLines.HorizontalSpace = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        TpgGridLines.VerticalWidth = struct.unpack_from ('H', bytearray(readbytes), 4)[0]
        TpgGridLines.VerticalSpace = struct.unpack_from ('H', bytearray(readbytes), 6)[0]
        TpgGridLines.LineColorRed = struct.unpack_from ('H', bytearray(readbytes), 8)[0]
        TpgGridLines.LineColorGreen = struct.unpack_from ('H', bytearray(readbytes), 10)[0]
        TpgGridLines.LineColorBlue = struct.unpack_from ('H', bytearray(readbytes), 12)[0]
        TpgGridLines.BackgroundColorRed = struct.unpack_from ('H', bytearray(readbytes), 14)[0]
        TpgGridLines.BackgroundColorGreen = struct.unpack_from ('H', bytearray(readbytes), 16)[0]
        TpgGridLines.BackgroundColorBlue = struct.unpack_from ('H', bytearray(readbytes), 18)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, TpgGridLines

def WriteTpgColorBars(Width,  ColorEnableRed,  ColorEnableGreen,  ColorEnableBlue):
    "Sets current configuration for Color Bar Test Patterns"
    global Summary
    Summary.Command = "Write Tpg Color Bars"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',169))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',Width)))
        packerinit()
        value = setbits(int(ColorEnableRed), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(int(ColorEnableGreen), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(int(ColorEnableBlue), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadTpgColorBars():
    "Gets current configuration for Color Bar Test Patterns"
    global Summary
    Summary.Command = "Read Tpg Color Bars"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',169))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(5, writebytes, ProtocolData)
        Width = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        readdata = struct.unpack_from ('B', bytearray(readbytes), 2)[0]
        packerinit(readdata)
        ColorEnableRed = getbits(1, 0);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 3)[0]
        packerinit(readdata)
        ColorEnableGreen = getbits(1, 0);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 4)[0]
        packerinit(readdata)
        ColorEnableBlue = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Width, ColorEnableRed, ColorEnableGreen, ColorEnableBlue

def WriteTpgColorHorzRamp(RampStep,  Height,  ColorEnableRed,  ColorEnableGreen,  ColorEnableBlue):
    "Sets Configuration for Horizontal Color Ramp."
    global Summary
    Summary.Command = "Write Tpg Color Horz Ramp"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',170))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',RampStep.value)))
        writebytes.extend(list(struct.pack('H',Height)))
        packerinit()
        value = setbits(int(ColorEnableRed), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(int(ColorEnableGreen), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(int(ColorEnableBlue), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadTpgColorHorzRamp():
    "Gets Configuration for Horizontal Color Ramp"
    global Summary
    Summary.Command = "Read Tpg Color Horz Ramp"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',170))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(6, writebytes, ProtocolData)
        RampStepObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        Height = struct.unpack_from ('H', bytearray(readbytes), 1)[0]
        readdata = struct.unpack_from ('B', bytearray(readbytes), 3)[0]
        packerinit(readdata)
        ColorEnableRed = getbits(1, 0);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 4)[0]
        packerinit(readdata)
        ColorEnableGreen = getbits(1, 0);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 5)[0]
        packerinit(readdata)
        ColorEnableBlue = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, TpgHorzRampStepT(RampStepObj), Height, ColorEnableRed, ColorEnableGreen, ColorEnableBlue

def WriteTpgFixedRamp(TpgFixedRamp):
    "Sets Configuration for Fixed Ramp Test Pattern. This allows for non-zero intensity start and programable 'step speed' and color"
    global Summary
    Summary.Command = "Write Tpg Fixed Ramp"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',171))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',TpgFixedRamp.StartIntensity)))
        writebytes.extend(list(struct.pack('H',TpgFixedRamp.RampStepWidth)))
        writebytes.extend(list(struct.pack('H',TpgFixedRamp.RampStepInc)))
        writebytes.extend(list(struct.pack('H',TpgFixedRamp.BackgroundColorRed)))
        writebytes.extend(list(struct.pack('H',TpgFixedRamp.BackgroundColorGreen)))
        writebytes.extend(list(struct.pack('H',TpgFixedRamp.BackgroundColorBlue)))
        writebytes.extend(list(struct.pack('B',TpgFixedRamp.RampColor.value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadTpgFixedRamp():
    "Gets Configuration for Fixed Ramp Test Pattern"
    global Summary
    Summary.Command = "Read Tpg Fixed Ramp"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',171))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(13, writebytes, ProtocolData)
        TpgFixedRamp.StartIntensity = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        TpgFixedRamp.RampStepWidth = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        TpgFixedRamp.RampStepInc = struct.unpack_from ('H', bytearray(readbytes), 4)[0]
        TpgFixedRamp.BackgroundColorRed = struct.unpack_from ('H', bytearray(readbytes), 6)[0]
        TpgFixedRamp.BackgroundColorGreen = struct.unpack_from ('H', bytearray(readbytes), 8)[0]
        TpgFixedRamp.BackgroundColorBlue = struct.unpack_from ('H', bytearray(readbytes), 10)[0]
        TpgFixedRamp.RampColor = struct.unpack_from ('B', bytearray(readbytes), 12)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, TpgFixedRamp

def WriteTpgDiamondDiagLines(TpgDiamondDiagLines):
    "Sets Configuration for Diamond Diagonal Lines Test Pattern"
    global Summary
    Summary.Command = "Write Tpg Diamond Diag Lines"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',172))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',TpgDiamondDiagLines.ForwardLineStartColor.value)))
        writebytes.extend(list(struct.pack('B',TpgDiamondDiagLines.BackwardLineColor.value)))
        writebytes.extend(list(struct.pack('H',TpgDiamondDiagLines.BackgroundColorRed)))
        writebytes.extend(list(struct.pack('H',TpgDiamondDiagLines.BackgroundColorGreen)))
        writebytes.extend(list(struct.pack('H',TpgDiamondDiagLines.BackgroundColorBlue)))
        packerinit()
        value = setbits(int(TpgDiamondDiagLines.DoubleLineMode), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        writebytes.extend(list(struct.pack('H',TpgDiamondDiagLines.Distance)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadTpgDiamondDiagLines():
    "Gets Configuration for Diamond Diagonal Lines Test Pattern"
    global Summary
    Summary.Command = "Read Tpg Diamond Diag Lines"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',172))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(11, writebytes, ProtocolData)
        TpgDiamondDiagLines.ForwardLineStartColor = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        TpgDiamondDiagLines.BackwardLineColor = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        TpgDiamondDiagLines.BackgroundColorRed = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        TpgDiamondDiagLines.BackgroundColorGreen = struct.unpack_from ('H', bytearray(readbytes), 4)[0]
        TpgDiamondDiagLines.BackgroundColorBlue = struct.unpack_from ('H', bytearray(readbytes), 6)[0]
        readdata = struct.unpack_from ('B', bytearray(readbytes), 8)[0]
        packerinit(readdata)
        TpgDiamondDiagLines.DoubleLineMode = getbits(1, 0);
        TpgDiamondDiagLines.Distance = struct.unpack_from ('H', bytearray(readbytes), 9)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, TpgDiamondDiagLines

def WriteTpgCheckerboard(TpgCheckerboard):
    "Sets current configuration for Checker Board Test Patterns"
    global Summary
    Summary.Command = "Write Tpg Checkerboard"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',173))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',TpgCheckerboard.Width)))
        writebytes.extend(list(struct.pack('H',TpgCheckerboard.Height)))
        writebytes.extend(list(struct.pack('H',TpgCheckerboard.TopLeftCheckerColorRed)))
        writebytes.extend(list(struct.pack('H',TpgCheckerboard.TopLeftCheckerColorGreen)))
        writebytes.extend(list(struct.pack('H',TpgCheckerboard.TopLeftCheckerColorBlue)))
        writebytes.extend(list(struct.pack('H',TpgCheckerboard.NextCheckerColorRed)))
        writebytes.extend(list(struct.pack('H',TpgCheckerboard.NextCheckerColorGreen)))
        writebytes.extend(list(struct.pack('H',TpgCheckerboard.NextCheckerColorBlue)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadTpgCheckerboard():
    "Gets current configuration for Checker Board Test Patterns"
    global Summary
    Summary.Command = "Read Tpg Checkerboard"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',173))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(16, writebytes, ProtocolData)
        TpgCheckerboard.Width = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        TpgCheckerboard.Height = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        TpgCheckerboard.TopLeftCheckerColorRed = struct.unpack_from ('H', bytearray(readbytes), 4)[0]
        TpgCheckerboard.TopLeftCheckerColorGreen = struct.unpack_from ('H', bytearray(readbytes), 6)[0]
        TpgCheckerboard.TopLeftCheckerColorBlue = struct.unpack_from ('H', bytearray(readbytes), 8)[0]
        TpgCheckerboard.NextCheckerColorRed = struct.unpack_from ('H', bytearray(readbytes), 10)[0]
        TpgCheckerboard.NextCheckerColorGreen = struct.unpack_from ('H', bytearray(readbytes), 12)[0]
        TpgCheckerboard.NextCheckerColorBlue = struct.unpack_from ('H', bytearray(readbytes), 14)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, TpgCheckerboard

def WriteTpgCrossPattern(TpgCrossPattern):
    "Sets current configuration for Cross Pattern Test Pattern. A pair of horizontal/vertical lines (a cross) at the specified coordinates"
    global Summary
    Summary.Command = "Write Tpg Cross Pattern"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',174))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',TpgCrossPattern.CoordinateX)))
        writebytes.extend(list(struct.pack('H',TpgCrossPattern.CoordinateY)))
        writebytes.extend(list(struct.pack('H',TpgCrossPattern.LineColorRed)))
        writebytes.extend(list(struct.pack('H',TpgCrossPattern.LineColorGreen)))
        writebytes.extend(list(struct.pack('H',TpgCrossPattern.LineColorBlue)))
        writebytes.extend(list(struct.pack('H',TpgCrossPattern.BackgroundColorRed)))
        writebytes.extend(list(struct.pack('H',TpgCrossPattern.BackgroundColorGreen)))
        writebytes.extend(list(struct.pack('H',TpgCrossPattern.BackgroundColorBlue)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadTpgCrossPattern():
    "Sets current configuration for Cross Pattern Test Pattern. A pair of horizontal/vertical lines (a cross) at the specified coordinates"
    global Summary
    Summary.Command = "Read Tpg Cross Pattern"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',174))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(16, writebytes, ProtocolData)
        TpgCrossPattern.CoordinateX = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        TpgCrossPattern.CoordinateY = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        TpgCrossPattern.LineColorRed = struct.unpack_from ('H', bytearray(readbytes), 4)[0]
        TpgCrossPattern.LineColorGreen = struct.unpack_from ('H', bytearray(readbytes), 6)[0]
        TpgCrossPattern.LineColorBlue = struct.unpack_from ('H', bytearray(readbytes), 8)[0]
        TpgCrossPattern.BackgroundColorRed = struct.unpack_from ('H', bytearray(readbytes), 10)[0]
        TpgCrossPattern.BackgroundColorGreen = struct.unpack_from ('H', bytearray(readbytes), 12)[0]
        TpgCrossPattern.BackgroundColorBlue = struct.unpack_from ('H', bytearray(readbytes), 14)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, TpgCrossPattern

def WriteXprFixedOutputEnable(ChannelNum,  FixedOutputEnable):
    "**Fixed Output Enable** : Configures Actuator in fixed output mode. --> Byte 2: 0x00 - Disable 0x01 - Enable --> Byte 3-5: Reserved must be set to 0x000000"
    global Summary
    Summary.Command = "Write Xpr Fixed Output Enable"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x00]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('B',ChannelNum)))
        packerinit()
        value = setbits(int(FixedOutputEnable), 1, 0)
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadXprFixedOutputEnable(ChannelNum):
    "**Fixed Output Enable** : Configures Actuator in fixed output mode. --> Byte 2: 0x00 - Disable 0x01 - Enable --> Byte 3-5: Reserved must be set to 0x000000"
    global Summary
    Summary.Command = "Read Xpr Fixed Output Enable"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x00]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('B',ChannelNum)))
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        FixedOutputEnable = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, FixedOutputEnable

def WriteXprDacGain(ChannelNum,  DacGain):
    "**DAC Gain** : Set Waveform Generator DAC Gain. --> Byte 2: Range 0 - 255 format u1.7 (0 to 1.9921875)  --> Byte 3-5: Reserved must be set to 0x000000"
    global Summary
    Summary.Command = "Write Xpr Dac Gain"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x01]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('B',ChannelNum)))
        packerinit()
        ********** Invalid Write Bit Field Type - DLPComposer.Commands.Spec.FixedPtType;
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadXprDacGain(ChannelNum):
    "**DAC Gain** : Set Waveform Generator DAC Gain. --> Byte 2: Range 0 - 255 format u1.7 (0 to 1.9921875)  --> Byte 3-5: Reserved must be set to 0x000000"
    global Summary
    Summary.Command = "Read Xpr Dac Gain"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x01]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('B',ChannelNum)))
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        ********** Invalid Write Bit Field Type - DLPComposer.Commands.Spec.FixedPtType;
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DacGain

def WriteXprSubframeDelay(ChannelNum,  SubframeDelay):
    "**Subframe delay** : Subframe delay --> Bytes 2-5; Range 0 - 262144 and lsb = 133.333ns"
    global Summary
    Summary.Command = "Write Xpr Subframe Delay"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x02]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('B',ChannelNum)))
        packerinit()
        value = setbits(int(SubframeDelay), 32, 0)
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadXprSubframeDelay(ChannelNum):
    "**Subframe delay** : Subframe delay --> Bytes 2-5; Range 0 - 262144 and lsb = 133.333ns"
    global Summary
    Summary.Command = "Read Xpr Subframe Delay"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x02]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('B',ChannelNum)))
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        SubframeDelay = getbits(32, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SubframeDelay

def ReadXprActuatorType():
    "**Actuator Type (READ ONLY)** : Actuator type --> Byte 2:  0x00 - NONE  0x01 - Optotune (XPR-25 Model)  0x80 - TI Actuator Interface (EEPROM)  0x81 - TI Actuator Interface (MCU) "
    global Summary
    Summary.Command = "Read Xpr Actuator Type"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x03]
        writebytes.extend(valueArray)
        valueArray = [0x00]
        writebytes.extend(valueArray)
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        ActuatorType = getbits(8, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ActuatorType

def WriteXprOutputEnable(ChannelNum,  OutputEnable):
    "**Output Enable/Disable** : Actuator output enable/disable  --> Byte 2: 0x00 - Disable 0x01 - Enable  --> Byte 3-5: Reserved must be set to 0x000000"
    global Summary
    Summary.Command = "Write Xpr Output Enable"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x04]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('B',ChannelNum)))
        packerinit()
        value = setbits(int(OutputEnable), 1, 0)
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadXprOutputEnable(ChannelNum):
    "**Output Enable/Disable** : Actuator output enable/disable  --> Byte 2: 0x00 - Disable 0x01 - Enable  --> Byte 3-5: Reserved must be set to 0x000000"
    global Summary
    Summary.Command = "Read Xpr Output Enable"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x04]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('B',ChannelNum)))
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        OutputEnable = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, OutputEnable

def WriteXprClockWidth(ChannelNum,  ClockWidth):
    "**Clock Width** : Defines the high and low width for the output clock (the clock period will be 2*(ClkWidth+1))  0 = 1 (DAC clock period is two clocks); lsb = 8.33ns  --> Bytes 2-5 : ClkWidth  Example: ClkWidth = 0; will generate clock of 2*(1+1)*8.33 = 33.32ns"
    global Summary
    Summary.Command = "Write Xpr Clock Width"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x05]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('B',ChannelNum)))
        packerinit()
        value = setbits(int(ClockWidth), 32, 0)
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadXprClockWidth(ChannelNum):
    "**Clock Width** : Defines the high and low width for the output clock (the clock period will be 2*(ClkWidth+1))  0 = 1 (DAC clock period is two clocks); lsb = 8.33ns  --> Bytes 2-5 : ClkWidth  Example: ClkWidth = 0; will generate clock of 2*(1+1)*8.33 = 33.32ns"
    global Summary
    Summary.Command = "Read Xpr Clock Width"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x05]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('B',ChannelNum)))
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        ClockWidth = getbits(32, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ClockWidth

def WriteXprDacOffset(ChannelNum,  DacOffset):
    "**DAC Offset** : DAC Output Offset  --> Byte 2: Range -128 - +127 format S7 (-128 to +127)  --> Byte 3-5: Reserved must be set to 0x000000"
    global Summary
    Summary.Command = "Write Xpr Dac Offset"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x06]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('B',ChannelNum)))
        packerinit()
        ********** Invalid Write Bit Field Type - DLPComposer.Commands.Spec.Int8Type;
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadXprDacOffset(ChannelNum):
    "**DAC Offset** : DAC Output Offset  --> Byte 2: Range -128 - +127 format S7 (-128 to +127)  --> Byte 3-5: Reserved must be set to 0x000000"
    global Summary
    Summary.Command = "Read Xpr Dac Offset"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x06]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('B',ChannelNum)))
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        ********** Invalid Write Bit Field Type - DLPComposer.Commands.Spec.Int8Type;
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DacOffset

def WriteXprNumberOfSegments(ChannelNum,  NumberOfSegments):
    "**Number of Segments** : Defines number of segments  --> Byte 2: Range 2 - 255  --> Byte 3-5: Reserved must be set to 0x000000 "
    global Summary
    Summary.Command = "Write Xpr Number Of Segments"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x07]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('B',ChannelNum)))
        packerinit()
        value = setbits(int(NumberOfSegments), 8, 0)
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadXprNumberOfSegments(ChannelNum):
    "**Number of Segments** : Defines number of segments  --> Byte 2: Range 2 - 255  --> Byte 3-5: Reserved must be set to 0x000000 "
    global Summary
    Summary.Command = "Read Xpr Number Of Segments"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x07]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('B',ChannelNum)))
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        NumberOfSegments = getbits(8, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, NumberOfSegments

def WriteXprSegmentLength(ChannelNum,  SegmentLength):
    "**Segments Length** : Defines size of the segments  --> Bytes 2-3: Range 19 - 4095  --> Bytes 4-5: Reserved must be set to 0x0000"
    global Summary
    Summary.Command = "Write Xpr Segment Length"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x08]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('B',ChannelNum)))
        packerinit()
        value = setbits(int(SegmentLength), 16, 0)
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadXprSegmentLength(ChannelNum):
    "**Segments Length** : Defines size of the segments  --> Bytes 2-3: Range 19 - 4095  --> Bytes 4-5: Reserved must be set to 0x0000"
    global Summary
    Summary.Command = "Read Xpr Segment Length"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x08]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('B',ChannelNum)))
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        SegmentLength = getbits(16, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SegmentLength

def WriteXprInvertPwmA(ChannelNum,  InvertPwmA):
    "**Invert PWM A** : Applicable when AWC is configured to PWM type instead of DAC  --> Byte 2: 0x00 - No inversion 0x01 - Inverted  --> Byte 3-5: Reserved must be set to 0x000000"
    global Summary
    Summary.Command = "Write Xpr Invert Pwm A"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x09]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('B',ChannelNum)))
        packerinit()
        value = setbits(int(InvertPwmA), 1, 0)
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadXprInvertPwmA(ChannelNum):
    "**Invert PWM A** : Applicable when AWC is configured to PWM type instead of DAC  --> Byte 2: 0x00 - No inversion 0x01 - Inverted  --> Byte 3-5: Reserved must be set to 0x000000"
    global Summary
    Summary.Command = "Read Xpr Invert Pwm A"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x09]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('B',ChannelNum)))
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        InvertPwmA = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, InvertPwmA

def WriteXprInvertPwmB(ChannelNum,  InvertPwmB):
    "**Invert PWM ** : Applicable when AWC is configured to PWM type instead of DAC  --> Byte 2: 0x00 - No inversion 0x01 - Inverted  --> Byte 3-5: Reserved must be set to 0x000000"
    global Summary
    Summary.Command = "Write Xpr Invert Pwm B"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x0A]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('B',ChannelNum)))
        packerinit()
        value = setbits(int(InvertPwmB), 1, 0)
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadXprInvertPwmB(ChannelNum):
    "**Invert PWM ** : Applicable when AWC is configured to PWM type instead of DAC  --> Byte 2: 0x00 - No inversion 0x01 - Inverted  --> Byte 3-5: Reserved must be set to 0x000000"
    global Summary
    Summary.Command = "Read Xpr Invert Pwm B"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x0A]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('B',ChannelNum)))
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        InvertPwmB = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, InvertPwmB

def WriteXprSubframeFilterValue(ChannelNum,  SubframeFilterValue):
    "**Subframe Filter Value** : Sets Subframe Filter Value - defines the minimum time between Subframe edges. Edges closer than the set value will be filtered out.  --> Byte 2: 0 = Filter disabled, >0 = Filter time will be Val x 60us, Range: 0 - 255  --> Byte 3-5: Reserved must be set to 0x000000"
    global Summary
    Summary.Command = "Write Xpr Subframe Filter Value"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x0B]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('B',ChannelNum)))
        packerinit()
        value = setbits(int(SubframeFilterValue), 8, 0)
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadXprSubframeFilterValue(ChannelNum):
    "**Subframe Filter Value** : Sets Subframe Filter Value - defines the minimum time between Subframe edges. Edges closer than the set value will be filtered out.  --> Byte 2: 0 = Filter disabled, >0 = Filter time will be Val x 60us, Range: 0 - 255  --> Byte 3-5: Reserved must be set to 0x000000"
    global Summary
    Summary.Command = "Read Xpr Subframe Filter Value"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x0B]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('B',ChannelNum)))
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        SubframeFilterValue = getbits(8, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SubframeFilterValue

def WriteXprSubframeWatchDog(ChannelNum,  SubframeWatchDog):
    "**Subframe Watch Dog** : Defines the maximum time between Subframe edges; if timer expires, then the WG will automatically output the Fixed Output value.  and the normal output will resume on the next subframe edge.  --> Bytes 2-3: 0 = Subframe watchdog disabled, >0 = Watchdog time will be Time x 60us, Range: Range: 0 - 1023  --> Bytes 4-5: Reserved must be set to 0x0000"
    global Summary
    Summary.Command = "Write Xpr Subframe Watch Dog"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x0C]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('B',ChannelNum)))
        packerinit()
        value = setbits(int(SubframeWatchDog), 16, 0)
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadXprSubframeWatchDog(ChannelNum):
    "**Subframe Watch Dog** : Defines the maximum time between Subframe edges; if timer expires, then the WG will automatically output the Fixed Output value.  and the normal output will resume on the next subframe edge.  --> Bytes 2-3: 0 = Subframe watchdog disabled, >0 = Watchdog time will be Time x 60us, Range: Range: 0 - 1023  --> Bytes 4-5: Reserved must be set to 0x0000"
    global Summary
    Summary.Command = "Read Xpr Subframe Watch Dog"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x0C]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('B',ChannelNum)))
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        SubframeWatchDog = getbits(16, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SubframeWatchDog

def WriteXprFixedOutputValue(ChannelNum,  FixedOutputValue):
    "**Fixed Output Value** : Defines the value to be output on DAC when fixed output mode is selected. --> Byte 2: Value to be output on DAC, Range -128 to 127. --> Bytes 3-5: Reserved must be set to 0x000000"
    global Summary
    Summary.Command = "Write Xpr Fixed Output Value"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x0D]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('B',ChannelNum)))
        packerinit()
        ********** Invalid Write Bit Field Type - DLPComposer.Commands.Spec.Int8Type;
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadXprFixedOutputValue(ChannelNum):
    "**Fixed Output Value** : Defines the value to be output on DAC when fixed output mode is selected. --> Byte 2: Value to be output on DAC, Range -128 to 127. --> Bytes 3-5: Reserved must be set to 0x000000"
    global Summary
    Summary.Command = "Read Xpr Fixed Output Value"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',181))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x0D]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('B',ChannelNum)))
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        ********** Invalid Write Bit Field Type - DLPComposer.Commands.Spec.Int8Type;
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, FixedOutputValue

