#-------------------------------------
# Copyright (c) 2023 Texas Instruments
#-------------------------------------

# NOTE: This file is auto generated from a command definition file.
#       Please do not modify the file directly.                    
#
# Command Spec Version : 0.1

import sys
import clr

clr.AddReference('DLPComposer.Commands.DLPC843x')
from System import *
from DLPComposer.Commands.DLPC843x import * 

def ReadMode() :
    Summary, BootOrMainApp, ControllerConfiguration, FormatterOrFullApp = \
        Command.ReadMode()
    return Summary, BootOrMainApp, ControllerConfiguration, FormatterOrFullApp

def ReadVersion() :
    Summary, Major, Minor, Patch = \
        Command.ReadVersion()
    return Summary, int(Major), int(Minor), int(Patch)

def WriteSwitchMode(BootOrMainApp) :
    return Command.WriteSwitchMode(BootOrMainApp)

def WriteMemory(Address, Value) :
    return Command.WriteMemory(Address, Value)

def ReadMemory(Address) :
    Summary, Value = \
        Command.ReadMemory(Address)
    return Summary, int(Value)

def ReadFlashId() :
    Summary, ManufacturerId, DeviceId = \
        Command.ReadFlashId()
    return Summary, int(ManufacturerId), int(DeviceId)

def ReadFlashSectorInfo() :
    Summary, SectorInfo = \
        Command.ReadFlashSectorInfo()
    return Summary, list(SectorInfo)

def WriteUnlockFlashUpdate() :
    return Command.WriteUnlockFlashUpdate()

def WriteLockFlashUpdate() :
    return Command.WriteLockFlashUpdate()

def ReadFlashUpdateLock() :
    Summary, Unlocked = \
        Command.ReadFlashUpdateLock()
    return Summary, bool(Unlocked)

def WriteEraseSector(AddressOffset) :
    return Command.WriteEraseSector(AddressOffset)

def WriteInitFlashOperation(FlashAddressOffset, FlashReadWriteSize) :
    return Command.WriteInitFlashOperation(FlashAddressOffset, FlashReadWriteSize)

def WriteFlash(Data) :
    Data = Array[Byte](Data)
    return Command.WriteFlash(Data)

def ReadFlash(NumBytes) :
    Summary, Data = \
        Command.ReadFlash(NumBytes)
    return Summary, bytearray(Data)

def ReadChecksum(StartAddressOffset, NumBytes) :
    Summary, SimpleChecksum, SumOfSumChecksum = \
        Command.ReadChecksum(StartAddressOffset, NumBytes)
    return Summary, int(SimpleChecksum), int(SumOfSumChecksum)

