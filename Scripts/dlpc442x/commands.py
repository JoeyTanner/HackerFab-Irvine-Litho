#-------------------------------------
# Copyright (c) 2024 Texas Instruments
#-------------------------------------

# NOTE: This file is auto generated from a command definition file.
#       Please do not modify the file directly.                    
#
# Command Spec Version : 1.0

import sys
import clr

clr.AddReference('DLPComposer.Commands.DLPC442x')
from System import *
from DLPComposer.Commands.DLPC442x import * 

def WriteMemory(Address, Data) :
    return Command.WriteMemory(Address, Data)

def ReadMemory(Address) :
    Summary, Data = \
        Command.ReadMemory(Address)
    return Summary, int(Data)

