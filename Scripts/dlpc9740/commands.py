#-------------------------------------
# Copyright (c) 2024 Texas Instruments
#-------------------------------------

# NOTE: This file is auto generated from a command definition file.
#       Please do not modify the file directly.                    
#
# Command Spec Version : 1.1

import sys
import clr

clr.AddReference('DLPComposer.Commands.DLPC9740')
from System import *
from DLPComposer.Commands.DLPC9740 import * 

def WriteRegister(Address, Data) :
    return Command.WriteRegister(Address, Data)

def ReadRegister(Address) :
    Summary, Data = \
        Command.ReadRegister(Address)
    return Summary, int(Data)

def WriteRegisterSpi(Address, Data) :
    return Command.WriteRegisterSpi(Address, Data)

def ReadRegisterSpi(Address) :
    Summary, Data = \
        Command.ReadRegisterSpi(Address)
    return Summary, int(Data)

