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

class Src3DLrEncodingT(Enum):
    DlpReady = 0
    NoEncoding = 1
    Lr7525Encoding = 2

class SrcCscTablesT(Enum):
    TableFullrangeRgb = 0
    TableBt601YuvVideodecoder = 1
    TableFullrangeYuv1 = 2
    TableOffsetRgb = 3
    TableBt601OffsetYuv = 4
    TableFullrangeYuv = 5
    TableBt709OffsetYuv = 6
    TableSmpte240M = 7
    TableBt2020 = 8
    Maxtable = 9

class SplashCaptureStateT(Enum):
    Terminated = 0
    BufferWriteInProgress = 1
    BufferWriteComplete = 2
    FlashWriteInProgress = 3
    FlashWriteComplete = 4

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

class DbPixelWeightT(Enum):
    DbWeight0 = 0
    DbWeight25 = 1
    DbWeight50 = 2
    DbWeight75 = 3

class UrtRxDataSourceT(Enum):
    Rxd = 0
    Lampstat = 1

class DispEdgeBlendGeometryModeT(Enum):
    NoGeometricCorrection = 0
    KeystoneCorners = 1

class I2CPortT(Enum):
    Port0 = 0
    Port1 = 1
    Port2 = 2
    MaxPort = 3

class SrcVboByteModeT(Enum):
    SrcVbo3BytesMode = 1
    SrcVbo4BytesMode = 2
    SrcVbo5BytesMode = 3

class CmdSwitchTypeT(Enum):
    ToBoot = 0
    ToAppViaReset = 1
    ToAppDirect = 2
    ToAppTrueGlobalDirect = 3

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

class UrtParityT(Enum):
    _None = 0
    Even = 1
    Odd = 2

class SrcSyncConfigT(Enum):
    PortSyncNoinv = 0
    PortSyncInv = 1
    AlfSync = 2
    DecodedSync = 3

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

class Src3DOeReferenceT(Enum):
    OeOddisleft = 0
    OeOddisright = 1
    OeNoReference = 2

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

class DispfmtColorChannelSelectT(Enum):
    Broadcast = 0
    Green = 1
    Red = 2
    Blue = 3

class CmdFlashUpdateT(Enum):
    Lock = 0
    Unlock = 4154802215

class UrtFlowControlT(Enum):
    Off = 0
    Hw = 1

class DpScanStatus(Enum):
    DetectStableVideo = 0
    Searching = 1
    Syncdetected = 2
    Locked = 3
    Suspended = 4

class SrcDownSampleConfigT(Enum):
    NoDownsample = 0
    DownsampleFirstPxl = 1
    DownsampleSecondPxl = 2

class DispfmtImageSizeT(Enum):
    Fill = 0
    Native = 1
    Manual = 2
    AspectNative = 3
    Aspect43 = 4
    Aspect169 = 5

class UrtDataBitsT(Enum):
    UrtDatbits5 = 0
    UrtDatbits6 = 1
    UrtDatbits7 = 2
    UrtDatbits8 = 3

class UrtStopBitsT(Enum):
    UrtStpbits1 = 0
    UrtStpbits2 = 1

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

class DispfmtEdgeBlendStorageOptionsT(Enum):
    DontStore = 0
    WriteToStorage = 1
    WriteToStorageApplyAtStartup = 2

class Src3DColorT(Enum):
    ClrRed = 0
    ClrGreen = 1
    ClrBlue = 2
    ClrCyan = 3
    ClrMagenta = 4
    ClrYellow = 5
    ClrWhite = 6
    ClrBlack = 7
    Clr75Blue25Black = 8
    Clr25Blue75Black = 9

class SrcPixelFormatT(Enum):
    Rgb = 0
    Yuv444 = 1
    Yuv422 = 2
    Yuv420 = 3

class CmdAlfControl(Enum):
    Resync = 0
    Start = 1
    Stop = 2

class DpState(Enum):
    Standby = 0
    Initalizing = 1
    SplashAtStartup = 2
    Idling = 3
    Scaning = 4
    Autolock = 5
    Monitoring = 6

class Src3DTbReferenceT(Enum):
    TbTopisleft = 0
    TbTopisright = 1
    TbNoReference = 2

class WpcLedColorT(Enum):
    Red = 0
    Green = 1
    Blue = 2

class FlChipSelectT(Enum):
    Cs0 = 0
    Cs1 = 1
    Cs2 = 2

class SrcVboDataMapModeT(Enum):
    Mode0 = 0
    Mode1 = 1
    Mode2 = 2
    Mode3 = 3
    Mode4 = 4
    Mode5 = 5
    Mode6 = 6
    Mode7 = 7
    Mode8 = 8
    Mode9 = 9
    ModeNone = 10

class Src3DFormatT(Enum):
    VsyncSeparatedHalf = 0
    VsyncSeparatedFull = 1
    VertPackedHalf = 2
    VertPackedFull = 3
    HorizPackedHalf = 4
    HorizPackedFull = 5

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

class Src3DFrameDominanceT(Enum):
    LeftEye = 0
    RightEye = 1

class FrameFrcModeT(Enum):
    Fixed = 0
    Sync1X = 1
    Sync2X = 2
    Sync3X = 3
    Sync4X = 4
    Sync6X = 5
    Sync8X = 6
    Sync10X = 7

class UrtRxDataPolarityT(Enum):
    Noninv = 0
    Inv = 1

class CmdModeT(Enum):
    Bootloader = 0
    MainApplication = 1
    MainApplicationTrueGlobal = 2

class Src3DLrReferenceT(Enum):
    Lr3DrefIn = 0
    LrGpioIn = 1
    LrTopfield = 2
    Lr1StFrame = 3
    LrEmbeddedEncoding = 4

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

class ThreeDSourceConfiguration:
     Format: Src3DFormatT
     LrReference: Src3DLrReferenceT
     FrameDominance: Src3DFrameDominanceT
     LrEncoding: Src3DLrEncodingT
     TbReference: Src3DTbReferenceT
     OeReference: Src3DOeReferenceT
     NumActiveBlankLines: int               # int
     NumberOfEncodedLines: int              # int
     LeftEncodedLineLocation: int           # int
     RightEncodedLineLocation: int          # int
     BlankingColor: Src3DColorT

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
     Dlpa3005CommErr: bool
     UmcRefreshBwUnderflowErr: bool
     DmdInitErr: bool
     DmdPwrDownErr: bool
     SrcdefNotpresent: bool
     SeqbinNotpresent: bool
     ProductConfigurationFailed: bool
     TemporalDitherMaskNotLoading: bool
     EepromInitFail: bool

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

class WpcOptimalDutyCycle:
     RedIdealDutyCycle: float
     GreenIdealDutyCycle: float
     BlueIdealDutyCycle: float
     RedOptimalDutyCycle: float
     GreenOptimalDutyCycle: float
     BlueOptimalDutyCycle: float

class WpcCalibrationData:
     ChromaticX: int                        # int
     ChromaticY: int                        # int
     LuminanceY: int                        # int
     RedSensorOutput: int                   # int
     GreenSensorOutput: int                 # int
     BlueSensorOutput: int                  # int
     DutyCycle: float

class WpcCalibrationStructureOverride:
     LedColor: WpcLedColorT
     ChromaticX: int                        # int
     ChromaticY: int                        # int
     LuminanceY: int                        # int
     RedSensorOutput: int                   # int
     GreenSensorOutput: int                 # int
     BlueSensorOutput: int                  # int
     DutyCycle: float

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
     GroupEventsCurrentCount: int           # int
     MailboxCurrentCount: int               # int
     MemoryPoolsCurrentCount: int           # int
     SemaphoreCurrentCount: int             # int

class DisplayImageSize:
     ImageSizeType: DispfmtImageSizeT
     CroppedAreaFirstPixel: int             # int
     CroppedAreaFirstLine: int              # int
     CroppedAreaPixelsPerLine: int          # int
     CroppedAreaLinesPerFrame: int          # int
     DisplayAreaFirstPixel: int             # int
     DisplayAreaFirstLine: int              # int
     DisplayAreaPixelsPerLine: int          # int
     DisplayAreaLinesPerFrame: int          # int

class SourceConfigurationWrite:
     VSyncConfiguration: SrcSyncConfigT
     HSyncConfiguration: SrcSyncConfigT
     TopFieldConfiguration: SrcSyncConfigT
     DownSampleConfiguration: SrcDownSampleConfigT
     IsThreeD: bool
     IsClockPolarityPositive: bool
     PixelFormat: SrcPixelFormatT
     IsExternalDataEnable: bool
     IsInterlaced: bool
     IsOffsetBinary: bool
     IsTopFieldInvertedAtScaler: bool
     TotalAreaPixelsPerLine: int            # int
     TotalAreaLinesPerFrame: int            # int
     ActiveAreaFirstPixel: int              # int
     ActiveAreaFirstLine: int               # int
     ActiveAreaPixelsPerLine: int           # int
     ActiveAreaLinesPerFrame: int           # int
     BottomFieldFirstLine: int              # int
     PixelClockFreqInKiloHertz: int         # int
     ColorSpaceConvCoeffs0: int             # int
     ColorSpaceConversionCoefficients1: int # int
     ColorSpaceConversionCoefficients2: int # int
     ColorSpaceConversionCoefficients3: int # int
     ColorSpaceConversionCoefficients4: int # int
     ColorSpaceConversionCoefficients5: int # int
     ColorSpaceConversionCoefficients6: int # int
     ColorSpaceConversionCoefficients7: int # int
     ColorSpaceConversionCoefficients8: int # int
     OffsetRed: int                         # int
     OffsetGreen: int                       # int
     OffsetBlue: int                        # int
     IsVideo: int                           # int
     IsHighDefinitionVideo: int             # int
     FrameRate: float

class SourceConfigurationRead:
     VSyncConfiguration: SrcSyncConfigT
     HSyncConfiguration: SrcSyncConfigT
     TopFieldConfiguration: SrcSyncConfigT
     DownSampleConfiguration: SrcDownSampleConfigT
     IsThreeD: bool
     IsClockPolarityPositive: bool
     PixelFormat: SrcPixelFormatT
     IsExternalDataEnable: bool
     IsInterlaced: bool
     IsOffsetBinary: bool
     IsTopFieldInvertedAtScaler: bool
     TotalAreaPixelsPerLine: int            # int
     TotalAreaLinesPerFrame: int            # int
     ActiveAreaFirstPixel: int              # int
     ActiveAreaFirstLine: int               # int
     ActiveAreaPixelsPerLine: int           # int
     ActiveAreaLinesPerFrame: int           # int
     BottomFieldFirstLine: int              # int
     PixelClockFreqInKiloHertz: int         # int
     ColorSpaceConversionCoefficients0: int # int
     ColorSpaceConversionCoefficients1: int # int
     ColorSpaceConversionCoefficients2: int # int
     ColorSpaceConversionCoefficients3: int # int
     ColorSpaceConversionCoefficients4: int # int
     ColorSpaceConversionCoefficients5: int # int
     ColorSpaceConversionCoefficients6: int # int
     ColorSpaceConversionCoefficients7: int # int
     ColorSpaceConversionCoefficients8: int # int
     OffsetRed: int                         # int
     OffsetGreen: int                       # int
     OffsetBlue: int                        # int
     IsVideo: int                           # int
     IsHighDefinitionVideo: int             # int
     FrameRate: float

class KeystoneCorners:
     TopLeftX: int                          # int
     TopLeftY: int                          # int
     TopRightX: int                         # int
     TopRightY: int                         # int
     BottomLeftX: int                       # int
     BottomLeftY: int                       # int
     BottomRightX: int                      # int
     BottomRightY: int                      # int

class ImageAlgorithmEnable:
     ChromaTransientImprovementEnableBit: bool
     GammaCorrectionEnableBit: bool
     ColorCoordinateAdjustmentEnableBit: bool
     BrilliantColorEnableBit: bool
     WhitePointCorrectionEnableBit: bool
     DynamicBlackEnableBit: bool
     HdrEnableBit: bool

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

_readcommand = None
_writecommand = None

def DLP471TPEVMinit(readcommandcb, writecommandcb):
    global _readcommand
    global _writecommand
    _readcommand = readcommandcb
    _writecommand = writecommandcb

    global Summary
    Summary.CommInterface = "DLP471TPEVM"

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
        readbytes = _readcommand(14, writebytes, ProtocolData)
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
    "This command returns the flash device and manufacturer IDs. Only CFI compliant flash devices are supported. The system can have multiple flash devices. The command returns the info for the flash present at the given chip select. Note: Chip Select 0 Flash is required for system operation. Other Flash Chip Selects are technically optional but required for Splash Capture and Warp Operations."
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

def ReadProgrammableFlashSectorInformation():
    "This command returns the flash sector information read from CFI compliant flash devices. If the flash is non-CFI compliant, this command will fail. The sectors returned by this command are the only ones available for programming a flash image. The system is designed such that the flash image is in a contiguous memory space. If a system has multiple flash parts, then the software checks the size of the flash at ChipSelect 0. If this is equal to the maximum supported size (32MB), then a flash device at ChipSelect 1 (if present) will also be supported for flash programming. Similarly, if the size of flash devices at both ChipSelect 0 and 1 are 32MB, then a flash device at ChipSelect 2 (if present) will be supported for flash programming as well. The command appends the sector information for each part, which is supported for flash programming, and provides them as output."
    global Summary
    Summary.Command = "Read Programmable Flash Sector Information"
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
    "This command erases the sector of the flash where the given address falls in. This command is a flash update command, and requires flash operations to be unlocked using Unlock Flash for Update command. The sector address shall be specified as an offset from flash start address. For example in a flash device where all sectors are 64KB of size, sector addresses shall be specified as follows:<br> Sector 0 = 0 <br> Sector 1 = 0x10000 <br> Sector 2 = 0x20000 <br> and so on... <br>"
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
    "This command initializes flash read/write operation. This command shall be called before Flash Write command is sent.<BR> Note: For Flash Write, the Address and download size set up shall both be even."
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
    "This command is used to program data to flash. This command shall be called only after setting the start address and size using the Initialize Flash Read/Write Settings command. This command is a flash update command, and requires flash operations to be unlocked using Unlock Flash for Update command. <BR> Flash write commands can be chained till the initialized number of bytes are programmed. The bootloader will auto-increment the address and size for each command. Only the initialized number of bytes will be programmed even if more data is provided. <BR> It is important to send only even number of bytes per flash write command to ensure all bytes are written. This is done so that all flash writes are optimized as per the multi-word write supported by the flash device.<BR> This command supports variable sized payload."
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
    "This command is used to read data from flash. This command shall be called only after setting the start address and size using the Initialize Flash Read/Write Settings command. <BR> Flash read commands can be chained until the initialized number of bytes are returned. The bootloader will auto-increment the address and size for each command. Only the initialized number of bytes will be returned. Calling the function after returning requested data will return in command failure. This command supports variable sized response."
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
    "This command computes and returns the checksum starting at the given address for the specified number of bytes. Checksum is calculated as below: <BR> uint32 SimpleChecksum = 0; <BR> uint32 SumofSumChecksum = 0; <BR> uint08 *Addr = (uint08 *) StartAddress; <BR> <BR> while (NumBytes--) <BR> { <BR> SimpleChecksum += *Addr++; <BR> SumofSumChecksum += SimpleChecksum; <BR> } <BR>"
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

def WriteResetFlash(Chip):
    "This command resets the Flash device connected to the given chip select. Any partial commands given gets reset and the flash is put in read mode."
    global Summary
    Summary.Command = "Write Reset Flash"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 1;
    try:
        writebytes=list(struct.pack('B',39))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Chip)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteMemory(Address,  Value):
    "This command attempts a direct write of the given 32-bit value to the given 32-bit memory address. The memory address is not verified whether it is a valid location."
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
    "Writes a stream of words into the RAM memory (DRAM or IRAM) starting from the address specified. Performs no checks whether the specified memory address given is valid."
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
    "Reads a stream of words from memory starting from the address specified. Performs no checks whether the specified memory address given is valid."
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

def ReadSfgResolution():
    "Gets the resolution of the displayed SFG image."
    global Summary
    Summary.Command = "Read Sfg Resolution"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',25))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        HorizontalResolution = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        VerticalResolution = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, HorizontalResolution, VerticalResolution

def WriteTpgPredefinedPattern(PatternNumber):
    "This command will set one of the pre-defined test patterns stored in flash (configured using DLP Composer tool). The function selects a pattern to load from flash into the test pattern generator hardware. The information retrieved from the flash includes pattern definition, color definition, and the resolution. The pre-defined patterns are included in the flash configuration data. Set Display command must be called to switch the display mode from other modes to TPG prior to or after this command ."
    global Summary
    Summary.Command = "Write Tpg Predefined Pattern"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',20))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',PatternNumber)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadTpgPredefinedPattern():
    "Returns the current selection for pre-defined test patterns."
    global Summary
    Summary.Command = "Read Tpg Predefined Pattern"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',20))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        PatternNumber = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, PatternNumber

def WriteEnableThreeD(Enable3D):
    "Enables 3D functionality."
    global Summary
    Summary.Command = "Write Enable Three D"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',177))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(Enable3D), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadEnableThreeD():
    "Returns whether 3D is enabled or not."
    global Summary
    Summary.Command = "Read Enable Three D"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',177))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        Enable3D = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Enable3D

def WriteThreeDSourceConfiguration(ThreeDSourceConfiguration):
    ""
    global Summary
    Summary.Command = "Write Three D Source Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',178))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',ThreeDSourceConfiguration.Format.value)))
        writebytes.extend(list(struct.pack('B',ThreeDSourceConfiguration.LrReference.value)))
        writebytes.extend(list(struct.pack('B',ThreeDSourceConfiguration.FrameDominance.value)))
        writebytes.extend(list(struct.pack('B',ThreeDSourceConfiguration.LrEncoding.value)))
        writebytes.extend(list(struct.pack('B',ThreeDSourceConfiguration.TbReference.value)))
        writebytes.extend(list(struct.pack('B',ThreeDSourceConfiguration.OeReference.value)))
        writebytes.extend(list(struct.pack('B',ThreeDSourceConfiguration.NumActiveBlankLines)))
        writebytes.extend(list(struct.pack('B',ThreeDSourceConfiguration.NumberOfEncodedLines)))
        writebytes.extend(list(struct.pack('H',ThreeDSourceConfiguration.LeftEncodedLineLocation)))
        writebytes.extend(list(struct.pack('H',ThreeDSourceConfiguration.RightEncodedLineLocation)))
        writebytes.extend(list(struct.pack('B',ThreeDSourceConfiguration.BlankingColor.value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadThreeDSourceConfiguration():
    ""
    global Summary
    Summary.Command = "Read Three D Source Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',178))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(13, writebytes, ProtocolData)
        ThreeDSourceConfiguration.Format = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        ThreeDSourceConfiguration.LrReference = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        ThreeDSourceConfiguration.FrameDominance = struct.unpack_from ('B', bytearray(readbytes), 2)[0]
        ThreeDSourceConfiguration.LrEncoding = struct.unpack_from ('B', bytearray(readbytes), 3)[0]
        ThreeDSourceConfiguration.TbReference = struct.unpack_from ('B', bytearray(readbytes), 4)[0]
        ThreeDSourceConfiguration.OeReference = struct.unpack_from ('B', bytearray(readbytes), 5)[0]
        ThreeDSourceConfiguration.NumActiveBlankLines = struct.unpack_from ('B', bytearray(readbytes), 6)[0]
        ThreeDSourceConfiguration.NumberOfEncodedLines = struct.unpack_from ('B', bytearray(readbytes), 7)[0]
        ThreeDSourceConfiguration.LeftEncodedLineLocation = struct.unpack_from ('H', bytearray(readbytes), 8)[0]
        ThreeDSourceConfiguration.RightEncodedLineLocation = struct.unpack_from ('H', bytearray(readbytes), 10)[0]
        ThreeDSourceConfiguration.BlankingColor = struct.unpack_from ('B', bytearray(readbytes), 12)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ThreeDSourceConfiguration

def WriteLeftRightSignalPolarity(Invert):
    "This command inverts the L/R signal polarity."
    global Summary
    Summary.Command = "Write Left Right Signal Polarity"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',179))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(Invert), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadLeftRightSignalPolarity():
    "This command tells whether L/R signal polarity is inverted or not."
    global Summary
    Summary.Command = "Read Left Right Signal Polarity"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',179))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        Invert = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Invert

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
    "Returns the DMD information."
    global Summary
    Summary.Command = "Read Dmd Info"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(17, writebytes, ProtocolData)
        DmdId = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        FuseId = struct.unpack_from ('I', bytearray(readbytes), 4)[0]
        DmdName = str(bytearray(readbytes), encoding)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DmdId, FuseId, DmdName

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
        SystemStatus.Dlpa3005CommErr = getbits(1, 20);
        SystemStatus.UmcRefreshBwUnderflowErr = getbits(1, 21);
        SystemStatus.DmdInitErr = getbits(1, 22);
        SystemStatus.DmdPwrDownErr = getbits(1, 23);
        SystemStatus.SrcdefNotpresent = getbits(1, 24);
        SystemStatus.SeqbinNotpresent = getbits(1, 25);
        SystemStatus.ProductConfigurationFailed = getbits(1, 26);
        SystemStatus.TemporalDitherMaskNotLoading = getbits(1, 27);
        readdata = struct.unpack_from ('I', bytearray(readbytes), 8)[0]
        packerinit(readdata)
        SystemStatus.EepromInitFail = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SystemStatus

def ReadEepromDataPresent():
    "Reports which of the calibration data blocks are present in EEPROM. Use this command before sending EEPROM Invalidate command (0x0A)."
    global Summary
    Summary.Command = "Read Eeprom Data Present"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',7))
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
        writebytes=list(struct.pack('B',8))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('I',DelayInMilliseconds)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteEepromInvalidate(EepromInvalidate):
    "Invalidates the user settings portion of EEPROM data or calibration portion of EEPROM data or both as per input arguments and restarts the system. If none of the settings or calibration data is selected, then the command does nothing. Note: Chose valid flags as returned in Get EEPROM Data Present command."
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

def WriteSplashCapture():
    "Captures the current external image displayed on the screen and stores it into the Flash memory as a Splash image."
    global Summary
    Summary.Command = "Write Splash Capture"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',11))
        ProtocolData.OpcodeLength = 1;
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadSplashCaptureStatus():
    "Returns the current status of splash capture."
    global Summary
    Summary.Command = "Read Splash Capture Status"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',12))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(2, writebytes, ProtocolData)
        CaptureStateObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        CaptureCompletionPercentage = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SplashCaptureStateT(CaptureStateObj), CaptureCompletionPercentage

def WriteTerminateSplashCapture():
    "Terminates any ongoing Splash Capture"
    global Summary
    Summary.Command = "Write Terminate Splash Capture"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',13))
        ProtocolData.OpcodeLength = 1;
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteAutolockControl(AutolockControl):
    "This command provides user control to relock to a source or to start/stop autolock algorithm."
    global Summary
    Summary.Command = "Write Autolock Control"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',36))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',AutolockControl.value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteBlendMapGainValues(CompressionEnabled,  ColorChannelSelect,  TotalNumberOfCompressedValues,  Index,  GainValues):
    "This command takes input from the user of Gain values of control points as part of the Blend Map"
    global Summary
    Summary.Command = "Write Blend Map Gain Values"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',43))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(CompressionEnabled), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        writebytes.extend(list(struct.pack('B',ColorChannelSelect.value)))
        writebytes.extend(list(struct.pack('H',TotalNumberOfCompressedValues)))
        writebytes.extend(list(struct.pack('H',Index)))
        ********** Invalid Write Data Field Type - DLPComposer.Commands.Spec.ArrayType;
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadBlendMapGainValues(ColorChannelSelect,  Index,  NoOfValues):
    "This command reads from the blend map table already loaded using CMD_SetBlendMapGainValues command. N Blend map gain values (that does not exceed the command packet size) can be read at a time from anywhere within the table."
    global Summary
    Summary.Command = "Read Blend Map Gain Values"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',43))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',ColorChannelSelect.value)))
        writebytes.extend(list(struct.pack('H',Index)))
        writebytes.extend(list(struct.pack('H',NoOfValues)))
        readbytes = _readcommand(1, writebytes, ProtocolData)
        IsCompressionEnabled = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        ********** Invalid Write Data Field Type - DLPComposer.Commands.Spec.ArrayType;
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, IsCompressionEnabled, GainValues

def WriteApplyBlendMap(BlendMapUploadEnable):
    "This command passes the entire blend map to lower layer - API"
    global Summary
    Summary.Command = "Write Apply Blend Map"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',44))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(BlendMapUploadEnable), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteBlendMapOffsetValues(CompressionEnabled,  ColorChannelSelect,  TotalNumberOfCompressedValues,  Index,  OffsetValues):
    "This command takes input from the user of offset values of control points for the blend map"
    global Summary
    Summary.Command = "Write Blend Map Offset Values"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',45))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(CompressionEnabled), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        writebytes.extend(list(struct.pack('B',ColorChannelSelect.value)))
        writebytes.extend(list(struct.pack('H',TotalNumberOfCompressedValues)))
        writebytes.extend(list(struct.pack('H',Index)))
        ********** Invalid Write Data Field Type - DLPComposer.Commands.Spec.ArrayType;
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadBlendMapOffsetValues(ColorChannelSelect,  Index,  NoOfValues):
    "This command reads from the blend map compressed offset values already loaded using Set Blend Map Offset Values command. N Blend map offset values (that does not exceed the command packet size) can be read at a time from anywhere within the table."
    global Summary
    Summary.Command = "Read Blend Map Offset Values"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',45))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',ColorChannelSelect.value)))
        writebytes.extend(list(struct.pack('H',Index)))
        writebytes.extend(list(struct.pack('H',NoOfValues)))
        readbytes = _readcommand(1, writebytes, ProtocolData)
        IsCompressionEnabled = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        ********** Invalid Write Data Field Type - DLPComposer.Commands.Spec.ArrayType;
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, IsCompressionEnabled, OffsetValues

def WriteBlendMapControlPoints(HorizontalResolutionProjector,  VerticalResolutionProjector,  HorizontalCtrlPoints,  VerticalCtrlPoints):
    "This command takes input of the user defined control points location in horizontal and vertical direction as part of the Blend Map"
    global Summary
    Summary.Command = "Write Blend Map Control Points"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',46))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',HorizontalResolutionProjector)))
        writebytes.extend(list(struct.pack('H',VerticalResolutionProjector)))
        ********** Invalid Write Data Field Type - DLPComposer.Commands.Spec.ArrayType;
        ********** Invalid Write Data Field Type - DLPComposer.Commands.Spec.ArrayType;
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadBlendMapControlPoints():
    "This command gets the user defined blend map control points location stored in EEPROM."
    global Summary
    Summary.Command = "Read Blend Map Control Points"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',46))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(190, writebytes, ProtocolData)
        ********** Invalid Write Data Field Type - DLPComposer.Commands.Spec.ArrayType;
        ********** Invalid Write Data Field Type - DLPComposer.Commands.Spec.ArrayType;
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, HorizontalCtrlPoints, VerticalCtrlPoints

def WriteEnableEdgeBlending(EdgeBlendingEnable):
    "It enables or disables the Edge blending function"
    global Summary
    Summary.Command = "Write Enable Edge Blending"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',47))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(EdgeBlendingEnable), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadEnableEdgeBlending():
    "Returns whether the Edge blending function is enabled or not."
    global Summary
    Summary.Command = "Read Enable Edge Blending"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',47))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        EdgeBlendingEnable = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, EdgeBlendingEnable

def WriteEdgeBlendingSystemParams(NumProjectorsColumns,  NumProjectorsRows,  SelfProjectorColumn,  SelfProjectorRow,  WhiteBlackLevels):
    "This command sets the blending system parameters for semi-manual edge blending. This command does not change the state of the warping map or the blending map"
    global Summary
    Summary.Command = "Write Edge Blending System Params"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',61))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',NumProjectorsColumns)))
        writebytes.extend(list(struct.pack('H',NumProjectorsRows)))
        writebytes.extend(list(struct.pack('H',SelfProjectorColumn)))
        writebytes.extend(list(struct.pack('H',SelfProjectorRow)))
        ********** Invalid Write Data Field Type - DLPComposer.Commands.Spec.ArrayType;
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadEdgeBlendingSystemParams():
    "This command gets the blending system parameters for semi-manual edge blending"
    global Summary
    Summary.Command = "Read Edge Blending System Params"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',61))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(8, writebytes, ProtocolData)
        NumProjectorsColumns = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        NumProjectorsRows = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        SelfProjectorColumn = struct.unpack_from ('H', bytearray(readbytes), 4)[0]
        SelfProjectorRow = struct.unpack_from ('H', bytearray(readbytes), 6)[0]
        ********** Invalid Write Data Field Type - DLPComposer.Commands.Spec.ArrayType;
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, NumProjectorsColumns, NumProjectorsRows, SelfProjectorColumn, SelfProjectorRow, WhiteBlackLevels

def WriteEdgeBlendingConfiguration(OverlapHorizontal,  OverlapVertical,  GeometricAdjustmentType,  StorageOptions,  GeometryParams):
    "This command sets overlap and geometry parameters for semi-manual edge blending, creates and applies blending and warping maps for given blending inputs. It is necessary to call commands to enable manual warping and enable edge blending separately, for the results to take effect. Geometry parameters are dependent on geometric adjustment type. For no geometric correction, no parameters are used. For correction by keystone corners, the 8 parameters are the (x,y) coordinates (zero based) of the keystone corners in raster scan order: top-left, top-right, bottom-left, bottom-right."
    global Summary
    Summary.Command = "Write Edge Blending Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',62))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',OverlapHorizontal)))
        writebytes.extend(list(struct.pack('H',OverlapVertical)))
        writebytes.extend(list(struct.pack('B',GeometricAdjustmentType.value)))
        writebytes.extend(list(struct.pack('B',StorageOptions.value)))
        ********** Invalid Write Data Field Type - DLPComposer.Commands.Spec.ArrayType;
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadEdgeBlendingConfiguration():
    "This command gets geometry and overlap parameters for semi-manual edge blending. Geometry parameters are dependent on geometric adjustment type. For no geometric correction, no parameters are used. For correction by keystone corners, the 8 parameters are the (x,y) coordinates (zero based) of the keystone corners in raster scan order: top-left, top-right, bottom-left, bottom-right."
    global Summary
    Summary.Command = "Read Edge Blending Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',62))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(6, writebytes, ProtocolData)
        OverlapHorizontal = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        OverlapVertical = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        GeometricAdjustmentTypeObj = struct.unpack_from ('B', bytearray(readbytes), 4)[0]
        StorageOptionsObj = struct.unpack_from ('B', bytearray(readbytes), 5)[0]
        ********** Invalid Write Data Field Type - DLPComposer.Commands.Spec.ArrayType;
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, OverlapHorizontal, OverlapVertical, DispEdgeBlendGeometryModeT(GeometricAdjustmentTypeObj), DispfmtEdgeBlendStorageOptionsT(StorageOptionsObj), GeometryParams

def WriteXprCalibrationPatternDisplay():
    "This command loads a pre-defined XPR Calibration pattern as a splash image and displays it on the screen. A 64x64 pattern is repeated over a 3840x2160 display area."
    global Summary
    Summary.Command = "Write Xpr Calibration Pattern Display"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',171))
        ProtocolData.OpcodeLength = 1;
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteXpr4WayOrientation(XprOrientationNumber):
    "This command sets the orientation number of the actuator position (which gets stored in EEPROM) There are 24 possible options 0 - 23; use this commmand while performing XPR calibration using TI provided XPR calibration splash image.<BR> Note: Use Display Image Size command to make sure the display area is 3840x2160 If the reported display resolution is <= 1080p this command will not have any influence on the displayed image."
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
    "This command configures/sets up the Actuator Waveform Control(AWC) block. Here, AWCx can be AWC 0 or 1. Bytes 2-5 contains the XPR command data as mentioned in Byte 0. Byte 1 contains AWC channel number, possible values are 0 or 1.<BR><BR> **Fixed Output Enable**: Configures Actuator in fixed output mode.<BR> Byte    2: 0x00 - Disable 0x01 - Enable  <BR> Bytes 3-5: Reserved must be set to 0x000000<BR><BR> **Gain**: Set Waveform Generator DAC/PWM Gain.<BR> Byte    2: Range 0 - 255 format u1.7 (0 to 1.9921875) <BR> Bytes 3-5: Reserved must be set to 0x000000<BR><BR> **Subframe delay**: Subframe delay Bytes 2-5; Range 0 - 262143 and lsb = 133.333ns  <BR><BR> **Actuator Type (READ ONLY)**: Actuator type <BR> Byte    2: <BR>0x00 - NONE <BR> 0x01 - Optotune (XPR-25 Model) <BR> 0x80 - TI Actuator Interface (EEPROM) <BR> 0x81 - TI Actuator Interface (MCU) <BR> Bytes 3-5: Reserved must be set to 0x000000<BR><BR> **Output Enable/Disable**: Actuator output enable/disable <BR> Byte    2: 0x00 - Disable 0x01 - Enable  <BR> Bytes 3-5: Reserved must be set to 0x000000<BR><BR> Note: Both AWC0 and AWC1 disabled/enabled together <BR> **Clock Width**: Defines the high and low width for the output clock (the clock period will be 2*(ClkWidth+1)) <BR> 0 = 1 (Clock period is two clocks); lsb = 8.33ns <BR> Bytes 2-5: ClkWidth <BR> Example: ClkWidth = 0; will generate clock of 2*(0+1)*8.33 = 16.66ns <BR><BR> **Offset**: DAC/PWM Output Offset <BR> Byte    2: Range -128 - +127 format S7 (-128 to +127) <BR> Bytes 3-5: Reserved must be set to 0x000000<BR><BR> **Number of Segments**: Defines number of segments <BR> Byte    2: Range 2 - 255<BR> Bytes 3-5: Reserved must be set to 0x000000<BR><BR> **Segments Length**: Defines size of the segments <BR> Bytes 2-3: Range 19 - 4095<BR> Bytes 4-5: Reserved must be set to 0x0000<BR><BR> **Invert PWM A**: Applicable when AWC is configured to PWM type instead of DAC <BR> Byte    2: 0x00 - No inversion <BR> 0x01 - Inverted  <BR> Bytes 3-5: Reserved must be set to 0x000000<BR><BR> **Invert PWM B**: Applicable when AWC is configured to PWM type instead of DAC <BR> Byte    2: 0x00 - No inversion 0x01 - Inverted  <BR> Bytes 3-5: Reserved must be set to 0x000000<BR><BR> **Subframe Filter Value**: Sets Subframe Filter Value - defines the minimum time between Subframe edges. Edges closer than the set value will be filtered out <BR> Byte    2: 0 = Filter disabled, >0 = Filter time will be Val x 60us, Range: 0 - 255 <BR> Bytes 3-5: Reserved must be set to 0x000000<BR><BR> **Subframe Watch Dog**: Defines the maximum time between Subframe edges; if timer expires, then the WG will automatically output the Fixed Output value, and the normal output will resume on the next subframe edge.<BR> Bytes 2-3: 0 = Subframe watchdog disabled, >0 = Watchdog time will be Time x 60us, Range: Range: 0 - 1023 <BR> Bytes 4-5: Reserved must be set to 0x0000<BR><BR> **Fixed Output Value** : Defines the value to be output on DAC/PWM when fixed output mode is selected.<BR> Byte    2: Value to be output on DAC/PWM, Range -128 to 127 Bytes 3-5: Reserved must be set to 0x000000<BR><BR> **Note**: To use **Subframe Filter Value** and **Subframe Watch Dog** care must be taken to set a value which aproximately 10% more than 2x of the operating frequency. <BR> For example - 4K @ 60Hz, the value can be set as (1/(60*2))*1.10*10^6 = 9166us."
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
    "This command gets the parameter set to the AWC waveform generator.<BR> Note: This command is supposed to be used only during the normal operating mode and not during the standby state."
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

def WriteDbBorderConfiguration(Top,  Bottom,  Left,  Right):
    "This command configures area of the DynamicBlack border region for the border exclusion function. The border exclusion function allows the user to reduce the letterbox (black border) effect on a primarily bright image where letterbox area reduces the overall scene brightness for the algorithm. It also helps the algorithm better handle images with bright subtitles where the subtitles increase the overall scene brightness. This command will also be used in a multi-controller configuration to exclude any image overlap required for other image processing algorithms."
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
    "This Command returns the border region area for the DynamicBlack border exclusion function."
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
    "Sets weight value of the DynamicBlack border region for the border exclusion function"
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
    "This command returns currently configured number of steps to allow the DynamicBlack aperture to move."
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
    "This command controls the DynamicBlack gain value. Typical value range is 1.0 to 8.0. Manual Mode needs to be enabled to set the gain as it will override the gain value that is calculated every frame."
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
    "This command gets the DynamicBlack gain value. Typical value range is 1.0 to 8.0"
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

def ReadDbHistogram():
    "This command returns the start address of the DynamicBlack(DB) histogram data. The histogram contains scene brightness data from the previous frame. The DB histogram contains 34 bins measuring non-overlapping intensity ranges in the displayed image. The value of each bin equals the number of pixels within the bin's intensity range. Each pixel's intensity is calculated as the maximum of its red, green, and blue values. In other words, pixel intensity = MAX( R, G, B ). Each pixel has a format of unsigned 8.8, making 16 bit values. Bins 32 and 33 are special bins that represent pixels that have values of exactly zero and only fractional values respectively. This function can be used independently of aperture control for image improvement in dark scenes."
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

def ReadCurrentLedColorPoint():
    "Gets x,y coordinates of system's current white point. WPC should be initialized and calibration data should be set before calling this command."
    global Summary
    Summary.Command = "Read Current Led Color Point"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',196))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(8, writebytes, ProtocolData)
        ChromaticX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 0)[0], 32768)
        ChromaticY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 2)[0], 32768)
        LuminanceY = struct.unpack_from ('I', bytearray(readbytes), 4)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ChromaticX, ChromaticY, LuminanceY

def WriteWpcOptimalDutyCycle():
    "Searches available duty cycles and sets the optimal one for corerct LED white point. Sensor calibration Data should be set before using this command. @retval PASS Successful @retval WPC_ERR_CALIBRATION_DATA_NOT_SET WPC calibration data not set"
    global Summary
    Summary.Command = "Write Wpc Optimal Duty Cycle"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',197))
        ProtocolData.OpcodeLength = 1;
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadWpcOptimalDutyCycle():
    "Gets Ideal Duty Cycle for Current Target Color Point and the closest Duty Cycle Avaialable. Sensor calibration Data should be set before using this command."
    global Summary
    Summary.Command = "Read Wpc Optimal Duty Cycle"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',197))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(12, writebytes, ProtocolData)
        WpcOptimalDutyCycle.RedIdealDutyCycle = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 0)[0], 256)
        WpcOptimalDutyCycle.GreenIdealDutyCycle = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 2)[0], 256)
        WpcOptimalDutyCycle.BlueIdealDutyCycle = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 4)[0], 256)
        WpcOptimalDutyCycle.RedOptimalDutyCycle = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 6)[0], 256)
        WpcOptimalDutyCycle.GreenOptimalDutyCycle = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 8)[0], 256)
        WpcOptimalDutyCycle.BlueOptimalDutyCycle = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 10)[0], 256)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, WpcOptimalDutyCycle

def WriteWpcCalibrationData(LedColor,  ChromaticX,  ChromaticY,  LuminanceY):
    "Set WPC sensor calibration data through this command. WPC_Init() should complete succesfully before invoking this command."
    global Summary
    Summary.Command = "Write Wpc Calibration Data"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',198))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',LedColor.value)))
        writebytes.extend(list(struct.pack('H',ChromaticX)))
        writebytes.extend(list(struct.pack('H',ChromaticY)))
        writebytes.extend(list(struct.pack('I',LuminanceY)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadWpcCalibrationData(LedColor):
    "Gets WPC sensor calibration data through this command"
    global Summary
    Summary.Command = "Read Wpc Calibration Data"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',198))
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

def ReadWpcSensorOutput():
    "Returns Output of Integrating Sensor for Red, Blue and Green"
    global Summary
    Summary.Command = "Read Wpc Sensor Output"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',205))
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

def WriteWpcCalibrationStructureOverride(WpcCalibrationStructureOverride):
    "Set the entire WPC sensor calibration data structure through this command.  WPC_Init() should complete succesfully before invoking this command."
    global Summary
    Summary.Command = "Write Wpc Calibration Structure Override"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',210))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',WpcCalibrationStructureOverride.LedColor.value)))
        writebytes.extend(list(struct.pack('H',WpcCalibrationStructureOverride.ChromaticX)))
        writebytes.extend(list(struct.pack('H',WpcCalibrationStructureOverride.ChromaticY)))
        writebytes.extend(list(struct.pack('I',WpcCalibrationStructureOverride.LuminanceY)))
        writebytes.extend(list(struct.pack('I',WpcCalibrationStructureOverride.RedSensorOutput)))
        writebytes.extend(list(struct.pack('I',WpcCalibrationStructureOverride.GreenSensorOutput)))
        writebytes.extend(list(struct.pack('I',WpcCalibrationStructureOverride.BlueSensorOutput)))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(WpcCalibrationStructureOverride.DutyCycle,256)))))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

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

def WriteEnableUsbDebugLog(Enable):
    "Enables or disables the USB logging of messages. When USB logging is enabled, UART logging is stopped."
    global Summary
    Summary.Command = "Write Enable Usb Debug Log"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',225))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Enable)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

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
    "This function reads data from EEPROM connected to the Controller which has settings and calibration data. Note: EEPROM data can be read without unlocking."
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

def WriteDlpa3005Register(RegisterAddress,  RegisterValue):
    "Command that writes specified value to the specified register address. Refer to DLPA30005 datasheet for more information (https://www.ti.com/product/DLPA3005)"
    global Summary
    Summary.Command = "Write Dlpa 3005 Register"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',227))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',RegisterAddress)))
        writebytes.extend(list(struct.pack('B',RegisterValue)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDlpa3005Register(RegisterAddress):
    "Returns specified register value from DLPA3005. Refer to DLPA30005 datasheet for more information (https://www.ti.com/product/DLPA3005)"
    global Summary
    Summary.Command = "Read Dlpa 3005 Register"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',227))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',RegisterAddress)))
        readbytes = _readcommand(1, writebytes, ProtocolData)
        RegisterValue = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, RegisterValue

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

def WriteDmdTrueGlobalReset(GlobalResetEnable):
    "The TrueGlobalMode should be set to TRUE only during factory/assembly operation."
    global Summary
    Summary.Command = "Write Dmd True Global Reset"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',235))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(GlobalResetEnable), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDmdTrueGlobalReset():
    ""
    global Summary
    Summary.Command = "Read Dmd True Global Reset"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',235))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        GlobalResetEnable = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, GlobalResetEnable

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
    "Prints(on UART) information of all tasks defined/created with RTOS."
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
        Resource.GroupEventsCurrentCount = struct.unpack_from ('B', bytearray(readbytes), 8)[0]
        Resource.MailboxCurrentCount = struct.unpack_from ('B', bytearray(readbytes), 9)[0]
        Resource.MemoryPoolsCurrentCount = struct.unpack_from ('B', bytearray(readbytes), 10)[0]
        Resource.SemaphoreCurrentCount = struct.unpack_from ('B', bytearray(readbytes), 11)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Resource

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
    "Displays the specified source.<BR> Note: If Display External projection mode is selected and if there is no source present it will show Splash or Solid Field depending on the default settings in the system."
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

def WriteEnableLowLatencyMode(Enable):
    "Enables or disables the Low latency mode of operation in which processing delay (from the input source to the frame sent to DMD) by the Controller is limited to a maximum of one and a half frame delays."
    global Summary
    Summary.Command = "Write Enable Low Latency Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',18))
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

def ReadEnableLowLatencyMode():
    "Returns whether low latency mode is enabled or not."
    global Summary
    Summary.Command = "Read Enable Low Latency Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',18))
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

def WriteTpgBorder(Width,  BorderColorRed,  BorderColorGreen,  BorderColorBlue):
    "Draws a border around the test pattern of given width and color.<BR> Note: To be used only when the Display is set as Test Pattern."
    global Summary
    Summary.Command = "Write Tpg Border"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',21))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Width)))
        writebytes.extend(list(struct.pack('H',BorderColorRed)))
        writebytes.extend(list(struct.pack('H',BorderColorGreen)))
        writebytes.extend(list(struct.pack('H',BorderColorBlue)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadTpgBorder():
    "Returns Width in number of pixels and Color of Border for a test Pattern."
    global Summary
    Summary.Command = "Read Tpg Border"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',21))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(7, writebytes, ProtocolData)
        Width = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        BorderColorRed = struct.unpack_from ('H', bytearray(readbytes), 1)[0]
        BorderColorGreen = struct.unpack_from ('H', bytearray(readbytes), 3)[0]
        BorderColorBlue = struct.unpack_from ('H', bytearray(readbytes), 5)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Width, BorderColorRed, BorderColorGreen, BorderColorBlue

def WriteTpgResolution(HorizontalResolution,  VerticalResolution):
    "Sets horizontal and vertical resolution in number of pixels for current test pattern."
    global Summary
    Summary.Command = "Write Tpg Resolution"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',22))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',HorizontalResolution)))
        writebytes.extend(list(struct.pack('H',VerticalResolution)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadTpgResolution():
    "Returns horizontal and vertical resolution in number of pixels for current test pattern."
    global Summary
    Summary.Command = "Read Tpg Resolution"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',22))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        HorizontalResolution = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        VerticalResolution = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, HorizontalResolution, VerticalResolution

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
    "Configures the solid color to be displayed when display is set to solid field generator (SFG). This command only sets the SFG color and does NOT display it. In order to display the SFG, Display needs to be set with SFG as source(Use Set Display command for this.)"
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
    "Command to set the color to be  used in curtain mode. Use Set Display command to switch to curtain mode."
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
    "Sets the index of the splash image to be loaded and displayed. If already in Splash mode the requested splash image is displayed.<BR>"
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
    "Flips the data output to the display vertically or horizontally. This feature is provided to support use cases like ceiling mount, rear projection etc."
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
    "Returns whether image flipping is enabled."
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
    "It enables or disables display freeze which freezes the current frame being displayed on the screen.<BR> Caution: Set Curtain or any operation that requires curtain will override Freeze and frozen image on the wall will be lost.<BR> The following operations require curtain (and will override Freeze): <BR> Source Type Switch (Standard - XPR - 3D) <BR> Source Type Switch (interlaced - non-interlaced) <BR> Switch to Splash Display <BR> Splash Capture <BR> Low Latency Mode Switch <BR> Source Relocking <BR> Switch to Stand-By/Low-Power mode"
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
    "Returns whether the current display is frozen."
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

def WriteKeystoneAngles(Pitch,  Yaw,  Roll):
    "Configures the Keystone correction when the pitch, yaw, roll, throw ratio and vertical offset of corrected image are known.<BR> Keystone correction is used to remove the distortion caused when the projector is not orthogonal to the projection surface (screen).<BR> Keystone feature will be automatically enabled when this command is executed.<BR> Note: The actual range of these parameters depends on the light engine (projection optics); the range of Pitch, Yaw and Roll is derived from optical engine Vertical offset and Throw Ratio.(Maximum range: -40 to +40 degrees)"
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
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(Roll,256)))))
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
        readbytes = _readcommand(6, writebytes, ProtocolData)
        Pitch = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 0)[0], 256)
        Yaw = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 2)[0], 256)
        Roll = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 4)[0], 256)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Pitch, Yaw, Roll

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

def WriteEnableAnamorphicScaling(Enable):
    "Enables or disables the anamorphic scaling"
    global Summary
    Summary.Command = "Write Enable Anamorphic Scaling"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',32))
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

def ReadEnableAnamorphicScaling():
    "Returns whether anamorphic scaling is enabled or not."
    global Summary
    Summary.Command = "Read Enable Anamorphic Scaling"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',32))
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

def WriteDisplayImageSize(DisplayImageSize):
    "Configures the cropping of input image and resizing of image that is displayed. Cropped area can be equal to or less than the input image size. The display area has has to be within DMD effective number of pixels and lines. Note: 1. Cropped Area and Display Area parameters are valid only when image size type is set to Manual. 2. For TPG, SFG and Splash, Cropped Area parameter is ignored. For those sources, cropped area is automatically set as explained below: <BR> a. For TPG, cropped area is set to TPG resolution. <BR> b. For Splash, cropped area is set to Splash image size. <BR> c. For SFG, cropped area is set to SFG resolution which is equal to source area of last stable external source or TPG. <BR>"
    global Summary
    Summary.Command = "Write Display Image Size"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',33))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',DisplayImageSize.ImageSizeType.value)))
        writebytes.extend(list(struct.pack('H',DisplayImageSize.CroppedAreaFirstPixel)))
        writebytes.extend(list(struct.pack('H',DisplayImageSize.CroppedAreaFirstLine)))
        writebytes.extend(list(struct.pack('H',DisplayImageSize.CroppedAreaPixelsPerLine)))
        writebytes.extend(list(struct.pack('H',DisplayImageSize.CroppedAreaLinesPerFrame)))
        writebytes.extend(list(struct.pack('H',DisplayImageSize.DisplayAreaFirstPixel)))
        writebytes.extend(list(struct.pack('H',DisplayImageSize.DisplayAreaFirstLine)))
        writebytes.extend(list(struct.pack('H',DisplayImageSize.DisplayAreaPixelsPerLine)))
        writebytes.extend(list(struct.pack('H',DisplayImageSize.DisplayAreaLinesPerFrame)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDisplayImageSize():
    "Returns current image size, cropping and display settings."
    global Summary
    Summary.Command = "Read Display Image Size"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',33))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(17, writebytes, ProtocolData)
        DisplayImageSize.ImageSizeType = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        DisplayImageSize.CroppedAreaFirstPixel = struct.unpack_from ('H', bytearray(readbytes), 1)[0]
        DisplayImageSize.CroppedAreaFirstLine = struct.unpack_from ('H', bytearray(readbytes), 3)[0]
        DisplayImageSize.CroppedAreaPixelsPerLine = struct.unpack_from ('H', bytearray(readbytes), 5)[0]
        DisplayImageSize.CroppedAreaLinesPerFrame = struct.unpack_from ('H', bytearray(readbytes), 7)[0]
        DisplayImageSize.DisplayAreaFirstPixel = struct.unpack_from ('H', bytearray(readbytes), 9)[0]
        DisplayImageSize.DisplayAreaFirstLine = struct.unpack_from ('H', bytearray(readbytes), 11)[0]
        DisplayImageSize.DisplayAreaPixelsPerLine = struct.unpack_from ('H', bytearray(readbytes), 13)[0]
        DisplayImageSize.DisplayAreaLinesPerFrame = struct.unpack_from ('H', bytearray(readbytes), 15)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DisplayImageSize

def WriteSourceConfiguration(SourceConfiguration):
    "Configures the characteristics of the source on the Current active port. Note: 1. After sending CMD_SetSourceConfiguration command, CMD_SetDisplayImageSize command must be sent for the changes to take effect. 2. CSC will take effect only after sending the CMD_SetDisplayImageSize command. 3. CMD_SetSourceConfiguration command should not be used when the Display is set as TPG."
    global Summary
    Summary.Command = "Write Source Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',34))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',SourceConfiguration.VSyncConfiguration.value)))
        writebytes.extend(list(struct.pack('B',SourceConfiguration.HSyncConfiguration.value)))
        writebytes.extend(list(struct.pack('B',SourceConfiguration.TopFieldConfiguration.value)))
        writebytes.extend(list(struct.pack('B',SourceConfiguration.DownSampleConfiguration.value)))
        packerinit()
        value = setbits(int(SourceConfiguration.IsThreeD), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(int(SourceConfiguration.IsClockPolarityPositive), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        writebytes.extend(list(struct.pack('B',SourceConfiguration.PixelFormat.value)))
        packerinit()
        value = setbits(int(SourceConfiguration.IsExternalDataEnable), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(int(SourceConfiguration.IsInterlaced), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(int(SourceConfiguration.IsOffsetBinary), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(int(SourceConfiguration.IsTopFieldInvertedAtScaler), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        writebytes.extend(list(struct.pack('H',SourceConfiguration.TotalAreaPixelsPerLine)))
        writebytes.extend(list(struct.pack('H',SourceConfiguration.TotalAreaLinesPerFrame)))
        writebytes.extend(list(struct.pack('H',SourceConfiguration.ActiveAreaFirstPixel)))
        writebytes.extend(list(struct.pack('H',SourceConfiguration.ActiveAreaFirstLine)))
        writebytes.extend(list(struct.pack('H',SourceConfiguration.ActiveAreaPixelsPerLine)))
        writebytes.extend(list(struct.pack('H',SourceConfiguration.ActiveAreaLinesPerFrame)))
        writebytes.extend(list(struct.pack('H',SourceConfiguration.BottomFieldFirstLine)))
        writebytes.extend(list(struct.pack('I',SourceConfiguration.PixelClockFreqInKiloHertz)))
        writebytes.extend(list(struct.pack('H',SourceConfiguration.ColorSpaceConvCoeffs0)))
        writebytes.extend(list(struct.pack('H',SourceConfiguration.ColorSpaceConversionCoefficients1)))
        writebytes.extend(list(struct.pack('H',SourceConfiguration.ColorSpaceConversionCoefficients2)))
        writebytes.extend(list(struct.pack('H',SourceConfiguration.ColorSpaceConversionCoefficients3)))
        writebytes.extend(list(struct.pack('H',SourceConfiguration.ColorSpaceConversionCoefficients4)))
        writebytes.extend(list(struct.pack('H',SourceConfiguration.ColorSpaceConversionCoefficients5)))
        writebytes.extend(list(struct.pack('H',SourceConfiguration.ColorSpaceConversionCoefficients6)))
        writebytes.extend(list(struct.pack('H',SourceConfiguration.ColorSpaceConversionCoefficients7)))
        writebytes.extend(list(struct.pack('H',SourceConfiguration.ColorSpaceConversionCoefficients8)))
        writebytes.extend(list(struct.pack('H',SourceConfiguration.OffsetRed)))
        writebytes.extend(list(struct.pack('H',SourceConfiguration.OffsetGreen)))
        writebytes.extend(list(struct.pack('H',SourceConfiguration.OffsetBlue)))
        writebytes.extend(list(struct.pack('B',SourceConfiguration.IsVideo)))
        writebytes.extend(list(struct.pack('B',SourceConfiguration.IsHighDefinitionVideo)))
        writebytes.extend(list(struct.pack('I',int(convertfloattofixed(SourceConfiguration.FrameRate,65536)))))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadSourceConfiguration():
    "Retrieves the source characteristics for the current active port."
    global Summary
    Summary.Command = "Read Source Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',34))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(59, writebytes, ProtocolData)
        SourceConfiguration.VSyncConfiguration = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        SourceConfiguration.HSyncConfiguration = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        SourceConfiguration.TopFieldConfiguration = struct.unpack_from ('B', bytearray(readbytes), 2)[0]
        SourceConfiguration.DownSampleConfiguration = struct.unpack_from ('B', bytearray(readbytes), 3)[0]
        readdata = struct.unpack_from ('B', bytearray(readbytes), 4)[0]
        packerinit(readdata)
        SourceConfiguration.IsThreeD = getbits(1, 0);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 5)[0]
        packerinit(readdata)
        SourceConfiguration.IsClockPolarityPositive = getbits(1, 0);
        SourceConfiguration.PixelFormat = struct.unpack_from ('B', bytearray(readbytes), 6)[0]
        readdata = struct.unpack_from ('B', bytearray(readbytes), 7)[0]
        packerinit(readdata)
        SourceConfiguration.IsExternalDataEnable = getbits(1, 0);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 8)[0]
        packerinit(readdata)
        SourceConfiguration.IsInterlaced = getbits(1, 0);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 9)[0]
        packerinit(readdata)
        SourceConfiguration.IsOffsetBinary = getbits(1, 0);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 10)[0]
        packerinit(readdata)
        SourceConfiguration.IsTopFieldInvertedAtScaler = getbits(1, 0);
        SourceConfiguration.TotalAreaPixelsPerLine = struct.unpack_from ('H', bytearray(readbytes), 11)[0]
        SourceConfiguration.TotalAreaLinesPerFrame = struct.unpack_from ('H', bytearray(readbytes), 13)[0]
        SourceConfiguration.ActiveAreaFirstPixel = struct.unpack_from ('H', bytearray(readbytes), 15)[0]
        SourceConfiguration.ActiveAreaFirstLine = struct.unpack_from ('H', bytearray(readbytes), 17)[0]
        SourceConfiguration.ActiveAreaPixelsPerLine = struct.unpack_from ('H', bytearray(readbytes), 19)[0]
        SourceConfiguration.ActiveAreaLinesPerFrame = struct.unpack_from ('H', bytearray(readbytes), 21)[0]
        SourceConfiguration.BottomFieldFirstLine = struct.unpack_from ('H', bytearray(readbytes), 23)[0]
        SourceConfiguration.PixelClockFreqInKiloHertz = struct.unpack_from ('I', bytearray(readbytes), 25)[0]
        SourceConfiguration.ColorSpaceConversionCoefficients0 = struct.unpack_from ('H', bytearray(readbytes), 29)[0]
        SourceConfiguration.ColorSpaceConversionCoefficients1 = struct.unpack_from ('H', bytearray(readbytes), 31)[0]
        SourceConfiguration.ColorSpaceConversionCoefficients2 = struct.unpack_from ('H', bytearray(readbytes), 33)[0]
        SourceConfiguration.ColorSpaceConversionCoefficients3 = struct.unpack_from ('H', bytearray(readbytes), 35)[0]
        SourceConfiguration.ColorSpaceConversionCoefficients4 = struct.unpack_from ('H', bytearray(readbytes), 37)[0]
        SourceConfiguration.ColorSpaceConversionCoefficients5 = struct.unpack_from ('H', bytearray(readbytes), 39)[0]
        SourceConfiguration.ColorSpaceConversionCoefficients6 = struct.unpack_from ('H', bytearray(readbytes), 41)[0]
        SourceConfiguration.ColorSpaceConversionCoefficients7 = struct.unpack_from ('H', bytearray(readbytes), 43)[0]
        SourceConfiguration.ColorSpaceConversionCoefficients8 = struct.unpack_from ('H', bytearray(readbytes), 45)[0]
        SourceConfiguration.OffsetRed = struct.unpack_from ('H', bytearray(readbytes), 47)[0]
        SourceConfiguration.OffsetGreen = struct.unpack_from ('H', bytearray(readbytes), 49)[0]
        SourceConfiguration.OffsetBlue = struct.unpack_from ('H', bytearray(readbytes), 51)[0]
        SourceConfiguration.IsVideo = struct.unpack_from ('B', bytearray(readbytes), 53)[0]
        SourceConfiguration.IsHighDefinitionVideo = struct.unpack_from ('B', bytearray(readbytes), 54)[0]
        SourceConfiguration.FrameRate = convertfixedtofloat(struct.unpack_from ('I', bytearray(readbytes), 55)[0], 65536)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SourceConfiguration

def ReadDatapathScanStatus():
    "Returns Current status of source detection."
    global Summary
    Summary.Command = "Read Datapath Scan Status"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',37))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(2, writebytes, ProtocolData)
        ScanStatusObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        DatapathStateObj = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DpScanStatus(ScanStatusObj), DpState(DatapathStateObj)

def ReadFrameRateParms():
    "Returns current Input Frame Rate, Output Frame rate anf FRC mode"
    global Summary
    Summary.Command = "Read Frame Rate Parms"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',38))
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

def WriteVboConfiguration(DataMapMode,  ByteMode,  NumberOfLanes,  EnablePixelRepeat):
    "Configures the characteristics of the Vx1 source."
    global Summary
    Summary.Command = "Write Vbo Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',48))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',DataMapMode.value)))
        writebytes.extend(list(struct.pack('B',ByteMode.value)))
        writebytes.extend(list(struct.pack('B',NumberOfLanes)))
        packerinit()
        value = setbits(int(EnablePixelRepeat), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadVboConfiguration():
    "Retruns the characteristics of the Vx1 source."
    global Summary
    Summary.Command = "Read Vbo Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',48))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        DataMapModeObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        ByteModeObj = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        NumberOfLanes = struct.unpack_from ('B', bytearray(readbytes), 2)[0]
        readdata = struct.unpack_from ('B', bytearray(readbytes), 3)[0]
        packerinit(readdata)
        EnablePixelRepeat = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SrcVboDataMapModeT(DataMapModeObj), SrcVboByteModeT(ByteModeObj), NumberOfLanes, EnablePixelRepeat

def WriteKeystoneCorners(KeystoneCorners):
    "Configures the 2D Keystone correction when the corners of the corrected image are known. Keystone correction is used to remove the distortion caused when the projector is not orthogonal to the projection surface (screen). For the effects to take place, the Keystone feature has to be enabled."
    global Summary
    Summary.Command = "Write Keystone Corners"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',58))
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
        writebytes=list(struct.pack('B',58))
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

def WriteWarpTimingValidationEnableAdjustWrp(Enable):
    "This commands sets whether automatic warp geometry adjustment should be allowed or not."
    global Summary
    Summary.Command = "Write Warp Timing Validation Enable Adjust Wrp"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',59))
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

def ReadWarpTimingValidationEnableAdjustWrp():
    "Returns whether Automatic Warp Adjustment is enabled or not."
    global Summary
    Summary.Command = "Read Warp Timing Validation Enable Adjust Wrp"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',59))
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

def ReadIsWarpGeometryModified():
    "Returns whether the Warp geomtery got modified or not."
    global Summary
    Summary.Command = "Read Is Warp Geometry Modified"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',60))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        State = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, State

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

def WriteDlpa3005IlluminationCurrent(DriveLevelRed,  DriveLevelGreen,  DriveLevelBlue):
    "Sets DLPA3005 Drive Current Levels input as 10-bit DriveLevel per LED in the range 0 - 874. Command should not be used if Dynamic Black or White Point Correction is enabled <BR> Current output in Amps is calculated as described below. <BR> OutputCurrent = ((DriveLevel + 1)/1024)*((0.15/0.004)) Amps <BR> Example: For DriveLevel = 874; OutputCurrent = 32.04345703Amps <BR>"
    global Summary
    Summary.Command = "Write Dlpa 3005 Illumination Current"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',132))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',DriveLevelRed)))
        writebytes.extend(list(struct.pack('H',DriveLevelGreen)))
        writebytes.extend(list(struct.pack('H',DriveLevelBlue)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDlpa3005IlluminationCurrent():
    "Gets DLPA3005 Drive Current Levels."
    global Summary
    Summary.Command = "Read Dlpa 3005 Illumination Current"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',132))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(6, writebytes, ProtocolData)
        DriveLevelRed = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        DriveLevelGreen = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        DriveLevelBlue = struct.unpack_from ('H', bytearray(readbytes), 4)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DriveLevelRed, DriveLevelGreen, DriveLevelBlue

def WriteImageAlgorithmEnable(ImageAlgorithmEnable):
    "Sets enable flag for all Image Algorithms.<BR> 0 = Disable <BR> 1 = Enable  <BR> **Chroma Transient Improvement** : <BR> This function enables/disables the Chroma Transient Improvement (CTI) function which filters the 4:4:4 sampled, chrominance (Cr and Cb) data on the B and C data channels. The chroma transient functions performs band pass filtering (supports two center frequencies) and median filtering for ringing minimization. It performs limiting and coring functions for the filtered output. <BR> **Gamma Correction** : <BR> This function enables/disables the Gamma Correction function which implements the removal of gamma transfer function applied at the source, via table lookup process called de-gamma. When enabled, perform de-gamma translation of the 10-bit RGB input to the common 12-bit floating point (S0M8E4) RGB output. When disabled, the full 10 bits of each data input to the Gamma Correction function are zero padded and MSB-aligned to 12-bits and passed through unmodified.<BR> **Color Coordinate Adjustment** : <BR> This function enables/disables the Spatially Adaptive Seven Primaries Color Correction Function Enable. When Disable forces 3x3 CSC (Color Space Conversion) with identity. <BR> **Brilliant Color** : <BR> This function enables/disables the BrilliantColor technology, Brilliant Color uses up to five colors, instead of just the three primary colors, red, green and blue, to improve color accuracy and brightens of secondary colors. This results in a new level of color performance that increases the brightness of the colors. <BR> **White Point Correction** : <BR> This function enables/disables the White Point Correction, typically used on LED type illumination systems. Sometimes due to increase in LED operating temperature or LED aging the LEDs output wavelentgh drifts, therefore white point of the system shifts. This algorithm using active light sensor feedback and factory calibrated values help maintaing white point of the system. <BR> **Dynamic Black** : <BR> Dynamic Black (DB) is an algorithm that reduces the amount of light reaching the projection path by means of LED output power through current control and compensates for reduced light by gaining up the RGB signals. <BR> **HDR** : <BR> High Dynamic Range (HDR) is an algorithm that maps wider brightness and color range of HDR source to the projector display range. HDR is affected by several factors such as illimuniation characterstics, duty cycle distribution and current running sequence. A valid HDR source should be set by HDR_SetHdrSourceConfiguration() before enabling HDR processing.<BR> Note: **Chroma Transient Improvement** is applicable to Analog SDTV sources only. DLPC654x controller doesn't support Analog sources. Even if enabled on DLPC65x controller, there is no changes in the displayed image when enabled."
    global Summary
    Summary.Command = "Write Image Algorithm Enable"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',64))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(ImageAlgorithmEnable.ChromaTransientImprovementEnableBit), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(int(ImageAlgorithmEnable.GammaCorrectionEnableBit), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(int(ImageAlgorithmEnable.ColorCoordinateAdjustmentEnableBit), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(int(ImageAlgorithmEnable.BrilliantColorEnableBit), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(int(ImageAlgorithmEnable.WhitePointCorrectionEnableBit), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(int(ImageAlgorithmEnable.DynamicBlackEnableBit), 1, 0)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(int(ImageAlgorithmEnable.HdrEnableBit), 1, 0)
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
        readbytes = _readcommand(7, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        ImageAlgorithmEnable.ChromaTransientImprovementEnableBit = getbits(1, 0);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        packerinit(readdata)
        ImageAlgorithmEnable.GammaCorrectionEnableBit = getbits(1, 0);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 2)[0]
        packerinit(readdata)
        ImageAlgorithmEnable.ColorCoordinateAdjustmentEnableBit = getbits(1, 0);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 3)[0]
        packerinit(readdata)
        ImageAlgorithmEnable.BrilliantColorEnableBit = getbits(1, 0);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 4)[0]
        packerinit(readdata)
        ImageAlgorithmEnable.WhitePointCorrectionEnableBit = getbits(1, 0);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 5)[0]
        packerinit(readdata)
        ImageAlgorithmEnable.DynamicBlackEnableBit = getbits(1, 0);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 6)[0]
        packerinit(readdata)
        ImageAlgorithmEnable.HdrEnableBit = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ImageAlgorithmEnable

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

def WriteImageRgbOffset(RedOffset,  GreenOffset,  BlueOffset):
    "Offsets the levels of the RGB channels at a point in the data path after the following image processing functions have been applied - source offset,  contrast, RGB Gain, brightness and color space conversion (including hue and color adjustment)."
    global Summary
    Summary.Command = "Write Image Rgb Offset"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',69))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(RedOffset,4)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(GreenOffset,4)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(BlueOffset,4)))))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadImageRgbOffset():
    "Returns Red, Green and Blue channel offset settings."
    global Summary
    Summary.Command = "Read Image Rgb Offset"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',69))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(6, writebytes, ProtocolData)
        RedOffset = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 0)[0], 4)
        GreenOffset = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 2)[0], 4)
        BlueOffset = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 4)[0], 4)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, RedOffset, GreenOffset, BlueOffset

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
        return Summary, SrcCscTablesT(IndexObj)

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

def WriteSpccControlPoints(ControlPointY,  ControlPointX1,  ControlPointX2):
    "Sets positions of control points for Multipoint sPCC."
    global Summary
    Summary.Command = "Write Spcc Control Points"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',83))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',ControlPointY)))
        writebytes.extend(list(struct.pack('H',ControlPointX1)))
        writebytes.extend(list(struct.pack('H',ControlPointX2)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadSpccControlPoints():
    "Returns positions of control points for Multipoint sPCC"
    global Summary
    Summary.Command = "Read Spcc Control Points"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',83))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(6, writebytes, ProtocolData)
        ControlPointY = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        ControlPointX1 = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        ControlPointX2 = struct.unpack_from ('H', bytearray(readbytes), 4)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ControlPointY, ControlPointX1, ControlPointX2

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

def WriteWpcTargetManualMode(Enable):
    "Sets/Resets the manual mode for speciying WPC target color point at run-time. When manual mode is set, all target color points specified in the project will be ignored. Software will set only the user specified target color point until the manual mode is reset using this same command."
    global Summary
    Summary.Command = "Write Wpc Target Manual Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',212))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Enable)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadWpcTargetManualMode():
    "Gets whether the manual mode for speciying WPC target color point at run-time is active. When manual mode is set, all target color points specified in the project will be ignored. Software will set only the user specified target color point until the manual mode is reset."
    global Summary
    Summary.Command = "Read Wpc Target Manual Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',212))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        Enable = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Enable

def WriteWpcTargetColorPoint(CieX,  CieY):
    "Sets the target color point while in WPC Target Manual Mode."
    global Summary
    Summary.Command = "Write Wpc Target Color Point"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',213))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(CieX,65536)))))
        writebytes.extend(list(struct.pack('H',int(convertfloattofixed(CieY,65536)))))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadWpcTargetColorPoint():
    "Gets the currently active target color point for WPC."
    global Summary
    Summary.Command = "Read Wpc Target Color Point"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',213))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        CieX = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 0)[0], 65536)
        CieY = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 2)[0], 65536)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, CieX, CieY

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

def WriteActuatorEepromFreeMemoryAccess(Offset,  Size,  DataBytes):
    "Writes data to Actuator EEPROM available memory."
    global Summary
    Summary.Command = "Write Actuator Eeprom Free Memory Access"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',110))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',Offset)))
        writebytes.extend(list(struct.pack('H',Size)))
        writebytes.extend(list(DataBytes))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadActuatorEepromFreeMemoryAccess(Offset,  Size):
    "This function reads data from Actuator EEPROM memory."
    global Summary
    Summary.Command = "Read Actuator Eeprom Free Memory Access"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',110))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',Offset)))
        writebytes.extend(list(struct.pack('H',Size)))
        readbytes = _readcommand(Size, writebytes, ProtocolData)
        DataBytes = bytearray(readbytes)[0, 1]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DataBytes

def ReadActuatorEepromFreeMemoryInfo():
    "This function indicates the XPR EEPROM address offset which corresponds to the start of free area."
    global Summary
    Summary.Command = "Read Actuator Eeprom Free Memory Info"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',111))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        Offset = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        Size = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Offset, Size

def WriteManualWarpTable(WarpTableIndex,  WarpPoints):
    "This command writes to the warp map table that can be enabled using the Set Apply Manual Warping command. N warp map points (that does not exceed the command packet size) can be loaded at a time to anywhere within the table. Maximum number of points that can be set using this command is 62 in the horizontal direction and 32 in the vertical direction. Overall max 1984 points. The number of points set by this command should match the number of control points specified using Set Manual Warp Control Points command."
    global Summary
    Summary.Command = "Write Manual Warp Table"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',52))
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
    "This command reads from the warp map table already loaded using Set Manual Warp Table command. N warp map points (that does not exceed the command packet size) can be read at a time from anywhere within the table. Maximum table size is 1952."
    global Summary
    Summary.Command = "Read Manual Warp Table"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',52))
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

def WriteManualWarpControlPoints(ControlPointsDefinedByArray,  HorizontalCtrlPoints,  VerticalCtrlPoints):
    "This command sets up the user defined control points of the warp map that shall be applied on top of the keystone correction, anamorphic scaling and other warp dependent feature settings if they are enabled. The warping map table loaded by the manual warp table write command is used as a two dimensional array with dimension which is defined based on the first argument of this command: - TRUE  = (NumHorzCtrlPoints x NumVertCtrlPoints) - FALSE = (62 x 32) The points in the map should lie within the display area defined by display image size command. Any points lying outside the display area shall get cropped."
    global Summary
    Summary.Command = "Write Manual Warp Control Points"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',53))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',ControlPointsDefinedByArray)))
        ********** Invalid Write Data Field Type - DLPComposer.Commands.Spec.ArrayType;
        ********** Invalid Write Data Field Type - DLPComposer.Commands.Spec.ArrayType;
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadManualWarpControlPoints():
    "This command gets up the user defined warping map control points."
    global Summary
    Summary.Command = "Read Manual Warp Control Points"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',53))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        ControlPointsDefinedByArray = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        ********** Invalid Write Data Field Type - DLPComposer.Commands.Spec.ArrayType;
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ControlPointsDefinedByArray, CtrlPoints

def WriteApplyManualWarping(WarpEnabled):
    "This command applies the manual warping control points and map table to the HW defined by Set Manual Warp Control Points and Set Manual Warp Table respectively."
    global Summary
    Summary.Command = "Write Apply Manual Warping"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',54))
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
    "This command returns whether warping feature is enabled or disabled for various use cases as described below."
    global Summary
    Summary.Command = "Read Apply Manual Warping"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',54))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        ManualWarpEnabled = getbits(1, 0);
        SurfaceCorrectionWarpEnabled = getbits(1, 1);
        LensCorrectionWarpEnabled = getbits(1, 2);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ManualWarpEnabled, SurfaceCorrectionWarpEnabled, LensCorrectionWarpEnabled

def WriteSmoothWarpTable(NumColumns,  NumRows,  SmoothWarpPoints):
    "This command sets up the user defined MxN warping map that creates a parameteric smooth curve. To disable this feature use ConfigureWarpMap command."
    global Summary
    Summary.Command = "Write Smooth Warp Table"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',56))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',NumColumns)))
        writebytes.extend(list(struct.pack('B',NumRows)))
        ********** Invalid Write Data Field Type - DLPComposer.Commands.Spec.ArrayType;
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadSmoothWarpTable():
    "This command returns the user defined MxN warping map points"
    global Summary
    Summary.Command = "Read Smooth Warp Table"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',56))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(2, writebytes, ProtocolData)
        NumColumns = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        NumRows = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        ********** Invalid Write Data Field Type - DLPComposer.Commands.Spec.ArrayType;
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, NumColumns, NumRows, SmoothWarpPoints

def WriteManualWarpTableUpdateMode(Mode):
    "This command sets Manula Warp Table write Mode"
    global Summary
    Summary.Command = "Write Manual Warp Table Update Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',57))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Mode)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadManualWarpTableUpdateMode():
    "This command returns if manual warping is enabled or disabled."
    global Summary
    Summary.Command = "Read Manual Warp Table Update Mode"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 4;
    try:
        writebytes=list(struct.pack('B',57))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        Mode = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Mode

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

