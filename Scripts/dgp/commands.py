#-------------------------------------
# Copyright (c) 2024 Texas Instruments
#-------------------------------------

# NOTE: This file is auto generated from a command definition file.
#       Please do not modify the file directly.                    
#
# Command Spec Version : 1.0

import sys
import clr

clr.AddReference('DLPComposer.Commands.DGP')
from System import *
from DLPComposer.Commands.DGP import * 

def WriteInternalRegister(Address, Data) :
    return Command.WriteInternalRegister(Address, Data)

def ReadInternalRegister(Address) :
    Summary, Data = \
        Command.ReadInternalRegister(Address)
    return Summary, int(Data)

def WriteFpgaInterruptClear(Data) :
    return Command.WriteFpgaInterruptClear(Data)

def ReadFpgaInterruptClear() :
    Summary, Data = \
        Command.ReadFpgaInterruptClear()
    return Summary, int(Data)

def WriteFpgaInterruptSet(Data) :
    return Command.WriteFpgaInterruptSet(Data)

def ReadFpgaInterruptSet() :
    Summary, Data = \
        Command.ReadFpgaInterruptSet()
    return Summary, int(Data)

def WriteFpgaInterruptEnable(RegisterAccessTimeoutIrq, InitDoneIrq, BrownoutIrq, VidLoopCompIrq, VidConfigCompIrq) :
    return Command.WriteFpgaInterruptEnable(RegisterAccessTimeoutIrq, InitDoneIrq, BrownoutIrq, VidLoopCompIrq, VidConfigCompIrq)

def ReadFpgaInterruptEnable() :
    Summary, RegisterAccessTimeoutIrq, InitDoneIrq, BrownoutIrq, VidLoopCompIrq, VidConfigCompIrq = \
        Command.ReadFpgaInterruptEnable()
    return Summary, bool(RegisterAccessTimeoutIrq), bool(InitDoneIrq), bool(BrownoutIrq), bool(VidLoopCompIrq), bool(VidConfigCompIrq)

def WriteFpgaMainStatus(MainStatusSsfPllLocked) :
    return Command.WriteFpgaMainStatus(MainStatusSsfPllLocked)

def ReadFpgaMainStatus() :
    Summary, MainStatusSsfPllLocked = \
        Command.ReadFpgaMainStatus()
    return Summary, bool(MainStatusSsfPllLocked)

def ReadFpgaVersion() :
    Summary, BuildNumber, VersionMajor, VersionMinor, BuildLevel = \
        Command.ReadFpgaVersion()
    return Summary, int(BuildNumber), int(VersionMajor), int(VersionMinor), int(BuildLevel)

def WriteFpgaControl(FpgaControlDifTpgEn, FpgaControlLdcEn) :
    return Command.WriteFpgaControl(FpgaControlDifTpgEn, FpgaControlLdcEn)

def ReadFpgaControl() :
    Summary, FpgaControlDifTpgEn, FpgaControlLdcEn = \
        Command.ReadFpgaControl()
    return Summary, bool(FpgaControlDifTpgEn), bool(FpgaControlLdcEn)

def WriteFmtFlip(DmdSflip, DmdLflip) :
    return Command.WriteFmtFlip(DmdSflip, DmdLflip)

def ReadFmtFlip() :
    Summary, DmdSflip, DmdLflip = \
        Command.ReadFmtFlip()
    return Summary, bool(DmdSflip), bool(DmdLflip)

def WriteFmtControl(FmtCtrlTrcen, FmtCtrlCmboutswap) :
    return Command.WriteFmtControl(FmtCtrlTrcen, FmtCtrlCmboutswap)

def ReadFmtControl() :
    Summary, FmtCtrlTrcen, FmtCtrlCmboutswap = \
        Command.ReadFmtControl()
    return Summary, bool(FmtCtrlTrcen), bool(FmtCtrlCmboutswap)

def WriteFmtCmbStatus(FmtCmbQueuewrn, FmtCmbCmderr, FmtCmbMulterr, FmtCmbNodataerr) :
    return Command.WriteFmtCmbStatus(FmtCmbQueuewrn, FmtCmbCmderr, FmtCmbMulterr, FmtCmbNodataerr)

def ReadFmtCmbStatus() :
    Summary, FmtCmbQueuewrn, FmtCmbCmderr, FmtCmbMulterr, FmtCmbNodataerr = \
        Command.ReadFmtCmbStatus()
    return Summary, bool(FmtCmbQueuewrn), bool(FmtCmbCmderr), bool(FmtCmbMulterr), bool(FmtCmbNodataerr)

def WriteFmtFrbStatus(FmtFrbEmpty, FmtFrbOverflow) :
    return Command.WriteFmtFrbStatus(FmtFrbEmpty, FmtFrbOverflow)

def ReadFmtFrbStatus() :
    Summary, FmtFrbEmpty, FmtFrbOverflow = \
        Command.ReadFmtFrbStatus()
    return Summary, bool(FmtFrbEmpty), bool(FmtFrbOverflow)

def WriteRscSwDmdUnpark(RscSwDmdUnpark) :
    return Command.WriteRscSwDmdUnpark(RscSwDmdUnpark)

def ReadRscSwDmdUnpark() :
    Summary, RscSwDmdUnpark = \
        Command.ReadRscSwDmdUnpark()
    return Summary, bool(RscSwDmdUnpark)

def WriteRscParkWaveformCtrl(RscParkVcclvFld) :
    return Command.WriteRscParkWaveformCtrl(RscParkVcclvFld)

def ReadRscParkWaveformCtrl() :
    Summary, RscParkVcclvFld = \
        Command.ReadRscParkWaveformCtrl()
    return Summary, bool(RscParkVcclvFld)

def WriteRscUnused(Data) :
    return Command.WriteRscUnused(Data)

def ReadRscUnused() :
    Summary, Data = \
        Command.ReadRscUnused()
    return Summary, int(Data)

def WriteRscMiscControl(RscMctrlShadowenable) :
    return Command.WriteRscMiscControl(RscMctrlShadowenable)

def ReadRscMiscControl() :
    Summary, RscMctrlShadowenable = \
        Command.ReadRscMiscControl()
    return Summary, bool(RscMctrlShadowenable)

def WriteRscSeqControl(RscSeqctrlSeqen, RscSeqctrlVectincen, RscSeqctrlSeqvect, RscSeqctrlNumsubvect) :
    return Command.WriteRscSeqControl(RscSeqctrlSeqen, RscSeqctrlVectincen, RscSeqctrlSeqvect, RscSeqctrlNumsubvect)

def ReadRscSeqControl() :
    Summary, RscSeqctrlSeqen, RscSeqctrlVectincen, RscSeqctrlSeqvect, RscSeqctrlNumsubvect = \
        Command.ReadRscSeqControl()
    return Summary, bool(RscSeqctrlSeqen), bool(RscSeqctrlVectincen), int(RscSeqctrlSeqvect), int(RscSeqctrlNumsubvect)

def WriteSequenceSelect(SeqbufSelect) :
    return Command.WriteSequenceSelect(SeqbufSelect)

def ReadSequenceSelect() :
    Summary, SeqbufSelect = \
        Command.ReadSequenceSelect()
    return Summary, bool(SeqbufSelect)

def WritePwmControl(RpwmDc, GpwmDc, BpwmDc, PwmEn) :
    return Command.WritePwmControl(RpwmDc, GpwmDc, BpwmDc, PwmEn)

def ReadPwmControl() :
    Summary, RpwmDc, GpwmDc, BpwmDc, PwmEn = \
        Command.ReadPwmControl()
    return Summary, int(RpwmDc), int(GpwmDc), int(BpwmDc), bool(PwmEn)

def WriteVideoFrameRate(VideoFrameRate) :
    return Command.WriteVideoFrameRate(VideoFrameRate)

def ReadVideoFrameRate() :
    Summary, VideoFrameRate = \
        Command.ReadVideoFrameRate()
    return Summary, int(VideoFrameRate)

def WriteVideoStartAddress1(StartAddr1) :
    return Command.WriteVideoStartAddress1(StartAddr1)

def ReadVideoStartAddress1() :
    Summary, StartAddr1 = \
        Command.ReadVideoStartAddress1()
    return Summary, int(StartAddr1)

def WriteVideoConfiguration1(FrameCnt1, LoopCnt1) :
    return Command.WriteVideoConfiguration1(FrameCnt1, LoopCnt1)

def ReadVideoConfiguration1() :
    Summary, FrameCnt1, LoopCnt1 = \
        Command.ReadVideoConfiguration1()
    return Summary, int(FrameCnt1), int(LoopCnt1)

def WriteVideoStartAddress2(StartAddr2) :
    return Command.WriteVideoStartAddress2(StartAddr2)

def ReadVideoStartAddress2() :
    Summary, StartAddr2 = \
        Command.ReadVideoStartAddress2()
    return Summary, int(StartAddr2)

def WriteVideoConfiguration2(FrameCnt2, LoopCnt2) :
    return Command.WriteVideoConfiguration2(FrameCnt2, LoopCnt2)

def ReadVideoConfiguration2() :
    Summary, FrameCnt2, LoopCnt2 = \
        Command.ReadVideoConfiguration2()
    return Summary, int(FrameCnt2), int(LoopCnt2)

def WriteVideoControl(VideoControl) :
    return Command.WriteVideoControl(VideoControl)

def ReadVideoControl() :
    Summary, VideoControl = \
        Command.ReadVideoControl()
    return Summary, VideoControl

def ReadVideoStatus() :
    Summary, VidInProgress, CurrConfigPtr, SeqAbortErr = \
        Command.ReadVideoStatus()
    return Summary, bool(VidInProgress), bool(CurrConfigPtr), bool(SeqAbortErr)

def WriteVcmSeqabort(VcmMaxSeqabort) :
    return Command.WriteVcmSeqabort(VcmMaxSeqabort)

def ReadVcmSeqabort() :
    Summary, VcmMaxSeqabort = \
        Command.ReadVcmSeqabort()
    return Summary, int(VcmMaxSeqabort)

def WriteVcmTmsel(VcmTmsel) :
    return Command.WriteVcmTmsel(VcmTmsel)

def ReadVcmTmsel() :
    Summary, VcmTmsel = \
        Command.ReadVcmTmsel()
    return Summary, int(VcmTmsel)

def WriteTmpCtrl(NFactor, I2CSlaveAddr, CtrlEn) :
    return Command.WriteTmpCtrl(NFactor, I2CSlaveAddr, CtrlEn)

def ReadTmpCtrl() :
    Summary, NFactor, I2CSlaveAddr, CtrlEn = \
        Command.ReadTmpCtrl()
    return Summary, int(NFactor), int(I2CSlaveAddr), bool(CtrlEn)

def ReadTmpStatus() :
    Summary, Pass, Valid = \
        Command.ReadTmpStatus()
    return Summary, bool(Pass), bool(Valid)

def ReadTemperatureRemoteChannel() :
    Summary, TmpRemoteRaw, TmpRemoteFiltered = \
        Command.ReadTemperatureRemoteChannel()
    return Summary, int(TmpRemoteRaw), int(TmpRemoteFiltered)

def ReadTemperatureLocalChannel() :
    Summary, TmpLocalRaw, TmpLocalFiltered = \
        Command.ReadTemperatureLocalChannel()
    return Summary, int(TmpLocalRaw), int(TmpLocalFiltered)

def WriteDestopTimeoutDebugInfoReg(DestopTimeoutAddrOffs, DestopTimeoutRnw) :
    return Command.WriteDestopTimeoutDebugInfoReg(DestopTimeoutAddrOffs, DestopTimeoutRnw)

def ReadDestopTimeoutDebugInfoReg() :
    Summary, DestopTimeoutAddrOffs, DestopTimeoutRnw = \
        Command.ReadDestopTimeoutDebugInfoReg()
    return Summary, int(DestopTimeoutAddrOffs), bool(DestopTimeoutRnw)

def WriteDestopMbox0SaptrReg(DestopMbox0Saptr) :
    return Command.WriteDestopMbox0SaptrReg(DestopMbox0Saptr)

def ReadDestopMbox0SaptrReg() :
    Summary, DestopMbox0Saptr = \
        Command.ReadDestopMbox0SaptrReg()
    return Summary, int(DestopMbox0Saptr)

def WriteDestopMbox0CtrlReg(DestopMbox0Mbasel, DestopMbox0Saptrhld) :
    return Command.WriteDestopMbox0CtrlReg(DestopMbox0Mbasel, DestopMbox0Saptrhld)

def ReadDestopMbox0CtrlReg() :
    Summary, DestopMbox0Mbasel, DestopMbox0Saptrhld = \
        Command.ReadDestopMbox0CtrlReg()
    return Summary, int(DestopMbox0Mbasel), bool(DestopMbox0Saptrhld)

def WriteDestopMbox0DataReg(DestopMbox0Data) :
    return Command.WriteDestopMbox0DataReg(DestopMbox0Data)

def ReadDestopMbox0DataReg() :
    Summary, DestopMbox0Data = \
        Command.ReadDestopMbox0DataReg()
    return Summary, int(DestopMbox0Data)

def WriteDestopMbox1SaptrReg(DestopMbox1Saptr) :
    return Command.WriteDestopMbox1SaptrReg(DestopMbox1Saptr)

def ReadDestopMbox1SaptrReg() :
    Summary, DestopMbox1Saptr = \
        Command.ReadDestopMbox1SaptrReg()
    return Summary, int(DestopMbox1Saptr)

def WriteDestopMbox1CtrlReg(DestopMbox1Mbasel, DestopMbox1Saptrhld) :
    return Command.WriteDestopMbox1CtrlReg(DestopMbox1Mbasel, DestopMbox1Saptrhld)

def ReadDestopMbox1CtrlReg() :
    Summary, DestopMbox1Mbasel, DestopMbox1Saptrhld = \
        Command.ReadDestopMbox1CtrlReg()
    return Summary, int(DestopMbox1Mbasel), bool(DestopMbox1Saptrhld)

def WriteDestopMbox1DataReg(DestopMbox1Data) :
    return Command.WriteDestopMbox1DataReg(DestopMbox1Data)

def ReadDestopMbox1DataReg() :
    Summary, DestopMbox1Data = \
        Command.ReadDestopMbox1DataReg()
    return Summary, int(DestopMbox1Data)

