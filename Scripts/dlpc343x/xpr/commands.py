#-------------------------------------
# Copyright (c) 2024 Texas Instruments
#-------------------------------------

# NOTE: This file is auto generated from a command definition file.
#       Please do not modify the file directly.                    
#
# Command Spec Version : 1.0

import sys
import clr

clr.AddReference('DLPComposer.Commands.DLPC343x.XPR')
from System import *
from DLPComposer.Commands.DLPC343x.XPR import * 

def WriteSourceSelect(Source, ExternalCalibrationEnable) :
    return Command.WriteSourceSelect(Source, ExternalCalibrationEnable)

def ReadSourceSelect() :
    Summary, Source, ExternalCalibrationEnable = \
        Command.ReadSourceSelect()
    return Summary, Source, ExternalCalibrationEnable

def WriteInputImageSize(PixelsPerLine, LinesPerFrame) :
    return Command.WriteInputImageSize(PixelsPerLine, LinesPerFrame)

def ReadInputImageSize() :
    Summary, PixelsPerLine, LinesPerFrame = \
        Command.ReadInputImageSize()
    return Summary, int(PixelsPerLine), int(LinesPerFrame)

def WriteParallelVideoControl(PixelsClockSamplingEdge, IvalidPolarity, HsyncPolarity, VsyncPolarity) :
    return Command.WriteParallelVideoControl(PixelsClockSamplingEdge, IvalidPolarity, HsyncPolarity, VsyncPolarity)

def ReadParallelVideoControl() :
    Summary, PixelsClockSamplingEdge, IvalidPolarity, HsyncPolarity, VsyncPolarity = \
        Command.ReadParallelVideoControl()
    return Summary, PixelsClockSamplingEdge, IvalidPolarity, HsyncPolarity, VsyncPolarity

def WriteSplashScreenSelect(SplashScreenIndex) :
    return Command.WriteSplashScreenSelect(SplashScreenIndex)

def ReadSplashScreenSelect() :
    Summary, SplashScreenIndex = \
        Command.ReadSplashScreenSelect()
    return Summary, int(SplashScreenIndex)

def ReadSplashScreenHeader(SplashScreenNumber) :
    Summary, SplashScreenHeader = \
        Command.ReadSplashScreenHeader(SplashScreenNumber)
    return Summary, SplashScreenHeader

def WriteExternalVideoSourceFormatSelect(VideoFormat) :
    return Command.WriteExternalVideoSourceFormatSelect(VideoFormat)

def ReadExternalVideoSourceFormatSelect() :
    Summary, VideoFormat = \
        Command.ReadExternalVideoSourceFormatSelect()
    return Summary, VideoFormat

def WriteFpdLinkConfiguration(BitRate, PixelMapMode) :
    return Command.WriteFpdLinkConfiguration(BitRate, PixelMapMode)

def ReadFpdLinkConfiguration() :
    Summary, BitRate, PixelMapMode = \
        Command.ReadFpdLinkConfiguration()
    return Summary, int(BitRate), int(PixelMapMode)

def WriteVideoChromaChannelSwapSelect(ChromaChannelSwap) :
    return Command.WriteVideoChromaChannelSwapSelect(ChromaChannelSwap)

def ReadVideoChromaChannelSwapSelect() :
    Summary, ChromaChannelSwap = \
        Command.ReadVideoChromaChannelSwapSelect()
    return Summary, ChromaChannelSwap

def ReadAutoFramingInformation() :
    Summary, AutoFramingInformation = \
        Command.ReadAutoFramingInformation()
    return Summary, AutoFramingInformation

def ReadDmdSequencerSyncMode() :
    Summary, DmdSequencerSyncMode, SystemAutoSyncSetting = \
        Command.ReadDmdSequencerSyncMode()
    return Summary, DmdSequencerSyncMode, SystemAutoSyncSetting

def WriteThreeDControl(ThreeDFrameDominance, ThreeDReferencePolarity) :
    return Command.WriteThreeDControl(ThreeDFrameDominance, ThreeDReferencePolarity)

def ReadThreeDControl() :
    Summary, ThreeDMode, ThreeDFrameDominance, ThreeDReferencePolarity = \
        Command.ReadThreeDControl()
    return Summary, ThreeDMode, ThreeDFrameDominance, ThreeDReferencePolarity

def WriteThreeDReference(ThreeDReference) :
    return Command.WriteThreeDReference(ThreeDReference)

def WriteDisplayImageOrientation(LongAxisImageFlip, ShortAxisImageFlip) :
    return Command.WriteDisplayImageOrientation(LongAxisImageFlip, ShortAxisImageFlip)

def ReadDisplayImageOrientation() :
    Summary, LongAxisImageFlip, ShortAxisImageFlip = \
        Command.ReadDisplayImageOrientation()
    return Summary, LongAxisImageFlip, ShortAxisImageFlip

def WriteDisplayImageCurtain(Enable, Color) :
    return Command.WriteDisplayImageCurtain(Enable, Color)

def ReadDisplayImageCurtain() :
    Summary, Enable, Color = \
        Command.ReadDisplayImageCurtain()
    return Summary, bool(Enable), Color

def WriteImageFreeze(Enable) :
    return Command.WriteImageFreeze(Enable)

def ReadImageFreeze() :
    Summary, Enable = \
        Command.ReadImageFreeze()
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

def WriteKeystoneProjectionPitchAngle(PitchAngle) :
    return Command.WriteKeystoneProjectionPitchAngle(PitchAngle)

def ReadKeystoneProjectionPitchAngle() :
    Summary, PitchAngle = \
        Command.ReadKeystoneProjectionPitchAngle()
    return Summary, float(PitchAngle)

def WriteKeystoneCorrectionControl(KeystoneCorrectionEnable, OpticalThrowRatio, OpticalDmdOffset, AnchorControlSteps) :
    return Command.WriteKeystoneCorrectionControl(KeystoneCorrectionEnable, OpticalThrowRatio, OpticalDmdOffset, AnchorControlSteps)

def ReadKeystoneCorrectionControl() :
    Summary, KeystoneCorrectionEnable, OpticalThrowRatio, OpticalDmdOffset, AnchorControlSteps = \
        Command.ReadKeystoneCorrectionControl()
    return Summary, bool(KeystoneCorrectionEnable), float(OpticalThrowRatio), float(OpticalDmdOffset), int(AnchorControlSteps)

def WriteExecuteFlashBatchFile(BatchFileNumber) :
    return Command.WriteExecuteFlashBatchFile(BatchFileNumber)

def WriteDelay(DelayInMicroseconds) :
    return Command.WriteDelay(DelayInMicroseconds)

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

def WriteCmtSelect(DegammaCmtIndex) :
    return Command.WriteCmtSelect(DegammaCmtIndex)

def ReadCmtSelect() :
    Summary, DegammaCmtIndex = \
        Command.ReadCmtSelect()
    return Summary, int(DegammaCmtIndex)

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

def WriteCaicImageProcessingControl(CaicImageProcessingControl) :
    return Command.WriteCaicImageProcessingControl(CaicImageProcessingControl)

def ReadCaicImageProcessingControl() :
    Summary, CaicImageProcessingControl = \
        Command.ReadCaicImageProcessingControl()
    return Summary, CaicImageProcessingControl

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

def ReadFpgaVersion() :
    Summary, FpgaVersion, FpgaEcoRevision, FpgaArmSwVersion = \
        Command.ReadFpgaVersion()
    return Summary, int(FpgaVersion), int(FpgaEcoRevision), int(FpgaArmSwVersion)

def ReadFpgaStatus() :
    Summary, DisplayMode, FpgaKeyingStatus = \
        Command.ReadFpgaStatus()
    return Summary, DisplayMode, FpgaKeyingStatus

def ReadFlashUpdatePrecheck(FlashUpdatePackage) :
    Summary, PackageSizeStatus, PacakgeConfigurationCollapsed, PacakgeConfigurationIdentifier = \
        Command.ReadFlashUpdatePrecheck(FlashUpdatePackage)
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

def WriteXprFpgaRegister(Address, Data) :
    return Command.WriteXprFpgaRegister(Address, Data)

def ReadXprFpgaRegister(Address) :
    Summary, Data = \
        Command.ReadXprFpgaRegister(Address)
    return Summary, int(Data)

def WriteFpgaTestPatternSelect(TestPatternBorder, Color, PatternSelect, Size) :
    return Command.WriteFpgaTestPatternSelect(TestPatternBorder, Color, PatternSelect, Size)

def ReadFpgaTestPatternSelect() :
    Summary, TestPatternBorder, Color, PatternSelect, Size = \
        Command.ReadFpgaTestPatternSelect()
    return Summary, TestPatternBorder, Color, PatternSelect, int(Size)

def WriteFpgaSolidField(Color) :
    return Command.WriteFpgaSolidField(Color)

def WriteFpgaGrid() :
    return Command.WriteFpgaGrid()

def WriteFpgaHorizontalRamp() :
    return Command.WriteFpgaHorizontalRamp()

def WriteFpgaVerticalRamp() :
    return Command.WriteFpgaVerticalRamp()

def WriteFpgaCheckerboard() :
    return Command.WriteFpgaCheckerboard()

def WriteFpgaHorizontalLines() :
    return Command.WriteFpgaHorizontalLines()

def WriteFpgaVerticalLines() :
    return Command.WriteFpgaVerticalLines()

def WriteFpgaDiagonalLines() :
    return Command.WriteFpgaDiagonalLines()

def WriteFpgaActuatorCalibrationPattern() :
    return Command.WriteFpgaActuatorCalibrationPattern()

def WriteFpga3DTestPattern() :
    return Command.WriteFpga3DTestPattern()

def WriteFpgaColorBarTestPattern() :
    return Command.WriteFpgaColorBarTestPattern()

def WriteFpgaFrameAndCrossTestPattern() :
    return Command.WriteFpgaFrameAndCrossTestPattern()

def WriteActuatorConfigurationSelect(VoiceCoil, Axis) :
    return Command.WriteActuatorConfigurationSelect(VoiceCoil, Axis)

def ReadActuatorConfigurationSelect() :
    Summary, VoiceCoil, Axis = \
        Command.ReadActuatorConfigurationSelect()
    return Summary, VoiceCoil, Axis

def WriteActuatorOutputSelect(ActuatorOutputSelect) :
    return Command.WriteActuatorOutputSelect(ActuatorOutputSelect)

def ReadActuatorOutputSelect() :
    Summary, ActuatorOutputSelect = \
        Command.ReadActuatorOutputSelect()
    return Summary, ActuatorOutputSelect

def WriteActuatorEdgeTableAddressMode(ActuatorEdgeTableAddressMode) :
    return Command.WriteActuatorEdgeTableAddressMode(ActuatorEdgeTableAddressMode)

def ReadActuatorEdgeTableAddressMode() :
    Summary, ActuatorEdgeTableAddressMode = \
        Command.ReadActuatorEdgeTableAddressMode()
    return Summary, ActuatorEdgeTableAddressMode

def WriteActuatorFixedOutputLevel(ActuatorFixedOutputLevel) :
    return Command.WriteActuatorFixedOutputLevel(ActuatorFixedOutputLevel)

def ReadActuatorFixedOutputLevel() :
    Summary, ActuatorFixedOutputLevel = \
        Command.ReadActuatorFixedOutputLevel()
    return Summary, int(ActuatorFixedOutputLevel)

def WriteActuatorReferenceOutputLevel(ActuatorReferenceOutputLevel) :
    return Command.WriteActuatorReferenceOutputLevel(ActuatorReferenceOutputLevel)

def ReadActuatorReferenceOutputLevel() :
    Summary, ActuatorReferenceOutputLevel = \
        Command.ReadActuatorReferenceOutputLevel()
    return Summary, int(ActuatorReferenceOutputLevel)

def WriteActuatorGain(ActuatorGain) :
    return Command.WriteActuatorGain(ActuatorGain)

def ReadActuatorGain() :
    Summary, ActuatorGain = \
        Command.ReadActuatorGain()
    return Summary, int(ActuatorGain)

def WriteActuatorOffset(ManualActuatorOffset, AutoOffsetEnable) :
    return Command.WriteActuatorOffset(ManualActuatorOffset, AutoOffsetEnable)

def ReadActuatorOffset() :
    Summary, ManualActuatorOffset, AutoOffsetEnable = \
        Command.ReadActuatorOffset()
    return Summary, int(ManualActuatorOffset), AutoOffsetEnable

def WriteActuatorSegmentLength(SegmentLength) :
    return Command.WriteActuatorSegmentLength(SegmentLength)

def ReadActuatorSegmentLength() :
    Summary, SegmentLength = \
        Command.ReadActuatorSegmentLength()
    return Summary, int(SegmentLength)

def WriteActuatorNumberOfSegments(NumberOfSegments) :
    return Command.WriteActuatorNumberOfSegments(NumberOfSegments)

def ReadActuatorNumberOfSegments() :
    Summary, NumberOfSegments = \
        Command.ReadActuatorNumberOfSegments()
    return Summary, int(NumberOfSegments)

def WriteActuatorSyncDelay(SyncDelayValue, ManualSyncDelayEnable) :
    return Command.WriteActuatorSyncDelay(SyncDelayValue, ManualSyncDelayEnable)

def ReadActuatorSyncDelay() :
    Summary, SyncDelayValue, ManualSyncDelayEnable = \
        Command.ReadActuatorSyncDelay()
    return Summary, int(SyncDelayValue), ManualSyncDelayEnable

def WriteActuatorLatency(SyncLatencyValue, ManualLatencyEnable, AutoLatencyScalingEnable) :
    return Command.WriteActuatorLatency(SyncLatencyValue, ManualLatencyEnable, AutoLatencyScalingEnable)

def ReadActuatorLatency() :
    Summary, SyncLatencyValue, ManualLatencyEnable, AutoLatencyScalingEnable = \
        Command.ReadActuatorLatency()
    return Summary, int(SyncLatencyValue), ManualLatencyEnable, AutoLatencyScalingEnable

def WriteActuatorClockStretch(PeriodStretch) :
    return Command.WriteActuatorClockStretch(PeriodStretch)

def ReadActuatorClockStretch() :
    Summary, PeriodStretch = \
        Command.ReadActuatorClockStretch()
    return Summary, int(PeriodStretch)

def WriteActuatorDacOutputEnable(ActuatorDacOutputEnable) :
    return Command.WriteActuatorDacOutputEnable(ActuatorDacOutputEnable)

def ReadActuatorDacOutputEnable() :
    Summary, ActuatorDacOutputEnable = \
        Command.ReadActuatorDacOutputEnable()
    return Summary, ActuatorDacOutputEnable

