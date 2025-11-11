#-------------------------------------
# Copyright (c) 2024 Texas Instruments
#-------------------------------------

# NOTE: This file is auto generated from a command definition file.
#       Please do not modify the file directly.                    
#
# Command Spec Version : 1.0

import sys
import clr

clr.AddReference('DLPComposer.Commands.DLPC347x')
from System import *
from DLPComposer.Commands.DLPC347x import * 

def WriteOperatingModeSelect(OperatingMode) :
    return Command.WriteOperatingModeSelect(OperatingMode)

def ReadOperatingModeSelect() :
    Summary, OperatingMode = \
        Command.ReadOperatingModeSelect()
    return Summary, OperatingMode

def WriteIdleModeSelect(IdleMode) :
    return Command.WriteIdleModeSelect(IdleMode)

def ReadIdleModeSelect() :
    Summary, IdleMode, MotionVideoType, PreviousFrameStill, PreviousFrameActive = \
        Command.ReadIdleModeSelect()
    return Summary, IdleMode, MotionVideoType, PreviousFrameStill, PreviousFrameActive

def WriteSplashScreenSelect(SplashScreenIndex) :
    return Command.WriteSplashScreenSelect(SplashScreenIndex)

def ReadSplashScreenSelect() :
    Summary, SplashScreenIndex = \
        Command.ReadSplashScreenSelect()
    return Summary, int(SplashScreenIndex)

def WriteSplashScreenExecute() :
    return Command.WriteSplashScreenExecute()

def ReadSplashScreenHeader(SplashScreenIndex) :
    Summary, SplashScreenHeader = \
        Command.ReadSplashScreenHeader(SplashScreenIndex)
    return Summary, SplashScreenHeader

def WriteExternalVideoSourceFormatSelect(VideoFormat) :
    return Command.WriteExternalVideoSourceFormatSelect(VideoFormat)

def ReadExternalVideoSourceFormatSelect() :
    Summary, VideoFormat = \
        Command.ReadExternalVideoSourceFormatSelect()
    return Summary, VideoFormat

def WriteVideoChromaProcessingSelect(ChromaInterpolationMethod, ChromaChannelSwap, CscCoefficientSet) :
    return Command.WriteVideoChromaProcessingSelect(ChromaInterpolationMethod, ChromaChannelSwap, CscCoefficientSet)

def ReadVideoChromaProcessingSelect() :
    Summary, ChromaInterpolationMethod, ChromaChannelSwap, CscCoefficientSet = \
        Command.ReadVideoChromaProcessingSelect()
    return Summary, ChromaInterpolationMethod, ChromaChannelSwap, int(CscCoefficientSet)

def ReadDmdSequencerSyncMode() :
    Summary, DmdSequencerSyncMode, SystemAutoSyncSetting = \
        Command.ReadDmdSequencerSyncMode()
    return Summary, DmdSequencerSyncMode, SystemAutoSyncSetting

def Write3DControl(ThreeDFrameDominance, ThreeDReferencePolarity) :
    return Command.Write3DControl(ThreeDFrameDominance, ThreeDReferencePolarity)

def Read3DControl() :
    Summary, ThreeDMode, ThreeDFrameDominance, ThreeDReferencePolarity = \
        Command.Read3DControl()
    return Summary, ThreeDMode, ThreeDFrameDominance, ThreeDReferencePolarity

def WriteInputImageSize(PixelsPerLine, LinesPerFrame) :
    return Command.WriteInputImageSize(PixelsPerLine, LinesPerFrame)

def ReadInputImageSize() :
    Summary, PixelsPerLine, LinesPerFrame = \
        Command.ReadInputImageSize()
    return Summary, int(PixelsPerLine), int(LinesPerFrame)

def WriteImageCrop(CaptureStartPixel, CaptureStartLine, PixelsPerLine, LinesPerFrame) :
    return Command.WriteImageCrop(CaptureStartPixel, CaptureStartLine, PixelsPerLine, LinesPerFrame)

def ReadImageCrop() :
    Summary, CaptureStartPixel, CaptureStartLine, PixelsPerLine, LinesPerFrame = \
        Command.ReadImageCrop()
    return Summary, int(CaptureStartPixel), int(CaptureStartLine), int(PixelsPerLine), int(LinesPerFrame)

def WriteDisplaySizeLegacy(PixelsPerLine, LinesPerFrame) :
    return Command.WriteDisplaySizeLegacy(PixelsPerLine, LinesPerFrame)

def ReadDisplaySizeLegacy() :
    Summary, PixelsPerLine, LinesPerFrame = \
        Command.ReadDisplaySizeLegacy()
    return Summary, int(PixelsPerLine), int(LinesPerFrame)

def WriteDisplaySize(StartPixel, StartLine, PixelsPerLine, LinesPerFrame) :
    return Command.WriteDisplaySize(StartPixel, StartLine, PixelsPerLine, LinesPerFrame)

def ReadDisplaySize() :
    Summary, StartPixel, StartLine, PixelsPerLine, LinesPerFrame = \
        Command.ReadDisplaySize()
    return Summary, int(StartPixel), int(StartLine), int(PixelsPerLine), int(LinesPerFrame)

def WriteDisplayImageOrientation(ImageRotation, LongAxisImageFlip, ShortAxisImageFlip) :
    return Command.WriteDisplayImageOrientation(ImageRotation, LongAxisImageFlip, ShortAxisImageFlip)

def ReadDisplayImageOrientation() :
    Summary, ImageRotation, LongAxisImageFlip, ShortAxisImageFlip = \
        Command.ReadDisplayImageOrientation()
    return Summary, ImageRotation, LongAxisImageFlip, ShortAxisImageFlip

def WriteDisplayImageCurtain(Enable, Color) :
    return Command.WriteDisplayImageCurtain(Enable, Color)

def ReadDisplayImageCurtain() :
    Summary, Enable, Color = \
        Command.ReadDisplayImageCurtain()
    return Summary, Enable, Color

def WriteImageFreeze(Enable) :
    return Command.WriteImageFreeze(Enable)

def ReadImageFreeze() :
    Summary, Enable = \
        Command.ReadImageFreeze()
    return Summary, bool(Enable)

def WriteSingleBufferMode(Enable) :
    return Command.WriteSingleBufferMode(Enable)

def ReadSingleBufferMode() :
    Summary, Enable = \
        Command.ReadSingleBufferMode()
    return Summary, bool(Enable)

def WriteBorderColor(DisplayBorderColor) :
    return Command.WriteBorderColor(DisplayBorderColor)

def ReadBorderColor() :
    Summary, DisplayBorderColor, PillarBoxBorderColorSource = \
        Command.ReadBorderColor()
    return Summary, DisplayBorderColor, PillarBoxBorderColorSource

def WriteMirrorLock(MirrorLockOption) :
    return Command.WriteMirrorLock(MirrorLockOption)

def ReadMirrorLock() :
    Summary, MirrorLockOption = \
        Command.ReadMirrorLock()
    return Summary, MirrorLockOption

def WriteSolidField(Border, ForegroundColor) :
    return Command.WriteSolidField(Border, ForegroundColor)

def WriteHorizontalRamp(Border, ForegroundColor, StartValue, EndValue) :
    return Command.WriteHorizontalRamp(Border, ForegroundColor, StartValue, EndValue)

def WriteVerticalRamp(Border, ForegroundColor, StartValue, EndValue) :
    return Command.WriteVerticalRamp(Border, ForegroundColor, StartValue, EndValue)

def WriteHorizontalLines(Border, BackgroundColor, ForegroundColor, ForegroundLineWidth, BackgroundLineWidth) :
    return Command.WriteHorizontalLines(Border, BackgroundColor, ForegroundColor, ForegroundLineWidth, BackgroundLineWidth)

def WriteDiagonalLines(Border, BackgroundColor, ForegroundColor, HorizontalSpacing, VerticalSpacing) :
    return Command.WriteDiagonalLines(Border, BackgroundColor, ForegroundColor, HorizontalSpacing, VerticalSpacing)

def WriteVerticalLines(Border, BackgroundColor, ForegroundColor, ForegroundLineWidth, BackgroundLineWidth) :
    return Command.WriteVerticalLines(Border, BackgroundColor, ForegroundColor, ForegroundLineWidth, BackgroundLineWidth)

def WriteGridLines(GridLines) :
    return Command.WriteGridLines(GridLines)

def WriteCheckerboard(Border, BackgroundColor, ForegroundColor, HorizontalCheckerCount, VerticalCheckerCount) :
    return Command.WriteCheckerboard(Border, BackgroundColor, ForegroundColor, HorizontalCheckerCount, VerticalCheckerCount)

def WriteColorbars(Border) :
    return Command.WriteColorbars(Border)

def ReadTestPatternSelect() :
    Summary, TestPatternSelect = \
        Command.ReadTestPatternSelect()
    return Summary, TestPatternSelect

def WriteKeystoneProjectionPitchAngle(PitchAngle) :
    return Command.WriteKeystoneProjectionPitchAngle(PitchAngle)

def ReadKeystoneProjectionPitchAngle() :
    Summary, PitchAngle = \
        Command.ReadKeystoneProjectionPitchAngle()
    return Summary, float(PitchAngle)

def WriteKeystoneCorrectionControl(KeystoneCorrectionEnable, OpticalThrowRatio, OpticalDmdOffset) :
    return Command.WriteKeystoneCorrectionControl(KeystoneCorrectionEnable, OpticalThrowRatio, OpticalDmdOffset)

def ReadKeystoneCorrectionControl() :
    Summary, KeystoneCorrectionEnable, OpticalThrowRatio, OpticalDmdOffset = \
        Command.ReadKeystoneCorrectionControl()
    return Summary, bool(KeystoneCorrectionEnable), float(OpticalThrowRatio), float(OpticalDmdOffset)

def WriteExecuteFlashBatchFile(BatchFileNumber) :
    return Command.WriteExecuteFlashBatchFile(BatchFileNumber)

def WriteBatchFileDelay(DelayInMicroseconds) :
    return Command.WriteBatchFileDelay(DelayInMicroseconds)

def WriteLedOutputControlMethod(LedControlMethod) :
    return Command.WriteLedOutputControlMethod(LedControlMethod)

def ReadLedOutputControlMethod() :
    Summary, LedControlMethod = \
        Command.ReadLedOutputControlMethod()
    return Summary, LedControlMethod

def WriteRgbLedEnable(RedLedEnable, GreenLedEnable, BlueLedEnable) :
    return Command.WriteRgbLedEnable(RedLedEnable, GreenLedEnable, BlueLedEnable)

def ReadRgbLedEnable() :
    Summary, RedLedEnable, GreenLedEnable, BlueLedEnable = \
        Command.ReadRgbLedEnable()
    return Summary, bool(RedLedEnable), bool(GreenLedEnable), bool(BlueLedEnable)

def WriteRgbLedCurrent(RedLedCurrent, GreenLedCurrent, BlueLedCurrent) :
    return Command.WriteRgbLedCurrent(RedLedCurrent, GreenLedCurrent, BlueLedCurrent)

def ReadRgbLedCurrent() :
    Summary, RedLedCurrent, GreenLedCurrent, BlueLedCurrent = \
        Command.ReadRgbLedCurrent()
    return Summary, int(RedLedCurrent), int(GreenLedCurrent), int(BlueLedCurrent)

def ReadCaicLedMaxAvailablePower() :
    Summary, MaxLedPower = \
        Command.ReadCaicLedMaxAvailablePower()
    return Summary, float(MaxLedPower)

def WriteRgbLedMaxCurrent(MaxRedLedCurrent, MaxGreenLedCurrent, MaxBlueLedCurrent) :
    return Command.WriteRgbLedMaxCurrent(MaxRedLedCurrent, MaxGreenLedCurrent, MaxBlueLedCurrent)

def ReadRgbLedMaxCurrent() :
    Summary, MaxRedLedCurrent, MaxGreenLedCurrent, MaxBlueLedCurrent = \
        Command.ReadRgbLedMaxCurrent()
    return Summary, int(MaxRedLedCurrent), int(MaxGreenLedCurrent), int(MaxBlueLedCurrent)

def ReadCaicRgbLedCurrent() :
    Summary, RedLedCurrent, GreenLedCurrent, BlueLedCurrent = \
        Command.ReadCaicRgbLedCurrent()
    return Summary, int(RedLedCurrent), int(GreenLedCurrent), int(BlueLedCurrent)

def WriteLookSelect(LookNumber) :
    return Command.WriteLookSelect(LookNumber)

def ReadLookSelect() :
    Summary, LookNumber, SequenceIndex, SequenceFrameTime = \
        Command.ReadLookSelect()
    return Summary, int(LookNumber), int(SequenceIndex), float(SequenceFrameTime)

def ReadSequenceHeaderAttributes() :
    Summary, SequenceHeaderAttributes = \
        Command.ReadSequenceHeaderAttributes()
    return Summary, SequenceHeaderAttributes

def WriteLocalAreaBrightnessBoostControl(LabbControl, SharpnessStrength, LabbStrengthSetting) :
    return Command.WriteLocalAreaBrightnessBoostControl(LabbControl, SharpnessStrength, LabbStrengthSetting)

def ReadLocalAreaBrightnessBoostControl() :
    Summary, LabbControl, SharpnessStrength, LabbStrengthSetting, LabbGainValue = \
        Command.ReadLocalAreaBrightnessBoostControl()
    return Summary, LabbControl, int(SharpnessStrength), int(LabbStrengthSetting), int(LabbGainValue)

def WriteCaicImageProcessingControl(CaicGainDisplayScale, CaicGainDisplayEnable, CaicMaxLumensGain, CaicClippingThreshold) :
    return Command.WriteCaicImageProcessingControl(CaicGainDisplayScale, CaicGainDisplayEnable, CaicMaxLumensGain, CaicClippingThreshold)

def ReadCaicImageProcessingControl() :
    Summary, CaicGainDisplayScale, CaicGainDisplayEnable, CaicMaxLumensGain, CaicClippingThreshold = \
        Command.ReadCaicImageProcessingControl()
    return Summary, CaicGainDisplayScale, bool(CaicGainDisplayEnable), float(CaicMaxLumensGain), float(CaicClippingThreshold)

def WriteColorCoordinateAdjustmentControl(CcaEnable) :
    return Command.WriteColorCoordinateAdjustmentControl(CcaEnable)

def ReadColorCoordinateAdjustmentControl() :
    Summary, CcaEnable = \
        Command.ReadColorCoordinateAdjustmentControl()
    return Summary, bool(CcaEnable)

def ReadShortStatus() :
    Summary, ShortStatus = \
        Command.ReadShortStatus()
    return Summary, ShortStatus

def ReadSystemStatus() :
    Summary, SystemStatus = \
        Command.ReadSystemStatus()
    return Summary, SystemStatus

def ReadCommunicationStatus() :
    Summary, CommunicationStatus = \
        Command.ReadCommunicationStatus()
    return Summary, CommunicationStatus

def ReadSystemSoftwareVersion() :
    Summary, PatchVersion, MinorVersion, MajorVersion = \
        Command.ReadSystemSoftwareVersion()
    return Summary, int(PatchVersion), int(MinorVersion), int(MajorVersion)

def ReadControllerDeviceId() :
    Summary, DeviceId = \
        Command.ReadControllerDeviceId()
    return Summary, DeviceId

def ReadDmdDeviceId(DmdDataSelection) :
    Summary, DeviceId = \
        Command.ReadDmdDeviceId(DmdDataSelection)
    return Summary, int(DeviceId)

def ReadFirmwareBuildVersion() :
    Summary, PatchVersion, MinorVersion, MajorVersion = \
        Command.ReadFirmwareBuildVersion()
    return Summary, int(PatchVersion), int(MinorVersion), int(MajorVersion)

def ReadSystemTemperature() :
    Summary, Temperature = \
        Command.ReadSystemTemperature()
    return Summary, float(Temperature)

def ReadFlashUpdatePrecheck(FlashUpdatePackageSize) :
    Summary, PackageSizeStatus, PacakgeConfigurationCollapsed, PacakgeConfigurationIdentifier = \
        Command.ReadFlashUpdatePrecheck(FlashUpdatePackageSize)
    return Summary, PackageSizeStatus, PacakgeConfigurationCollapsed, PacakgeConfigurationIdentifier

def WriteFlashDataTypeSelect(FlashSelect) :
    return Command.WriteFlashDataTypeSelect(FlashSelect)

def WriteFlashDataLength(FlashDataLength) :
    return Command.WriteFlashDataLength(FlashDataLength)

def WriteFlashErase() :
    return Command.WriteFlashErase()

def WriteFlashStart(Data) :
    Data = Array[Byte](Data)
    return Command.WriteFlashStart(Data)

def ReadFlashStart(Length) :
    Summary, Data = \
        Command.ReadFlashStart(Length)
    return Summary, bytearray(Data)

def WriteFlashContinue(Data) :
    Data = Array[Byte](Data)
    return Command.WriteFlashContinue(Data)

def ReadFlashContinue(Length) :
    Summary, Data = \
        Command.ReadFlashContinue(Length)
    return Summary, bytearray(Data)

def WriteInternalRegisterAddress(Address) :
    return Command.WriteInternalRegisterAddress(Address)

def WriteInternalRegister(Data) :
    return Command.WriteInternalRegister(Data)

def ReadInternalRegister() :
    Summary, Data = \
        Command.ReadInternalRegister()
    return Summary, int(Data)

def ReadDeviceKeyfusecheck(IdSelection) :
    Summary, RetVal = \
        Command.ReadDeviceKeyfusecheck(IdSelection)
    return Summary, int(RetVal)

def WritePadRegisterAddress(Address, DataLength, ReadWrite) :
    return Command.WritePadRegisterAddress(Address, DataLength, ReadWrite)

def WritePadRegister(Data) :
    Data = Array[Byte](Data)
    return Command.WritePadRegister(Data)

def ReadPadRegister(Length) :
    Summary, Data = \
        Command.ReadPadRegister(Length)
    return Summary, bytearray(Data)

def ReadThreadState(ThreadId) :
    Summary, State = \
        Command.ReadThreadState(ThreadId)
    return Summary, State

def ReadEventState(EventId) :
    Summary, State = \
        Command.ReadEventState(EventId)
    return Summary, int(State)

def ReadThreadPriority(ThreadId) :
    Summary, Priority = \
        Command.ReadThreadPriority(ThreadId)
    return Summary, int(Priority)

def ReadSequenceBinaryVersion() :
    Summary, PatchVersion, MinorVersion, MajorVersion = \
        Command.ReadSequenceBinaryVersion()
    return Summary, int(PatchVersion), int(MinorVersion), int(MajorVersion)

def WriteInternalPatternControl(PatternControl, RepeatCount) :
    return Command.WriteInternalPatternControl(PatternControl, RepeatCount)

def ReadValidateExposureTime(PatternMode, BitDepth, ExposureTime) :
    Summary, ExposureTimeSupported, ZeroDarkTimeSupported, MinimumExposureTime, PreExposureDarkTime, PostExposureDarkTime = \
        Command.ReadValidateExposureTime(PatternMode, BitDepth, ExposureTime)
    return Summary, ExposureTimeSupported, ZeroDarkTimeSupported, int(MinimumExposureTime), int(PreExposureDarkTime), int(PostExposureDarkTime)

def ReadPatternSetEntryHeader() :
    Summary, NumberOfPatterns, PatternDirection, BitDepth, PatternDataSize = \
        Command.ReadPatternSetEntryHeader()
    return Summary, int(NumberOfPatterns), PatternDirection, int(BitDepth), int(PatternDataSize)

def ReadSequenceInfo() :
    Summary, SequenceInfo = \
        Command.ReadSequenceInfo()
    return Summary, SequenceInfo

def WriteTriggerInConfiguration(TriggerEnable, TriggerPolarity) :
    return Command.WriteTriggerInConfiguration(TriggerEnable, TriggerPolarity)

def ReadTriggerInConfiguration() :
    Summary, TriggerEnable, TriggerPolarity = \
        Command.ReadTriggerInConfiguration()
    return Summary, TriggerEnable, TriggerPolarity

def WriteTriggerOutConfiguration(TriggerType, TriggerEnable, TriggerInversion, Delay) :
    return Command.WriteTriggerOutConfiguration(TriggerType, TriggerEnable, TriggerInversion, Delay)

def ReadTriggerOutConfiguration(Trigger) :
    Summary, TriggerEnable, TriggerInversion, Delay = \
        Command.ReadTriggerOutConfiguration(Trigger)
    return Summary, TriggerEnable, TriggerInversion, int(Delay)

def WritePatternReadyConfiguration(TriggerEnable, TriggerPolarity) :
    return Command.WritePatternReadyConfiguration(TriggerEnable, TriggerPolarity)

def ReadPatternReadyConfiguration() :
    Summary, TriggerEnable, TriggerPolarity = \
        Command.ReadPatternReadyConfiguration()
    return Summary, TriggerEnable, TriggerPolarity

def WritePatternConfiguration(PatternConfiguration) :
    return Command.WritePatternConfiguration(PatternConfiguration)

def ReadPatternConfiguration() :
    Summary, PatternConfiguration = \
        Command.ReadPatternConfiguration()
    return Summary, PatternConfiguration

def WriteInternalPatternDisplayConfiguration(DmdBlockStart, DmdBlockCount) :
    return Command.WriteInternalPatternDisplayConfiguration(DmdBlockStart, DmdBlockCount)

def ReadInternalPatternDisplayConfiguration() :
    Summary, DmdBlockStart, DmdBlockCount = \
        Command.ReadInternalPatternDisplayConfiguration()
    return Summary, int(DmdBlockStart), int(DmdBlockCount)

def WritePatternOrderTableEntry(WriteControl, PatternOrderTableEntry) :
    return Command.WritePatternOrderTableEntry(WriteControl, PatternOrderTableEntry)

def ReadPatternOrderTableEntry(PatternOrderTableEntryIndex) :
    Summary, PatternOrderTableEntry = \
        Command.ReadPatternOrderTableEntry(PatternOrderTableEntryIndex)
    return Summary, PatternOrderTableEntry

def ReadInternalPatternStatus() :
    Summary, InternalPatternStatus = \
        Command.ReadInternalPatternStatus()
    return Summary, InternalPatternStatus

def WriteDsiPortEnable(Enable) :
    return Command.WriteDsiPortEnable(Enable)

def ReadDsiPortEnable() :
    Summary, Enable = \
        Command.ReadDsiPortEnable()
    return Summary, Enable

def WriteDsiHsClockInput(ClockSpeed) :
    return Command.WriteDsiHsClockInput(ClockSpeed)

def ReadDsiHsClockInput() :
    Summary, ClockSpeed = \
        Command.ReadDsiHsClockInput()
    return Summary, int(ClockSpeed)

