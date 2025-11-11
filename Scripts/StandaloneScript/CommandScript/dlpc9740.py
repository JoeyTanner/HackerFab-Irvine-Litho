#-------------------------------------------------------------------------------
# Copyright (c) 2024 Texas Instruments Incorporated - http://www.ti.com/
#-------------------------------------------------------------------------------
#
# NOTE: This file is auto generated from a command definition file.
#       Please do not modify the file directly.                    
#
# Command Spec Version : 1.1
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

_readcommand = None
_writecommand = None

def DLPC9740init(readcommandcb, writecommandcb):
    global _readcommand
    global _writecommand
    _readcommand = readcommandcb
    _writecommand = writecommandcb

    global Summary
    Summary.CommInterface = "DLPC9740"

    global PortocolData
    ProtocolData.CommandDestination = 0
    ProtocolData.OpcodeLength = 0
    ProtocolData.BytesRead = 0

def WriteRegister(Address,  Data):
    "Write Register"
    global Summary
    Summary.Command = "Write Register"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',241))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('I',Address)))
        writebytes.extend(list(struct.pack('I',Data)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadRegister(Address):
    "Read Register"
    global Summary
    Summary.Command = "Read Register"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',242))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('I',Address)))
        readbytes = _readcommand(4, writebytes, ProtocolData)
        Data = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Data

def WriteRegisterSpi(Address,  Data):
    "Write Register spi"
    global Summary
    Summary.Command = "Write Register Spi"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',2))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('I',Address)))
        valueArray = [0x00]
        writebytes.extend(valueArray)
        writebytes.extend(list(struct.pack('I',Data)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadRegisterSpi(Address):
    "Read Register spi"
    global Summary
    Summary.Command = "Read Register Spi"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',1))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('I',Address)))
        valueArray = [0x00]
        writebytes.extend(valueArray)
        readbytes = _readcommand(4, writebytes, ProtocolData)
        Data = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Data

