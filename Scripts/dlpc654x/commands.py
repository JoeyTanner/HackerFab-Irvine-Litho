#-------------------------------------
# Copyright (c) 2024 Texas Instruments
#-------------------------------------

# NOTE: This file is auto generated from a command definition file.
#       Please do not modify the file directly.                    
#
# Command Spec Version : 0.1

import sys
import clr

clr.AddReference('DLPComposer.Commands.DLPC654x')
from System import *
from DLPComposer.Commands.DLPC654x import * 

def ReadMode() :
    Summary, AppMode, ControllerConfig = \
        Command.ReadMode()
    return Summary, AppMode, ControllerConfig

def ReadVersion() :
    Summary, Version = \
        Command.ReadVersion()
    return Summary, Version

def WriteSwitchMode(SwitchMode) :
    return Command.WriteSwitchMode(SwitchMode)

def ReadBootHoldReason() :
    Summary, ReasonCode = \
        Command.ReadBootHoldReason()
    return Summary, int(ReasonCode)

def ReadFlashInfo(ChipSelect) :
    Summary, ManfId, DevId, DevSize, SectorInfo, AvailableForProgramming = \
        Command.ReadFlashInfo(ChipSelect)
    return Summary, int(ManfId), int(DevId), int(DevSize), list(SectorInfo), bool(AvailableForProgramming)

def ReadProgrammableFlashSectorInformation() :
    Summary, SectorInfo = \
        Command.ReadProgrammableFlashSectorInformation()
    return Summary, list(SectorInfo)

def WriteUnlockFlashForUpdate(Unlock) :
    return Command.WriteUnlockFlashForUpdate(Unlock)

def ReadUnlockFlashForUpdate() :
    Summary, IsUnlocked = \
        Command.ReadUnlockFlashForUpdate()
    return Summary, int(IsUnlocked)

def WriteEraseSector(SectorAddress) :
    return Command.WriteEraseSector(SectorAddress)

def WriteInitializeFlashReadWriteSettings(StartAddress, NumBytes) :
    return Command.WriteInitializeFlashReadWriteSettings(StartAddress, NumBytes)

def WriteFlashWrite(Data) :
    Data = Array[Byte](Data)
    return Command.WriteFlashWrite(Data)

def ReadFlashWrite(NumBytesToRead) :
    Summary, Data = \
        Command.ReadFlashWrite(NumBytesToRead)
    return Summary, bytearray(Data)

def ReadChecksum(StartAddress, NumBytes) :
    Summary, SimpleChecksum, SumofSumChecksum = \
        Command.ReadChecksum(StartAddress, NumBytes)
    return Summary, int(SimpleChecksum), int(SumofSumChecksum)

def WriteResetFlash(Chip) :
    return Command.WriteResetFlash(Chip)

def WriteMemory(Address, Value) :
    return Command.WriteMemory(Address, Value)

def ReadMemory(Address) :
    Summary, Value = \
        Command.ReadMemory(Address)
    return Summary, int(Value)

def WriteMemoryArray(MemoryArray) :
    return Command.WriteMemoryArray(MemoryArray)

def ReadMemoryArray(StartAddress, AddressIncrement, AccessWidth, NumberOfWords, NumberOfBytesPerWord) :
    Summary, Data = \
        Command.ReadMemoryArray(StartAddress, AddressIncrement, AccessWidth, NumberOfWords, NumberOfBytesPerWord)
    return Summary, bytearray(Data)

def WriteAnrSpatialFilterStatus(IsNoiseFilterEnabled, FilterStrength) :
    return Command.WriteAnrSpatialFilterStatus(IsNoiseFilterEnabled, FilterStrength)

def ReadAnrSpatialFilterStatus() :
    Summary, IsNoiseFilterEnabled, FilterStrength = \
        Command.ReadAnrSpatialFilterStatus()
    return Summary, bool(IsNoiseFilterEnabled), FilterStrength

def WriteAnrTemporalFilterStatus(IsNoiseFilterEnabled, FilterStrength) :
    return Command.WriteAnrTemporalFilterStatus(IsNoiseFilterEnabled, FilterStrength)

def ReadAnrTemporalFilterStatus() :
    Summary, IsNoiseFilterEnabled, FilterStrength = \
        Command.ReadAnrTemporalFilterStatus()
    return Summary, bool(IsNoiseFilterEnabled), FilterStrength

def ReadAnrNoiseFloorEstimate() :
    Summary, NoiseFloor = \
        Command.ReadAnrNoiseFloorEstimate()
    return Summary, int(NoiseFloor)

def WriteEnableDeiForProgNoiseReduction(Enable) :
    return Command.WriteEnableDeiForProgNoiseReduction(Enable)

def ReadEnableDeiForProgNoiseReduction() :
    Summary, Enable = \
        Command.ReadEnableDeiForProgNoiseReduction()
    return Summary, bool(Enable)

def WriteCalibrateAdc() :
    return Command.WriteCalibrateAdc()

def WriteSourceConnector(ConnectorNum) :
    return Command.WriteSourceConnector(ConnectorNum)

def ReadSourceConnector() :
    Summary, Source = \
        Command.ReadSourceConnector()
    return Summary, int(Source)

def WriteAutoSourceSelect(AutoSelectEnable) :
    return Command.WriteAutoSourceSelect(AutoSelectEnable)

def ReadAutoSourceSelect() :
    Summary, AutoSelectEnable = \
        Command.ReadAutoSourceSelect()
    return Summary, bool(AutoSelectEnable)

def ReadAutolockStatus() :
    Summary, AutolockStatus = \
        Command.ReadAutolockStatus()
    return Summary, AutolockStatus

def WriteAutoLockAsmCfg(AutoLockAsmCfg) :
    return Command.WriteAutoLockAsmCfg(AutoLockAsmCfg)

def ReadAutoLockAsmCfg() :
    Summary, AutoLockAsmCfg = \
        Command.ReadAutoLockAsmCfg()
    return Summary, AutoLockAsmCfg

def WritePhase(Phase) :
    return Command.WritePhase(Phase)

def ReadPhase() :
    Summary, Phase = \
        Command.ReadPhase()
    return Summary, int(Phase)

def ReadVerticalFramingRegionLimits() :
    Summary, LowerLimit, UpperLimit = \
        Command.ReadVerticalFramingRegionLimits()
    return Summary, int(LowerLimit), int(UpperLimit)

def WriteGain(RedGain, GreenGain, BlueGain) :
    return Command.WriteGain(RedGain, GreenGain, BlueGain)

def ReadGain() :
    Summary, RedGain, GreenGain, BlueGain = \
        Command.ReadGain()
    return Summary, int(RedGain), int(GreenGain), int(BlueGain)

def WriteOffset(Red, Green, Blue) :
    return Command.WriteOffset(Red, Green, Blue)

def ReadOffset() :
    Summary, Red, Green, Blue = \
        Command.ReadOffset()
    return Summary, int(Red), int(Green), int(Blue)

def WriteLevelWindow(Left, Right, Top, Bottom) :
    return Command.WriteLevelWindow(Left, Right, Top, Bottom)

def ReadLevelWindow() :
    Summary, Left, Right, Top, Bottom = \
        Command.ReadLevelWindow()
    return Summary, int(Left), int(Right), int(Top), int(Bottom)

def ReadRgbLevel() :
    Summary, RgbLevel = \
        Command.ReadRgbLevel()
    return Summary, RgbLevel

def WriteBt656Reg(DevAddress, RegAddress, Value) :
    return Command.WriteBt656Reg(DevAddress, RegAddress, Value)

def ReadBt656Reg(DevAddress, RegAddress) :
    Summary, Value = \
        Command.ReadBt656Reg(DevAddress, RegAddress)
    return Summary, int(Value)

def WriteEnableBt656Gpio(Enable) :
    return Command.WriteEnableBt656Gpio(Enable)

def WriteFilmMode(Mode) :
    return Command.WriteFilmMode(Mode)

def ReadFilmMode() :
    Summary, Mode = \
        Command.ReadFilmMode()
    return Summary, Mode

def WriteFilmModeLockThresholds(BeforeLock, BeforeUnlock) :
    return Command.WriteFilmModeLockThresholds(BeforeLock, BeforeUnlock)

def ReadFilmModeLockThresholds() :
    Summary, BeforeLock, BeforeUnlock = \
        Command.ReadFilmModeLockThresholds()
    return Summary, int(BeforeLock), int(BeforeUnlock)

def ReadDeiStatus() :
    Summary, FilmLockRegion0, FilmLockRegion1 = \
        Command.ReadDeiStatus()
    return Summary, bool(FilmLockRegion0), bool(FilmLockRegion1)

def WriteDeiEnable(DeiEnable) :
    return Command.WriteDeiEnable(DeiEnable)

def ReadDeiEnable() :
    Summary, DeiEnable = \
        Command.ReadDeiEnable()
    return Summary, bool(DeiEnable)

def ReadIntraFieldInterpolationStrength() :
    Summary, Strength = \
        Command.ReadIntraFieldInterpolationStrength()
    return Summary, Strength

def WriteMotionAdaptiveMode(Mode) :
    return Command.WriteMotionAdaptiveMode(Mode)

def ReadMotionAdaptiveMode() :
    Summary, Mode = \
        Command.ReadMotionAdaptiveMode()
    return Summary, Mode

def WriteFilmRegionEnable(Enable) :
    return Command.WriteFilmRegionEnable(Enable)

def ReadFilmRegionEnable() :
    Summary, Enable = \
        Command.ReadFilmRegionEnable()
    return Summary, bool(Enable)

def WriteFilmRegion1Area(FirstPixel, FirstLine, PixelsPerLine, LinesPerFrame) :
    return Command.WriteFilmRegion1Area(FirstPixel, FirstLine, PixelsPerLine, LinesPerFrame)

def ReadFilmRegion1Area() :
    Summary, FirstPixel, FirstLine, PixelsPerLine, LinesPerFrame = \
        Command.ReadFilmRegion1Area()
    return Summary, int(FirstPixel), int(FirstLine), int(PixelsPerLine), int(LinesPerFrame)

def WriteUserInterpolationStrengthEnable(UserInterpolationStrengthEnable) :
    return Command.WriteUserInterpolationStrengthEnable(UserInterpolationStrengthEnable)

def ReadUserInterpolationStrengthEnable() :
    Summary, UserInterpolationStrengthEnable = \
        Command.ReadUserInterpolationStrengthEnable()
    return Summary, UserInterpolationStrengthEnable

def WriteMotionDetectionInChroma(DetectInChroma) :
    return Command.WriteMotionDetectionInChroma(DetectInChroma)

def ReadMotionDetectionInChroma() :
    Summary, DetectInChroma = \
        Command.ReadMotionDetectionInChroma()
    return Summary, bool(DetectInChroma)

def WriteRateFactorUpdate(Enable) :
    return Command.WriteRateFactorUpdate(Enable)

def WriteSysTestMode(Enable) :
    return Command.WriteSysTestMode(Enable)

def ReadSysTestMode() :
    Summary, Enable = \
        Command.ReadSysTestMode()
    return Summary, bool(Enable)

def ReadTaskStatus(TaskId) :
    Summary, Priority, StackSize, StackUnused, StackUsed = \
        Command.ReadTaskStatus(TaskId)
    return Summary, int(Priority), int(StackSize), int(StackUnused), int(StackUsed)

def ReadMaxIntDisableTime() :
    Summary, MaxIntDisableTime = \
        Command.ReadMaxIntDisableTime()
    return Summary, int(MaxIntDisableTime)

def WriteResetMaxIntDisableTime() :
    return Command.WriteResetMaxIntDisableTime()

def ReadTaskTimeProfile(TaskName) :
    Summary, MaxExecutionTime, MinExecutionTime = \
        Command.ReadTaskTimeProfile(TaskName)
    return Summary, int(MaxExecutionTime), int(MinExecutionTime)

def WriteResetTaskTimeProfile(TaskName) :
    return Command.WriteResetTaskTimeProfile(TaskName)

def WriteToggleUsbMode() :
    return Command.WriteToggleUsbMode()

def WriteSendUsbMouseCode(MouseClick, MouseX, MouseY) :
    return Command.WriteSendUsbMouseCode(MouseClick, MouseX, MouseY)

def WriteSendUsbKeyboardCode(KeyCode) :
    return Command.WriteSendUsbKeyboardCode(KeyCode)

def WriteLmpEnable(Enable) :
    return Command.WriteLmpEnable(Enable)

def ReadIsLampLit() :
    Summary, Enable = \
        Command.ReadIsLampLit()
    return Summary, bool(Enable)

def WriteGpioPins(GpioPins) :
    return Command.WriteGpioPins(GpioPins)

def ReadGpioPins(MaskBits1, MaskBits2, MaskBits3) :
    Summary, LogicValue1, LogicValue2, LogicValue3 = \
        Command.ReadGpioPins(MaskBits1, MaskBits2, MaskBits3)
    return Summary, int(LogicValue1), int(LogicValue2), int(LogicValue3)

def WriteGpioInterruptSource(InterruptSource, Pin) :
    return Command.WriteGpioInterruptSource(InterruptSource, Pin)

def ReadGpioInterruptSource(InterruptSource) :
    Summary, Pin = \
        Command.ReadGpioInterruptSource(InterruptSource)
    return Summary, Pin

def ReadGpioEnable(Pin) :
    Summary, Enable, AlternateFuncSelect = \
        Command.ReadGpioEnable(Pin)
    return Summary, bool(Enable), bool(AlternateFuncSelect)

def WriteGpioEnableAlternateFunction(Function, AlternateFunctionEnable) :
    return Command.WriteGpioEnableAlternateFunction(Function, AlternateFunctionEnable)

def WriteGpioInterruptConfig(InterruptSource, TriggerType, TriggerPolarity) :
    return Command.WriteGpioInterruptConfig(InterruptSource, TriggerType, TriggerPolarity)

def ReadGpioInterruptConfig(InterruptSource) :
    Summary, TriggerType, TriggerPolarity = \
        Command.ReadGpioInterruptConfig(InterruptSource)
    return Summary, TriggerType, TriggerPolarity

def ReadGpioInterruptStatus(InterruptSource) :
    Summary, InterruptActive = \
        Command.ReadGpioInterruptStatus(InterruptSource)
    return Summary, bool(InterruptActive)

def ReadGpioPinName(PinNum) :
    Summary, PinName = \
        Command.ReadGpioPinName(PinNum)
    return Summary, bytearray(PinName)

def WriteEnableScaleRingMinimization(Enable) :
    return Command.WriteEnableScaleRingMinimization(Enable)

def ReadEnableScaleRingMinimization() :
    Summary, Enable = \
        Command.ReadEnableScaleRingMinimization()
    return Summary, bool(Enable)

def WriteScalingFilter(Filter) :
    return Command.WriteScalingFilter(Filter)

def ReadScalingFilter() :
    Summary, Filter = \
        Command.ReadScalingFilter()
    return Summary, Filter

def WriteEnableKeystone(Enabled) :
    return Command.WriteEnableKeystone(Enabled)

def ReadEnableKeystone() :
    Summary, Enabled = \
        Command.ReadEnableKeystone()
    return Summary, bool(Enabled)

def WriteHdrMode(HdrMode) :
    return Command.WriteHdrMode(HdrMode)

def ReadHdrMode() :
    Summary, HdrMode = \
        Command.ReadHdrMode()
    return Summary, HdrMode

def WriteImageCphw(ImageCphw) :
    return Command.WriteImageCphw(ImageCphw)

def ReadImageCphw() :
    Summary, ImageCphw = \
        Command.ReadImageCphw()
    return Summary, ImageCphw

def WriteImageCpeep(Profile, ImageCpeep) :
    return Command.WriteImageCpeep(Profile, ImageCpeep)

def ReadImageCpeep(Profile) :
    Summary, ImageCpeep = \
        Command.ReadImageCpeep(Profile)
    return Summary, ImageCpeep

def WriteImageCtIup(HdSourceEnable) :
    return Command.WriteImageCtIup(HdSourceEnable)

def ReadImageCtIup() :
    Summary, HdSourceEnable = \
        Command.ReadImageCtIup()
    return Summary, bool(HdSourceEnable)

def WriteImageCtiGain(Gain) :
    return Command.WriteImageCtiGain(Gain)

def ReadImageCtiGain() :
    Summary, Gain = \
        Command.ReadImageCtiGain()
    return Summary, Gain

def ReadImageInverseHsg() :
    Summary, ImageInverseHsg = \
        Command.ReadImageInverseHsg()
    return Summary, ImageInverseHsg

def ReadLibSignature(LibName) :
    Summary, LibSignature, ChangesetSignature = \
        Command.ReadLibSignature(LibName)
    return Summary, bytearray(LibSignature), bytearray(ChangesetSignature)

def WritePrintAllLibSignatures() :
    return Command.WritePrintAllLibSignatures()

def ReadOsdDisplayStatus() :
    Summary, OsdDisplayed = \
        Command.ReadOsdDisplayStatus()
    return Summary, bool(OsdDisplayed)

def WriteNavigateosd(Key) :
    return Command.WriteNavigateosd(Key)

def WriteOsdUpdateMode(UpdateMode) :
    return Command.WriteOsdUpdateMode(UpdateMode)

def ReadOsdUpdateMode() :
    Summary, UpdateMode = \
        Command.ReadOsdUpdateMode()
    return Summary, UpdateMode

def WriteEnableOsd(Enable) :
    return Command.WriteEnableOsd(Enable)

def WriteEnableWindow(WindowNumber, Enable) :
    return Command.WriteEnableWindow(WindowNumber, Enable)

def WriteGenerateWindow(WindowNumber, Left, Top, Height, Width) :
    return Command.WriteGenerateWindow(WindowNumber, Left, Top, Height, Width)

def WriteSspPassthru(SspPassthru) :
    return Command.WriteSspPassthru(SspPassthru)

def ReadSspPassthru(Port, ChipSelect, DeviceType, ClockRate, Command) :
    Summary, Data = \
        Command.ReadSspPassthru(Port, ChipSelect, DeviceType, ClockRate, Command)
    return Summary, int(Data)

def WriteComposerPassthruData(Cmd, InpNumBytes, InputData) :
    InputData = Array[Byte](InputData)
    return Command.WriteComposerPassthruData(Cmd, InpNumBytes, InputData)

def ReadComposerPassthruData(Cmd, InpNumBytes, OutNumBytes, InputData) :
    Summary, OutputData = \
        Command.ReadComposerPassthruData(Cmd, InpNumBytes, OutNumBytes, InputData)
    return Summary, bytearray(OutputData)

def WriteSetSubframeMask(SubframeNumber, SubframePattern) :
    return Command.WriteSetSubframeMask(SubframeNumber, SubframePattern)

def WriteEnableSubframeOverride(Enable, Subframe) :
    return Command.WriteEnableSubframeOverride(Enable, Subframe)

def WriteEnableBnmUpdate(Enable) :
    return Command.WriteEnableBnmUpdate(Enable)

def ReadEnableBnmUpdate() :
    Summary, Enable = \
        Command.ReadEnableBnmUpdate()
    return Summary, bool(Enable)

def ReadGetSequenceNumber() :
    Summary, Current = \
        Command.ReadGetSequenceNumber()
    return Summary, int(Current)

def WriteSetXpr25AdjustmentFactor(Adjustment) :
    return Command.WriteSetXpr25AdjustmentFactor(Adjustment)

def ReadSetXpr25AdjustmentFactor() :
    Summary, Adjustment = \
        Command.ReadSetXpr25AdjustmentFactor()
    return Summary, int(Adjustment)

def ReadSfgResolution() :
    Summary, HorizontalResolution, VerticalResolution = \
        Command.ReadSfgResolution()
    return Summary, int(HorizontalResolution), int(VerticalResolution)

def WriteActivePortConfiguration(Port, PortWidth, AbcMux, IsClockPolarityPositive) :
    return Command.WriteActivePortConfiguration(Port, PortWidth, AbcMux, IsClockPolarityPositive)

def ReadActivePortConfiguration() :
    Summary, Port, PortWidth, AbcMux, IsClockPolarityPositive = \
        Command.ReadActivePortConfiguration()
    return Summary, Port, PortWidth, AbcMux, bool(IsClockPolarityPositive)

def WriteSplashFrameRate(FrameRate) :
    return Command.WriteSplashFrameRate(FrameRate)

def ReadSplashFrameRate() :
    Summary, FrameRate = \
        Command.ReadSplashFrameRate()
    return Summary, float(FrameRate)

def ReadCaptureExternalFrame() :
    Summary, CaptureExternalFrame = \
        Command.ReadCaptureExternalFrame()
    return Summary, CaptureExternalFrame

def ReadCapturedFrameWithComp() :
    Summary, FrameData = \
        Command.ReadCapturedFrameWithComp()
    return Summary, bytearray(FrameData)

def ReadSplashCaptureTime() :
    Summary, CaptureTime = \
        Command.ReadSplashCaptureTime()
    return Summary, int(CaptureTime)

def WriteEnableStructuredPatterns(Enable) :
    return Command.WriteEnableStructuredPatterns(Enable)

def ReadEnableStructuredPatterns() :
    Summary, Enable = \
        Command.ReadEnableStructuredPatterns()
    return Summary, bool(Enable)

def WriteInvertStructuredPatternBitplane(BitPlaneNum, Invert) :
    return Command.WriteInvertStructuredPatternBitplane(BitPlaneNum, Invert)

def ReadInvertStructuredPatternBitplane(BitPlaneNum) :
    Summary, Invert = \
        Command.ReadInvertStructuredPatternBitplane(BitPlaneNum)
    return Summary, bool(Invert)

def WriteSetStructuredPatternBitplane(BitPlaneNum, IsVerticalPattern, NumOfBytes, Bytes) :
    Bytes = Array[Byte](Bytes)
    return Command.WriteSetStructuredPatternBitplane(BitPlaneNum, IsVerticalPattern, NumOfBytes, Bytes)

def WriteSetStructuredPatternStripes(SetStructuredPatternStripes) :
    return Command.WriteSetStructuredPatternStripes(SetStructuredPatternStripes)

def ReadTpgPatternType() :
    Summary, PatternType = \
        Command.ReadTpgPatternType()
    return Summary, PatternType

def WriteTpgPredefinedPattern(PatternNumber) :
    return Command.WriteTpgPredefinedPattern(PatternNumber)

def ReadTpgPredefinedPattern() :
    Summary, PatternNumber = \
        Command.ReadTpgPredefinedPattern()
    return Summary, int(PatternNumber)

def ReadTpgPixelClkFreq() :
    Summary, PixelClockFrequency = \
        Command.ReadTpgPixelClkFreq()
    return Summary, int(PixelClockFrequency)

def WriteTpgSolidField(SolidColorRed, SolidColorGreen, SolidColorBlue) :
    return Command.WriteTpgSolidField(SolidColorRed, SolidColorGreen, SolidColorBlue)

def ReadTpgSolidField() :
    Summary, SolidColorRed, SolidColorGreen, SolidColorBlue = \
        Command.ReadTpgSolidField()
    return Summary, int(SolidColorRed), int(SolidColorGreen), int(SolidColorBlue)

def WriteTpgRampHorizontal(RampStep, RampColor) :
    return Command.WriteTpgRampHorizontal(RampStep, RampColor)

def ReadTpgRampHorizontal() :
    Summary, RampStep, RampColor = \
        Command.ReadTpgRampHorizontal()
    return Summary, RampStep, RampColor

def WriteTpgRampVertical(RampStep, RampColor) :
    return Command.WriteTpgRampVertical(RampStep, RampColor)

def ReadTpgRampVertical() :
    Summary, RampStep, RampColor = \
        Command.ReadTpgRampVertical()
    return Summary, RampStep, RampColor

def WriteTpgHorizontalLines(TpgHorizontalLines) :
    return Command.WriteTpgHorizontalLines(TpgHorizontalLines)

def ReadTpgHorizontalLines() :
    Summary, TpgHorizontalLines = \
        Command.ReadTpgHorizontalLines()
    return Summary, TpgHorizontalLines

def WriteTpgVerticalLines(TpgVerticalLines) :
    return Command.WriteTpgVerticalLines(TpgVerticalLines)

def ReadTpgVerticalLines() :
    Summary, TpgVerticalLines = \
        Command.ReadTpgVerticalLines()
    return Summary, TpgVerticalLines

def WriteTpgDiagonalLines(TpgDiagonalLines) :
    return Command.WriteTpgDiagonalLines(TpgDiagonalLines)

def ReadTpgDiagonalLines() :
    Summary, TpgDiagonalLines = \
        Command.ReadTpgDiagonalLines()
    return Summary, TpgDiagonalLines

def WriteTpgGridLines(TpgGridLines) :
    return Command.WriteTpgGridLines(TpgGridLines)

def ReadTpgGridLines() :
    Summary, TpgGridLines = \
        Command.ReadTpgGridLines()
    return Summary, TpgGridLines

def WriteTpgColorBars(Width, ColorEnableRed, ColorEnableGreen, ColorEnableBlue) :
    return Command.WriteTpgColorBars(Width, ColorEnableRed, ColorEnableGreen, ColorEnableBlue)

def ReadTpgColorBars() :
    Summary, Width, ColorEnableRed, ColorEnableGreen, ColorEnableBlue = \
        Command.ReadTpgColorBars()
    return Summary, int(Width), bool(ColorEnableRed), bool(ColorEnableGreen), bool(ColorEnableBlue)

def WriteTpgColorHorzRamp(RampStep, Height, ColorEnableRed, ColorEnableGreen, ColorEnableBlue) :
    return Command.WriteTpgColorHorzRamp(RampStep, Height, ColorEnableRed, ColorEnableGreen, ColorEnableBlue)

def ReadTpgColorHorzRamp() :
    Summary, RampStep, Height, ColorEnableRed, ColorEnableGreen, ColorEnableBlue = \
        Command.ReadTpgColorHorzRamp()
    return Summary, RampStep, int(Height), bool(ColorEnableRed), bool(ColorEnableGreen), bool(ColorEnableBlue)

def WriteTpgFixedRamp(TpgFixedRamp) :
    return Command.WriteTpgFixedRamp(TpgFixedRamp)

def ReadTpgFixedRamp() :
    Summary, TpgFixedRamp = \
        Command.ReadTpgFixedRamp()
    return Summary, TpgFixedRamp

def WriteTpgDiamondDiagLines(TpgDiamondDiagLines) :
    return Command.WriteTpgDiamondDiagLines(TpgDiamondDiagLines)

def ReadTpgDiamondDiagLines() :
    Summary, TpgDiamondDiagLines = \
        Command.ReadTpgDiamondDiagLines()
    return Summary, TpgDiamondDiagLines

def WriteTpgInterlacedEnable(InterlaceEnable) :
    return Command.WriteTpgInterlacedEnable(InterlaceEnable)

def ReadTpgInterlacedEnable() :
    Summary, InterlaceEnable = \
        Command.ReadTpgInterlacedEnable()
    return Summary, bool(InterlaceEnable)

def WriteTpgCheckerboard(TpgCheckerboard) :
    return Command.WriteTpgCheckerboard(TpgCheckerboard)

def ReadTpgCheckerboard() :
    Summary, TpgCheckerboard = \
        Command.ReadTpgCheckerboard()
    return Summary, TpgCheckerboard

def WriteEnableThreeD(Enable3D) :
    return Command.WriteEnableThreeD(Enable3D)

def ReadEnableThreeD() :
    Summary, Enable3D = \
        Command.ReadEnableThreeD()
    return Summary, bool(Enable3D)

def WriteThreeDSourceConfiguration(ThreeDSourceConfiguration) :
    return Command.WriteThreeDSourceConfiguration(ThreeDSourceConfiguration)

def ReadThreeDSourceConfiguration() :
    Summary, ThreeDSourceConfiguration = \
        Command.ReadThreeDSourceConfiguration()
    return Summary, ThreeDSourceConfiguration

def WriteLeftRightSignalPolarity(Invert) :
    return Command.WriteLeftRightSignalPolarity(Invert)

def ReadLeftRightSignalPolarity() :
    Summary, Invert = \
        Command.ReadLeftRightSignalPolarity()
    return Summary, bool(Invert)

def ReadControllerInfo() :
    Summary, ControllerId, ControllerName = \
        Command.ReadControllerInfo()
    return Summary, int(ControllerId), ControllerName

def ReadDmdInfo() :
    Summary, DmdId, FuseId, DmdName = \
        Command.ReadDmdInfo()
    return Summary, int(DmdId), int(FuseId), DmdName

def ReadDmdResolution() :
    Summary, Width, Height = \
        Command.ReadDmdResolution()
    return Summary, int(Width), int(Height)

def ReadFlashVersion() :
    Summary, FlashVersionMajor, FlashVersionMinor, FlashVersionSubminor = \
        Command.ReadFlashVersion()
    return Summary, int(FlashVersionMajor), int(FlashVersionMinor), int(FlashVersionSubminor)

def ReadFlashLayoutVersion() :
    Summary, FlashConfigLayoutVersion, FlashConfigLayoutHash, ApplicationConfigLayoutVersion, ApplicationConfigLayoutHash = \
        Command.ReadFlashLayoutVersion()
    return Summary, int(FlashConfigLayoutVersion), FlashConfigLayoutHash, int(ApplicationConfigLayoutVersion), ApplicationConfigLayoutHash

def ReadProductConfigurationFailureCause() :
    Summary, ProductConfigFailCause = \
        Command.ReadProductConfigurationFailureCause()
    return Summary, ProductConfigFailCause

def ReadSystemStatus() :
    Summary, SystemStatus = \
        Command.ReadSystemStatus()
    return Summary, SystemStatus

def ReadEepromDataPresent() :
    Summary, EepromDataPresent = \
        Command.ReadEepromDataPresent()
    return Summary, EepromDataPresent

def WriteGeneralDelayCommand(DelayInMilliseconds) :
    return Command.WriteGeneralDelayCommand(DelayInMilliseconds)

def WriteEepromInvalidate(EepromInvalidate) :
    return Command.WriteEepromInvalidate(EepromInvalidate)

def WriteSplashCapture() :
    return Command.WriteSplashCapture()

def ReadSplashCaptureStatus() :
    Summary, CaptureState, CaptureCompletionPercentage = \
        Command.ReadSplashCaptureStatus()
    return Summary, CaptureState, int(CaptureCompletionPercentage)

def WriteTerminateSplashCapture() :
    return Command.WriteTerminateSplashCapture()

def ReadComposerVersion() :
    Summary, Major, Minor1, Minor2, Patch, BuildHash = \
        Command.ReadComposerVersion()
    return Summary, int(Major), int(Minor1), int(Minor2), int(Patch), BuildHash

def WriteAutolockControl(AutolockControl) :
    return Command.WriteAutolockControl(AutolockControl)

def WriteBlendMapGainValues(CompressionEnabled, ColorChannelSelect, TotalNumberOfCompressedValues, Index, GainValues) :
    GainValues = Array[UInt16](GainValues)
    return Command.WriteBlendMapGainValues(CompressionEnabled, ColorChannelSelect, TotalNumberOfCompressedValues, Index, GainValues)

def ReadBlendMapGainValues(ColorChannelSelect, Index, NoOfValues) :
    Summary, IsCompressionEnabled, GainValues = \
        Command.ReadBlendMapGainValues(ColorChannelSelect, Index, NoOfValues)
    return Summary, int(IsCompressionEnabled), list(GainValues)

def WriteApplyBlendMap(BlendMapUploadEnable) :
    return Command.WriteApplyBlendMap(BlendMapUploadEnable)

def WriteBlendMapOffsetValues(CompressionEnabled, ColorChannelSelect, TotalNumberOfCompressedValues, Index, OffsetValues) :
    OffsetValues = Array[UInt16](OffsetValues)
    return Command.WriteBlendMapOffsetValues(CompressionEnabled, ColorChannelSelect, TotalNumberOfCompressedValues, Index, OffsetValues)

def ReadBlendMapOffsetValues(ColorChannelSelect, Index, NoOfValues) :
    Summary, IsCompressionEnabled, OffsetValues = \
        Command.ReadBlendMapOffsetValues(ColorChannelSelect, Index, NoOfValues)
    return Summary, int(IsCompressionEnabled), list(OffsetValues)

def WriteBlendMapControlPoints(HorizontalResolutionProjector, VerticalResolutionProjector, HorizontalCtrlPoints, VerticalCtrlPoints) :
    HorizontalCtrlPoints = Array[UInt16](HorizontalCtrlPoints)
    VerticalCtrlPoints = Array[UInt16](VerticalCtrlPoints)
    return Command.WriteBlendMapControlPoints(HorizontalResolutionProjector, VerticalResolutionProjector, HorizontalCtrlPoints, VerticalCtrlPoints)

def ReadBlendMapControlPoints() :
    Summary, HorizontalCtrlPoints, VerticalCtrlPoints = \
        Command.ReadBlendMapControlPoints()
    return Summary, list(HorizontalCtrlPoints), list(VerticalCtrlPoints)

def WriteEnableEdgeBlending(EdgeBlendingEnable) :
    return Command.WriteEnableEdgeBlending(EdgeBlendingEnable)

def ReadEnableEdgeBlending() :
    Summary, EdgeBlendingEnable = \
        Command.ReadEnableEdgeBlending()
    return Summary, bool(EdgeBlendingEnable)

def WriteEdgeBlendingSystemParams(NumProjectorsColumns, NumProjectorsRows, SelfProjectorColumn, SelfProjectorRow, WhiteBlackLevels) :
    WhiteBlackLevels = Array[UInt32](WhiteBlackLevels)
    return Command.WriteEdgeBlendingSystemParams(NumProjectorsColumns, NumProjectorsRows, SelfProjectorColumn, SelfProjectorRow, WhiteBlackLevels)

def ReadEdgeBlendingSystemParams() :
    Summary, NumProjectorsColumns, NumProjectorsRows, SelfProjectorColumn, SelfProjectorRow, WhiteBlackLevels = \
        Command.ReadEdgeBlendingSystemParams()
    return Summary, int(NumProjectorsColumns), int(NumProjectorsRows), int(SelfProjectorColumn), int(SelfProjectorRow), list(WhiteBlackLevels)

def WriteEdgeBlendingConfiguration(OverlapHorizontal, OverlapVertical, GeometricAdjustmentType, StorageOptions, GeometryParams) :
    GeometryParams = Array[UInt16](GeometryParams)
    return Command.WriteEdgeBlendingConfiguration(OverlapHorizontal, OverlapVertical, GeometricAdjustmentType, StorageOptions, GeometryParams)

def ReadEdgeBlendingConfiguration() :
    Summary, OverlapHorizontal, OverlapVertical, GeometricAdjustmentType, StorageOptions, GeometryParams = \
        Command.ReadEdgeBlendingConfiguration()
    return Summary, int(OverlapHorizontal), int(OverlapVertical), GeometricAdjustmentType, StorageOptions, list(GeometryParams)

def WriteCwIndexDelay(Wheel, DegreesInteger, DegreesFraction) :
    return Command.WriteCwIndexDelay(Wheel, DegreesInteger, DegreesFraction)

def ReadCwIndexDelay(Wheel) :
    Summary, DegreesInteger, DegreesFraction = \
        Command.ReadCwIndexDelay(Wheel)
    return Summary, int(DegreesInteger), int(DegreesFraction)

def WriteInitializeOnTheFlyLoadSplashImage(SplashHeader, Width, Height) :
    SplashHeader = Array[Byte](SplashHeader)
    return Command.WriteInitializeOnTheFlyLoadSplashImage(SplashHeader, Width, Height)

def WriteLoadSplashImageOnTheFly(ImageData) :
    ImageData = Array[Byte](ImageData)
    return Command.WriteLoadSplashImageOnTheFly(ImageData)

def WriteXprCalibrationPatternDisplay() :
    return Command.WriteXprCalibrationPatternDisplay()

def WriteXpr4WayOrientation(XprOrientationNumber) :
    return Command.WriteXpr4WayOrientation(XprOrientationNumber)

def ReadXpr4WayOrientation() :
    Summary, XprOrientationNumber = \
        Command.ReadXpr4WayOrientation()
    return Summary, int(XprOrientationNumber)

def WriteXprActuatorWaveformControlParameter(XprCommand, AwcChannel, Data) :
    return Command.WriteXprActuatorWaveformControlParameter(XprCommand, AwcChannel, Data)

def ReadXprActuatorWaveformControlParameter(XprCommand, AwcChannel) :
    Summary, Data = \
        Command.ReadXprActuatorWaveformControlParameter(XprCommand, AwcChannel)
    return Summary, int(Data)

def WriteLoad4WayXprWaveform(AwcChannel, Index, Data) :
    Data = Array[Byte](Data)
    return Command.WriteLoad4WayXprWaveform(AwcChannel, Index, Data)

def WriteDbAperturePosition(Position) :
    return Command.WriteDbAperturePosition(Position)

def ReadDbAperturePosition() :
    Summary, Position = \
        Command.ReadDbAperturePosition()
    return Summary, int(Position)

def WriteDbApertureMinMax(AptMin, AptMax) :
    return Command.WriteDbApertureMinMax(AptMin, AptMax)

def ReadDbApertureMinMax() :
    Summary, AptMin, AptMax = \
        Command.ReadDbApertureMinMax()
    return Summary, int(AptMin), int(AptMax)

def WriteDbManualMode(Enable) :
    return Command.WriteDbManualMode(Enable)

def ReadDbManualMode() :
    Summary, Enable = \
        Command.ReadDbManualMode()
    return Summary, int(Enable)

def WriteDbBorderConfiguration(Top, Bottom, Left, Right) :
    return Command.WriteDbBorderConfiguration(Top, Bottom, Left, Right)

def ReadDbBorderConfiguration() :
    Summary, Top, Bottom, Left, Right = \
        Command.ReadDbBorderConfiguration()
    return Summary, int(Top), int(Bottom), int(Left), int(Right)

def WriteDbBorderWeight(BorderWeight) :
    return Command.WriteDbBorderWeight(BorderWeight)

def ReadDbBorderWeight() :
    Summary, BorderWeight = \
        Command.ReadDbBorderWeight()
    return Summary, BorderWeight

def WriteDbClipPixels(ClipPixels) :
    return Command.WriteDbClipPixels(ClipPixels)

def ReadDbClipPixels() :
    Summary, ClipPixels = \
        Command.ReadDbClipPixels()
    return Summary, int(ClipPixels)

def WriteDbGain(DbGain) :
    return Command.WriteDbGain(DbGain)

def ReadDbGain() :
    Summary, DbGain = \
        Command.ReadDbGain()
    return Summary, float(DbGain)

def WriteDbNumSteps(Steps) :
    return Command.WriteDbNumSteps(Steps)

def ReadDbNumSteps() :
    Summary, Steps = \
        Command.ReadDbNumSteps()
    return Summary, int(Steps)

def WriteDbApertureSpeed(Speed) :
    return Command.WriteDbApertureSpeed(Speed)

def ReadDbApertureSpeed() :
    Summary, Speed = \
        Command.ReadDbApertureSpeed()
    return Summary, int(Speed)

def WriteDbStrength(Strength) :
    return Command.WriteDbStrength(Strength)

def ReadDbStrength() :
    Summary, Strength = \
        Command.ReadDbStrength()
    return Summary, int(Strength)

def ReadDbHistogram() :
    Summary, HistPtr = \
        Command.ReadDbHistogram()
    return Summary, bytearray(HistPtr)

def ReadDbCurrentApertPos() :
    Summary, Position = \
        Command.ReadDbCurrentApertPos()
    return Summary, int(Position)

def ReadCurrentLedColorPoint() :
    Summary, ChromaticX, ChromaticY, LuminanceY = \
        Command.ReadCurrentLedColorPoint()
    return Summary, float(ChromaticX), float(ChromaticY), int(LuminanceY)

def WriteWpcOptimalDutyCycle() :
    return Command.WriteWpcOptimalDutyCycle()

def ReadWpcOptimalDutyCycle() :
    Summary, WpcOptimalDutyCycle = \
        Command.ReadWpcOptimalDutyCycle()
    return Summary, WpcOptimalDutyCycle

def WriteWpcCalibrationData(LedColor, ChromaticX, ChromaticY, LuminanceY) :
    return Command.WriteWpcCalibrationData(LedColor, ChromaticX, ChromaticY, LuminanceY)

def ReadWpcCalibrationData(LedColor) :
    Summary, WpcCalibrationData = \
        Command.ReadWpcCalibrationData(LedColor)
    return Summary, WpcCalibrationData

def ReadNumberOfBrightnessTableEntries(ReadFrom) :
    Summary, NumberOfEntries = \
        Command.ReadNumberOfBrightnessTableEntries(ReadFrom)
    return Summary, int(NumberOfEntries)

def WriteWpcBrightnessTableEntry(Index, AperturePosition, RedDriveLevel, GreenDriveLevel, BlueDriveLevel) :
    return Command.WriteWpcBrightnessTableEntry(Index, AperturePosition, RedDriveLevel, GreenDriveLevel, BlueDriveLevel)

def ReadWpcBrightnessTableEntry(ReadFrom, Index) :
    Summary, AperturePosition, RedDriveLevel, GreenDriveLevel, BlueDriveLevel = \
        Command.ReadWpcBrightnessTableEntry(ReadFrom, Index)
    return Summary, int(AperturePosition), int(RedDriveLevel), int(GreenDriveLevel), int(BlueDriveLevel)

def WriteTransferWpcBrightnessTableToEeprom() :
    return Command.WriteTransferWpcBrightnessTableToEeprom()

def WriteWpcBrightnessTableApertureValues(Size, ApertureValues) :
    ApertureValues = Array[UInt16](ApertureValues)
    return Command.WriteWpcBrightnessTableApertureValues(Size, ApertureValues)

def WriteWpcBrightnessTableBuildStart() :
    return Command.WriteWpcBrightnessTableBuildStart()

def ReadWpcBrightnessTableBuildStart() :
    Summary, TableUnderBuildProcess, CurrentBuildIndex = \
        Command.ReadWpcBrightnessTableBuildStart()
    return Summary, int(TableUnderBuildProcess), int(CurrentBuildIndex)

def WriteWpcBrightnessTableBuildAbort() :
    return Command.WriteWpcBrightnessTableBuildAbort()

def ReadWpcSensorOutput() :
    Summary, Red, Green, Blue = \
        Command.ReadWpcSensorOutput()
    return Summary, int(Red), int(Green), int(Blue)

def WriteMaximumSsiDriveLevel(Color, MaxDriveLevel) :
    return Command.WriteMaximumSsiDriveLevel(Color, MaxDriveLevel)

def ReadMaximumSsiDriveLevel(Color) :
    Summary, MaxDriveLevel = \
        Command.ReadMaximumSsiDriveLevel(Color)
    return Summary, int(MaxDriveLevel)

def WriteSsiDutyCycleIndex(Index) :
    return Command.WriteSsiDutyCycleIndex(Index)

def ReadSsiDutyCycleIndex() :
    Summary, SsiDutyCycleIndex = \
        Command.ReadSsiDutyCycleIndex()
    return Summary, SsiDutyCycleIndex

def WriteEnableXprCalibrationMode(Enable) :
    return Command.WriteEnableXprCalibrationMode(Enable)

def ReadEnableXprCalibrationMode() :
    Summary, Enable = \
        Command.ReadEnableXprCalibrationMode()
    return Summary, int(Enable)

def WriteWpcCalibrationStructureOverride(WpcCalibrationStructureOverride) :
    return Command.WriteWpcCalibrationStructureOverride(WpcCalibrationStructureOverride)

def WriteDebugMessageMask(DebugMessageMask) :
    return Command.WriteDebugMessageMask(DebugMessageMask)

def ReadDebugMessageMask() :
    Summary, DebugMessageMask = \
        Command.ReadDebugMessageMask()
    return Summary, DebugMessageMask

def WriteEnableUsbDebugLog(Enable) :
    return Command.WriteEnableUsbDebugLog(Enable)

def WriteEepromMemory(Index, Size, Pwd, Data) :
    Data = Array[Byte](Data)
    return Command.WriteEepromMemory(Index, Size, Pwd, Data)

def ReadEepromMemory(Index, Size) :
    Summary, Data = \
        Command.ReadEepromMemory(Index, Size)
    return Summary, bytearray(Data)

def WriteDlpa3005Register(RegisterAddress, RegisterValue) :
    return Command.WriteDlpa3005Register(RegisterAddress, RegisterValue)

def ReadDlpa3005Register(RegisterAddress) :
    Summary, RegisterValue = \
        Command.ReadDlpa3005Register(RegisterAddress)
    return Summary, int(RegisterValue)

def WriteTiActuatorInterfaceDebug(TiActQueryType, TiActAddr, TiActNumData) :
    return Command.WriteTiActuatorInterfaceDebug(TiActQueryType, TiActAddr, TiActNumData)

def ReadTiActuatorInterfaceDebug() :
    Summary, ActuatorData = \
        Command.ReadTiActuatorInterfaceDebug()
    return Summary, bytearray(ActuatorData)

def ReadVsyncPeriod() :
    Summary, FramePeriod = \
        Command.ReadVsyncPeriod()
    return Summary, int(FramePeriod)

def WriteSoftwareReset() :
    return Command.WriteSoftwareReset()

def ReadRstCountCause() :
    Summary, ResetCount, ResetCause = \
        Command.ReadRstCountCause()
    return Summary, int(ResetCount), int(ResetCause)

def ReadDmdPower() :
    Summary, Enable = \
        Command.ReadDmdPower()
    return Summary, bool(Enable)

def WriteDmdPark(Park) :
    return Command.WriteDmdPark(Park)

def ReadDmdPark() :
    Summary, Park = \
        Command.ReadDmdPark()
    return Summary, bool(Park)

def WriteDmdTrueGlobalReset(GlobalResetEnable) :
    return Command.WriteDmdTrueGlobalReset(GlobalResetEnable)

def ReadDmdTrueGlobalReset() :
    Summary, GlobalResetEnable = \
        Command.ReadDmdTrueGlobalReset()
    return Summary, bool(GlobalResetEnable)

def WriteTpmHardware(SigNo, SigType) :
    return Command.WriteTpmHardware(SigNo, SigType)

def ReadTpmHardware(SigNo) :
    Summary, SigType = \
        Command.ReadTpmHardware(SigNo)
    return Summary, int(SigType)

def WriteTpmSoftware(SigNo, SigType) :
    return Command.WriteTpmSoftware(SigNo, SigType)

def ReadTpmSoftware(SigNo) :
    Summary, SigType = \
        Command.ReadTpmSoftware(SigNo)
    return Summary, int(SigType)

def ReadIntStack() :
    Summary, StackSize, StackUsed, StackFree = \
        Command.ReadIntStack()
    return Summary, int(StackSize), int(StackUsed), int(StackFree)

def WritePrintAllTaskInformation() :
    return Command.WritePrintAllTaskInformation()

def ReadResource() :
    Summary, Resource = \
        Command.ReadResource()
    return Summary, Resource

def WriteCwStart(Start) :
    return Command.WriteCwStart(Start)

def ReadCwStart(Wheel) :
    Summary, Running = \
        Command.ReadCwStart(Wheel)
    return Summary, int(Running)

def WriteCwOperationStatus(CoastEnabled, EnableDebugMode) :
    return Command.WriteCwOperationStatus(CoastEnabled, EnableDebugMode)

def ReadCwOperationStatus() :
    Summary, CwGetSpinning, CwIsCoastEnabled, CwGetDebugMode = \
        Command.ReadCwOperationStatus()
    return Summary, int(CwGetSpinning), int(CwIsCoastEnabled), int(CwGetDebugMode)

def WriteCwSpeed(Speed) :
    return Command.WriteCwSpeed(Speed)

def ReadCwSpeed(Wheel) :
    Summary, Period, Frequency = \
        Command.ReadCwSpeed(Wheel)
    return Summary, int(Period), int(Frequency)

def WriteCwDualTrackMode(Mode) :
    return Command.WriteCwDualTrackMode(Mode)

def ReadCwDualTrackMode() :
    Summary, Mode = \
        Command.ReadCwDualTrackMode()
    return Summary, Mode

def WriteCwSpokeTestConfiguration(Enable, SpokeNumber, RevolutionNumber, Mode) :
    return Command.WriteCwSpokeTestConfiguration(Enable, SpokeNumber, RevolutionNumber, Mode)

def ReadCwSpokeTestConfiguration() :
    Summary, Enable, SpokeNumber, RevolutionNumber, Mode = \
        Command.ReadCwSpokeTestConfiguration()
    return Summary, int(Enable), int(SpokeNumber), int(RevolutionNumber), Mode

def WriteSeqEnable(Enable) :
    return Command.WriteSeqEnable(Enable)

def ReadSeqEnable() :
    Summary, SeqIsEnabled = \
        Command.ReadSeqEnable()
    return Summary, int(SeqIsEnabled)

def ReadEepromFreeAreaOffset() :
    Summary, FreeAreaOffset = \
        Command.ReadEepromFreeAreaOffset()
    return Summary, int(FreeAreaOffset)

def ReadVx1HwStatus() :
    Summary, Vx1HwStatus = \
        Command.ReadVx1HwStatus()
    return Summary, Vx1HwStatus

def WritePower() :
    return Command.WritePower()

def ReadPower() :
    Summary, PowerState = \
        Command.ReadPower()
    return Summary, PowerState

def WriteDisplay(Source) :
    return Command.WriteDisplay(Source)

def ReadDisplay() :
    Summary, Source = \
        Command.ReadDisplay()
    return Summary, Source

def WriteEnableLowLatencyMode(Enable) :
    return Command.WriteEnableLowLatencyMode(Enable)

def ReadEnableLowLatencyMode() :
    Summary, Enable = \
        Command.ReadEnableLowLatencyMode()
    return Summary, bool(Enable)

def WriteSystemLook(System) :
    return Command.WriteSystemLook(System)

def ReadSystemLook() :
    Summary, System = \
        Command.ReadSystemLook()
    return Summary, int(System)

def WriteTpgBorder(Width, BorderColorRed, BorderColorGreen, BorderColorBlue) :
    return Command.WriteTpgBorder(Width, BorderColorRed, BorderColorGreen, BorderColorBlue)

def ReadTpgBorder() :
    Summary, Width, BorderColorRed, BorderColorGreen, BorderColorBlue = \
        Command.ReadTpgBorder()
    return Summary, int(Width), int(BorderColorRed), int(BorderColorGreen), int(BorderColorBlue)

def WriteTpgResolution(HorizontalResolution, VerticalResolution) :
    return Command.WriteTpgResolution(HorizontalResolution, VerticalResolution)

def ReadTpgResolution() :
    Summary, HorizontalResolution, VerticalResolution = \
        Command.ReadTpgResolution()
    return Summary, int(HorizontalResolution), int(VerticalResolution)

def WriteTpgFrameRate(FrameRate) :
    return Command.WriteTpgFrameRate(FrameRate)

def ReadTpgFrameRate() :
    Summary, FrameRate = \
        Command.ReadTpgFrameRate()
    return Summary, int(FrameRate)

def WriteSfgColor(Red, Green, Blue) :
    return Command.WriteSfgColor(Red, Green, Blue)

def ReadSfgColor() :
    Summary, Red, Green, Blue = \
        Command.ReadSfgColor()
    return Summary, int(Red), int(Green), int(Blue)

def WriteCurtainColor(Color) :
    return Command.WriteCurtainColor(Color)

def ReadCurtainColor() :
    Summary, Color = \
        Command.ReadCurtainColor()
    return Summary, Color

def WriteSplashLoadImage(Index) :
    return Command.WriteSplashLoadImage(Index)

def ReadSplashLoadImage() :
    Summary, Index = \
        Command.ReadSplashLoadImage()
    return Summary, int(Index)

def WriteEnableImageFlip(VertFlip, HorzFlip) :
    return Command.WriteEnableImageFlip(VertFlip, HorzFlip)

def ReadEnableImageFlip() :
    Summary, VertFlip, HorzFlip = \
        Command.ReadEnableImageFlip()
    return Summary, bool(VertFlip), bool(HorzFlip)

def WriteEnableFreeze(Freeze) :
    return Command.WriteEnableFreeze(Freeze)

def ReadEnableFreeze() :
    Summary, Freeze = \
        Command.ReadEnableFreeze()
    return Summary, bool(Freeze)

def WriteKeystoneAngles(Pitch, Yaw, Roll) :
    return Command.WriteKeystoneAngles(Pitch, Yaw, Roll)

def ReadKeystoneAngles() :
    Summary, Pitch, Yaw, Roll = \
        Command.ReadKeystoneAngles()
    return Summary, float(Pitch), float(Yaw), float(Roll)

def WriteKeystoneConfigOverride(ThrowRatio, VerticalOffset) :
    return Command.WriteKeystoneConfigOverride(ThrowRatio, VerticalOffset)

def ReadKeystoneConfigOverride() :
    Summary, ThrowRatio, VerticalOffset = \
        Command.ReadKeystoneConfigOverride()
    return Summary, float(ThrowRatio), float(VerticalOffset)

def WriteEnableAnamorphicScaling(Enable) :
    return Command.WriteEnableAnamorphicScaling(Enable)

def ReadEnableAnamorphicScaling() :
    Summary, Enable = \
        Command.ReadEnableAnamorphicScaling()
    return Summary, bool(Enable)

def WriteDisplayImageSize(DisplayImageSize) :
    return Command.WriteDisplayImageSize(DisplayImageSize)

def ReadDisplayImageSize() :
    Summary, DisplayImageSize = \
        Command.ReadDisplayImageSize()
    return Summary, DisplayImageSize

def WriteSourceConfiguration(SourceConfiguration) :
    return Command.WriteSourceConfiguration(SourceConfiguration)

def ReadSourceConfiguration() :
    Summary, SourceConfiguration = \
        Command.ReadSourceConfiguration()
    return Summary, SourceConfiguration

def ReadDatapathScanStatus() :
    Summary, ScanStatus, DatapathState = \
        Command.ReadDatapathScanStatus()
    return Summary, ScanStatus, DatapathState

def ReadFrameRateParms() :
    Summary, InputFrameRate, OutputFrameRate, FrcMode = \
        Command.ReadFrameRateParms()
    return Summary, float(InputFrameRate), float(OutputFrameRate), FrcMode

def WriteXprEnableModeCommand(Mode) :
    return Command.WriteXprEnableModeCommand(Mode)

def ReadXprEnableModeCommand() :
    Summary, Mode = \
        Command.ReadXprEnableModeCommand()
    return Summary, Mode

def ReadExecutionTimeOfLastCommandSent() :
    Summary, CommandId, CommandExecutionTime, TotalExecutionTime = \
        Command.ReadExecutionTimeOfLastCommandSent()
    return Summary, int(CommandId), int(CommandExecutionTime), int(TotalExecutionTime)

def WriteVboConfiguration(DataMapMode, ByteMode, NumberOfLanes, EnablePixelRepeat) :
    return Command.WriteVboConfiguration(DataMapMode, ByteMode, NumberOfLanes, EnablePixelRepeat)

def ReadVboConfiguration() :
    Summary, DataMapMode, ByteMode, NumberOfLanes, EnablePixelRepeat = \
        Command.ReadVboConfiguration()
    return Summary, DataMapMode, ByteMode, int(NumberOfLanes), bool(EnablePixelRepeat)

def WriteFpdConfiguration(FpdMode, DataInterfaceMode, Enable3DRef, EnableField, EnablePixelRepeat) :
    return Command.WriteFpdConfiguration(FpdMode, DataInterfaceMode, Enable3DRef, EnableField, EnablePixelRepeat)

def ReadFpdConfiguration() :
    Summary, FpdMode, DataInterfaceMode, Enable3DRef, EnableField, EnablePixelRepeat = \
        Command.ReadFpdConfiguration()
    return Summary, FpdMode, DataInterfaceMode, bool(Enable3DRef), bool(EnableField), bool(EnablePixelRepeat)

def WriteKeystoneCorners(KeystoneCorners) :
    return Command.WriteKeystoneCorners(KeystoneCorners)

def ReadKeystoneCorners() :
    Summary, KeystoneCorners = \
        Command.ReadKeystoneCorners()
    return Summary, KeystoneCorners

def WriteWarpTimingValidationEnableAdjustWrp(Enable) :
    return Command.WriteWarpTimingValidationEnableAdjustWrp(Enable)

def ReadWarpTimingValidationEnableAdjustWrp() :
    Summary, Enable = \
        Command.ReadWarpTimingValidationEnableAdjustWrp()
    return Summary, bool(Enable)

def ReadIsWarpGeometryModified() :
    Summary, State = \
        Command.ReadIsWarpGeometryModified()
    return Summary, bool(State)

def WriteIlluminationEnable(Enable) :
    return Command.WriteIlluminationEnable(Enable)

def ReadIlluminationEnable() :
    Summary, Enable = \
        Command.ReadIlluminationEnable()
    return Summary, int(Enable)

def WriteDlpa3005IlluminationCurrent(DriveLevelRed, DriveLevelGreen, DriveLevelBlue) :
    return Command.WriteDlpa3005IlluminationCurrent(DriveLevelRed, DriveLevelGreen, DriveLevelBlue)

def ReadDlpa3005IlluminationCurrent() :
    Summary, DriveLevelRed, DriveLevelGreen, DriveLevelBlue = \
        Command.ReadDlpa3005IlluminationCurrent()
    return Summary, int(DriveLevelRed), int(DriveLevelGreen), int(DriveLevelBlue)

def WriteSsiDriveLevels(PwmGroup, SsiDriveLevels) :
    return Command.WriteSsiDriveLevels(PwmGroup, SsiDriveLevels)

def ReadSsiDriveLevels(PwmGroup) :
    Summary, SsiDriveLevels = \
        Command.ReadSsiDriveLevels(PwmGroup)
    return Summary, SsiDriveLevels

def WriteVarLmpEnableComms(Enable) :
    return Command.WriteVarLmpEnableComms(Enable)

def ReadVarLmpEnableComms() :
    Summary, Enable = \
        Command.ReadVarLmpEnableComms()
    return Summary, int(Enable)

def WriteVarLmpWaveformIndex(WaveformIndex) :
    return Command.WriteVarLmpWaveformIndex(WaveformIndex)

def ReadVarLmpWaveformIndex() :
    Summary, WaveformIndex = \
        Command.ReadVarLmpWaveformIndex()
    return Summary, int(WaveformIndex)

def ReadVarLmpWaveformId() :
    Summary, WaveformId = \
        Command.ReadVarLmpWaveformId()
    return Summary, int(WaveformId)

def ReadVarLmpNumOfWaveForms() :
    Summary, NumWaveforms = \
        Command.ReadVarLmpNumOfWaveForms()
    return Summary, int(NumWaveforms)

def WriteVarLmpWaveformGain(WaveformGain) :
    return Command.WriteVarLmpWaveformGain(WaveformGain)

def ReadVarLmpWaveformGain() :
    Summary, WaveformGain = \
        Command.ReadVarLmpWaveformGain()
    return Summary, int(WaveformGain)

def WriteLmpSyncType(SyncType, NegativePolarity, LampSyncSel) :
    return Command.WriteLmpSyncType(SyncType, NegativePolarity, LampSyncSel)

def ReadLmpSyncType() :
    Summary, SyncType, NegativePolarity, LampSyncSel = \
        Command.ReadLmpSyncType()
    return Summary, SyncType, int(NegativePolarity), int(LampSyncSel)

def WriteLmpSyncDelay(ThisDelay) :
    return Command.WriteLmpSyncDelay(ThisDelay)

def ReadLmpSyncDelay() :
    Summary, ThisDelay = \
        Command.ReadLmpSyncDelay()
    return Summary, int(ThisDelay)

def ReadVarLmpMinGain() :
    Summary, MinGain = \
        Command.ReadVarLmpMinGain()
    return Summary, int(MinGain)

def ReadVarLmpMaxGain() :
    Summary, MaxGain = \
        Command.ReadVarLmpMaxGain()
    return Summary, int(MaxGain)

def ReadVarLmpManufactureId() :
    Summary, ManufacturerId = \
        Command.ReadVarLmpManufactureId()
    return Summary, int(ManufacturerId)

def ReadVarLmpBallastId() :
    Summary, BallastId = \
        Command.ReadVarLmpBallastId()
    return Summary, int(BallastId)

def ReadVarLmpBallastStatus() :
    Summary, BallastStatus = \
        Command.ReadVarLmpBallastStatus()
    return Summary, int(BallastStatus)

def ReadVarLmpLampStatus() :
    Summary, SafeMode, ErrorCode = \
        Command.ReadVarLmpLampStatus()
    return Summary, int(SafeMode), int(ErrorCode)

def WriteLmpDynGain(PowerGain) :
    return Command.WriteLmpDynGain(PowerGain)

def WriteLmpDynGainState(State) :
    return Command.WriteLmpDynGainState(State)

def ReadLmpDynGainStatus() :
    Summary, LmpDynGainStatus = \
        Command.ReadLmpDynGainStatus()
    return Summary, LmpDynGainStatus

def WriteLmpWaveformIndexOverride(WaveformIndexOverrideEnable) :
    return Command.WriteLmpWaveformIndexOverride(WaveformIndexOverrideEnable)

def ReadLmpWaveformIndexOverride() :
    Summary, WaveformIndexOverrideEnable = \
        Command.ReadLmpWaveformIndexOverride()
    return Summary, int(WaveformIndexOverrideEnable)

def WriteImageAlgorithmEnable(ImageAlgorithmEnable) :
    return Command.WriteImageAlgorithmEnable(ImageAlgorithmEnable)

def ReadImageAlgorithmEnable() :
    Summary, ImageAlgorithmEnable = \
        Command.ReadImageAlgorithmEnable()
    return Summary, ImageAlgorithmEnable

def WriteImageBrightness(BrightnessAdjustment) :
    return Command.WriteImageBrightness(BrightnessAdjustment)

def ReadImageBrightness() :
    Summary, BrightnessAdjustment = \
        Command.ReadImageBrightness()
    return Summary, float(BrightnessAdjustment)

def WriteImageContrast(Contrast) :
    return Command.WriteImageContrast(Contrast)

def ReadImageContrast() :
    Summary, Contrast = \
        Command.ReadImageContrast()
    return Summary, int(Contrast)

def WriteImageHueAndColorControl(HueAdjustmentAngle, ColorControlGain) :
    return Command.WriteImageHueAndColorControl(HueAdjustmentAngle, ColorControlGain)

def ReadImageHueAndColorControl() :
    Summary, HueAdjustmentAngle, ColorControlGain = \
        Command.ReadImageHueAndColorControl()
    return Summary, int(HueAdjustmentAngle), int(ColorControlGain)

def WriteImageSharpness(Sharpness) :
    return Command.WriteImageSharpness(Sharpness)

def ReadImageSharpness() :
    Summary, Sharpness = \
        Command.ReadImageSharpness()
    return Summary, int(Sharpness)

def WriteImageRgbOffset(RedOffset, GreenOffset, BlueOffset) :
    return Command.WriteImageRgbOffset(RedOffset, GreenOffset, BlueOffset)

def ReadImageRgbOffset() :
    Summary, RedOffset, GreenOffset, BlueOffset = \
        Command.ReadImageRgbOffset()
    return Summary, float(RedOffset), float(GreenOffset), float(BlueOffset)

def WriteImageRgbGain(RedGain, GreenGain, BlueGain) :
    return Command.WriteImageRgbGain(RedGain, GreenGain, BlueGain)

def ReadImageRgbGain() :
    Summary, RedGain, GreenGain, BlueGain = \
        Command.ReadImageRgbGain()
    return Summary, int(RedGain), int(GreenGain), int(BlueGain)

def WriteCscTable(Index) :
    return Command.WriteCscTable(Index)

def ReadCscTable() :
    Summary, Index = \
        Command.ReadCscTable()
    return Summary, Index

def WriteImageCcaCoordinates(ImageCcaCoordinates) :
    return Command.WriteImageCcaCoordinates(ImageCcaCoordinates)

def ReadImageCcaCoordinates() :
    Summary, ImageCcaCoordinates = \
        Command.ReadImageCcaCoordinates()
    return Summary, ImageCcaCoordinates

def WriteImageHsg(ImageHsg) :
    return Command.WriteImageHsg(ImageHsg)

def ReadImageHsg() :
    Summary, ImageHsg = \
        Command.ReadImageHsg()
    return Summary, ImageHsg

def WriteImageGammaLut(GammaLutNumber) :
    return Command.WriteImageGammaLut(GammaLutNumber)

def ReadImageGammaLut() :
    Summary, GammaLutNumber = \
        Command.ReadImageGammaLut()
    return Summary, int(GammaLutNumber)

def WriteImageGammaCurveShift(RedShift, GreenShift, BlueShift, AllColorShift) :
    return Command.WriteImageGammaCurveShift(RedShift, GreenShift, BlueShift, AllColorShift)

def ReadImageGammaCurveShift() :
    Summary, RedShift, GreenShift, BlueShift, AllColorShift = \
        Command.ReadImageGammaCurveShift()
    return Summary, int(RedShift), int(GreenShift), int(BlueShift), int(AllColorShift)

def WriteImgWhitePeakingFactor(WhitePeakingVal) :
    return Command.WriteImgWhitePeakingFactor(WhitePeakingVal)

def ReadImgWhitePeakingFactor() :
    Summary, WhitePeakingVal = \
        Command.ReadImgWhitePeakingFactor()
    return Summary, int(WhitePeakingVal)

def WriteXprFilterStrengthCommand(Strength) :
    return Command.WriteXprFilterStrengthCommand(Strength)

def ReadXprFilterStrengthCommand() :
    Summary, Strength = \
        Command.ReadXprFilterStrengthCommand()
    return Summary, int(Strength)

def WriteHdrSourceConfiguration(HdrSourceConfiguration) :
    return Command.WriteHdrSourceConfiguration(HdrSourceConfiguration)

def ReadHdrSourceConfiguration() :
    Summary, HdrSourceConfiguration = \
        Command.ReadHdrSourceConfiguration()
    return Summary, HdrSourceConfiguration

def WriteHdrStrengthSetting(HdrStrength) :
    return Command.WriteHdrStrengthSetting(HdrStrength)

def ReadHdrStrengthSetting() :
    Summary, HdrStrength = \
        Command.ReadHdrStrengthSetting()
    return Summary, int(HdrStrength)

def WriteSystemBrightnessRangeSetting(MinBrightness, MaxBrightness) :
    return Command.WriteSystemBrightnessRangeSetting(MinBrightness, MaxBrightness)

def ReadSystemBrightnessRangeSetting() :
    Summary, MinBrightness, MaxBrightness = \
        Command.ReadSystemBrightnessRangeSetting()
    return Summary, float(MinBrightness), float(MaxBrightness)

def WriteImageColorProfile(ColorProfile) :
    return Command.WriteImageColorProfile(ColorProfile)

def WriteImagePointHsg(Point, ImagePointHsg) :
    return Command.WriteImagePointHsg(Point, ImagePointHsg)

def ReadImagePointHsg(Point) :
    Summary, ImagePointHsg = \
        Command.ReadImagePointHsg(Point)
    return Summary, ImagePointHsg

def WriteSpccControlPoints(ControlPointY, ControlPointX1, ControlPointX2) :
    return Command.WriteSpccControlPoints(ControlPointY, ControlPointX1, ControlPointX2)

def ReadSpccControlPoints() :
    Summary, ControlPointY, ControlPointX1, ControlPointX2 = \
        Command.ReadSpccControlPoints()
    return Summary, int(ControlPointY), int(ControlPointX1), int(ControlPointX2)

def WritePccCoefficientsDirect(Point, PccCoefficientsDirect) :
    return Command.WritePccCoefficientsDirect(Point, PccCoefficientsDirect)

def ReadPccCoefficientsDirect(Point) :
    Summary, PccCoefficientsDirect = \
        Command.ReadPccCoefficientsDirect(Point)
    return Summary, PccCoefficientsDirect

def WriteWpcTargetManualMode(Enable) :
    return Command.WriteWpcTargetManualMode(Enable)

def ReadWpcTargetManualMode() :
    Summary, Enable = \
        Command.ReadWpcTargetManualMode()
    return Summary, int(Enable)

def WriteWpcTargetColorPoint(CieX, CieY) :
    return Command.WriteWpcTargetColorPoint(CieX, CieY)

def ReadWpcTargetColorPoint() :
    Summary, CieX, CieY = \
        Command.ReadWpcTargetColorPoint()
    return Summary, float(CieX), float(CieY)

def WriteGpioPinConfig(PinNumber, Output, LogicVal, OpenDrain) :
    return Command.WriteGpioPinConfig(PinNumber, Output, LogicVal, OpenDrain)

def ReadGpioPinConfig(PinNumber) :
    Summary, Output, LogicVal, OpenDrain = \
        Command.ReadGpioPinConfig(PinNumber)
    return Summary, bool(Output), bool(LogicVal), bool(OpenDrain)

def WriteGpioPin(PinNumber, LogicVal) :
    return Command.WriteGpioPin(PinNumber, LogicVal)

def ReadGpioPin(PinNumber) :
    Summary, LogicVal = \
        Command.ReadGpioPin(PinNumber)
    return Summary, bool(LogicVal)

def WriteStatusIntMask(StatusIntMask) :
    return Command.WriteStatusIntMask(StatusIntMask)

def ReadStatusIntMask() :
    Summary, StatusIntMask = \
        Command.ReadStatusIntMask()
    return Summary, StatusIntMask

def WriteGenPurpseClockEnable(Clk, Enabled, Freq) :
    return Command.WriteGenPurpseClockEnable(Clk, Enabled, Freq)

def ReadGenPurpseClockEnable(Clk) :
    Summary, IsEnabled = \
        Command.ReadGenPurpseClockEnable(Clk)
    return Summary, int(IsEnabled)

def ReadGenPurpseClockFrequency(Clk) :
    Summary, Freq = \
        Command.ReadGenPurpseClockFrequency(Clk)
    return Summary, int(Freq)

def WritePwmOutputConfiguration(Port, Frequency, DutyCycle, OutputEnabled) :
    return Command.WritePwmOutputConfiguration(Port, Frequency, DutyCycle, OutputEnabled)

def ReadPwmOutputConfiguration(Port) :
    Summary, Frequency, DutyCycle, OutputEnabledBit = \
        Command.ReadPwmOutputConfiguration(Port)
    return Summary, int(Frequency), int(DutyCycle), bool(OutputEnabledBit)

def WritePwmInputConfiguration(Port, SampleRate, InCounterEnabled) :
    return Command.WritePwmInputConfiguration(Port, SampleRate, InCounterEnabled)

def ReadPwmInputConfiguration(Port) :
    Summary, SampleRate, InCounterEnabled, HighPulseWidth, LowPulseWidth, DutyCycle = \
        Command.ReadPwmInputConfiguration(Port)
    return Summary, int(SampleRate), int(InCounterEnabled), int(HighPulseWidth), int(LowPulseWidth), int(DutyCycle)

def WriteI2CPassthrough(I2CPassthrough) :
    return Command.WriteI2CPassthrough(I2CPassthrough)

def ReadI2CPassthrough(Port, Is7Bit, HasSubaddr, ClockRate, DeviceAddress, ByteCount, SubAddr) :
    Summary, DataBytes = \
        Command.ReadI2CPassthrough(Port, Is7Bit, HasSubaddr, ClockRate, DeviceAddress, ByteCount, SubAddr)
    return Summary, bytearray(DataBytes)

def WriteCwPwmConfiguration(Port, Enable, DutyCycle) :
    return Command.WriteCwPwmConfiguration(Port, Enable, DutyCycle)

def ReadCwPwmConfiguration(Port) :
    Summary, Available, Enable, DutyCycle = \
        Command.ReadCwPwmConfiguration(Port)
    return Summary, int(Available), int(Enable), int(DutyCycle)

def ReadDmdTemperature() :
    Summary, Temperature = \
        Command.ReadDmdTemperature()
    return Summary, int(Temperature)

def WriteLmpFanCtl(FanNum, SwFreq, DutyCycle, Select) :
    return Command.WriteLmpFanCtl(FanNum, SwFreq, DutyCycle, Select)

def ReadLmpFanCtl(FanNum, Select) :
    Summary, SwFreq, DutyCycle = \
        Command.ReadLmpFanCtl(FanNum, Select)
    return Summary, int(SwFreq), int(DutyCycle)

def WriteEepromLockState(LockState) :
    return Command.WriteEepromLockState(LockState)

def ReadEepromLockState() :
    Summary, LockState = \
        Command.ReadEepromLockState()
    return Summary, int(LockState)

def WriteUartConfiguration(Port, UartConfiguration) :
    return Command.WriteUartConfiguration(Port, UartConfiguration)

def ReadUartConfiguration(Port) :
    Summary, UartConfiguration = \
        Command.ReadUartConfiguration(Port)
    return Summary, UartConfiguration

def WriteActuatorEepromFreeMemoryAccess(Offset, Size, DataBytes) :
    DataBytes = Array[Byte](DataBytes)
    return Command.WriteActuatorEepromFreeMemoryAccess(Offset, Size, DataBytes)

def ReadActuatorEepromFreeMemoryAccess(Offset, Size) :
    Summary, DataBytes = \
        Command.ReadActuatorEepromFreeMemoryAccess(Offset, Size)
    return Summary, bytearray(DataBytes)

def ReadActuatorEepromFreeMemoryInfo() :
    Summary, Offset, Size = \
        Command.ReadActuatorEepromFreeMemoryInfo()
    return Summary, int(Offset), int(Size)

def WriteManualWarpTable(WarpTableIndex, WarpPoints) :
    WarpPoints = Array[UInt16](WarpPoints)
    return Command.WriteManualWarpTable(WarpTableIndex, WarpPoints)

def ReadManualWarpTable(WarpTableIndex, NumEntries) :
    Summary, WarpPoints = \
        Command.ReadManualWarpTable(WarpTableIndex, NumEntries)
    return Summary, list(WarpPoints)

def WriteManualWarpControlPoints(ControlPointsDefinedByArray, HorizontalCtrlPoints, VerticalCtrlPoints) :
    HorizontalCtrlPoints = Array[UInt16](HorizontalCtrlPoints)
    VerticalCtrlPoints = Array[UInt16](VerticalCtrlPoints)
    return Command.WriteManualWarpControlPoints(ControlPointsDefinedByArray, HorizontalCtrlPoints, VerticalCtrlPoints)

def ReadManualWarpControlPoints() :
    Summary, ControlPointsDefinedByArray, CtrlPoints = \
        Command.ReadManualWarpControlPoints()
    return Summary, int(ControlPointsDefinedByArray), list(CtrlPoints)

def WriteApplyManualWarping(WarpEnabled) :
    return Command.WriteApplyManualWarping(WarpEnabled)

def ReadApplyManualWarping() :
    Summary, ManualWarpEnabled, SurfaceCorrectionWarpEnabled, LensCorrectionWarpEnabled = \
        Command.ReadApplyManualWarping()
    return Summary, bool(ManualWarpEnabled), bool(SurfaceCorrectionWarpEnabled), bool(LensCorrectionWarpEnabled)

def WriteSmoothWarpTable(NumColumns, NumRows, SmoothWarpPoints) :
    SmoothWarpPoints = Array[UInt16](SmoothWarpPoints)
    return Command.WriteSmoothWarpTable(NumColumns, NumRows, SmoothWarpPoints)

def ReadSmoothWarpTable() :
    Summary, NumColumns, NumRows, SmoothWarpPoints = \
        Command.ReadSmoothWarpTable()
    return Summary, int(NumColumns), int(NumRows), list(SmoothWarpPoints)

def WriteManualWarpTableUpdateMode(Mode) :
    return Command.WriteManualWarpTableUpdateMode(Mode)

def ReadManualWarpTableUpdateMode() :
    Summary, Mode = \
        Command.ReadManualWarpTableUpdateMode()
    return Summary, int(Mode)

def WritePadChipIdentificationRegister(RevId, ChipId) :
    return Command.WritePadChipIdentificationRegister(RevId, ChipId)

def ReadPadChipIdentificationRegister() :
    Summary, RevId, ChipId = \
        Command.ReadPadChipIdentificationRegister()
    return Summary, int(RevId), int(ChipId)

def WritePadEnableRegister(PadEnableRegister) :
    return Command.WritePadEnableRegister(PadEnableRegister)

def ReadPadEnableRegister() :
    Summary, PadEnableRegister = \
        Command.ReadPadEnableRegister()
    return Summary, PadEnableRegister

def WritePadIregSwitchControl(IllumSwCurrentLimitEnable, IllumSwCurrentLimit) :
    return Command.WritePadIregSwitchControl(IllumSwCurrentLimitEnable, IllumSwCurrentLimit)

def ReadPadIregSwitchControl() :
    Summary, IllumSwCurrentLimitEnable, IllumSwCurrentLimit = \
        Command.ReadPadIregSwitchControl()
    return Summary, int(IllumSwCurrentLimitEnable), int(IllumSwCurrentLimit)

def WritePadSw1IdacMsbBits8And9(SwLedCurrentCh1Msb) :
    return Command.WritePadSw1IdacMsbBits8And9(SwLedCurrentCh1Msb)

def ReadPadSw1IdacMsbBits8And9() :
    Summary, SwLedCurrentCh1Msb = \
        Command.ReadPadSw1IdacMsbBits8And9()
    return Summary, int(SwLedCurrentCh1Msb)

def WritePadSw1IdacLsbBits0To7(SwLedCurrentCh1Lsb) :
    return Command.WritePadSw1IdacLsbBits0To7(SwLedCurrentCh1Lsb)

def ReadPadSw1IdacLsbBits0To7() :
    Summary, SwLedCurrentCh1Lsb = \
        Command.ReadPadSw1IdacLsbBits0To7()
    return Summary, int(SwLedCurrentCh1Lsb)

def WritePadSw2IdacMsbBits8And9(SwLedCurrentCh2Msb) :
    return Command.WritePadSw2IdacMsbBits8And9(SwLedCurrentCh2Msb)

def ReadPadSw2IdacMsbBits8And9() :
    Summary, SwLedCurrentCh2Msb = \
        Command.ReadPadSw2IdacMsbBits8And9()
    return Summary, int(SwLedCurrentCh2Msb)

def WritePadSw2IdacLsbBits0To7(SwLedCurrentCh2Lsb) :
    return Command.WritePadSw2IdacLsbBits0To7(SwLedCurrentCh2Lsb)

def ReadPadSw2IdacLsbBits0To7() :
    Summary, SwLedCurrentCh2Lsb = \
        Command.ReadPadSw2IdacLsbBits0To7()
    return Summary, int(SwLedCurrentCh2Lsb)

def WritePadSw3IdacMsbBits8And9(SwLedCurrentCh3Msb) :
    return Command.WritePadSw3IdacMsbBits8And9(SwLedCurrentCh3Msb)

def ReadPadSw3IdacMsbBits8And9() :
    Summary, SwLedCurrentCh3Msb = \
        Command.ReadPadSw3IdacMsbBits8And9()
    return Summary, int(SwLedCurrentCh3Msb)

def WritePadSw3IdacLsbBits0To7(SwLedCurrentCh3Lsb) :
    return Command.WritePadSw3IdacLsbBits0To7(SwLedCurrentCh3Lsb)

def ReadPadSw3IdacLsbBits0To7() :
    Summary, SwLedCurrentCh3Lsb = \
        Command.ReadPadSw3IdacLsbBits0To7()
    return Summary, int(SwLedCurrentCh3Lsb)

def WritePadSwitchOnOffControl(Sw1Enable, Sw2Enable, Sw3Enable) :
    return Command.WritePadSwitchOnOffControl(Sw1Enable, Sw2Enable, Sw3Enable)

def ReadPadSwitchOnOffControl() :
    Summary, Sw1Enable, Sw2Enable, Sw3Enable = \
        Command.ReadPadSwitchOnOffControl()
    return Summary, bool(Sw1Enable), bool(Sw2Enable), bool(Sw3Enable)

def WritePadAnalogFrontEnd1(AfeSel, AfeGain, AfeCalDisable, AfeEnable) :
    return Command.WritePadAnalogFrontEnd1(AfeSel, AfeGain, AfeCalDisable, AfeEnable)

def ReadPadAnalogFrontEnd1() :
    Summary, AfeSel, AfeGain, AfeCalDisable, AfeEnable = \
        Command.ReadPadAnalogFrontEnd1()
    return Summary, int(AfeSel), int(AfeGain), bool(AfeCalDisable), bool(AfeEnable)

def WritePadAnalogFrontEnd2(AfeDivSel, SampleLabbEnable, TsampleSel) :
    return Command.WritePadAnalogFrontEnd2(AfeDivSel, SampleLabbEnable, TsampleSel)

def ReadPadAnalogFrontEnd2() :
    Summary, AfeDivSel, SampleLabbEnable, TsampleSel = \
        Command.ReadPadAnalogFrontEnd2()
    return Summary, int(AfeDivSel), bool(SampleLabbEnable), int(TsampleSel)

def WritePadMainStatusRegister(PadMainStatusRegister) :
    return Command.WritePadMainStatusRegister(PadMainStatusRegister)

def ReadPadMainStatusRegister() :
    Summary, PadMainStatusRegister = \
        Command.ReadPadMainStatusRegister()
    return Summary, PadMainStatusRegister

def WritePadInterruptMaskRegister(PadInterruptMaskRegister) :
    return Command.WritePadInterruptMaskRegister(PadInterruptMaskRegister)

def ReadPadInterruptMaskRegister() :
    Summary, PadInterruptMaskRegister = \
        Command.ReadPadInterruptMaskRegister()
    return Summary, PadInterruptMaskRegister

def WritePadBreakBeforeMakeDelay(BbmDelay) :
    return Command.WritePadBreakBeforeMakeDelay(BbmDelay)

def ReadPadBreakBeforeMakeDelay() :
    Summary, BbmDelay = \
        Command.ReadPadBreakBeforeMakeDelay()
    return Summary, int(BbmDelay)

def WritePadFastShutdownTimingReg(Vbias, Vofs) :
    return Command.WritePadFastShutdownTimingReg(Vbias, Vofs)

def ReadPadFastShutdownTimingReg() :
    Summary, Vbias, Vofs = \
        Command.ReadPadFastShutdownTimingReg()
    return Summary, int(Vbias), int(Vofs)

def WritePadVofsStateDurationReg(LowbattSel, VofsStateDuration) :
    return Command.WritePadVofsStateDurationReg(LowbattSel, VofsStateDuration)

def ReadPadVofsStateDurationReg() :
    Summary, LowbattSel, VofsStateDuration = \
        Command.ReadPadVofsStateDurationReg()
    return Summary, int(LowbattSel), int(VofsStateDuration)

def WritePadVbiasStateDurationReg(UvloSel, VbiasStateDuration) :
    return Command.WritePadVbiasStateDurationReg(UvloSel, VbiasStateDuration)

def ReadPadVbiasStateDurationReg() :
    Summary, UvloSel, VbiasStateDuration = \
        Command.ReadPadVbiasStateDurationReg()
    return Summary, int(UvloSel), int(VbiasStateDuration)

def WritePadGp1BuckConverterVoltageSelection(BuckGp1ConvVoltageSel) :
    return Command.WritePadGp1BuckConverterVoltageSelection(BuckGp1ConvVoltageSel)

def ReadPadGp1BuckConverterVoltageSelection() :
    Summary, BuckGp1ConvVoltageSel = \
        Command.ReadPadGp1BuckConverterVoltageSelection()
    return Summary, int(BuckGp1ConvVoltageSel)

def WritePadGp2BuckConverterVoltageSelection(BuckGp2ConvVoltageSel) :
    return Command.WritePadGp2BuckConverterVoltageSelection(BuckGp2ConvVoltageSel)

def ReadPadGp2BuckConverterVoltageSelection() :
    Summary, BuckGp2ConvVoltageSel = \
        Command.ReadPadGp2BuckConverterVoltageSelection()
    return Summary, int(BuckGp2ConvVoltageSel)

def WritePadGp3BuckConverterVoltageSelection(BuckGp3ConvVoltageSel) :
    return Command.WritePadGp3BuckConverterVoltageSelection(BuckGp3ConvVoltageSel)

def ReadPadGp3BuckConverterVoltageSelection() :
    Summary, BuckGp3ConvVoltageSel = \
        Command.ReadPadGp3BuckConverterVoltageSelection()
    return Summary, int(BuckGp3ConvVoltageSel)

def WritePadGp1BuckSkipMode(BuckGp1ConvVoltageSel) :
    return Command.WritePadGp1BuckSkipMode(BuckGp1ConvVoltageSel)

def ReadPadGp1BuckSkipMode() :
    Summary, BuckGp1ConvVoltageSel = \
        Command.ReadPadGp1BuckSkipMode()
    return Summary, int(BuckGp1ConvVoltageSel)

def WritePadUserConfigurationSelection(PadUserConfigurationSelection) :
    return Command.WritePadUserConfigurationSelection(PadUserConfigurationSelection)

def ReadPadUserConfigurationSelection() :
    Summary, PadUserConfigurationSelection = \
        Command.ReadPadUserConfigurationSelection()
    return Summary, PadUserConfigurationSelection

def WritePadOlvLaserBypassVinDivisionFactor(IllumLaserBypEl, IllumOlvSel) :
    return Command.WritePadOlvLaserBypassVinDivisionFactor(IllumLaserBypEl, IllumOlvSel)

def ReadPadOlvLaserBypassVinDivisionFactor() :
    Summary, IllumLaserBypEl, IllumOlvSel = \
        Command.ReadPadOlvLaserBypassVinDivisionFactor()
    return Summary, int(IllumLaserBypEl), int(IllumOlvSel)

def WritePadIllumBuckConverterOvervoltageFaultLevel(IllumBcOvFaultSel) :
    return Command.WritePadIllumBuckConverterOvervoltageFaultLevel(IllumBcOvFaultSel)

def ReadPadIllumBuckConverterOvervoltageFaultLevel() :
    Summary, IllumBcOvFaultSel = \
        Command.ReadPadIllumBuckConverterOvervoltageFaultLevel()
    return Summary, int(IllumBcOvFaultSel)

def WritePadCwPwmVoltageLsb0To7(CwPwmLsb) :
    return Command.WritePadCwPwmVoltageLsb0To7(CwPwmLsb)

def ReadPadCwPwmVoltageLsb0To7() :
    Summary, CwPwmLsb = \
        Command.ReadPadCwPwmVoltageLsb0To7()
    return Summary, int(CwPwmLsb)

def WritePadCwPwmVoltageMsb8To15(CwPwmMsb) :
    return Command.WritePadCwPwmVoltageMsb8To15(CwPwmMsb)

def ReadPadCwPwmVoltageMsb8To15() :
    Summary, CwPwmMsb = \
        Command.ReadPadCwPwmVoltageMsb8To15()
    return Summary, int(CwPwmMsb)

def WritePadCapabilityRegister(PadCapabilityRegister) :
    return Command.WritePadCapabilityRegister(PadCapabilityRegister)

def ReadPadCapabilityRegister() :
    Summary, PadCapabilityRegister = \
        Command.ReadPadCapabilityRegister()
    return Summary, PadCapabilityRegister

def WritePadDetailedStatusRegister1(IllumBc2PgFault, IllumBc1PgFault, BuckGp2PgFault, BuckGp1PgFault, BuckGp3PgFault) :
    return Command.WritePadDetailedStatusRegister1(IllumBc2PgFault, IllumBc1PgFault, BuckGp2PgFault, BuckGp1PgFault, BuckGp3PgFault)

def ReadPadDetailedStatusRegister1() :
    Summary, IllumBc2PgFault, IllumBc1PgFault, BuckGp2PgFault, BuckGp1PgFault, BuckGp3PgFault = \
        Command.ReadPadDetailedStatusRegister1()
    return Summary, bool(IllumBc2PgFault), bool(IllumBc1PgFault), bool(BuckGp2PgFault), bool(BuckGp1PgFault), bool(BuckGp3PgFault)

def WritePadDetailedStatusRegister2(IllumBc2OvFault, IllumBc1OvFault, BuckGp2OvFault, BuckGp1OvFault, BuckGp3OvFault) :
    return Command.WritePadDetailedStatusRegister2(IllumBc2OvFault, IllumBc1OvFault, BuckGp2OvFault, BuckGp1OvFault, BuckGp3OvFault)

def ReadPadDetailedStatusRegister2() :
    Summary, IllumBc2OvFault, IllumBc1OvFault, BuckGp2OvFault, BuckGp1OvFault, BuckGp3OvFault = \
        Command.ReadPadDetailedStatusRegister2()
    return Summary, bool(IllumBc2OvFault), bool(IllumBc1OvFault), bool(BuckGp2OvFault), bool(BuckGp1OvFault), bool(BuckGp3OvFault)

def WritePadDetailedStatusRegister3(Gp2OrDmd2PgFault, Gp1OrDmd1PgFault, BuckDmd2PgFault, BuckDmd1PgFault, DmdPgFault) :
    return Command.WritePadDetailedStatusRegister3(Gp2OrDmd2PgFault, Gp1OrDmd1PgFault, BuckDmd2PgFault, BuckDmd1PgFault, DmdPgFault)

def ReadPadDetailedStatusRegister3() :
    Summary, Gp2OrDmd2PgFault, Gp1OrDmd1PgFault, BuckDmd2PgFault, BuckDmd1PgFault, DmdPgFault = \
        Command.ReadPadDetailedStatusRegister3()
    return Summary, bool(Gp2OrDmd2PgFault), bool(Gp1OrDmd1PgFault), bool(BuckDmd2PgFault), bool(BuckDmd1PgFault), bool(DmdPgFault)

def WritePadDetailedStatusRegister4(Gp2OrDmd2OvFault, Gp1OrDmd1OvFault, BuckDmd2OvFault, BuckDmd1OvFault) :
    return Command.WritePadDetailedStatusRegister4(Gp2OrDmd2OvFault, Gp1OrDmd1OvFault, BuckDmd2OvFault, BuckDmd1OvFault)

def ReadPadDetailedStatusRegister4() :
    Summary, Gp2OrDmd2OvFault, Gp1OrDmd1OvFault, BuckDmd2OvFault, BuckDmd1OvFault = \
        Command.ReadPadDetailedStatusRegister4()
    return Summary, bool(Gp2OrDmd2OvFault), bool(Gp1OrDmd1OvFault), bool(BuckDmd2OvFault), bool(BuckDmd1OvFault)

def WritePadChipIdExtension(ChipIdExtension) :
    return Command.WritePadChipIdExtension(ChipIdExtension)

def ReadPadChipIdExtension() :
    Summary, ChipIdExtension = \
        Command.ReadPadChipIdExtension()
    return Summary, int(ChipIdExtension)

def WritePadUserPassword(UserPassword) :
    return Command.WritePadUserPassword(UserPassword)

def ReadPadUserPassword() :
    Summary, UserPassword = \
        Command.ReadPadUserPassword()
    return Summary, int(UserPassword)

def WritePadUserProtectionRegister(ProtectUserReg, DirectMode) :
    return Command.WritePadUserProtectionRegister(ProtectUserReg, DirectMode)

def ReadPadUserProtectionRegister() :
    Summary, ProtectUserReg, DirectMode = \
        Command.ReadPadUserProtectionRegister()
    return Summary, bool(ProtectUserReg), bool(DirectMode)

def WritePadUserEepromRegister1(UserEepromReg1) :
    return Command.WritePadUserEepromRegister1(UserEepromReg1)

def ReadPadUserEepromRegister1() :
    Summary, UserEepromReg1 = \
        Command.ReadPadUserEepromRegister1()
    return Summary, int(UserEepromReg1)

def WritePadUserEepromRegister2(UserEepromReg2) :
    return Command.WritePadUserEepromRegister2(UserEepromReg2)

def ReadPadUserEepromRegister2() :
    Summary, UserEepromReg2 = \
        Command.ReadPadUserEepromRegister2()
    return Summary, int(UserEepromReg2)

def WritePadUserEepromRegister3(UserEepromReg3) :
    return Command.WritePadUserEepromRegister3(UserEepromReg3)

def ReadPadUserEepromRegister3() :
    Summary, UserEepromReg3 = \
        Command.ReadPadUserEepromRegister3()
    return Summary, int(UserEepromReg3)

def WritePadUserEepromRegister4(UserEepromReg4) :
    return Command.WritePadUserEepromRegister4(UserEepromReg4)

def ReadPadUserEepromRegister4() :
    Summary, UserEepromReg4 = \
        Command.ReadPadUserEepromRegister4()
    return Summary, int(UserEepromReg4)

def WritePadUserEepromRegister5(UserEepromReg5) :
    return Command.WritePadUserEepromRegister5(UserEepromReg5)

def ReadPadUserEepromRegister5() :
    Summary, UserEepromReg5 = \
        Command.ReadPadUserEepromRegister5()
    return Summary, int(UserEepromReg5)

def WritePadUserEepromRegister6(UserEepromReg6) :
    return Command.WritePadUserEepromRegister6(UserEepromReg6)

def ReadPadUserEepromRegister6() :
    Summary, UserEepromReg6 = \
        Command.ReadPadUserEepromRegister6()
    return Summary, int(UserEepromReg6)

def WriteDmdModeRegister(DmdModeRegister) :
    return Command.WriteDmdModeRegister(DmdModeRegister)

def ReadDmdModeRegister() :
    Summary, DmdModeRegister = \
        Command.ReadDmdModeRegister()
    return Summary, DmdModeRegister

def WriteDmdIrwTimingRegister(IrwTsVcc2Delay, IrwTrplDelay, IrwToffsetDelay, IrwThVcc2Delay) :
    return Command.WriteDmdIrwTimingRegister(IrwTsVcc2Delay, IrwTrplDelay, IrwToffsetDelay, IrwThVcc2Delay)

def ReadDmdIrwTimingRegister() :
    Summary, IrwTsVcc2Delay, IrwTrplDelay, IrwToffsetDelay, IrwThVcc2Delay = \
        Command.ReadDmdIrwTimingRegister()
    return Summary, int(IrwTsVcc2Delay), int(IrwTrplDelay), int(IrwToffsetDelay), int(IrwThVcc2Delay)

def WriteDmdTestRegister(DmdTestRegister) :
    return Command.WriteDmdTestRegister(DmdTestRegister)

def ReadDmdTestRegister() :
    Summary, DmdTestRegister = \
        Command.ReadDmdTestRegister()
    return Summary, DmdTestRegister

def WriteDmdErrorStatusRegister(HssiPktError, LsifPktError, LsifParityError, MpsTimeoutMonitor) :
    return Command.WriteDmdErrorStatusRegister(HssiPktError, LsifPktError, LsifParityError, MpsTimeoutMonitor)

def ReadDmdErrorStatusRegister() :
    Summary, DmdErrorStatusRegister = \
        Command.ReadDmdErrorStatusRegister()
    return Summary, DmdErrorStatusRegister

def WriteDmdHssiConfig1Register(DmdHssiConfig1Register) :
    return Command.WriteDmdHssiConfig1Register(DmdHssiConfig1Register)

def ReadDmdHssiConfig1Register() :
    Summary, DmdHssiConfig1Register = \
        Command.ReadDmdHssiConfig1Register()
    return Summary, DmdHssiConfig1Register

def WriteDmdHssiConfig2Register(DmdHssiConfig2Register) :
    return Command.WriteDmdHssiConfig2Register(DmdHssiConfig2Register)

def ReadDmdHssiConfig2Register() :
    Summary, DmdHssiConfig2Register = \
        Command.ReadDmdHssiConfig2Register()
    return Summary, DmdHssiConfig2Register

def WriteDmdHssiLaneEnable0Register(DmdHssiLaneEnable0Register) :
    return Command.WriteDmdHssiLaneEnable0Register(DmdHssiLaneEnable0Register)

def ReadDmdHssiLaneEnable0Register() :
    Summary, DmdHssiLaneEnable0Register = \
        Command.ReadDmdHssiLaneEnable0Register()
    return Summary, DmdHssiLaneEnable0Register

def WriteDmdHssiLaneEnable1Register(DmdHssiLaneEnable1Register) :
    return Command.WriteDmdHssiLaneEnable1Register(DmdHssiLaneEnable1Register)

def ReadDmdHssiLaneEnable1Register() :
    Summary, DmdHssiLaneEnable1Register = \
        Command.ReadDmdHssiLaneEnable1Register()
    return Summary, DmdHssiLaneEnable1Register

def WriteDmdHssiLaneEnable2Register(DmdHssiLaneEnable2Register) :
    return Command.WriteDmdHssiLaneEnable2Register(DmdHssiLaneEnable2Register)

def ReadDmdHssiLaneEnable2Register() :
    Summary, DmdHssiLaneEnable2Register = \
        Command.ReadDmdHssiLaneEnable2Register()
    return Summary, DmdHssiLaneEnable2Register

def WriteDmdHssiLaneEnable3Register(DmdHssiLaneEnable3Register) :
    return Command.WriteDmdHssiLaneEnable3Register(DmdHssiLaneEnable3Register)

def ReadDmdHssiLaneEnable3Register() :
    Summary, DmdHssiLaneEnable3Register = \
        Command.ReadDmdHssiLaneEnable3Register()
    return Summary, DmdHssiLaneEnable3Register

def WriteDmdHssiMacroEnableRegister(DmdHssiMacroEnableRegister) :
    return Command.WriteDmdHssiMacroEnableRegister(DmdHssiMacroEnableRegister)

def ReadDmdHssiMacroEnableRegister() :
    Summary, DmdHssiMacroEnableRegister = \
        Command.ReadDmdHssiMacroEnableRegister()
    return Summary, DmdHssiMacroEnableRegister

def WriteDmdAmuxDmuxSelectRegister(AmuxSel, DmuxSel, MacroSel, CoreAmuxSel, CoreDmuxSel) :
    return Command.WriteDmdAmuxDmuxSelectRegister(AmuxSel, DmuxSel, MacroSel, CoreAmuxSel, CoreDmuxSel)

def ReadDmdAmuxDmuxSelectRegister() :
    Summary, AmuxSel, DmuxSel, MacroSel, CoreAmuxSel, CoreDmuxSel = \
        Command.ReadDmdAmuxDmuxSelectRegister()
    return Summary, int(AmuxSel), int(DmuxSel), int(MacroSel), bool(CoreAmuxSel), bool(CoreDmuxSel)

def WriteDmdLsRwTestRegister(LsRwTest) :
    return Command.WriteDmdLsRwTestRegister(LsRwTest)

def ReadDmdLsRwTestRegister() :
    Summary, LsRwTest = \
        Command.ReadDmdLsRwTestRegister()
    return Summary, int(LsRwTest)

def WriteDmdDriveControlRegister(WlDriver20PercentEnable, WlDriver40PercentEnable, BlDriverEnable, ProgrammableTimingEnable, BlockClearTransistorsEnable) :
    return Command.WriteDmdDriveControlRegister(WlDriver20PercentEnable, WlDriver40PercentEnable, BlDriverEnable, ProgrammableTimingEnable, BlockClearTransistorsEnable)

def ReadDmdDriveControlRegister() :
    Summary, WlDriver20PercentEnable, WlDriver40PercentEnable, BlDriverEnable, ProgrammableTimingEnable, BlockClearTransistorsEnable = \
        Command.ReadDmdDriveControlRegister()
    return Summary, bool(WlDriver20PercentEnable), bool(WlDriver40PercentEnable), int(BlDriverEnable), bool(ProgrammableTimingEnable), bool(BlockClearTransistorsEnable)

def WriteDmdVarTimingRegister(DmdVarTimingRegister) :
    return Command.WriteDmdVarTimingRegister(DmdVarTimingRegister)

def ReadDmdVarTimingRegister() :
    Summary, DmdVarTimingRegister = \
        Command.ReadDmdVarTimingRegister()
    return Summary, DmdVarTimingRegister

def ReadDmdProgFuseGroup1Register() :
    Summary, ProgrammableFuseByte0, ProgrammableFuseByte1, ProgrammableFuseByte2, ProgrammableFuseByte3 = \
        Command.ReadDmdProgFuseGroup1Register()
    return Summary, int(ProgrammableFuseByte0), int(ProgrammableFuseByte1), int(ProgrammableFuseByte2), int(ProgrammableFuseByte3)

def ReadDmdProgFuseGroup2Register() :
    Summary, ProgrammableFuseByte0, ProgrammableFuseByte1, ProgrammableFuseByte2, ProgrammableFuseByte3 = \
        Command.ReadDmdProgFuseGroup2Register()
    return Summary, int(ProgrammableFuseByte0), int(ProgrammableFuseByte1), int(ProgrammableFuseByte2), int(ProgrammableFuseByte3)

def ReadDmdProgFuseGroup3Register() :
    Summary, ProgrammableFuseByte0, ProgrammableFuseByte1, ProgrammableFuseByte2, ProgrammableFuseByte3 = \
        Command.ReadDmdProgFuseGroup3Register()
    return Summary, int(ProgrammableFuseByte0), int(ProgrammableFuseByte1), int(ProgrammableFuseByte2), int(ProgrammableFuseByte3)

def ReadDmdProgFuseGroup4Register() :
    Summary, ProgrammableFuseByte0, ProgrammableFuseByte1, ProgrammableFuseByte2, ProgrammableFuseByte3 = \
        Command.ReadDmdProgFuseGroup4Register()
    return Summary, int(ProgrammableFuseByte0), int(ProgrammableFuseByte1), int(ProgrammableFuseByte2), int(ProgrammableFuseByte3)

def ReadDmdIdRegister() :
    Summary, DmdIdByte0, DmdIdByte1, DmdIdByte2, DmdIdByte3 = \
        Command.ReadDmdIdRegister()
    return Summary, int(DmdIdByte0), int(DmdIdByte1), int(DmdIdByte2), int(DmdIdByte3)

def ReadColorMode() :
    Summary, ByteMode = \
        Command.ReadColorMode()
    return Summary, int(ByteMode)

def ReadLaneEnable() :
    Summary, LaneEnable = \
        Command.ReadLaneEnable()
    return Summary, LaneEnable

def ReadPhyReset() :
    Summary, PhyReset = \
        Command.ReadPhyReset()
    return Summary, bool(PhyReset)

def ReadPhyEnable() :
    Summary, PhyEnable = \
        Command.ReadPhyEnable()
    return Summary, bool(PhyEnable)

def ReadHotPlugDetectControl() :
    Summary, HtpdnDeAssert = \
        Command.ReadHotPlugDetectControl()
    return Summary, bool(HtpdnDeAssert)

def ReadInterruptEnable() :
    Summary, InterruptEnable = \
        Command.ReadInterruptEnable()
    return Summary, InterruptEnable

def ReadInterruptStatus() :
    Summary, InterruptStatus = \
        Command.ReadInterruptStatus()
    return Summary, InterruptStatus

def ReadInterruptClear() :
    Summary, InterruptClear = \
        Command.ReadInterruptClear()
    return Summary, InterruptClear

def ReadLockMonitor() :
    Summary, BitLocked, ByteLocked, DataLocked = \
        Command.ReadLockMonitor()
    return Summary, bool(BitLocked), bool(ByteLocked), bool(DataLocked)

def ReadBitLockMonitorLan0ToLane7() :
    Summary, BitLockMonitorLan0ToLane7 = \
        Command.ReadBitLockMonitorLan0ToLane7()
    return Summary, BitLockMonitorLan0ToLane7

def ReadBitLockMonitorLane8ToLane15() :
    Summary, BitLockMonitorLane8ToLane15 = \
        Command.ReadBitLockMonitorLane8ToLane15()
    return Summary, BitLockMonitorLane8ToLane15

def ReadByteLockMonitorLane0ToLane7() :
    Summary, ByteLockMonitorLane0ToLane7 = \
        Command.ReadByteLockMonitorLane0ToLane7()
    return Summary, ByteLockMonitorLane0ToLane7

def ReadByteLockMonitorLane8ToLane15() :
    Summary, ByteLockMonitorLane8ToLane15 = \
        Command.ReadByteLockMonitorLane8ToLane15()
    return Summary, ByteLockMonitorLane8ToLane15

def ReadDataLockMonitorLane0ToLane7() :
    Summary, DataLockMonitorLane0ToLane7 = \
        Command.ReadDataLockMonitorLane0ToLane7()
    return Summary, DataLockMonitorLane0ToLane7

def ReadDataLockMonitorLane8ToLane15() :
    Summary, DataLockMonitorLane8ToLane15 = \
        Command.ReadDataLockMonitorLane8ToLane15()
    return Summary, DataLockMonitorLane8ToLane15

def ReadVideoOutputEnableLane0ToLane7() :
    Summary, VideoOutputEnableLane0ToLane7 = \
        Command.ReadVideoOutputEnableLane0ToLane7()
    return Summary, VideoOutputEnableLane0ToLane7

def ReadVideoOutputEnableLane8ToLane15() :
    Summary, VideoOutputEnableLane8ToLane15 = \
        Command.ReadVideoOutputEnableLane8ToLane15()
    return Summary, VideoOutputEnableLane8ToLane15

def ReadComIntmode() :
    Summary, ComIntmode = \
        Command.ReadComIntmode()
    return Summary, bool(ComIntmode)

def ReadComModeLow() :
    Summary, ComModeLow = \
        Command.ReadComModeLow()
    return Summary, int(ComModeLow)

def ReadComModeHigh() :
    Summary, ComModeHigh = \
        Command.ReadComModeHigh()
    return Summary, int(ComModeHigh)

def ReadRxmBand0EqTrim() :
    Summary, RxmBand0EqTrim = \
        Command.ReadRxmBand0EqTrim()
    return Summary, int(RxmBand0EqTrim)

def ReadRxmBand1EqTrim() :
    Summary, RxmBand1EqTrim = \
        Command.ReadRxmBand1EqTrim()
    return Summary, int(RxmBand1EqTrim)

def ReadRxmBand2EqTrim() :
    Summary, RxmBand2EqTrim = \
        Command.ReadRxmBand2EqTrim()
    return Summary, int(RxmBand2EqTrim)

def ReadRxmBand3EqTrim() :
    Summary, RxmBand3EqTrim = \
        Command.ReadRxmBand3EqTrim()
    return Summary, int(RxmBand3EqTrim)

def WriteXprFixedOutputEnable(ChannelNum, FixedOutputEnable) :
    return Command.WriteXprFixedOutputEnable(ChannelNum, FixedOutputEnable)

def ReadXprFixedOutputEnable(ChannelNum) :
    Summary, FixedOutputEnable = \
        Command.ReadXprFixedOutputEnable(ChannelNum)
    return Summary, bool(FixedOutputEnable)

def WriteXprDacGain(ChannelNum, DacGain) :
    return Command.WriteXprDacGain(ChannelNum, DacGain)

def ReadXprDacGain(ChannelNum) :
    Summary, DacGain = \
        Command.ReadXprDacGain(ChannelNum)
    return Summary, float(DacGain)

def WriteXprSubframeDelay(ChannelNum, SubframeDelay) :
    return Command.WriteXprSubframeDelay(ChannelNum, SubframeDelay)

def ReadXprSubframeDelay(ChannelNum) :
    Summary, SubframeDelay = \
        Command.ReadXprSubframeDelay(ChannelNum)
    return Summary, int(SubframeDelay)

def ReadXprActuatorType() :
    Summary, ActuatorType = \
        Command.ReadXprActuatorType()
    return Summary, int(ActuatorType)

def WriteXprOutputEnable(ChannelNum, OutputEnable) :
    return Command.WriteXprOutputEnable(ChannelNum, OutputEnable)

def ReadXprOutputEnable(ChannelNum) :
    Summary, OutputEnable = \
        Command.ReadXprOutputEnable(ChannelNum)
    return Summary, bool(OutputEnable)

def WriteXprClockWidth(ChannelNum, ClockWidth) :
    return Command.WriteXprClockWidth(ChannelNum, ClockWidth)

def ReadXprClockWidth(ChannelNum) :
    Summary, ClockWidth = \
        Command.ReadXprClockWidth(ChannelNum)
    return Summary, int(ClockWidth)

def WriteXprDacOffset(ChannelNum, DacOffset) :
    return Command.WriteXprDacOffset(ChannelNum, DacOffset)

def ReadXprDacOffset(ChannelNum) :
    Summary, DacOffset = \
        Command.ReadXprDacOffset(ChannelNum)
    return Summary, int(DacOffset)

def WriteXprNumberOfSegments(ChannelNum, NumberOfSegments) :
    return Command.WriteXprNumberOfSegments(ChannelNum, NumberOfSegments)

def ReadXprNumberOfSegments(ChannelNum) :
    Summary, NumberOfSegments = \
        Command.ReadXprNumberOfSegments(ChannelNum)
    return Summary, int(NumberOfSegments)

def WriteXprSegmentLength(ChannelNum, SegmentLength) :
    return Command.WriteXprSegmentLength(ChannelNum, SegmentLength)

def ReadXprSegmentLength(ChannelNum) :
    Summary, SegmentLength = \
        Command.ReadXprSegmentLength(ChannelNum)
    return Summary, int(SegmentLength)

def WriteXprInvertPwmA(ChannelNum, InvertPwmA) :
    return Command.WriteXprInvertPwmA(ChannelNum, InvertPwmA)

def ReadXprInvertPwmA(ChannelNum) :
    Summary, InvertPwmA = \
        Command.ReadXprInvertPwmA(ChannelNum)
    return Summary, bool(InvertPwmA)

def WriteXprInvertPwmB(ChannelNum, InvertPwmB) :
    return Command.WriteXprInvertPwmB(ChannelNum, InvertPwmB)

def ReadXprInvertPwmB(ChannelNum) :
    Summary, InvertPwmB = \
        Command.ReadXprInvertPwmB(ChannelNum)
    return Summary, bool(InvertPwmB)

def WriteXprSubframeFilterValue(ChannelNum, SubframeFilterValue) :
    return Command.WriteXprSubframeFilterValue(ChannelNum, SubframeFilterValue)

def ReadXprSubframeFilterValue(ChannelNum) :
    Summary, SubframeFilterValue = \
        Command.ReadXprSubframeFilterValue(ChannelNum)
    return Summary, int(SubframeFilterValue)

def WriteXprSubframeWatchDog(ChannelNum, SubframeWatchDog) :
    return Command.WriteXprSubframeWatchDog(ChannelNum, SubframeWatchDog)

def ReadXprSubframeWatchDog(ChannelNum) :
    Summary, SubframeWatchDog = \
        Command.ReadXprSubframeWatchDog(ChannelNum)
    return Summary, int(SubframeWatchDog)

def WriteXprFixedOutputValue(ChannelNum, FixedOutputValue) :
    return Command.WriteXprFixedOutputValue(ChannelNum, FixedOutputValue)

def ReadXprFixedOutputValue(ChannelNum) :
    Summary, FixedOutputValue = \
        Command.ReadXprFixedOutputValue(ChannelNum)
    return Summary, int(FixedOutputValue)

