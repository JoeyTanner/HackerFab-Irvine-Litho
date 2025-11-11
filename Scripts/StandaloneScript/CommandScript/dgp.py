#-------------------------------------------------------------------------------
# Copyright (c) 2024 Texas Instruments Incorporated - http://www.ti.com/
#-------------------------------------------------------------------------------
#
# NOTE: This file is auto generated from a command definition file.
#       Please do not modify the file directly.                    
#
# Command Spec Version : 1.0
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

class Summary:
    Command: str
    CommInterface: str
    Successful: bool

class ProtocolData:
    CommandDestination: int
    OpcodeLength: int
    BytesRead: int

class VideoControl:
     Play: bool
     Stop: bool
     Autostop: bool
     BufPtr: bool
     LoopConfigs: bool
     ToggleConfigs: bool

_readcommand = None
_writecommand = None

def DGPinit(readcommandcb, writecommandcb):
    global _readcommand
    global _writecommand
    _readcommand = readcommandcb
    _writecommand = writecommandcb

    global Summary
    Summary.CommInterface = "DGP"

    global PortocolData
    ProtocolData.CommandDestination = 0
    ProtocolData.OpcodeLength = 0
    ProtocolData.BytesRead = 0

def WriteFpgaInterruptClear(Data):
    "Interrupt Clear/Status Register"
    global Summary
    Summary.Command = "Write FPGA Interrupt Clear"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',0))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x00, 0x00]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('I',Data)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadFpgaInterruptClear():
    "Interrupt Clear/Status Register"
    global Summary
    Summary.Command = "Read FPGA Interrupt Clear"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x00, 0x00]
        writebytes.extend(valueArray)
        readbytes = _readcommand(4, writebytes, ProtocolData)
        Data = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Data

def WriteFpgaInterruptSet(Data):
    "Interrupt Clear/Status Register"
    global Summary
    Summary.Command = "Write FPGA Interrupt Set"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',0))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x04, 0x00]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('I',Data)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadFpgaInterruptSet():
    "Interrupt Clear/Status Register"
    global Summary
    Summary.Command = "Read FPGA Interrupt Set"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x04, 0x00]
        writebytes.extend(valueArray)
        readbytes = _readcommand(4, writebytes, ProtocolData)
        Data = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Data

def WriteFpgaInterruptEnable(RegisterAccessTimeoutIrq,  InitDoneIrq,  BrownoutIrq,  VidLoopCompIrq,  VidConfigCompIrq):
    "Interrupt Clear/Status Register"
    global Summary
    Summary.Command = "Write FPGA Interrupt Enable"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',0))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x08, 0x00]
        writebytes.extend(valueArray)
        packerinit()
        value = setbits(int(RegisterAccessTimeoutIrq), 1, 0)
        value = setbits(int(InitDoneIrq), 1, 1)
        value = setbits(int(BrownoutIrq), 1, 2)
        value = setbits(int(VidLoopCompIrq), 1, 3)
        value = setbits(int(VidConfigCompIrq), 1, 4)
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadFpgaInterruptEnable():
    "Interrupt Clear/Status Register"
    global Summary
    Summary.Command = "Read FPGA Interrupt Enable"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x08, 0x00]
        writebytes.extend(valueArray)
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        RegisterAccessTimeoutIrq = getbits(1, 0);
        InitDoneIrq = getbits(1, 1);
        BrownoutIrq = getbits(1, 2);
        VidLoopCompIrq = getbits(1, 3);
        VidConfigCompIrq = getbits(1, 4);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, RegisterAccessTimeoutIrq, InitDoneIrq, BrownoutIrq, VidLoopCompIrq, VidConfigCompIrq

def ReadFpgaVersion():
    "FPGA bitstream version"
    global Summary
    Summary.Command = "Read FPGA Version"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x10, 0x00]
        writebytes.extend(valueArray)
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        BuildNumber = getbits(12, 0);
        VersionMajor = getbits(8, 12);
        VersionMinor = getbits(8, 20);
        BuildLevel = getbits(4, 28);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, BuildNumber, VersionMajor, VersionMinor, BuildLevel

def WriteFmtFlip(DmdSflip,  DmdLflip):
    "FMT Flip Control"
    global Summary
    Summary.Command = "Write FMT Flip"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',0))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x20, 0x00]
        writebytes.extend(valueArray)
        packerinit()
        value = setbits(int(DmdSflip), 1, 0)
        value = setbits(int(DmdLflip), 1, 4)
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadFmtFlip():
    "FMT Flip Control"
    global Summary
    Summary.Command = "Read FMT Flip"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x20, 0x00]
        writebytes.extend(valueArray)
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        DmdSflip = getbits(1, 0);
        DmdLflip = getbits(1, 4);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DmdSflip, DmdLflip

def WriteSequenceSelect(SeqbufSelect):
    "Sequence Buffer Select"
    global Summary
    Summary.Command = "Write Sequence Select"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',0))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x44, 0x00]
        writebytes.extend(valueArray)
        packerinit()
        value = setbits(int(SeqbufSelect), 1, 0)
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadSequenceSelect():
    "Sequence Buffer Select"
    global Summary
    Summary.Command = "Read Sequence Select"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x44, 0x00]
        writebytes.extend(valueArray)
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        SeqbufSelect = getbits(1, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SeqbufSelect

def WritePwmControl(RpwmDc,  GpwmDc,  BpwmDc,  PwmEn):
    "PWM Control"
    global Summary
    Summary.Command = "Write PWM Control"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',0))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x50, 0x00]
        writebytes.extend(valueArray)
        packerinit()
        value = setbits(int(RpwmDc), 10, 0)
        value = setbits(int(GpwmDc), 10, 10)
        value = setbits(int(BpwmDc), 10, 20)
        value = setbits(int(PwmEn), 1, 30)
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadPwmControl():
    "PWM Control"
    global Summary
    Summary.Command = "Read PWM Control"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x50, 0x00]
        writebytes.extend(valueArray)
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        RpwmDc = getbits(10, 0);
        GpwmDc = getbits(10, 10);
        BpwmDc = getbits(10, 20);
        PwmEn = getbits(1, 30);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, RpwmDc, GpwmDc, BpwmDc, PwmEn

def WriteVideoFrameRate(VideoFrameRate):
    "Video frame rate"
    global Summary
    Summary.Command = "Write Video Frame Rate"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',0))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x60, 0x00]
        writebytes.extend(valueArray)
        packerinit()
        value = setbits(int(VideoFrameRate), 24, 0)
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadVideoFrameRate():
    "Video frame rate"
    global Summary
    Summary.Command = "Read Video Frame Rate"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x60, 0x00]
        writebytes.extend(valueArray)
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        VideoFrameRate = getbits(24, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, VideoFrameRate

def WriteVideoStartAddress1(StartAddr1):
    "Video start address 1"
    global Summary
    Summary.Command = "Write Video Start Address 1"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',0))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x64, 0x00]
        writebytes.extend(valueArray)
        packerinit()
        value = setbits(int(StartAddr1), 32, 0)
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadVideoStartAddress1():
    "Video start address 1"
    global Summary
    Summary.Command = "Read Video Start Address 1"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x64, 0x00]
        writebytes.extend(valueArray)
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        StartAddr1 = getbits(32, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, StartAddr1

def WriteVideoConfiguration1(FrameCnt1,  LoopCnt1):
    "Video configuration 1"
    global Summary
    Summary.Command = "Write Video Configuration 1"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',0))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x68, 0x00]
        writebytes.extend(valueArray)
        packerinit()
        value = setbits(int(FrameCnt1), 12, 0)
        value = setbits(int(LoopCnt1), 12, 12)
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadVideoConfiguration1():
    "Video configuration 1"
    global Summary
    Summary.Command = "Read Video Configuration 1"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x68, 0x00]
        writebytes.extend(valueArray)
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        FrameCnt1 = getbits(12, 0);
        LoopCnt1 = getbits(12, 12);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, FrameCnt1, LoopCnt1

def WriteVideoStartAddress2(StartAddr2):
    "Video start address 2"
    global Summary
    Summary.Command = "Write Video Start Address 2"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',0))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x6C, 0x00]
        writebytes.extend(valueArray)
        packerinit()
        value = setbits(int(StartAddr2), 32, 0)
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadVideoStartAddress2():
    "Video start address 2"
    global Summary
    Summary.Command = "Read Video Start Address 2"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x6C, 0x00]
        writebytes.extend(valueArray)
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        StartAddr2 = getbits(32, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, StartAddr2

def WriteVideoConfiguration2(FrameCnt2,  LoopCnt2):
    "Video configuration 2"
    global Summary
    Summary.Command = "Write Video Configuration 2"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',0))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x70, 0x00]
        writebytes.extend(valueArray)
        packerinit()
        value = setbits(int(FrameCnt2), 12, 0)
        value = setbits(int(LoopCnt2), 12, 12)
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadVideoConfiguration2():
    "Video configuration 2"
    global Summary
    Summary.Command = "Read Video Configuration 2"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x70, 0x00]
        writebytes.extend(valueArray)
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        FrameCnt2 = getbits(12, 0);
        LoopCnt2 = getbits(12, 12);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, FrameCnt2, LoopCnt2

def WriteVideoControl(VideoControl):
    "Video control"
    global Summary
    Summary.Command = "Write Video Control"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',0))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x74, 0x00]
        writebytes.extend(valueArray)
        packerinit()
        value = setbits(int(VideoControl.Play), 1, 0)
        value = setbits(int(VideoControl.Stop), 1, 1)
        value = setbits(int(VideoControl.Autostop), 1, 2)
        value = setbits(int(VideoControl.BufPtr), 1, 3)
        value = setbits(int(VideoControl.LoopConfigs), 1, 4)
        value = setbits(int(VideoControl.ToggleConfigs), 1, 5)
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadVideoControl():
    "Video control"
    global Summary
    Summary.Command = "Read Video Control"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x74, 0x00]
        writebytes.extend(valueArray)
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        VideoControl.Play = getbits(1, 0);
        VideoControl.Stop = getbits(1, 1);
        VideoControl.Autostop = getbits(1, 2);
        VideoControl.BufPtr = getbits(1, 3);
        VideoControl.LoopConfigs = getbits(1, 4);
        VideoControl.ToggleConfigs = getbits(1, 5);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, VideoControl

def WriteTmpCtrl(NFactor,  I2CSlaveAddr,  CtrlEn):
    "Temperature control"
    global Summary
    Summary.Command = "Write TMP CTRL"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',0))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x90, 0x00]
        writebytes.extend(valueArray)
        packerinit()
        value = setbits(int(NFactor), 8, 0)
        value = setbits(int(I2CSlaveAddr), 8, 8)
        value = setbits(int(CtrlEn), 1, 16)
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadTmpCtrl():
    "Temperature control"
    global Summary
    Summary.Command = "Read TMP CTRL"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x90, 0x00]
        writebytes.extend(valueArray)
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        NFactor = getbits(8, 0);
        I2CSlaveAddr = getbits(8, 8);
        CtrlEn = getbits(1, 16);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, NFactor, I2CSlaveAddr, CtrlEn

def ReadTmpStatus():
    "Temperature status"
    global Summary
    Summary.Command = "Read TMP STATUS"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x94, 0x00]
        writebytes.extend(valueArray)
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        Pass = getbits(1, 0);
        Valid = getbits(1, 1);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Pass, Valid

def ReadTemperatureRemoteChannel():
    "Temperature sensor remote channel"
    global Summary
    Summary.Command = "Read Temperature Remote Channel"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x98, 0x00]
        writebytes.extend(valueArray)
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        TmpRemoteRaw = getbits(12, 0);
        TmpRemoteFiltered = getbits(12, 16);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, TmpRemoteRaw, TmpRemoteFiltered

def ReadTemperatureLocalChannel():
    "Temperature sensor local channel"
    global Summary
    Summary.Command = "Read Temperature Local Channel"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x9C, 0x00]
        writebytes.extend(valueArray)
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        TmpLocalRaw = getbits(12, 0);
        TmpLocalFiltered = getbits(12, 16);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, TmpLocalRaw, TmpLocalFiltered

def ReadDestopTimeoutDebugInfoReg():
    "DESTOP Timeout Debug Information Register"
    global Summary
    Summary.Command = "Read DESTOP TIMEOUT DEBUG INFO REG"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0xDC, 0x00]
        writebytes.extend(valueArray)
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        DestopTimeoutAddrOffs = getbits(12, 0);
        DestopTimeoutRnw = getbits(1, 12);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DestopTimeoutAddrOffs, DestopTimeoutRnw

def WriteDestopMbox0SaptrReg(DestopMbox0Saptr):
    "Sub-Address Pointer Register"
    global Summary
    Summary.Command = "Write DESTOP MBOX 0 SAPTR REG"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',0))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0xE0, 0x00]
        writebytes.extend(valueArray)
        packerinit()
        value = setbits(int(DestopMbox0Saptr), 6, 0)
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDestopMbox0SaptrReg():
    "Sub-Address Pointer Register"
    global Summary
    Summary.Command = "Read DESTOP MBOX 0 SAPTR REG"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0xE0, 0x00]
        writebytes.extend(valueArray)
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        DestopMbox0Saptr = getbits(6, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DestopMbox0Saptr

def WriteDestopMbox0CtrlReg(DestopMbox0Mbasel,  DestopMbox0Saptrhld):
    "Access Control Register"
    global Summary
    Summary.Command = "Write DESTOP MBOX 0 CTRL REG"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',0))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0xE4, 0x00]
        writebytes.extend(valueArray)
        packerinit()
        value = setbits(int(DestopMbox0Mbasel), 4, 0)
        value = setbits(int(DestopMbox0Saptrhld), 1, 4)
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDestopMbox0CtrlReg():
    "Access Control Register"
    global Summary
    Summary.Command = "Read DESTOP MBOX 0 CTRL REG"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0xE4, 0x00]
        writebytes.extend(valueArray)
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        DestopMbox0Mbasel = getbits(4, 0);
        DestopMbox0Saptrhld = getbits(1, 4);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DestopMbox0Mbasel, DestopMbox0Saptrhld

def WriteDestopMbox0DataReg(DestopMbox0Data):
    "Mailbox Data Register"
    global Summary
    Summary.Command = "Write DESTOP MBOX 0 DATA REG"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',0))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0xF0, 0x00]
        writebytes.extend(valueArray)
        packerinit()
        value = setbits(int(DestopMbox0Data), 32, 0)
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDestopMbox0DataReg():
    "Mailbox Data Register"
    global Summary
    Summary.Command = "Read DESTOP MBOX 0 DATA REG"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0xF0, 0x00]
        writebytes.extend(valueArray)
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        DestopMbox0Data = getbits(32, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DestopMbox0Data

def WriteDestopMbox1SaptrReg(DestopMbox1Saptr):
    "Sub-Address Pointer Register"
    global Summary
    Summary.Command = "Write DESTOP MBOX 1 SAPTR REG"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',0))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x00, 0x01]
        writebytes.extend(valueArray)
        packerinit()
        value = setbits(int(DestopMbox1Saptr), 12, 0)
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDestopMbox1SaptrReg():
    "Sub-Address Pointer Register"
    global Summary
    Summary.Command = "Read DESTOP MBOX 1 SAPTR REG"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x00, 0x01]
        writebytes.extend(valueArray)
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        DestopMbox1Saptr = getbits(12, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DestopMbox1Saptr

def WriteDestopMbox1CtrlReg(DestopMbox1Mbasel,  DestopMbox1Saptrhld):
    "Access Control Register"
    global Summary
    Summary.Command = "Write DESTOP MBOX 1 CTRL REG"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',0))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x04, 0x01]
        writebytes.extend(valueArray)
        packerinit()
        value = setbits(int(DestopMbox1Mbasel), 4, 0)
        value = setbits(int(DestopMbox1Saptrhld), 1, 4)
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDestopMbox1CtrlReg():
    "Access Control Register"
    global Summary
    Summary.Command = "Read DESTOP MBOX 1 CTRL REG"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x04, 0x01]
        writebytes.extend(valueArray)
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        DestopMbox1Mbasel = getbits(4, 0);
        DestopMbox1Saptrhld = getbits(1, 4);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DestopMbox1Mbasel, DestopMbox1Saptrhld

def WriteDestopMbox1DataReg(DestopMbox1Data):
    "Mailbox Data Register"
    global Summary
    Summary.Command = "Write DESTOP MBOX 1 DATA REG"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',0))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x10, 0x01]
        writebytes.extend(valueArray)
        packerinit()
        value = setbits(int(DestopMbox1Data), 32, 0)
        writebytes.extend(list(struct.pack('L',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDestopMbox1DataReg():
    "Mailbox Data Register"
    global Summary
    Summary.Command = "Read DESTOP MBOX 1 DATA REG"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x10, 0x01]
        writebytes.extend(valueArray)
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        DestopMbox1Data = getbits(32, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DestopMbox1Data

