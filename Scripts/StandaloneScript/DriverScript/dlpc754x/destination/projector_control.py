	
#!/cygdrive/c/Python27/python
# ******************************************************************************
# 
#   Copyright (c) 2019 Texas Instruments
# 
# ******************************************************************************/
# 
#  Projector control commands.
#  
# ******************************************************************************

import sys
import time
import os
import array
from cStringIO import StringIO

from command_handler.core.core import *
import command_handler.core.utils as utils

class ProjectorControl:
    
	DESTINATION_VALUE = 2
	NUM_CMD_BYTES = 2

	def __init__(self, phy, use_seq, use_len, use_checksum):
		self.tx_header = TxHeader(ProjectorControl.DESTINATION_VALUE, ProjectorControl.NUM_CMD_BYTES, use_seq, use_len, use_checksum)
		self.phy = phy
		
	def CMD_GetMem( self, addr ):
		cmd = Command(0x0100, self.tx_header)
		cmd.put_int(4, addr)
		response = cmd.read(self.phy, 4)
		if not utils.check_response_and_print_error(response, False, "MEM_RW32"):
			return False
		data = response.get_int(4)

		return data

	def CMD_SetMem( self, addr, value ):
		cmd = Command(0x0100, self.tx_header)
		cmd.put_int(4, addr)
		cmd.put_int(4, value)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "MEM_RW32"):
			return False

		return True

	#Function parsing failed
	def CMD_GetMem32Array( ):
		return False

	#Function parsing failed
	def CMD_SetMem32Array( ):
		return False

	#Function parsing failed
	def CMD_GetMem16Array( ):
		return False

	#Function parsing failed
	def CMD_SetMem16Array( ):
		return False

	#Function parsing failed
	def CMD_GetMem08Array( ):
		return False

	#Function parsing failed
	def CMD_SetMem08Array( ):
		return False

	#Function parsing failed
	def CMD_Mem32ArrayCompare( ):
		return False

	#Function parsing failed
	def CMD_Mem16ArrayCompare( ):
		return False

	#Function parsing failed
	def CMD_Mem08ArrayCompare( ):
		return False

	#Function parsing failed
	def CMD_GetMemPoolInfo( ):
		return False

	def CMD_MemDump( self, addr, count ):
		cmd = Command(0x0108, self.tx_header)
		cmd.put_int(4, addr)
		cmd.put_int(2, count)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "MEM_DUMP"):
			return False

		return True

	def cmdMem_Bist_wr( self, bist_parms_TestEndAddress, bist_parms_TestStartAddress, bist_parms_TestType, bist_parms_BistType, bist_parms_HWBistType ):
		cmd = Command(0x010A, self.tx_header)
		cmd.put_int(4, bist_parms_TestEndAddress)
		cmd.put_int(4, bist_parms_TestStartAddress)
		cmd.put_int(1, bist_parms_TestType)
		cmd.put_int(1, bist_parms_BistType)
		cmd.put_int(1, bist_parms_HWBistType)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "MEM_BIST"):
			return False

		return True

	def cmdApp_Power_wr( self ):
		cmd = Command(0x0200, self.tx_header)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_POWERUP"):
			return False

		return True

	def CMD_PrintAllTaskInfo( self ):
		cmd = Command(0x0201, self.tx_header)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_SHOWTASKINFO"):
			return False

		return True

	def CMD_GetDebugMsgMask( self ):
		cmd = Command(0x0202, self.tx_header)
		response = cmd.read(self.phy, 8)
		if not utils.check_response_and_print_error(response, False, "APP_DEBUGLEVEL"):
			return False
		debug_mask = response.get_int(4)
		alloc = response.get_int(2)
		used = response.get_int(2)

		return debug_mask, alloc, used

	def CMD_SetDebugMsgMask( self, debug_mask ):
		cmd = Command(0x0202, self.tx_header)
		cmd.put_int(4, debug_mask)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_DEBUGLEVEL"):
			return False

		return True

	def cmdApp_Resrce_rd( self ):
		cmd = Command(0x0203, self.tx_header)
		response = cmd.read(self.phy, 12)
		if not utils.check_response_and_print_error(response, False, "APP_RESOURCE"):
			return False
		highCount_Tasks = response.get_int(1)
		highCount_Evts = response.get_int(1)
		highCount_GrpEvts = response.get_int(1)
		highCount_Mbxs = response.get_int(1)
		highCount_MemPools = response.get_int(1)
		highCount_Sems = response.get_int(1)
		currCount_Tasks = response.get_int(1)
		currCount_Evts = response.get_int(1)
		currCount_GrpEvts = response.get_int(1)
		currCount_Mbxs = response.get_int(1)
		currCount_MemPools = response.get_int(1)
		currCount_Sems = response.get_int(1)

		return highCount_Tasks, highCount_Evts, highCount_GrpEvts, highCount_Mbxs, highCount_MemPools, highCount_Sems, currCount_Tasks, currCount_Evts, currCount_GrpEvts, currCount_Mbxs, currCount_MemPools, currCount_Sems

	def cmdApp_GUINav_rd( self, rep_key ):
		cmd = Command(0x0204, self.tx_header)
		cmd.put_int(1, rep_key)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_GUINAVIGATE"):
			return False

		return True

	#Function parsing failed
	def CMD_GetVersions( ):
		return False

	def CMD_GetTaskStatus( self, index ):
		cmd = Command(0x0206, self.tx_header)
		cmd.put_int(1, index)
		response = cmd.read(self.phy, 11)
		if not utils.check_response_and_print_error(response, False, "APP_GETTASKINFO"):
			return False
		info_taskID = response.get_int(4)
		info_priority = response.get_int(1)
		info_stackSize = response.get_int(2)
		info_stackUnused = response.get_int(2)
		info_stackUsed = response.get_int(2)

		return info_taskID, info_priority, info_stackSize, info_stackUnused, info_stackUsed

	def cmdApp_State_rd( self ):
		cmd = Command(0x0207, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "APP_APP_STATE"):
			return False
		PowerState = response.get_int(1)

		return PowerState

	def cmdApp_Prior_wr( self, index, priority ):
		cmd = Command(0x0208, self.tx_header)
		cmd.put_int(1, index)
		cmd.put_int(1, priority)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_SETPRIORITY"):
			return False

		return True

	def cmdApp_Susp_wr( self, index, tState ):
		cmd = Command(0x0209, self.tx_header)
		cmd.put_int(1, index)
		cmd.put_int(1, tState)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_SUSP_RESUME"):
			return False

		return True

	#Function parsing failed
	def cmdApp_I2CPass_rd( ):
		return False

	#Function parsing failed
	def cmdApp_I2CPass_wr( ):
		return False

	def cmdApp_EDID_wr( self, eeAddr ):
		cmd = Command(0x020B, self.tx_header)
		cmd.put_int(2, eeAddr)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_EDID_WRITE"):
			return False

		return True

	def cmdApp_EDID_rd( self, eeAddr, EdidBlock ):
		cmd = Command(0x020C, self.tx_header)
		cmd.put_int(2, eeAddr)
		cmd.put_int(2, EdidBlock)
		response = cmd.read(self.phy, 128)
		if not utils.check_response_and_print_error(response, False, "APP_EDID_READ"):
			return False
		PT_DataArray = []
		PT_DataArray += response.get_arr(128)

		return PT_DataArray

	def cmdApp_EDID_comp( self, eeAddr, EdidBlock ):
		cmd = Command(0x020D, self.tx_header)
		cmd.put_int(2, eeAddr)
		cmd.put_int(2, EdidBlock)
		response = cmd.read(self.phy, 128)
		if not utils.check_response_and_print_error(response, False, "APP_EDID_COMP"):
			return False
		PT_DataArray = []
		PT_DataArray += response.get_arr(128)

		return PT_DataArray

	def cmdApp_TIDInfo_rd( self, taskID ):
		cmd = Command(0x020E, self.tx_header)
		cmd.put_int(4, taskID)
		response = cmd.read(self.phy, 8)
		if not utils.check_response_and_print_error(response, False, "APP_TID_INFO"):
			return False
		priority = response.get_int(4)
		unuStack = response.get_int(4)

		return priority, unuStack

	def cmdApp_TIDPrio_wr( self, taskID, priority ):
		cmd = Command(0x020F, self.tx_header)
		cmd.put_int(4, taskID)
		cmd.put_int(4, priority)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_TID_PRIORITY"):
			return False

		return True

	def cmdApp_TIDSusp_wr( self, taskID, tState ):
		cmd = Command(0x0210, self.tx_header)
		cmd.put_int(4, taskID)
		cmd.put_int(1, tState)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_TID_SUSP"):
			return False

		return True

	def cmdApp_ERestore_wr( self ):
		cmd = Command(0x0211, self.tx_header)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_EE_RESTORE"):
			return False

		return True

	def cmdApp_IntStack_rd( self ):
		cmd = Command(0x0212, self.tx_header)
		response = cmd.read(self.phy, 12)
		if not utils.check_response_and_print_error(response, False, "APP_INTSTACK"):
			return False
		ssize = response.get_int(4)
		sused = response.get_int(4)
		sfree = response.get_int(4)

		return ssize, sused, sfree

	def cmdApp_CIDebug_wr( self ):
		cmd = Command(0x0213, self.tx_header)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_DDCCI_DEBUG"):
			return False

		return True

	def cmdApp_GUIUpDt_rd( self ):
		cmd = Command(0x0214, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "APP_GUIUPDATEMODE"):
			return False
		updateMode = response.get_int(1)

		return updateMode

	def cmdApp_GUIUpDt_wr( self, updateMode ):
		cmd = Command(0x0214, self.tx_header)
		cmd.put_int(1, updateMode)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_GUIUPDATEMODE"):
			return False

		return True

	def cmdApp_GUIUpWin_rd( self ):
		cmd = Command(0x0215, self.tx_header)
		response = cmd.read(self.phy, 4)
		if not utils.check_response_and_print_error(response, False, "APP_GUIUPDTWIN"):
			return False
		updateTime = response.get_int(4)

		return updateTime

	def cmdAppGUItime_rd( self ):
		cmd = Command(0x0216, self.tx_header)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "APP_GUIUPDATETIME"):
			return False
		minUpdateTime = response.get_int(2)

		return minUpdateTime

	def cmdAppGUItime_wr( self, minUpdateTime ):
		cmd = Command(0x0216, self.tx_header)
		cmd.put_int(2, minUpdateTime)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_GUIUPDATETIME"):
			return False

		return True

	def cmdAppCCcmd_wr( self, byte1, byte2 ):
		cmd = Command(0x0217, self.tx_header)
		cmd.put_int(1, byte1)
		cmd.put_int(1, byte2)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_SENDCCCMD"):
			return False

		return True

	def cmdAppCCChannel_rd( self ):
		cmd = Command(0x0218, self.tx_header)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "APP_CC_MODE"):
			return False
		isEnable = response.get_int(1)
		cc_channel = response.get_int(1)

		return isEnable, cc_channel

	def cmdAppCCChannel_wr( self, isEnable, cc_channel ):
		cmd = Command(0x0218, self.tx_header)
		cmd.put_int(1, isEnable)
		cmd.put_int(1, cc_channel)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_CC_MODE"):
			return False

		return True

	def cmdAppMsgService_wr( self, type ):
		cmd = Command(0x0219, self.tx_header)
		cmd.put_int(1, type)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_MSGSERVICE"):
			return False

		return True

	def cmdAppMsgService_rd( self ):
		cmd = Command(0x0219, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "APP_MSGSERVICE"):
			return False
		supported = response.get_int(1)

		return supported

	def cmdAppMessage_wr( self, uCode ):
		cmd = Command(0x0236, self.tx_header)
		cmd.put_int(2, uCode)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_MSGUNICODE"):
			return False

		return True

	def cmdAppCCParOvEn_wr( self, isEnable ):
		cmd = Command(0x0224, self.tx_header)
		cmd.put_int(1, isEnable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_CC_PARITY"):
			return False

		return True

	def cmdAppCCParOvEn_rd( self ):
		cmd = Command(0x0224, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "APP_CC_PARITY"):
			return False
		isEnable = response.get_int(1)

		return isEnable

	def cmdAppCCDbgEn_wr( self, isEnable ):
		cmd = Command(0x0225, self.tx_header)
		cmd.put_int(1, isEnable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_CC_DEBUGMODE"):
			return False

		return True

	def cmdAppCCDbgEn_rd( self ):
		cmd = Command(0x0225, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "APP_CC_DEBUGMODE"):
			return False
		isEnable = response.get_int(1)

		return isEnable

	def cmdApp_CalADC_wr( self ):
		cmd = Command(0x0235, self.tx_header)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_CALIBRATE_ADC"):
			return False

		return True

	def cmdHostAppNetIPAdd_wr( self, IPAddress ):
		cmd = Command(0x0240, self.tx_header)
		cmd.put_int(4, IPAddress)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_NETWORKIPADD"):
			return False

		return True

	def cmdHostAppControl_wr( self, index ):
		cmd = Command(0x0241, self.tx_header)
		cmd.put_int(1, index)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_HOSTCONTROL"):
			return False

		return True

	def cmdHostAppControl_rd( self, index ):
		cmd = Command(0x0241, self.tx_header)
		cmd.put_int(1, index)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "APP_HOSTCONTROL"):
			return False
		value = response.get_int(1)

		return value

	def cmdHostSrcControl_wr( self, source ):
		cmd = Command(0x0242, self.tx_header)
		cmd.put_int(1, source)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_HOSTSRCCONTROL"):
			return False

		return True

	def cmdHostSrcControl_rd( self, index ):
		cmd = Command(0x0242, self.tx_header)
		cmd.put_int(1, index)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "APP_HOSTSRCCONTROL"):
			return False
		source = response.get_int(2)

		return source

	def cmdFeatureDisable_wr( self ):
		cmd = Command(0x0245, self.tx_header)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_FEATUREDISABLE"):
			return False

		return True

	def CMD_EnableUSBDebugMsg( self, flag ):
		cmd = Command(0x0246, self.tx_header)
		cmd.put_int(1, flag)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_ENABLEUSBMSG"):
			return False

		return True

	#Function parsing failed
	def CMD_GetLibSignature( ):
		return False

	def CMD_PrintAllLibSignatures( self ):
		cmd = Command(0x0248, self.tx_header)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_SHOWSIGNATURE"):
			return False

		return True

	def CMD_ToggleUsbMode( self ):
		cmd = Command(0x0249, self.tx_header)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_TOGGLEUSBMODE"):
			return False

		return True

	def CMD_SendUsbMouseCode( self, MouseClick, MouseX, MouseY ):
		cmd = Command(0x0250, self.tx_header)
		cmd.put_int(1, MouseClick)
		cmd.put_int(1, MouseX)
		cmd.put_int(1, MouseY)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_USBMOUSEDATA"):
			return False

		return True

	def CMD_SendUsbKeyboardCode( self, KeyCode ):
		cmd = Command(0x0251, self.tx_header)
		cmd.put_int(1, KeyCode)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_USBKBDATA"):
			return False

		return True

	def cmdCW_Start_wr( self, Start ):
		cmd = Command(0x0300, self.tx_header)
		cmd.put_int(1, Start)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "CW_START"):
			return False

		return True

	def cmdCW_Start_rd( self ):
		cmd = Command(0x0300, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "CW_START"):
			return False
		Started = response.get_int(1)

		return Started

	def cmdCW_Coast_wr( self, IsCwCoast ):
		cmd = Command(0x0301, self.tx_header)
		cmd.put_int(1, IsCwCoast)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "CW_COAST"):
			return False
		IsCwCoast = response.get_int(1)

		return IsCwCoast

	def cmdCW_Coast_rd( self ):
		cmd = Command(0x0301, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "CW_COAST"):
			return False
		Coasted = response.get_int(1)

		return Coasted

	def cmdCW_Debug_wr( self, cw_debug_mode ):
		cmd = Command(0x0303, self.tx_header)
		cmd.put_int(1, cw_debug_mode)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "CW_DEBUG"):
			return False

		return True

	def cmdCW_Debug_rd( self ):
		cmd = Command(0x0303, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "CW_DEBUG"):
			return False
		DebugMode = response.get_int(1)

		return DebugMode

	def cmdCW_OpStat_rd( self ):
		cmd = Command(0x0304, self.tx_header)
		response = cmd.read(self.phy, 3)
		if not utils.check_response_and_print_error(response, False, "CW_OPSTAT"):
			return False
		CW_GetSpinning = response.get_int(1)
		CW_IsCoastEnabled = response.get_int(1)
		CW_GetDebugMode = response.get_int(1)

		return CW_GetSpinning, CW_IsCoastEnabled, CW_GetDebugMode

	def cmdCW_IndexDelay_rd( self, Wheel ):
		cmd = Command(0x0305, self.tx_header)
		cmd.put_int(1, Wheel)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "CW_INDEXDELAY"):
			return False
		IndexDelay = response.get_int(2)

		return IndexDelay

	def cmdCW_IndexDelay_wr( self, Wheel, IndexDelay ):
		cmd = Command(0x0305, self.tx_header)
		cmd.put_int(1, Wheel)
		cmd.put_int(2, IndexDelay)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "CW_INDEXDELAY"):
			return False

		return True

	def cmdCW_ExpVSync_rd( self ):
		cmd = Command(0x0306, self.tx_header)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "CW_EXPVSYNC"):
			return False
		expVSync = response.get_int(2)

		return expVSync

	def cmdCW_ExpVSync_wr( self, expected_vysnc ):
		cmd = Command(0x0306, self.tx_header)
		cmd.put_int(2, expected_vysnc)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "CW_EXPVSYNC"):
			return False

		return True

	def cmdCW_IndexParm_rd( self ):
		cmd = Command(0x0307, self.tx_header)
		response = cmd.read(self.phy, 8)
		if not utils.check_response_and_print_error(response, False, "CW_INDEXPARM"):
			return False
		ixp32 = response.get_int(4)
		u32 = response.get_int(4)

		return ixp32, u32

	def cmdANR_Init_wr( self ):
		cmd = Command(0x0400, self.tx_header)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "ANR_INIT"):
			return False

		return True

	def cmdANR_State_rd( self, isSpatial ):
		cmd = Command(0x0401, self.tx_header)
		cmd.put_int(1, isSpatial)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "ANR_STATE"):
			return False
		isEnable = response.get_int(1)
		strength = response.get_int(1)

		return isEnable, strength

	def cmdANR_State_wr( self, isSpatial, isEnable, strength ):
		cmd = Command(0x0401, self.tx_header)
		cmd.put_int(1, isSpatial)
		cmd.put_int(1, isEnable)
		cmd.put_int(1, strength)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "ANR_STATE"):
			return False

		return True

	def cmdImgEnable_rd( self, Algo ):
		cmd = Command(0x0500, self.tx_header)
		cmd.put_int(1, Algo)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "IMG_ENABLE"):
			return False
		State = response.get_int(1)

		return State

	def cmdImgEnable_wr( self, Algo, State ):
		cmd = Command(0x0500, self.tx_header)
		cmd.put_int(1, Algo)
		cmd.put_int(1, State)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_ENABLE"):
			return False

		return True

	def cmdImgBright_rd( self ):
		cmd = Command(0x0501, self.tx_header)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "IMG_BRIGHTNESS"):
			return False
		bright = response.get_int(2)

		return bright

	def cmdImgBright_wr( self, bright ):
		cmd = Command(0x0501, self.tx_header)
		cmd.put_int(2, bright)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_BRIGHTNESS"):
			return False

		return True

	def cmdImgEnableall_rd( self ):
		cmd = Command(0x0502, self.tx_header)
		response = cmd.read(self.phy, 7)
		if not utils.check_response_and_print_error(response, False, "IMG_ENABLEALL"):
			return False
		chi_en = response.get_int(1)
		cti_en = response.get_int(1)
		gam_en = response.get_int(1)
		cca_en = response.get_int(1)
		bc_en = response.get_int(1)
		stm_en = response.get_int(1)
		brs_en = response.get_int(1)

		return chi_en, cti_en, gam_en, cca_en, bc_en, stm_en, brs_en

	def cmdImgContrast_rd( self ):
		cmd = Command(0x0503, self.tx_header)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "IMG_CONTRAST"):
			return False
		Contrast = response.get_int(2)

		return Contrast

	def cmdImgContrast_wr( self, Contrast ):
		cmd = Command(0x0503, self.tx_header)
		cmd.put_int(2, Contrast)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_CONTRAST"):
			return False

		return True

	def cmdImgHue_rd( self ):
		cmd = Command(0x0504, self.tx_header)
		response = cmd.read(self.phy, 3)
		if not utils.check_response_and_print_error(response, False, "IMG_HUE_ADJUST"):
			return False
		Angle = response.get_int(1)
		Control = response.get_int(2)

		return Angle, Control

	def cmdImgHue_wr( self, Angle, Control ):
		cmd = Command(0x0504, self.tx_header)
		cmd.put_int(1, Angle)
		cmd.put_int(2, Control)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_HUE_ADJUST"):
			return False

		return True

	def cmdImgVSharp_rd( self ):
		cmd = Command(0x050B, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "IMG_VERT_SHARPNESS"):
			return False
		VerticalSharpness = response.get_int(1)

		return VerticalSharpness

	def cmdImgVSharp_wr( self, VerticalSharpness ):
		cmd = Command(0x050B, self.tx_header)
		cmd.put_int(1, VerticalSharpness)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_VERT_SHARPNESS"):
			return False

		return True

	def cmdImgHSharp_rd( self ):
		cmd = Command(0x050C, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "IMG_HORIZ_SHARPNESS"):
			return False
		horizontal_sharpness = response.get_int(1)

		return horizontal_sharpness

	def cmdImgHSharp_wr( self, horizontal_sharpness ):
		cmd = Command(0x050C, self.tx_header)
		cmd.put_int(1, horizontal_sharpness)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_HORIZ_SHARPNESS"):
			return False

		return True

	def cmdImgGammaLUT_rd( self ):
		cmd = Command(0x050D, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "IMG_GAMMALUT"):
			return False
		lut_num = response.get_int(1)

		return lut_num

	def cmdImgGammaLUT_wr( self, lut_num ):
		cmd = Command(0x050D, self.tx_header)
		cmd.put_int(1, lut_num)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_GAMMALUT"):
			return False

		return True

	def cmdImgWhPeak_rd( self ):
		cmd = Command(0x050E, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "IMG_WHITEPEAKING"):
			return False
		white_peaking_val = response.get_int(1)

		return white_peaking_val

	def cmdImgWhPeak_wr( self, white_peaking_val ):
		cmd = Command(0x050E, self.tx_header)
		cmd.put_int(1, white_peaking_val)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_WHITEPEAKING"):
			return False

		return True

	def cmdImgCCA_rd( self ):
		cmd = Command(0x050F, self.tx_header)
		response = cmd.read(self.phy, 96)
		if not utils.check_response_and_print_error(response, False, "IMG_CCA"):
			return False
		OrigCoords_r_x = response.get_int(2)
		OrigCoords_r_y = response.get_int(2)
		OrigCoords_r_l = response.get_int(2)
		OrigCoords_g_x = response.get_int(2)
		OrigCoords_g_y = response.get_int(2)
		OrigCoords_g_l = response.get_int(2)
		OrigCoords_b_x = response.get_int(2)
		OrigCoords_b_y = response.get_int(2)
		OrigCoords_b_l = response.get_int(2)
		OrigCoords_w_x = response.get_int(2)
		OrigCoords_w_y = response.get_int(2)
		OrigCoords_w_l = response.get_int(2)
		OrigCoords_c1_x = response.get_int(2)
		OrigCoords_c1_y = response.get_int(2)
		OrigCoords_c1_l = response.get_int(2)
		OrigCoords_c2_x = response.get_int(2)
		OrigCoords_c2_y = response.get_int(2)
		OrigCoords_c2_l = response.get_int(2)
		OrigCoords_A_x = response.get_int(2)
		OrigCoords_A_y = response.get_int(2)
		OrigCoords_A_l = response.get_int(2)
		OrigCoords_B_x = response.get_int(2)
		OrigCoords_B_y = response.get_int(2)
		OrigCoords_B_l = response.get_int(2)
		OrigCoords_C_x = response.get_int(2)
		OrigCoords_C_y = response.get_int(2)
		OrigCoords_C_l = response.get_int(2)
		TargetCoords_r_x = response.get_int(2)
		TargetCoords_r_y = response.get_int(2)
		TargetCoords_r_g = response.get_int(2)
		TargetCoords_g_x = response.get_int(2)
		TargetCoords_g_y = response.get_int(2)
		TargetCoords_g_g = response.get_int(2)
		TargetCoords_b_x = response.get_int(2)
		TargetCoords_b_y = response.get_int(2)
		TargetCoords_b_g = response.get_int(2)
		TargetCoords_c_x = response.get_int(2)
		TargetCoords_c_y = response.get_int(2)
		TargetCoords_c_g = response.get_int(2)
		TargetCoords_m_x = response.get_int(2)
		TargetCoords_m_y = response.get_int(2)
		TargetCoords_m_g = response.get_int(2)
		TargetCoords_y_x = response.get_int(2)
		TargetCoords_y_y = response.get_int(2)
		TargetCoords_y_g = response.get_int(2)
		TargetCoords_w_x = response.get_int(2)
		TargetCoords_w_y = response.get_int(2)
		TargetCoords_w_g = response.get_int(2)

		return OrigCoords_r_x, OrigCoords_r_y, OrigCoords_r_l, OrigCoords_g_x, OrigCoords_g_y, OrigCoords_g_l, OrigCoords_b_x, OrigCoords_b_y, OrigCoords_b_l, OrigCoords_w_x, OrigCoords_w_y, OrigCoords_w_l, OrigCoords_c1_x, OrigCoords_c1_y, OrigCoords_c1_l, OrigCoords_c2_x, OrigCoords_c2_y, OrigCoords_c2_l, OrigCoords_A_x, OrigCoords_A_y, OrigCoords_A_l, OrigCoords_B_x, OrigCoords_B_y, OrigCoords_B_l, OrigCoords_C_x, OrigCoords_C_y, OrigCoords_C_l, TargetCoords_r_x, TargetCoords_r_y, TargetCoords_r_g, TargetCoords_g_x, TargetCoords_g_y, TargetCoords_g_g, TargetCoords_b_x, TargetCoords_b_y, TargetCoords_b_g, TargetCoords_c_x, TargetCoords_c_y, TargetCoords_c_g, TargetCoords_m_x, TargetCoords_m_y, TargetCoords_m_g, TargetCoords_y_x, TargetCoords_y_y, TargetCoords_y_g, TargetCoords_w_x, TargetCoords_w_y, TargetCoords_w_g

	def cmdImgCCA_wr( self, OrigCoords_r_x, OrigCoords_r_y, OrigCoords_r_l, OrigCoords_g_x, OrigCoords_g_y, OrigCoords_g_l, OrigCoords_b_x, OrigCoords_b_y, OrigCoords_b_l, OrigCoords_w_x, OrigCoords_w_y, OrigCoords_w_l, OrigCoords_c1_x, OrigCoords_c1_y, OrigCoords_c1_l, OrigCoords_c2_x, OrigCoords_c2_y, OrigCoords_c2_l, OrigCoords_A_x, OrigCoords_A_y, OrigCoords_A_l, OrigCoords_B_x, OrigCoords_B_y, OrigCoords_B_l, OrigCoords_C_x, OrigCoords_C_y, OrigCoords_C_l, TargetCoords_r_x, TargetCoords_r_y, TargetCoords_r_g, TargetCoords_g_x, TargetCoords_g_y, TargetCoords_g_g, TargetCoords_b_x, TargetCoords_b_y, TargetCoords_b_g, TargetCoords_c_x, TargetCoords_c_y, TargetCoords_c_g, TargetCoords_m_x, TargetCoords_m_y, TargetCoords_m_g, TargetCoords_y_x, TargetCoords_y_y, TargetCoords_y_g, TargetCoords_w_x, TargetCoords_w_y, TargetCoords_w_g ):
		cmd = Command(0x050F, self.tx_header)
		cmd.put_int(2, OrigCoords_r_x)
		cmd.put_int(2, OrigCoords_r_y)
		cmd.put_int(2, OrigCoords_r_l)
		cmd.put_int(2, OrigCoords_g_x)
		cmd.put_int(2, OrigCoords_g_y)
		cmd.put_int(2, OrigCoords_g_l)
		cmd.put_int(2, OrigCoords_b_x)
		cmd.put_int(2, OrigCoords_b_y)
		cmd.put_int(2, OrigCoords_b_l)
		cmd.put_int(2, OrigCoords_w_x)
		cmd.put_int(2, OrigCoords_w_y)
		cmd.put_int(2, OrigCoords_w_l)
		cmd.put_int(2, OrigCoords_c1_x)
		cmd.put_int(2, OrigCoords_c1_y)
		cmd.put_int(2, OrigCoords_c1_l)
		cmd.put_int(2, OrigCoords_c2_x)
		cmd.put_int(2, OrigCoords_c2_y)
		cmd.put_int(2, OrigCoords_c2_l)
		cmd.put_int(2, OrigCoords_A_x)
		cmd.put_int(2, OrigCoords_A_y)
		cmd.put_int(2, OrigCoords_A_l)
		cmd.put_int(2, OrigCoords_B_x)
		cmd.put_int(2, OrigCoords_B_y)
		cmd.put_int(2, OrigCoords_B_l)
		cmd.put_int(2, OrigCoords_C_x)
		cmd.put_int(2, OrigCoords_C_y)
		cmd.put_int(2, OrigCoords_C_l)
		cmd.put_int(2, TargetCoords_r_x)
		cmd.put_int(2, TargetCoords_r_y)
		cmd.put_int(2, TargetCoords_r_g)
		cmd.put_int(2, TargetCoords_g_x)
		cmd.put_int(2, TargetCoords_g_y)
		cmd.put_int(2, TargetCoords_g_g)
		cmd.put_int(2, TargetCoords_b_x)
		cmd.put_int(2, TargetCoords_b_y)
		cmd.put_int(2, TargetCoords_b_g)
		cmd.put_int(2, TargetCoords_c_x)
		cmd.put_int(2, TargetCoords_c_y)
		cmd.put_int(2, TargetCoords_c_g)
		cmd.put_int(2, TargetCoords_m_x)
		cmd.put_int(2, TargetCoords_m_y)
		cmd.put_int(2, TargetCoords_m_g)
		cmd.put_int(2, TargetCoords_y_x)
		cmd.put_int(2, TargetCoords_y_y)
		cmd.put_int(2, TargetCoords_y_g)
		cmd.put_int(2, TargetCoords_w_x)
		cmd.put_int(2, TargetCoords_w_y)
		cmd.put_int(2, TargetCoords_w_g)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_CCA"):
			return False

		return True

	def cmdImgHSG_rd( self ):
		cmd = Command(0x0510, self.tx_header)
		response = cmd.read(self.phy, 42)
		if not utils.check_response_and_print_error(response, False, "IMG_HSGVAL"):
			return False
		hsg_Red_Gain = response.get_int(2)
		hsg_Red_Saturation = response.get_int(2)
		hsg_Red_Hue = response.get_int(2)
		hsg_Green_Gain = response.get_int(2)
		hsg_Green_Saturation = response.get_int(2)
		hsg_Green_Hue = response.get_int(2)
		hsg_Blue_Gain = response.get_int(2)
		hsg_Blue_Saturation = response.get_int(2)
		hsg_Blue_Hue = response.get_int(2)
		hsg_Cyan_Gain = response.get_int(2)
		hsg_Cyan_Saturation = response.get_int(2)
		hsg_Cyan_Hue = response.get_int(2)
		hsg_Magenta_Gain = response.get_int(2)
		hsg_Magenta_Saturation = response.get_int(2)
		hsg_Magenta_Hue = response.get_int(2)
		hsg_Yellow_Gain = response.get_int(2)
		hsg_Yellow_Saturation = response.get_int(2)
		hsg_Yellow_Hue = response.get_int(2)
		hsg_White_RedGain = response.get_int(2)
		hsg_White_GreenGain = response.get_int(2)
		hsg_White_BlueGain = response.get_int(2)

		return hsg_Red_Gain, hsg_Red_Saturation, hsg_Red_Hue, hsg_Green_Gain, hsg_Green_Saturation, hsg_Green_Hue, hsg_Blue_Gain, hsg_Blue_Saturation, hsg_Blue_Hue, hsg_Cyan_Gain, hsg_Cyan_Saturation, hsg_Cyan_Hue, hsg_Magenta_Gain, hsg_Magenta_Saturation, hsg_Magenta_Hue, hsg_Yellow_Gain, hsg_Yellow_Saturation, hsg_Yellow_Hue, hsg_White_RedGain, hsg_White_GreenGain, hsg_White_BlueGain

	def cmdImgHSG_wr( self, hsg_Red_Gain, hsg_Red_Saturation, hsg_Red_Hue, hsg_Green_Gain, hsg_Green_Saturation, hsg_Green_Hue, hsg_Blue_Gain, hsg_Blue_Saturation, hsg_Blue_Hue, hsg_Cyan_Gain, hsg_Cyan_Saturation, hsg_Cyan_Hue, hsg_Magenta_Gain, hsg_Magenta_Saturation, hsg_Magenta_Hue, hsg_Yellow_Gain, hsg_Yellow_Saturation, hsg_Yellow_Hue, hsg_White_RedGain, hsg_White_GreenGain, hsg_White_BlueGain ):
		cmd = Command(0x0510, self.tx_header)
		cmd.put_int(2, hsg_Red_Gain)
		cmd.put_int(2, hsg_Red_Saturation)
		cmd.put_int(2, hsg_Red_Hue)
		cmd.put_int(2, hsg_Green_Gain)
		cmd.put_int(2, hsg_Green_Saturation)
		cmd.put_int(2, hsg_Green_Hue)
		cmd.put_int(2, hsg_Blue_Gain)
		cmd.put_int(2, hsg_Blue_Saturation)
		cmd.put_int(2, hsg_Blue_Hue)
		cmd.put_int(2, hsg_Cyan_Gain)
		cmd.put_int(2, hsg_Cyan_Saturation)
		cmd.put_int(2, hsg_Cyan_Hue)
		cmd.put_int(2, hsg_Magenta_Gain)
		cmd.put_int(2, hsg_Magenta_Saturation)
		cmd.put_int(2, hsg_Magenta_Hue)
		cmd.put_int(2, hsg_Yellow_Gain)
		cmd.put_int(2, hsg_Yellow_Saturation)
		cmd.put_int(2, hsg_Yellow_Hue)
		cmd.put_int(2, hsg_White_RedGain)
		cmd.put_int(2, hsg_White_GreenGain)
		cmd.put_int(2, hsg_White_BlueGain)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_HSGVAL"):
			return False

		return True

	#Function parsing failed
	def cmdImgCPHW_wr( ):
		return False

	#Function parsing failed
	def cmdImgCPHW_rd( ):
		return False

	#Function parsing failed
	def cmdImgCPEEP_wr( ):
		return False

	#Function parsing failed
	def cmdImgCPEEP_rd( ):
		return False

	def cmdImgCP_wr( self, profile ):
		cmd = Command(0x0513, self.tx_header)
		cmd.put_int(1, profile)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_COLPROF_SET"):
			return False

		return True

	def cmdImgCWRat_wr( self, def_table ):
		cmd = Command(0x0514, self.tx_header)
		cmd.put_int(1, def_table)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_CWRATDEF_SET"):
			return False

		return True

	def cmdImgRGBGain_rd( self, Chan ):
		cmd = Command(0x0515, self.tx_header)
		cmd.put_int(1, Chan)
		response = cmd.read(self.phy, 6)
		if not utils.check_response_and_print_error(response, False, "IMG_RGB_GAIN_ADJUST"):
			return False
		red_gain = response.get_int(2)
		grn_gain = response.get_int(2)
		blu_gain = response.get_int(2)

		return red_gain, grn_gain, blu_gain

	def cmdImgRGBGain_wr( self, Chan, red_gain, grn_gain, blu_gain ):
		cmd = Command(0x0515, self.tx_header)
		cmd.put_int(1, Chan)
		cmd.put_int(2, red_gain)
		cmd.put_int(2, grn_gain)
		cmd.put_int(2, blu_gain)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_RGB_GAIN_ADJUST"):
			return False

		return True

	def cmdImgGamCurve_rd( self ):
		cmd = Command(0x0516, self.tx_header)
		response = cmd.read(self.phy, 3)
		if not utils.check_response_and_print_error(response, False, "IMG_GAM_CURVESHIFTS"):
			return False
		red_shift = response.get_int(1)
		grn_shift = response.get_int(1)
		blu_shift = response.get_int(1)

		return red_shift, grn_shift, blu_shift

	def cmdImgGamCurve_wr( self, red_shift, grn_shift, blu_shift ):
		cmd = Command(0x0516, self.tx_header)
		cmd.put_int(1, red_shift)
		cmd.put_int(1, grn_shift)
		cmd.put_int(1, blu_shift)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_GAM_CURVESHIFTS"):
			return False

		return True

	def cmdImgCTISet_rd( self ):
		cmd = Command(0x0517, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "IMG_CTI_SETUP"):
			return False
		source_type = response.get_int(1)

		return source_type

	def cmdImgCTISet_wr( self, source_type ):
		cmd = Command(0x0517, self.tx_header)
		cmd.put_int(1, source_type)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_CTI_SETUP"):
			return False

		return True

	def cmdImgCTIGain_rd( self ):
		cmd = Command(0x0518, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "IMG_CTI_GAIN"):
			return False
		gain = response.get_int(1)

		return gain

	def cmdImgCTIGain_wr( self, gain_val ):
		cmd = Command(0x0518, self.tx_header)
		cmd.put_int(1, gain_val)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_CTI_GAIN"):
			return False

		return True

	def cmdImgRGBOff_rd( self ):
		cmd = Command(0x0519, self.tx_header)
		response = cmd.read(self.phy, 6)
		if not utils.check_response_and_print_error(response, False, "IMG_RGB_OFFSET_ADJ"):
			return False
		red_offset = response.get_int(2)
		grn_offset = response.get_int(2)
		blu_offset = response.get_int(2)

		return red_offset, grn_offset, blu_offset

	def cmdImgRGBOff_wr( self, red_offset, grn_offset, blu_offset ):
		cmd = Command(0x0519, self.tx_header)
		cmd.put_int(2, red_offset)
		cmd.put_int(2, grn_offset)
		cmd.put_int(2, blu_offset)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_RGB_OFFSET_ADJ"):
			return False

		return True

	def cmdImgExitCal_wr( self ):
		cmd = Command(0x0522, self.tx_header)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_EXIT_CALIBRATE"):
			return False

		return True

	def cmdImgSetPleaseBit_wr( self, w0, w1, w2 ):
		cmd = Command(0x0523, self.tx_header)
		cmd.put_int(4, w0)
		cmd.put_int(4, w1)
		cmd.put_int(4, w2)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_SET_PLEASE_BIT"):
			return False

		return True

	def cmdImgiHSG_rd( self ):
		cmd = Command(0x0560, self.tx_header)
		response = cmd.read(self.phy, 42)
		if not utils.check_response_and_print_error(response, False, "IMG_iHSGVAL"):
			return False
		hsg_Red_Gain = response.get_int(2)
		hsg_Red_Saturation = response.get_int(2)
		hsg_Red_Hue = response.get_int(2)
		hsg_Green_Gain = response.get_int(2)
		hsg_Green_Saturation = response.get_int(2)
		hsg_Green_Hue = response.get_int(2)
		hsg_Blue_Gain = response.get_int(2)
		hsg_Blue_Saturation = response.get_int(2)
		hsg_Blue_Hue = response.get_int(2)
		hsg_Cyan_Gain = response.get_int(2)
		hsg_Cyan_Saturation = response.get_int(2)
		hsg_Cyan_Hue = response.get_int(2)
		hsg_Magenta_Gain = response.get_int(2)
		hsg_Magenta_Saturation = response.get_int(2)
		hsg_Magenta_Hue = response.get_int(2)
		hsg_Yellow_Gain = response.get_int(2)
		hsg_Yellow_Saturation = response.get_int(2)
		hsg_Yellow_Hue = response.get_int(2)
		hsg_White_RedGain = response.get_int(2)
		hsg_White_GreenGain = response.get_int(2)
		hsg_White_BlueGain = response.get_int(2)

		return hsg_Red_Gain, hsg_Red_Saturation, hsg_Red_Hue, hsg_Green_Gain, hsg_Green_Saturation, hsg_Green_Hue, hsg_Blue_Gain, hsg_Blue_Saturation, hsg_Blue_Hue, hsg_Cyan_Gain, hsg_Cyan_Saturation, hsg_Cyan_Hue, hsg_Magenta_Gain, hsg_Magenta_Saturation, hsg_Magenta_Hue, hsg_Yellow_Gain, hsg_Yellow_Saturation, hsg_Yellow_Hue, hsg_White_RedGain, hsg_White_GreenGain, hsg_White_BlueGain

	def cmdImgBRSDisableDC_wr( self, disable ):
		cmd = Command(0x05A0, self.tx_header)
		cmd.put_int(1, disable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_BRS_DC_DIS"):
			return False

		return True

	def cmdImgBRSDisableDC_rd( self ):
		cmd = Command(0x05A0, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "IMG_BRS_DC_DIS"):
			return False
		disable = response.get_int(1)

		return disable

	def cmdImgBRSDiagCfg_wr( self, sc_end, gain_start, gain_end ):
		cmd = Command(0x05A1, self.tx_header)
		cmd.put_int(2, sc_end)
		cmd.put_int(2, gain_start)
		cmd.put_int(2, gain_end)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_BRS_DIAG_CFG"):
			return False

		return True

	def cmdImgBRSDiagCfg_rd( self ):
		cmd = Command(0x05A1, self.tx_header)
		response = cmd.read(self.phy, 6)
		if not utils.check_response_and_print_error(response, False, "IMG_BRS_DIAG_CFG"):
			return False
		sc_end = response.get_int(2)
		gain_start = response.get_int(2)
		gain_end = response.get_int(2)

		return sc_end, gain_start, gain_end

	def cmdImgBRSDiagEnable_wr( self, enable ):
		cmd = Command(0x05A2, self.tx_header)
		cmd.put_int(1, enable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_BRS_DIAG_EN"):
			return False

		return True

	def cmdImgBRSDiagEnable_rd( self ):
		cmd = Command(0x05A2, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "IMG_BRS_DIAG_EN"):
			return False
		enable = response.get_int(1)

		return enable

	def cmdImgBRSMaxGain_wr( self, gain, mode ):
		cmd = Command(0x05A3, self.tx_header)
		cmd.put_int(2, gain)
		cmd.put_int(1, mode)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_BRS_MAX_GAIN"):
			return False

		return True

	def cmdImgBRSMaxGain_rd( self ):
		cmd = Command(0x05A3, self.tx_header)
		response = cmd.read(self.phy, 3)
		if not utils.check_response_and_print_error(response, False, "IMG_BRS_MAX_GAIN"):
			return False
		gain = response.get_int(2)
		max_gain_mode = response.get_int(1)

		return gain, max_gain_mode

	def cmdImgBRSMaxDigGain_wr( self, gain, mode ):
		cmd = Command(0x05A4, self.tx_header)
		cmd.put_int(2, gain)
		cmd.put_int(1, mode)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_BRS_MAX_DIG_GAIN"):
			return False

		return True

	def cmdImgBRSMaxDigGain_rd( self ):
		cmd = Command(0x05A4, self.tx_header)
		response = cmd.read(self.phy, 3)
		if not utils.check_response_and_print_error(response, False, "IMG_BRS_MAX_DIG_GAIN"):
			return False
		gain = response.get_int(2)
		max_gain_mode = response.get_int(1)

		return gain, max_gain_mode

	def cmdImgBRSClipPct_wr( self, clip_pct, enable ):
		cmd = Command(0x05A5, self.tx_header)
		cmd.put_int(2, clip_pct)
		cmd.put_int(1, enable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_BRS_CLIP_PCT"):
			return False

		return True

	def cmdImgBRSClipPct_rd( self ):
		cmd = Command(0x05A5, self.tx_header)
		response = cmd.read(self.phy, 3)
		if not utils.check_response_and_print_error(response, False, "IMG_BRS_CLIP_PCT"):
			return False
		clip_pct = response.get_int(2)
		enable = response.get_int(1)

		return clip_pct, enable

	def cmdImgBRSSceneChgRate_wr( self, scene_change_rate ):
		cmd = Command(0x05A6, self.tx_header)
		cmd.put_int(1, scene_change_rate)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_SCENE_CHG_RATE"):
			return False

		return True

	def cmdImgBRSSceneChgRate_rd( self ):
		cmd = Command(0x05A6, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "IMG_SCENE_CHG_RATE"):
			return False
		scene_change_rate = response.get_int(1)

		return scene_change_rate

	def cmdImgBRSMinDC_wr( self, min_red_dc, min_grn_dc, min_blu_dc ):
		cmd = Command(0x05A7, self.tx_header)
		cmd.put_int(2, min_red_dc)
		cmd.put_int(2, min_grn_dc)
		cmd.put_int(2, min_blu_dc)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_BRS_MIN_DC"):
			return False

		return True

	def cmdImgBRSMinDC_rd( self ):
		cmd = Command(0x05A7, self.tx_header)
		response = cmd.read(self.phy, 6)
		if not utils.check_response_and_print_error(response, False, "IMG_BRS_MIN_DC"):
			return False
		min_red_dc = response.get_int(2)
		min_grn_dc = response.get_int(2)
		min_blu_dc = response.get_int(2)

		return min_red_dc, min_grn_dc, min_blu_dc

	def cmdImgBRSHistShift_wr( self, shift ):
		cmd = Command(0x05A8, self.tx_header)
		cmd.put_int(1, shift)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_BRS_LUMA_HIST_SHIFT"):
			return False

		return True

	def cmdImgBRSHistShift_rd( self ):
		cmd = Command(0x05A8, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "IMG_BRS_LUMA_HIST_SHIFT"):
			return False
		shift = response.get_int(1)

		return shift

	def cmdImgBRSHistRest_wr( self ):
		cmd = Command(0x05A9, self.tx_header)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_BRS_LUMA_HIST_REST"):
			return False

		return True

	def cmdImgBRSDynLumaShiftEnable_wr( self, enable ):
		cmd = Command(0x05AA, self.tx_header)
		cmd.put_int(1, enable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_BRS_SW_OVERRIDE"):
			return False

		return True

	def cmdImgBRSDynLumaShiftEnable_rd( self ):
		cmd = Command(0x05AA, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "IMG_BRS_SW_OVERRIDE"):
			return False
		enable = response.get_int(1)

		return enable

	def cmdImgBRSDynLumaShiftThr_wr( self, scene_change_thr ):
		cmd = Command(0x05AB, self.tx_header)
		cmd.put_int(4, scene_change_thr)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_BRS_SW_OVERRIDE_THR"):
			return False

		return True

	def cmdImgBRSDynLumaShiftThr_rd( self ):
		cmd = Command(0x05AB, self.tx_header)
		response = cmd.read(self.phy, 4)
		if not utils.check_response_and_print_error(response, False, "IMG_BRS_SW_OVERRIDE_THR"):
			return False
		scene_change_thr = response.get_int(4)

		return scene_change_thr

	def cmdImgBRSDynLumaShiftStatic_wr( self, stationary_luma_shift ):
		cmd = Command(0x05AC, self.tx_header)
		cmd.put_int(1, stationary_luma_shift)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_BRS_SW_OVERRIDE_LUMA_STATIC"):
			return False

		return True

	def cmdImgBRSDynLumaShiftStatic_rd( self ):
		cmd = Command(0x05AC, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "IMG_BRS_SW_OVERRIDE_LUMA_STATIC"):
			return False
		stationary_luma_shift = response.get_int(1)

		return stationary_luma_shift

	def cmdImgBRSDynLumaShiftMove_wr( self, moving_luma_shift ):
		cmd = Command(0x05AD, self.tx_header)
		cmd.put_int(1, moving_luma_shift)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_BRS_SW_OVERRIDE_LUMA_MOVE"):
			return False

		return True

	def cmdImgBRSDynLumaShiftMove_rd( self ):
		cmd = Command(0x05AD, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "IMG_BRS_SW_OVERRIDE_LUMA_MOVE"):
			return False
		moving_luma_shift = response.get_int(1)

		return moving_luma_shift

	def cmdImgBRSDynLumaShiftHistDelay_wr( self, delay ):
		cmd = Command(0x05AE, self.tx_header)
		cmd.put_int(1, delay)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_BRS_SW_OVERRIDE_HIST_DELAY"):
			return False

		return True

	def cmdImgBRSDynLumaShiftHistDelay_rd( self ):
		cmd = Command(0x05AE, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "IMG_BRS_SW_OVERRIDE_HIST_DELAY"):
			return False
		delay = response.get_int(1)

		return delay

	def cmdImgVICal_wr( self, color, Lutindex ):
		cmd = Command(0x05F3, self.tx_header)
		cmd.put_int(1, color)
		cmd.put_int(1, Lutindex)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "IMG_VI_CALIBRATE"):
			return False

		return True

	def cmdDmdPower_rd( self ):
		cmd = Command(0x0608, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DMD_POWER"):
			return False
		Enabled = response.get_int(1)

		return Enabled

	def cmdDmdPower_wr( self, Enable ):
		cmd = Command(0x0608, self.tx_header)
		cmd.put_int(1, Enable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DMD_POWER"):
			return False

		return True

	def cmdDmdPark_rd( self ):
		cmd = Command(0x0609, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DMD_PARK"):
			return False
		Parked = response.get_int(1)

		return Parked

	def cmdDmdPark_wr( self, Park ):
		cmd = Command(0x0609, self.tx_header)
		cmd.put_int(1, Park)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DMD_PARK"):
			return False

		return True

	def cmdDmdDevType_rd( self ):
		cmd = Command(0x0610, self.tx_header)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "DMD_DEVICETYPE"):
			return False
		dmdType = response.get_int(2)

		return dmdType

	def cmdDmdEmuReso_rd( self ):
		cmd = Command(0x0611, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DMD_EMU_SIZE"):
			return False
		dmd_res = response.get_int(1)

		return dmd_res

	def cmdDmdEmuReso_wr( self, dmd_res ):
		cmd = Command(0x0611, self.tx_header)
		cmd.put_int(1, dmd_res)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DMD_EMU_SIZE"):
			return False

		return True

	def cmdDmdReso_rd( self ):
		cmd = Command(0x0612, self.tx_header)
		response = cmd.read(self.phy, 4)
		if not utils.check_response_and_print_error(response, False, "DMD_RESOLUTION"):
			return False
		width = response.get_int(2)
		height = response.get_int(2)

		return width, height

	def cmdDmdSSpec_wr( self, ss_spread ):
		cmd = Command(0x0613, self.tx_header)
		cmd.put_int(1, ss_spread)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DMD_SSPEC"):
			return False

		return True

	def cmdDmdSSpec_rd( self ):
		cmd = Command(0x0613, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DMD_SSPEC"):
			return False
		DDP_GetSSC = response.get_int(1)

		return DDP_GetSSC

	def cmdDmdLock_wr( self, lock ):
		cmd = Command(0x0614, self.tx_header)
		cmd.put_int(1, lock)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DMD_MIRRLCK"):
			return False

		return True

	def cmdDmdLock_rd( self ):
		cmd = Command(0x0614, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DMD_MIRRLCK"):
			return False
		DMD_IsLocked = response.get_int(1)

		return DMD_IsLocked

	def cmdAlcStatus_rd( self ):
		cmd = Command(0x0700, self.tx_header)
		response = cmd.read(self.phy, 89)
		if not utils.check_response_and_print_error(response, False, "ALC_STATUS"):
			return False
		stat_AlgorithmControl = response.get_int(1)
		stat_Port1Command = response.get_int(1)
		stat_Port2Command = response.get_int(1)
		stat_Port3Command = response.get_int(1)
		stat_ActivePort = response.get_int(1)
		stat_PortVsyncPolarity = response.get_int(1)
		stat_PortHsyncPolarity = response.get_int(1)
		stat_PortIsInterlaced = response.get_int(1)
		stat_PortLinesPerFrame = response.get_int(2)
		stat_PortSystemClocksPerLine = response.get_int(2)
		stat_PortVertFreq = response.get_int(2)
		stat_PortHorzFreq = response.get_int(2)
		stat_PortActiveLines = response.get_int(2)
		stat_PortActivePixels = response.get_int(2)
		stat_PortPixelsPerLine = response.get_int(2)
		stat_PortPixelFreqInkHz = response.get_int(4)
		stat_RawSyncType = response.get_int(1)
		stat_RawVsyncPolarity = response.get_int(1)
		stat_RawHsyncPolarity = response.get_int(1)
		stat_RawIsInterlaced = response.get_int(1)
		stat_RawLinesPerFrame = response.get_int(2)
		stat_RawSystemClocksPerLine = response.get_int(2)
		stat_RawVertFreq = response.get_int(2)
		stat_RawHorzFreq = response.get_int(2)
		stat_ASMSourcePort = response.get_int(1)
		stat_ASMOperatingMode = response.get_int(1)
		stat_ASMStatus = response.get_int(1)
		stat_ASMIsPortSyncs = response.get_int(1)
		stat_ASMVRes = response.get_int(2)
		stat_ASMHRes = response.get_int(2)
		stat_ASMActiveTopLine = response.get_int(2)
		stat_ASMActiveBottomLine = response.get_int(2)
		stat_ASMActiveLeftPixel = response.get_int(2)
		stat_ASMActiveRightPixel = response.get_int(2)
		stat_ASMPhaseSetting = response.get_int(1)
		stat_ASMSampleClock = response.get_int(2)
		stat_ASMSampleClockFreqInkHz = response.get_int(4)
		stat_ASMIsComponentVideo = response.get_int(1)
		stat_ASMIsHDTV = response.get_int(1)
		stat_ASMIsYUV = response.get_int(1)
		stat_ASMIsSubSampled = response.get_int(1)
		stat_ASMIsTopfieldInverted = response.get_int(1)
		stat_ASMIsSavedMode = response.get_int(1)
		stat_ASMSavedModeGroup = response.get_int(1)
		stat_ASMSavedModeIndex = response.get_int(1)
		stat_ASMVsyncsUntilResolution = response.get_int(2)
		stat_DSMSourcePort = response.get_int(1)
		stat_DSMStatus = response.get_int(1)
		stat_DSMVRes = response.get_int(2)
		stat_DSMHRes = response.get_int(2)
		stat_DSMPixelsPerLine = response.get_int(2)
		stat_DSMPixelFreqInkHz = response.get_int(4)
		stat_DSMVsyncsUntilResolution = response.get_int(2)
		stat_PortPreviousEvent = response.get_int(1)
		stat_ASMPreviousEvent = response.get_int(1)
		stat_DSMPreviousEvent = response.get_int(1)
		stat_MiscPreviousEvent = response.get_int(1)

		return stat_AlgorithmControl, stat_Port1Command, stat_Port2Command, stat_Port3Command, stat_ActivePort, stat_PortVsyncPolarity, stat_PortHsyncPolarity, stat_PortIsInterlaced, stat_PortLinesPerFrame, stat_PortSystemClocksPerLine, stat_PortVertFreq, stat_PortHorzFreq, stat_PortActiveLines, stat_PortActivePixels, stat_PortPixelsPerLine, stat_PortPixelFreqInkHz, stat_RawSyncType, stat_RawVsyncPolarity, stat_RawHsyncPolarity, stat_RawIsInterlaced, stat_RawLinesPerFrame, stat_RawSystemClocksPerLine, stat_RawVertFreq, stat_RawHorzFreq, stat_ASMSourcePort, stat_ASMOperatingMode, stat_ASMStatus, stat_ASMIsPortSyncs, stat_ASMVRes, stat_ASMHRes, stat_ASMActiveTopLine, stat_ASMActiveBottomLine, stat_ASMActiveLeftPixel, stat_ASMActiveRightPixel, stat_ASMPhaseSetting, stat_ASMSampleClock, stat_ASMSampleClockFreqInkHz, stat_ASMIsComponentVideo, stat_ASMIsHDTV, stat_ASMIsYUV, stat_ASMIsSubSampled, stat_ASMIsTopfieldInverted, stat_ASMIsSavedMode, stat_ASMSavedModeGroup, stat_ASMSavedModeIndex, stat_ASMVsyncsUntilResolution, stat_DSMSourcePort, stat_DSMStatus, stat_DSMVRes, stat_DSMHRes, stat_DSMPixelsPerLine, stat_DSMPixelFreqInkHz, stat_DSMVsyncsUntilResolution, stat_PortPreviousEvent, stat_ASMPreviousEvent, stat_DSMPreviousEvent, stat_MiscPreviousEvent

	def cmdAlcCtrl_rd( self ):
		cmd = Command(0x0701, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "ALC_CONTROL"):
			return False
		stat_AlgorithmControl = response.get_int(1)

		return stat_AlgorithmControl

	def cmdAlcCtrl_wr( self, ctrl ):
		cmd = Command(0x0701, self.tx_header)
		cmd.put_int(1, ctrl)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "ALC_CONTROL"):
			return False

		return True

	def cmdAlcConfig_rd( self ):
		cmd = Command(0x0703, self.tx_header)
		response = cmd.read(self.phy, 30)
		if not utils.check_response_and_print_error(response, False, "ALC_CONFIG"):
			return False
		type = response.get_int(1)
		cfg_OperatingMode = response.get_int(1)
		cfg_ClockDetectionMode = response.get_int(1)
		cfg_WideMode = response.get_int(1)
		cfg_NumPhases = response.get_int(1)
		cfg_VsyncsUntilManual = response.get_int(2)
		cfg_RedCalibratedGain = response.get_int(2)
		cfg_GreenCalibratedGain = response.get_int(2)
		cfg_BlueCalibratedGain = response.get_int(2)
		cfg_RedCalibratedOffset = response.get_int(2)
		cfg_GreenCalibratedOffset = response.get_int(2)
		cfg_BlueCalibratedOffset = response.get_int(2)
		cfg_RedChMidLevelCalibratedOffset = response.get_int(2)
		cfg_BlueChMidLevelCalibratedOffset = response.get_int(2)
		cfg_Group1NumSavedModes = response.get_int(1)
		cfg_Group2NumSavedModes = response.get_int(1)
		cfg_SMTCfg = response.get_int(1)
		cfg_StateMachineDisable = response.get_int(4)

		return type, cfg_OperatingMode, cfg_ClockDetectionMode, cfg_WideMode, cfg_NumPhases, cfg_VsyncsUntilManual, cfg_RedCalibratedGain, cfg_GreenCalibratedGain, cfg_BlueCalibratedGain, cfg_RedCalibratedOffset, cfg_GreenCalibratedOffset, cfg_BlueCalibratedOffset, cfg_RedChMidLevelCalibratedOffset, cfg_BlueChMidLevelCalibratedOffset, cfg_Group1NumSavedModes, cfg_Group2NumSavedModes, cfg_SMTCfg, cfg_StateMachineDisable

	def cmdAlcConfig_wr( self, dummy, cfg_OperatingMode, cfg_ClockDetectionMode, cfg_WideMode, cfg_NumPhases, cfg_VsyncsUntilManual, cfg_RedCalibratedGain, cfg_GreenCalibratedGain, cfg_BlueCalibratedGain, cfg_RedCalibratedOffset, cfg_GreenCalibratedOffset, cfg_BlueCalibratedOffset, cfg_RedChMidLevelCalibratedOffset, cfg_BlueChMidLevelCalibratedOffset, dummy1, dummy2, cfg_SMTCfg ):
		cmd = Command(0x0703, self.tx_header)
		cmd.put_int(1, dummy)
		cmd.put_int(1, cfg_OperatingMode)
		cmd.put_int(1, cfg_ClockDetectionMode)
		cmd.put_int(1, cfg_WideMode)
		cmd.put_int(1, cfg_NumPhases)
		cmd.put_int(2, cfg_VsyncsUntilManual)
		cmd.put_int(2, cfg_RedCalibratedGain)
		cmd.put_int(2, cfg_GreenCalibratedGain)
		cmd.put_int(2, cfg_BlueCalibratedGain)
		cmd.put_int(2, cfg_RedCalibratedOffset)
		cmd.put_int(2, cfg_GreenCalibratedOffset)
		cmd.put_int(2, cfg_BlueCalibratedOffset)
		cmd.put_int(2, cfg_RedChMidLevelCalibratedOffset)
		cmd.put_int(2, cfg_BlueChMidLevelCalibratedOffset)
		cmd.put_int(1, dummy1)
		cmd.put_int(1, dummy2)
		cmd.put_int(1, cfg_SMTCfg)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "ALC_CONFIG"):
			return False

		return True

	def cmdAlcClock_rd( self ):
		cmd = Command(0x0704, self.tx_header)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "ALC_CLOCK"):
			return False
		sampleClock = response.get_int(2)

		return sampleClock

	def cmdAlcClock_wr( self, clock ):
		cmd = Command(0x0704, self.tx_header)
		cmd.put_int(2, clock)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "ALC_CLOCK"):
			return False

		return True

	def cmdAlcPhase_wr( self, Phase ):
		cmd = Command(0x0706, self.tx_header)
		cmd.put_int(1, Phase)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "ALC_PHASE"):
			return False

		return True

	def cmdAlcPhase_rd( self ):
		cmd = Command(0x0706, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "ALC_PHASE"):
			return False
		Phase = response.get_int(1)

		return Phase

	def cmdAlcPhaseInc_rd( self ):
		cmd = Command(0x0707, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "ALC_PHASEINC"):
			return False
		phase = response.get_int(1)

		return phase

	def cmdAlcPhaseDec_rd( self ):
		cmd = Command(0x0708, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "ALC_PHASEDEC"):
			return False
		phase = response.get_int(1)

		return phase

	def cmdAlcVFrameLim_rd( self ):
		cmd = Command(0x0709, self.tx_header)
		response = cmd.read(self.phy, 4)
		if not utils.check_response_and_print_error(response, False, "ALC_VFRAMELIM"):
			return False
		limit_LowerLimit = response.get_int(2)
		limit_UpperLimit = response.get_int(2)

		return limit_LowerLimit, limit_UpperLimit

	def cmdAlcHFrameLim_rd( self ):
		cmd = Command(0x070B, self.tx_header)
		response = cmd.read(self.phy, 4)
		if not utils.check_response_and_print_error(response, False, "ALC_HFRAMELIM"):
			return False
		limit_LowerLimit = response.get_int(2)
		limit_UpperLimit = response.get_int(2)

		return limit_LowerLimit, limit_UpperLimit

	def cmdAlcGain_wr( self, rgain, ggain, bgain ):
		cmd = Command(0x070C, self.tx_header)
		cmd.put_int(2, rgain)
		cmd.put_int(2, ggain)
		cmd.put_int(2, bgain)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "ALC_GAIN"):
			return False

		return True

	def cmdAlcGain_rd( self ):
		cmd = Command(0x070C, self.tx_header)
		response = cmd.read(self.phy, 6)
		if not utils.check_response_and_print_error(response, False, "ALC_GAIN"):
			return False
		rgb_Red = response.get_int(2)
		rgb_Green = response.get_int(2)
		rgb_Blue = response.get_int(2)

		return rgb_Red, rgb_Green, rgb_Blue

	def cmdAlcOffset_rd( self ):
		cmd = Command(0x070E, self.tx_header)
		response = cmd.read(self.phy, 6)
		if not utils.check_response_and_print_error(response, False, "ALC_OFFSET"):
			return False
		rgb_Red = response.get_int(2)
		rgb_Green = response.get_int(2)
		rgb_Blue = response.get_int(2)

		return rgb_Red, rgb_Green, rgb_Blue

	def cmdAlcOffset_wr( self, red, grn, blu ):
		cmd = Command(0x070E, self.tx_header)
		cmd.put_int(2, red)
		cmd.put_int(2, grn)
		cmd.put_int(2, blu)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "ALC_OFFSET"):
			return False

		return True

	def cmdAlcGetDevLim_rd( self ):
		cmd = Command(0x070F, self.tx_header)
		response = cmd.read(self.phy, 24)
		if not utils.check_response_and_print_error(response, False, "ALC_GETDEVLIM"):
			return False
		limit_LowerLimit = response.get_int(2)
		limit_UpperLimit = response.get_int(2)
		limit_LowerLimit = response.get_int(2)
		limit_UpperLimit = response.get_int(2)
		limit_LowerLimit = response.get_int(2)
		limit_UpperLimit = response.get_int(2)
		limit_LowerLimit = response.get_int(2)
		limit_UpperLimit = response.get_int(2)
		limit_LowerLimit = response.get_int(2)
		limit_UpperLimit = response.get_int(2)
		limit_LowerLimit = response.get_int(2)
		limit_UpperLimit = response.get_int(2)

		return limit_LowerLimit, limit_UpperLimit, limit_LowerLimit, limit_UpperLimit, limit_LowerLimit, limit_UpperLimit, limit_LowerLimit, limit_UpperLimit, limit_LowerLimit, limit_UpperLimit, limit_LowerLimit, limit_UpperLimit

	def cmdAlcLevelWin_wr( self, left, right, top, bottom ):
		cmd = Command(0x0710, self.tx_header)
		cmd.put_int(2, left)
		cmd.put_int(2, right)
		cmd.put_int(2, top)
		cmd.put_int(2, bottom)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "ALC_LEVELWIN"):
			return False

		return True

	def cmdAlcLevelWin_rd( self ):
		cmd = Command(0x0710, self.tx_header)
		response = cmd.read(self.phy, 8)
		if not utils.check_response_and_print_error(response, False, "ALC_LEVELWIN"):
			return False
		left = response.get_int(2)
		right = response.get_int(2)
		top = response.get_int(2)
		bottom = response.get_int(2)

		return left, right, top, bottom

	def cmdAlcRGBLevel_rd( self ):
		cmd = Command(0x0711, self.tx_header)
		response = cmd.read(self.phy, 12)
		if not utils.check_response_and_print_error(response, False, "ALC_RGBLEVELS"):
			return False
		rgb1_Red = response.get_int(2)
		rgb1_Green = response.get_int(2)
		rgb1_Blue = response.get_int(2)
		rgb2_Red = response.get_int(2)
		rgb2_Green = response.get_int(2)
		rgb2_Blue = response.get_int(2)

		return rgb1_Red, rgb1_Green, rgb1_Blue, rgb2_Red, rgb2_Green, rgb2_Blue

	def cmdAlcDebug_rd( self ):
		cmd = Command(0x0712, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "ALC_DEBUG"):
			return False
		ALC_GetEnableDebugMessages = response.get_int(1)

		return ALC_GetEnableDebugMessages

	def cmdAlcDebug_wr( self, enableALC ):
		cmd = Command(0x0712, self.tx_header)
		cmd.put_int(1, enableALC)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "ALC_DEBUG"):
			return False

		return True

	def cmdAlcMiscCtrl_rd( self ):
		cmd = Command(0x0713, self.tx_header)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "ALC_MISCCTRL"):
			return False
		ALC_GetIgnoreAlfSyncInputs = response.get_int(1)
		ALC_GetUseMaxSampleClock = response.get_int(1)

		return ALC_GetIgnoreAlfSyncInputs, ALC_GetUseMaxSampleClock

	def cmdAlcMiscCtrl_wr( self, ignore, use_max_clk ):
		cmd = Command(0x0713, self.tx_header)
		cmd.put_int(1, ignore)
		cmd.put_int(1, use_max_clk)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "ALC_MISCCTRL"):
			return False

		return True

	def cmdAlcResync_wr( self ):
		cmd = Command(0x0714, self.tx_header)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "ALC_RESYNC"):
			return False

		return True

	def cmdAlcPhaseRun_wr( self, startP, endP, stepP ):
		cmd = Command(0x0715, self.tx_header)
		cmd.put_int(1, startP)
		cmd.put_int(1, endP)
		cmd.put_int(1, stepP)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "ALC_PHASE_RUN"):
			return False

		return True

	def cmdAlcTRA_rd( self ):
		cmd = Command(0x0716, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "ALC_TRA"):
			return False
		enableTRA = response.get_int(1)

		return enableTRA

	def cmdAlcTRA_wr( self, enableTRA ):
		cmd = Command(0x0716, self.tx_header)
		cmd.put_int(1, enableTRA)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "ALC_TRA"):
			return False

		return True

	def cmdAlcDebugPtr_rd( self ):
		cmd = Command(0x0730, self.tx_header)
		response = cmd.read(self.phy, 4)
		if not utils.check_response_and_print_error(response, False, "ALC_DEBUG_PTR"):
			return False
		ptr = response.get_int(4)

		return ptr

	def cmdAlcDigRex_rd( self, i2c_addr, reg ):
		cmd = Command(0x0731, self.tx_header)
		cmd.put_int(1, i2c_addr)
		cmd.put_int(1, reg)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "ALC_DIGRX_RD"):
			return False
		rdata = response.get_int(1)

		return rdata

	def cmdAlcAFE_wr( self, reg, rdata ):
		cmd = Command(0x0733, self.tx_header)
		cmd.put_int(1, reg)
		cmd.put_int(1, rdata)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "ALC_AFE_RW"):
			return False

		return True

	def cmdAlcAFE_rd( self, reg ):
		cmd = Command(0x0733, self.tx_header)
		cmd.put_int(1, reg)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "ALC_AFE_RW"):
			return False
		rdata = response.get_int(1)

		return rdata

	def cmdAlcTRAStatus_rd( self ):
		cmd = Command(0x071C, self.tx_header)
		response = cmd.read(self.phy, 36)
		if not utils.check_response_and_print_error(response, False, "ALC_TRA_STATUS"):
			return False
		TRAStatus_VSyncWidthLines = response.get_int(1)
		TRAStatus_TimingRuleMatch = response.get_int(1)
		TRAStatus_CPAStatus = response.get_int(1)
		TRAStatus_EquationData_0_HRes = response.get_int(2)
		TRAStatus_EquationData_0_VRes = response.get_int(2)
		TRAStatus_EquationData_0_SampleClock = response.get_int(2)
		TRAStatus_EquationData_0_Left = response.get_int(2)
		TRAStatus_EquationData_0_Top = response.get_int(2)
		TRAStatus_EquationData_0_MatchType = response.get_int(1)
		TRAStatus_EquationData_1_HRes = response.get_int(2)
		TRAStatus_EquationData_1_VRes = response.get_int(2)
		TRAStatus_EquationData_1_SampleClock = response.get_int(2)
		TRAStatus_EquationData_1_Left = response.get_int(2)
		TRAStatus_EquationData_1_Top = response.get_int(2)
		TRAStatus_EquationData_1_MatchType = response.get_int(1)
		TRAStatus_EquationData_2_HRes = response.get_int(2)
		TRAStatus_EquationData_2_VRes = response.get_int(2)
		TRAStatus_EquationData_2_SampleClock = response.get_int(2)
		TRAStatus_EquationData_2_Left = response.get_int(2)
		TRAStatus_EquationData_2_Top = response.get_int(2)
		TRAStatus_EquationData_2_MatchType = response.get_int(1)

		return TRAStatus_VSyncWidthLines, TRAStatus_TimingRuleMatch, TRAStatus_CPAStatus, TRAStatus_EquationData_0_HRes, TRAStatus_EquationData_0_VRes, TRAStatus_EquationData_0_SampleClock, TRAStatus_EquationData_0_Left, TRAStatus_EquationData_0_Top, TRAStatus_EquationData_0_MatchType, TRAStatus_EquationData_1_HRes, TRAStatus_EquationData_1_VRes, TRAStatus_EquationData_1_SampleClock, TRAStatus_EquationData_1_Left, TRAStatus_EquationData_1_Top, TRAStatus_EquationData_1_MatchType, TRAStatus_EquationData_2_HRes, TRAStatus_EquationData_2_VRes, TRAStatus_EquationData_2_SampleClock, TRAStatus_EquationData_2_Left, TRAStatus_EquationData_2_Top, TRAStatus_EquationData_2_MatchType

	def cmdDDPCfgNum_rd( self ):
		cmd = Command(0x0800, self.tx_header)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "DDP_CONFIG_NUM"):
			return False
		SeqCfg = response.get_int(1)
		SWCfg = response.get_int(1)

		return SeqCfg, SWCfg

	def cmdDDPSWReset_wr( self, Proc ):
		cmd = Command(0x0802, self.tx_header)
		cmd.put_int(1, Proc)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DDP_SW_RESET"):
			return False

		return True

	#Function parsing failed
	def cmdDdpAsicCfgRev_rd( ):
		return False

	def cmdDDPUSBClk_rd( self ):
		cmd = Command(0x0804, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DDP_USB_CLOCK"):
			return False
		DDP_IsUSBClockEnabled = response.get_int(1)

		return DDP_IsUSBClockEnabled

	def cmdDDPUSBClk_wr( self, enable ):
		cmd = Command(0x0804, self.tx_header)
		cmd.put_int(1, enable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DDP_USB_CLOCK"):
			return False

		return True

	def cmdDdpRstCount_rd( self ):
		cmd = Command(0x0805, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DDP_RST_COUNT"):
			return False
		DDP_GetResetCount = response.get_int(1)

		return DDP_GetResetCount

	def cmdDdpRstCause_rd( self ):
		cmd = Command(0x0806, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DDP_RST_CAUSE"):
			return False
		DDP_GetResetCause = response.get_int(1)

		return DDP_GetResetCause

	def cmdDDPGenPurpseClkEnabled_rd( self, Clk ):
		cmd = Command(0x0807, self.tx_header)
		cmd.put_int(1, Clk)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DDP_OUTPUT_CLOCK"):
			return False
		IsEnabled = response.get_int(1)

		return IsEnabled

	def cmdDDPGenPurpseClkEnabled_wr( self, Clk, Enabled, Freq ):
		cmd = Command(0x0807, self.tx_header)
		cmd.put_int(1, Clk)
		cmd.put_int(1, Enabled)
		cmd.put_int(4, Freq)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DDP_OUTPUT_CLOCK"):
			return False

		return True

	def cmdDDPGenPurpseClkFreq_rd( self, Clk ):
		cmd = Command(0x0808, self.tx_header)
		cmd.put_int(1, Clk)
		response = cmd.read(self.phy, 4)
		if not utils.check_response_and_print_error(response, False, "DDP_CLOCK_FREQ"):
			return False
		Freq = response.get_int(4)

		return Freq

	def cmdDdpEmerShut_rd( self ):
		cmd = Command(0x080A, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DDP_EMER_SHUTDOWN"):
			return False
		DDP_IsEmergencyShutdownEnabled = response.get_int(1)

		return DDP_IsEmergencyShutdownEnabled

	def cmdDdpEmerShut_wr( self, flag ):
		cmd = Command(0x080A, self.tx_header)
		cmd.put_int(1, flag)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DDP_EMER_SHUTDOWN"):
			return False

		return True

	def cmdDDPASICInfo_rd( self ):
		cmd = Command(0x080B, self.tx_header)
		response = cmd.read(self.phy, 6)
		if not utils.check_response_and_print_error(response, False, "DDP_ASIC_INFO"):
			return False
		AsicID = response.get_int(1)
		AsicProductConfiguration = response.get_int(1)
		FlashProductConfiguration = response.get_int(4)

		return AsicID, AsicProductConfiguration, FlashProductConfiguration

	def cmdDdp_ErrStat_rd( self ):
		cmd = Command(0x080D, self.tx_header)
		response = cmd.read(self.phy, 4)
		if not utils.check_response_and_print_error(response, False, "DDP_ERROR_STATUS"):
			return False
		ErrorStatus = response.get_int(4)

		return ErrorStatus

	def cmdDdp_SysStat_rd( self ):
		cmd = Command(0x0810, self.tx_header)
		response = cmd.read(self.phy, 4)
		if not utils.check_response_and_print_error(response, False, "DDP_SYSTEM_STATUS"):
			return False
		system_status = response.get_int(4)

		return system_status

	#Function parsing failed
	def cmdDDPSysMode_rd( ):
		return False

	def cmdDDPSysModeNum_rd( self ):
		cmd = Command(0x0815, self.tx_header)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "DDP_SYSTEM_MODE_NUM"):
			return False
		ModeNum = response.get_int(2)

		return ModeNum

	def cmdDDPSysModeNum_wr( self, ModeNum ):
		cmd = Command(0x0815, self.tx_header)
		cmd.put_int(2, ModeNum)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DDP_SYSTEM_MODE_NUM"):
			return False

		return True

	#Function parsing failed
	def cmdDDPSysMode1_rd( ):
		return False

	def cmdTPGEnable_rd( self ):
		cmd = Command(0x0900, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "TPG_A_ENABLE"):
			return False
		Enabled = response.get_int(1)

		return Enabled

	def cmdTPGEnable_wr( self, enableTPG ):
		cmd = Command(0x0900, self.tx_header)
		cmd.put_int(1, enableTPG)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "TPG_A_ENABLE"):
			return False

		return True

	def cmdTPGPattern_rd( self ):
		cmd = Command(0x0901, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "TPG_A_PATTERN"):
			return False
		tpg_pattern = response.get_int(1)

		return tpg_pattern

	def cmdTPGPattern_wr( self, Pattern ):
		cmd = Command(0x0901, self.tx_header)
		cmd.put_int(1, Pattern)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "TPG_A_PATTERN"):
			return False

		return True

	def cmdTPGBorder_rd( self ):
		cmd = Command(0x0902, self.tx_header)
		response = cmd.read(self.phy, 7)
		if not utils.check_response_and_print_error(response, False, "TPG_A_BORDER_WIDTH"):
			return False
		Width = response.get_int(1)
		BorderColor_Red = response.get_int(2)
		BorderColor_Green = response.get_int(2)
		BorderColor_Blue = response.get_int(2)

		return Width, BorderColor_Red, BorderColor_Green, BorderColor_Blue

	def cmdTPGBorder_wr( self, Width, BorderColor_Red, BorderColor_Green, BorderColor_Blue ):
		cmd = Command(0x0902, self.tx_header)
		cmd.put_int(1, Width)
		cmd.put_int(2, BorderColor_Red)
		cmd.put_int(2, BorderColor_Green)
		cmd.put_int(2, BorderColor_Blue)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "TPG_A_BORDER_WIDTH"):
			return False

		return True

	def cmdTPGRes_rd( self ):
		cmd = Command(0x0903, self.tx_header)
		response = cmd.read(self.phy, 4)
		if not utils.check_response_and_print_error(response, False, "TPG_A_RESOLUTION"):
			return False
		hres = response.get_int(2)
		vres = response.get_int(2)

		return hres, vres

	def cmdTPGRes_wr( self, hres, vres ):
		cmd = Command(0x0903, self.tx_header)
		cmd.put_int(2, hres)
		cmd.put_int(2, vres)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "TPG_A_RESOLUTION"):
			return False

		return True

	def cmdTPGFrameRate_rd( self ):
		cmd = Command(0x0904, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "TPG_A_FRAME_RATE"):
			return False
		Rate = response.get_int(1)

		return Rate

	def cmdTPGFrameRate_wr( self, Rate ):
		cmd = Command(0x0904, self.tx_header)
		cmd.put_int(1, Rate)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "TPG_A_FRAME_RATE"):
			return False

		return True

	def cmdTPGPixelClk_rd( self ):
		cmd = Command(0x0905, self.tx_header)
		response = cmd.read(self.phy, 4)
		if not utils.check_response_and_print_error(response, False, "TPG_A_CLOCKRATE"):
			return False
		PixelClk = response.get_int(4)

		return PixelClk

	def cmdTPGSolidField_rd( self ):
		cmd = Command(0x0906, self.tx_header)
		response = cmd.read(self.phy, 6)
		if not utils.check_response_and_print_error(response, False, "TPG_A_SOLID_FIELD"):
			return False
		SolidColor_Red = response.get_int(2)
		SolidColor_Green = response.get_int(2)
		SolidColor_Blue = response.get_int(2)

		return SolidColor_Red, SolidColor_Green, SolidColor_Blue

	def cmdTPGSolidField_wr( self, SolidColor_Red, SolidColor_Green, SolidColor_Blue ):
		cmd = Command(0x0906, self.tx_header)
		cmd.put_int(2, SolidColor_Red)
		cmd.put_int(2, SolidColor_Green)
		cmd.put_int(2, SolidColor_Blue)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "TPG_A_SOLID_FIELD"):
			return False

		return True

	def cmdTPGRampHorizontal_rd( self ):
		cmd = Command(0x0907, self.tx_header)
		response = cmd.read(self.phy, 4)
		if not utils.check_response_and_print_error(response, False, "TPG_A_HORZ_RAMP"):
			return False
		RampStep = response.get_int(1)
		ColorEnbale_Red = response.get_int(1)
		ColorEnbale_Green = response.get_int(1)
		ColorEnbale_Blue = response.get_int(1)

		return RampStep, ColorEnbale_Red, ColorEnbale_Green, ColorEnbale_Blue

	def cmdTPGRampHorizontal_wr( self, RampStep, ColorEnbale_Red, ColorEnbale_Green, ColorEnbale_Blue ):
		cmd = Command(0x0907, self.tx_header)
		cmd.put_int(1, RampStep)
		cmd.put_int(1, ColorEnbale_Red)
		cmd.put_int(1, ColorEnbale_Green)
		cmd.put_int(1, ColorEnbale_Blue)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "TPG_A_HORZ_RAMP"):
			return False

		return True

	def cmdTPGRampVertical_rd( self ):
		cmd = Command(0x0908, self.tx_header)
		response = cmd.read(self.phy, 4)
		if not utils.check_response_and_print_error(response, False, "TPG_A_VERT_RAMP"):
			return False
		RampStep = response.get_int(1)
		ColorEnbale_Red = response.get_int(1)
		ColorEnbale_Green = response.get_int(1)
		ColorEnbale_Blue = response.get_int(1)

		return RampStep, ColorEnbale_Red, ColorEnbale_Green, ColorEnbale_Blue

	def cmdTPGRampVertical_wr( self, RampStep, ColorEnbale_Red, ColorEnbale_Green, ColorEnbale_Blue ):
		cmd = Command(0x0908, self.tx_header)
		cmd.put_int(1, RampStep)
		cmd.put_int(1, ColorEnbale_Red)
		cmd.put_int(1, ColorEnbale_Green)
		cmd.put_int(1, ColorEnbale_Blue)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "TPG_A_VERT_RAMP"):
			return False

		return True

	def cmdTPGHorzLines_rd( self ):
		cmd = Command(0x0909, self.tx_header)
		response = cmd.read(self.phy, 16)
		if not utils.check_response_and_print_error(response, False, "TPG_A_HORZ_LINES"):
			return False
		Width = response.get_int(2)
		Space = response.get_int(2)
		LineColor_Red = response.get_int(2)
		LineColor_Green = response.get_int(2)
		LineColor_Blue = response.get_int(2)
		BgndColor_Red = response.get_int(2)
		BgndColor_Green = response.get_int(2)
		BgndColor_Blue = response.get_int(2)

		return Width, Space, LineColor_Red, LineColor_Green, LineColor_Blue, BgndColor_Red, BgndColor_Green, BgndColor_Blue

	def cmdTPGHorzLines_wr( self, Width, Space, LineColor_Red, LineColor_Green, LineColor_Blue, BgndColor_Red, BgndColor_Green, BgndColor_Blue ):
		cmd = Command(0x0909, self.tx_header)
		cmd.put_int(2, Width)
		cmd.put_int(2, Space)
		cmd.put_int(2, LineColor_Red)
		cmd.put_int(2, LineColor_Green)
		cmd.put_int(2, LineColor_Blue)
		cmd.put_int(2, BgndColor_Red)
		cmd.put_int(2, BgndColor_Green)
		cmd.put_int(2, BgndColor_Blue)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "TPG_A_HORZ_LINES"):
			return False

		return True

	def cmdTPGVertLines_rd( self ):
		cmd = Command(0x090A, self.tx_header)
		response = cmd.read(self.phy, 16)
		if not utils.check_response_and_print_error(response, False, "TPG_A_VERT_LINES"):
			return False
		Width = response.get_int(2)
		Space = response.get_int(2)
		LineColor_Red = response.get_int(2)
		LineColor_Green = response.get_int(2)
		LineColor_Blue = response.get_int(2)
		BgndColor_Red = response.get_int(2)
		BgndColor_Green = response.get_int(2)
		BgndColor_Blue = response.get_int(2)

		return Width, Space, LineColor_Red, LineColor_Green, LineColor_Blue, BgndColor_Red, BgndColor_Green, BgndColor_Blue

	def cmdTPGVertLines_wr( self, Width, Space, LineColor_Red, LineColor_Green, LineColor_Blue, BgndColor_Red, BgndColor_Green, BgndColor_Blue ):
		cmd = Command(0x090A, self.tx_header)
		cmd.put_int(2, Width)
		cmd.put_int(2, Space)
		cmd.put_int(2, LineColor_Red)
		cmd.put_int(2, LineColor_Green)
		cmd.put_int(2, LineColor_Blue)
		cmd.put_int(2, BgndColor_Red)
		cmd.put_int(2, BgndColor_Green)
		cmd.put_int(2, BgndColor_Blue)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "TPG_A_VERT_LINES"):
			return False

		return True

	def cmdTPGDiagLines_rd( self ):
		cmd = Command(0x090B, self.tx_header)
		response = cmd.read(self.phy, 14)
		if not utils.check_response_and_print_error(response, False, "TPG_A_DIAG_LINES"):
			return False
		Period = response.get_int(2)
		LineColor_Red = response.get_int(2)
		LineColor_Green = response.get_int(2)
		LineColor_Blue = response.get_int(2)
		BgndColor_Red = response.get_int(2)
		BgndColor_Green = response.get_int(2)
		BgndColor_Blue = response.get_int(2)

		return Period, LineColor_Red, LineColor_Green, LineColor_Blue, BgndColor_Red, BgndColor_Green, BgndColor_Blue

	def cmdTPGDiagLines_wr( self, Period, LineColor_Red, LineColor_Green, LineColor_Blue, BgndColor_Red, BgndColor_Green, BgndColor_Blue ):
		cmd = Command(0x090B, self.tx_header)
		cmd.put_int(2, Period)
		cmd.put_int(2, LineColor_Red)
		cmd.put_int(2, LineColor_Green)
		cmd.put_int(2, LineColor_Blue)
		cmd.put_int(2, BgndColor_Red)
		cmd.put_int(2, BgndColor_Green)
		cmd.put_int(2, BgndColor_Blue)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "TPG_A_DIAG_LINES"):
			return False

		return True

	def cmdTPGGridLines_rd( self ):
		cmd = Command(0x090C, self.tx_header)
		response = cmd.read(self.phy, 20)
		if not utils.check_response_and_print_error(response, False, "TPG_A_GRID"):
			return False
		HWidth = response.get_int(2)
		HSpace = response.get_int(2)
		VWidth = response.get_int(2)
		VSpace = response.get_int(2)
		LineColor_Red = response.get_int(2)
		LineColor_Green = response.get_int(2)
		LineColor_Blue = response.get_int(2)
		BgndColor_Red = response.get_int(2)
		BgndColor_Green = response.get_int(2)
		BgndColor_Blue = response.get_int(2)

		return HWidth, HSpace, VWidth, VSpace, LineColor_Red, LineColor_Green, LineColor_Blue, BgndColor_Red, BgndColor_Green, BgndColor_Blue

	def cmdTPGGridLines_wr( self, HWidth, HSpace, VWidth, VSpace, LineColor_Red, LineColor_Green, LineColor_Blue, BgndColor_Red, BgndColor_Green, BgndColor_Blue ):
		cmd = Command(0x090C, self.tx_header)
		cmd.put_int(2, HWidth)
		cmd.put_int(2, HSpace)
		cmd.put_int(2, VWidth)
		cmd.put_int(2, VSpace)
		cmd.put_int(2, LineColor_Red)
		cmd.put_int(2, LineColor_Green)
		cmd.put_int(2, LineColor_Blue)
		cmd.put_int(2, BgndColor_Red)
		cmd.put_int(2, BgndColor_Green)
		cmd.put_int(2, BgndColor_Blue)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "TPG_A_GRID"):
			return False

		return True

	def cmdTPGCB_rd( self ):
		cmd = Command(0x090D, self.tx_header)
		response = cmd.read(self.phy, 16)
		if not utils.check_response_and_print_error(response, False, "TPG_A_CHECK_BRD"):
			return False
		Width = response.get_int(2)
		Height = response.get_int(2)
		TopLeftCheckerColor_Red = response.get_int(2)
		TopLeftCheckerColor_Green = response.get_int(2)
		TopLeftCheckerColor_Blue = response.get_int(2)
		NextCheckerColor_Red = response.get_int(2)
		NextCheckerColor_Green = response.get_int(2)
		NextCheckerColor_Blue = response.get_int(2)

		return Width, Height, TopLeftCheckerColor_Red, TopLeftCheckerColor_Green, TopLeftCheckerColor_Blue, NextCheckerColor_Red, NextCheckerColor_Green, NextCheckerColor_Blue

	def cmdTPGCB_wr( self, Width, Height, TopLeftCheckerColor_Red, TopLeftCheckerColor_Green, TopLeftCheckerColor_Blue, NextCheckerColor_Red, NextCheckerColor_Green, NextCheckerColor_Blue ):
		cmd = Command(0x090D, self.tx_header)
		cmd.put_int(2, Width)
		cmd.put_int(2, Height)
		cmd.put_int(2, TopLeftCheckerColor_Red)
		cmd.put_int(2, TopLeftCheckerColor_Green)
		cmd.put_int(2, TopLeftCheckerColor_Blue)
		cmd.put_int(2, NextCheckerColor_Red)
		cmd.put_int(2, NextCheckerColor_Green)
		cmd.put_int(2, NextCheckerColor_Blue)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "TPG_A_CHECK_BRD"):
			return False

		return True

	def cmdTPGColorBars_rd( self ):
		cmd = Command(0x090E, self.tx_header)
		response = cmd.read(self.phy, 5)
		if not utils.check_response_and_print_error(response, False, "TPG_A_COLOR_BARS"):
			return False
		Width = response.get_int(2)
		ColorEnable_Red = response.get_int(1)
		ColorEnable_Green = response.get_int(1)
		ColorEnable_Blue = response.get_int(1)

		return Width, ColorEnable_Red, ColorEnable_Green, ColorEnable_Blue

	def cmdTPGColorBars_wr( self, Width, ColorEnable_Red, ColorEnable_Green, ColorEnable_Blue ):
		cmd = Command(0x090E, self.tx_header)
		cmd.put_int(2, Width)
		cmd.put_int(1, ColorEnable_Red)
		cmd.put_int(1, ColorEnable_Green)
		cmd.put_int(1, ColorEnable_Blue)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "TPG_A_COLOR_BARS"):
			return False

		return True

	def cmdTPGColorHRamp_rd( self ):
		cmd = Command(0x090F, self.tx_header)
		response = cmd.read(self.phy, 6)
		if not utils.check_response_and_print_error(response, False, "TPG_A_COLOR_RAMP"):
			return False
		RampStep = response.get_int(1)
		Height = response.get_int(2)
		ColorEnable_Red = response.get_int(1)
		ColorEnable_Green = response.get_int(1)
		ColorEnable_Blue = response.get_int(1)

		return RampStep, Height, ColorEnable_Red, ColorEnable_Green, ColorEnable_Blue

	def cmdTPGColorHRamp_wr( self, RampStep, Height, ColorEnable_Red, ColorEnable_Green, ColorEnable_Blue ):
		cmd = Command(0x090F, self.tx_header)
		cmd.put_int(1, RampStep)
		cmd.put_int(2, Height)
		cmd.put_int(1, ColorEnable_Red)
		cmd.put_int(1, ColorEnable_Green)
		cmd.put_int(1, ColorEnable_Blue)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "TPG_A_COLOR_RAMP"):
			return False

		return True

	def cmdTPGFixedRamp_rd( self ):
		cmd = Command(0x0910, self.tx_header)
		response = cmd.read(self.phy, 15)
		if not utils.check_response_and_print_error(response, False, "TPG_A_FIXED_RAMP"):
			return False
		StartIntensity = response.get_int(2)
		RampStepWidth = response.get_int(2)
		RampStepInc = response.get_int(2)
		BgndColor_Red = response.get_int(2)
		BgndColor_Green = response.get_int(2)
		BgndColor_Blue = response.get_int(2)
		RampColorEnable_Red = response.get_int(1)
		RampColorEnable_Green = response.get_int(1)
		RampColorEnable_Blue = response.get_int(1)

		return StartIntensity, RampStepWidth, RampStepInc, BgndColor_Red, BgndColor_Green, BgndColor_Blue, RampColorEnable_Red, RampColorEnable_Green, RampColorEnable_Blue

	def cmdTPGFixedRamp_wr( self, StartIntensity, RampStepWidth, RampStepInc, BgndColor_Red, BgndColor_Green, BgndColor_Blue, RampColorEnable_Red, RampColorEnable_Green, RampColorEnable_Blue ):
		cmd = Command(0x0910, self.tx_header)
		cmd.put_int(2, StartIntensity)
		cmd.put_int(2, RampStepWidth)
		cmd.put_int(2, RampStepInc)
		cmd.put_int(2, BgndColor_Red)
		cmd.put_int(2, BgndColor_Green)
		cmd.put_int(2, BgndColor_Blue)
		cmd.put_int(1, RampColorEnable_Red)
		cmd.put_int(1, RampColorEnable_Green)
		cmd.put_int(1, RampColorEnable_Blue)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "TPG_A_FIXED_RAMP"):
			return False

		return True

	def cmdTPGDiamondDiagLines_rd( self ):
		cmd = Command(0x0911, self.tx_header)
		response = cmd.read(self.phy, 11)
		if not utils.check_response_and_print_error(response, False, "TPG_A_DIAMOND_DIAG_LINES"):
			return False
		FwdLineStartColor = response.get_int(1)
		BckwdLineColor = response.get_int(1)
		BgndColor_Red = response.get_int(2)
		BgndColor_Green = response.get_int(2)
		BgndColor_Blue = response.get_int(2)
		DoubleLineMode = response.get_int(1)
		Distance = response.get_int(2)

		return FwdLineStartColor, BckwdLineColor, BgndColor_Red, BgndColor_Green, BgndColor_Blue, DoubleLineMode, Distance

	def cmdTPGDiamondDiagLines_wr( self, FwdLineStartColor, BckwdLineColor, BgndColor_Red, BgndColor_Green, BgndColor_Blue, DoubleLineMode, Distance ):
		cmd = Command(0x0911, self.tx_header)
		cmd.put_int(1, FwdLineStartColor)
		cmd.put_int(1, BckwdLineColor)
		cmd.put_int(2, BgndColor_Red)
		cmd.put_int(2, BgndColor_Green)
		cmd.put_int(2, BgndColor_Blue)
		cmd.put_int(1, DoubleLineMode)
		cmd.put_int(2, Distance)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "TPG_A_DIAMOND_DIAG_LINES"):
			return False

		return True

	def cmdTPGMinBlankings_wr( self, MinHorzBackPorch, MinHorzFrontPorch, MinVertBackPorch, MinVertFrontPorch ):
		cmd = Command(0x0914, self.tx_header)
		cmd.put_int(2, MinHorzBackPorch)
		cmd.put_int(2, MinHorzFrontPorch)
		cmd.put_int(2, MinVertBackPorch)
		cmd.put_int(2, MinVertFrontPorch)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "TPG_A_MIN_BLANKINGS"):
			return False

		return True

	def cmdSrcPortCfg_rd( self, port ):
		cmd = Command(0x0A00, self.tx_header)
		cmd.put_int(1, port)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "SRC_PORT_CONF"):
			return False
		Port_Config_PortWidth = response.get_int(1)
		Port_Config_ABC_Mux = response.get_int(1)

		return Port_Config_PortWidth, Port_Config_ABC_Mux

	def cmdSrcPortCfg_wr( self, port, Port_Config_PortWidth, Port_Config_ABC_Mux ):
		cmd = Command(0x0A00, self.tx_header)
		cmd.put_int(1, port)
		cmd.put_int(1, Port_Config_PortWidth)
		cmd.put_int(1, Port_Config_ABC_Mux)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "SRC_PORT_CONF"):
			return False

		return True

	def cmdSrcConfig_rd( self, Port ):
		cmd = Command(0x0A02, self.tx_header)
		cmd.put_int(1, Port)
		response = cmd.read(self.phy, 53)
		if not utils.check_response_and_print_error(response, False, "SRC_SOURCE_CONF"):
			return False
		SourceConfig_VSyncCfg = response.get_int(1)
		SourceConfig_HSyncCfg = response.get_int(1)
		SourceConfig_TopField = response.get_int(1)
		SourceConfig_DownSampleCfg = response.get_int(1)
		SourceConfig_Is3D = response.get_int(1)
		SourceConfig_IsClockPolarityPositive = response.get_int(1)
		SourceConfig_PixelFormat = response.get_int(1)
		SourceConfig_IsExternalDE = response.get_int(1)
		SourceConfig_IsInterlaced = response.get_int(1)
		SourceConfig_IsOffsetBinary = response.get_int(1)
		SourceConfig_IsTopFieldInvertedAtScaler = response.get_int(1)
		SourceConfig_TotalArea_PixelsPerLine = []
		SourceConfig_TotalArea_PixelsPerLine += response.get_arr(2)
		SourceConfig_TotalArea_LinesPerFrame = []
		SourceConfig_TotalArea_LinesPerFrame += response.get_arr(2)
		SourceConfig_ActiveArea_FirstPixel = []
		SourceConfig_ActiveArea_FirstPixel += response.get_arr(2)
		SourceConfig_ActiveArea_FirstLine = []
		SourceConfig_ActiveArea_FirstLine += response.get_arr(2)
		SourceConfig_ActiveArea_PixelsPerLine = []
		SourceConfig_ActiveArea_PixelsPerLine += response.get_arr(2)
		SourceConfig_ActiveArea_LinesPerFrame = []
		SourceConfig_ActiveArea_LinesPerFrame += response.get_arr(2)
		SourceConfig_BottomFieldFirstLine = []
		SourceConfig_BottomFieldFirstLine += response.get_arr(2)
		SourceConfig_PixelClockFreqInkHz = []
		SourceConfig_PixelClockFreqInkHz += response.get_arr(4)
		SourceConfig_ColorSpaceConvCoeffs_0 = []
		SourceConfig_ColorSpaceConvCoeffs_0 += response.get_arr(2)
		SourceConfig_ColorSpaceConvCoeffs_1 = []
		SourceConfig_ColorSpaceConvCoeffs_1 += response.get_arr(2)
		SourceConfig_ColorSpaceConvCoeffs_2 = []
		SourceConfig_ColorSpaceConvCoeffs_2 += response.get_arr(2)
		SourceConfig_ColorSpaceConvCoeffs_3 = []
		SourceConfig_ColorSpaceConvCoeffs_3 += response.get_arr(2)
		SourceConfig_ColorSpaceConvCoeffs_4 = []
		SourceConfig_ColorSpaceConvCoeffs_4 += response.get_arr(2)
		SourceConfig_ColorSpaceConvCoeffs_5 = []
		SourceConfig_ColorSpaceConvCoeffs_5 += response.get_arr(2)
		SourceConfig_ColorSpaceConvCoeffs_6 = []
		SourceConfig_ColorSpaceConvCoeffs_6 += response.get_arr(2)
		SourceConfig_ColorSpaceConvCoeffs_7 = []
		SourceConfig_ColorSpaceConvCoeffs_7 += response.get_arr(2)
		SourceConfig_ColorSpaceConvCoeffs_8 = []
		SourceConfig_ColorSpaceConvCoeffs_8 += response.get_arr(2)
		SourceConfig_Offset_0 = []
		SourceConfig_Offset_0 += response.get_arr(2)
		SourceConfig_Offset_1 = []
		SourceConfig_Offset_1 += response.get_arr(2)
		SourceConfig_Offset_2 = []
		SourceConfig_Offset_2 += response.get_arr(2)

		return SourceConfig_VSyncCfg, SourceConfig_HSyncCfg, SourceConfig_TopField, SourceConfig_DownSampleCfg, SourceConfig_Is3D, SourceConfig_IsClockPolarityPositive, SourceConfig_PixelFormat, SourceConfig_IsExternalDE, SourceConfig_IsInterlaced, SourceConfig_IsOffsetBinary, SourceConfig_IsTopFieldInvertedAtScaler, SourceConfig_TotalArea_PixelsPerLine, SourceConfig_TotalArea_LinesPerFrame, SourceConfig_ActiveArea_FirstPixel, SourceConfig_ActiveArea_FirstLine, SourceConfig_ActiveArea_PixelsPerLine, SourceConfig_ActiveArea_LinesPerFrame, SourceConfig_BottomFieldFirstLine, SourceConfig_PixelClockFreqInkHz, SourceConfig_ColorSpaceConvCoeffs_0, SourceConfig_ColorSpaceConvCoeffs_1, SourceConfig_ColorSpaceConvCoeffs_2, SourceConfig_ColorSpaceConvCoeffs_3, SourceConfig_ColorSpaceConvCoeffs_4, SourceConfig_ColorSpaceConvCoeffs_5, SourceConfig_ColorSpaceConvCoeffs_6, SourceConfig_ColorSpaceConvCoeffs_7, SourceConfig_ColorSpaceConvCoeffs_8, SourceConfig_Offset_0, SourceConfig_Offset_1, SourceConfig_Offset_2

	def cmdSrcConfig_wr( self, Port, SourceConfig_VSyncCfg, SourceConfig_HSyncCfg, SourceConfig_TopField, SourceConfig_DownSampleCfg, SourceConfig_Is3D, SourceConfig_IsClockPolarityPositive, SourceConfig_PixelFormat, SourceConfig_IsExternalDE, SourceConfig_IsInterlaced, SourceConfig_IsOffsetBinary, SourceConfig_IsTopFieldInvertedAtScaler, SourceConfig_TotalArea_PixelsPerLine, SourceConfig_TotalArea_LinesPerFrame, SourceConfig_ActiveArea_FirstPixel, SourceConfig_ActiveArea_FirstLine, SourceConfig_ActiveArea_PixelsPerLine, SourceConfig_ActiveArea_LinesPerFrame, SourceConfig_BottomFieldFirstLine, SourceConfig_PixelClockFreqInkHz, SourceConfig_ColorSpaceConvCoeffs_0, SourceConfig_ColorSpaceConvCoeffs_1, SourceConfig_ColorSpaceConvCoeffs_2, SourceConfig_ColorSpaceConvCoeffs_3, SourceConfig_ColorSpaceConvCoeffs_4, SourceConfig_ColorSpaceConvCoeffs_5, SourceConfig_ColorSpaceConvCoeffs_6, SourceConfig_ColorSpaceConvCoeffs_7, SourceConfig_ColorSpaceConvCoeffs_8, SourceConfig_Offset_0, SourceConfig_Offset_1, SourceConfig_Offset_2, FrameRate ):
		cmd = Command(0x0A02, self.tx_header)
		cmd.put_int(1, Port)
		cmd.put_int(1, SourceConfig_VSyncCfg)
		cmd.put_int(1, SourceConfig_HSyncCfg)
		cmd.put_int(1, SourceConfig_TopField)
		cmd.put_int(1, SourceConfig_DownSampleCfg)
		cmd.put_int(1, SourceConfig_Is3D)
		cmd.put_int(1, SourceConfig_IsClockPolarityPositive)
		cmd.put_int(1, SourceConfig_PixelFormat)
		cmd.put_int(1, SourceConfig_IsExternalDE)
		cmd.put_int(1, SourceConfig_IsInterlaced)
		cmd.put_int(1, SourceConfig_IsOffsetBinary)
		cmd.put_int(1, SourceConfig_IsTopFieldInvertedAtScaler)
		cmd.put_int(2, SourceConfig_TotalArea_PixelsPerLine)
		cmd.put_int(2, SourceConfig_TotalArea_LinesPerFrame)
		cmd.put_int(2, SourceConfig_ActiveArea_FirstPixel)
		cmd.put_int(2, SourceConfig_ActiveArea_FirstLine)
		cmd.put_int(2, SourceConfig_ActiveArea_PixelsPerLine)
		cmd.put_int(2, SourceConfig_ActiveArea_LinesPerFrame)
		cmd.put_int(2, SourceConfig_BottomFieldFirstLine)
		cmd.put_int(4, SourceConfig_PixelClockFreqInkHz)
		cmd.put_int(2, SourceConfig_ColorSpaceConvCoeffs_0)
		cmd.put_int(2, SourceConfig_ColorSpaceConvCoeffs_1)
		cmd.put_int(2, SourceConfig_ColorSpaceConvCoeffs_2)
		cmd.put_int(2, SourceConfig_ColorSpaceConvCoeffs_3)
		cmd.put_int(2, SourceConfig_ColorSpaceConvCoeffs_4)
		cmd.put_int(2, SourceConfig_ColorSpaceConvCoeffs_5)
		cmd.put_int(2, SourceConfig_ColorSpaceConvCoeffs_6)
		cmd.put_int(2, SourceConfig_ColorSpaceConvCoeffs_7)
		cmd.put_int(2, SourceConfig_ColorSpaceConvCoeffs_8)
		cmd.put_int(2, SourceConfig_Offset_0)
		cmd.put_int(2, SourceConfig_Offset_1)
		cmd.put_int(2, SourceConfig_Offset_2)
		cmd.put_int(4, FrameRate)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "SRC_SOURCE_CONF"):
			return False

		return True

	def cmdSrcChanCfg_rd( self, Chan ):
		cmd = Command(0x0A03, self.tx_header)
		cmd.put_int(1, Chan)
		response = cmd.read(self.phy, 7)
		if not utils.check_response_and_print_error(response, False, "SRC_CHANNEL_CONF"):
			return False
		ChannelConfig_VSyncSource = response.get_int(1)
		ChannelConfig_HSyncSource = response.get_int(1)
		ChannelConfig_DataSource = response.get_int(1)
		ChannelConfig_DataEnableSource = response.get_int(1)
		ChannelConfig_FieldSource = response.get_int(1)
		ChannelConfig_ClockPort = response.get_int(1)
		ChannelConfig_IsClockPolarityPositive = response.get_int(1)

		return ChannelConfig_VSyncSource, ChannelConfig_HSyncSource, ChannelConfig_DataSource, ChannelConfig_DataEnableSource, ChannelConfig_FieldSource, ChannelConfig_ClockPort, ChannelConfig_IsClockPolarityPositive

	def cmdSrcChanCfg_wr( self, Chan, ChannelConfig_VSyncSource, ChannelConfig_HSyncSource, ChannelConfig_DataSource, ChannelConfig_DataEnableSource, ChannelConfig_FieldSource, ChannelConfig_ClockPort, ChannelConfig_IsClockPolarityPositive ):
		cmd = Command(0x0A03, self.tx_header)
		cmd.put_int(1, Chan)
		cmd.put_int(1, ChannelConfig_VSyncSource)
		cmd.put_int(1, ChannelConfig_HSyncSource)
		cmd.put_int(1, ChannelConfig_DataSource)
		cmd.put_int(1, ChannelConfig_DataEnableSource)
		cmd.put_int(1, ChannelConfig_FieldSource)
		cmd.put_int(1, ChannelConfig_ClockPort)
		cmd.put_int(1, ChannelConfig_IsClockPolarityPositive)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "SRC_CHANNEL_CONF"):
			return False

		return True

	def cmdSrcSyncType_rd( self ):
		cmd = Command(0x0A04, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "SRC_RAW_SYNC_TYPE"):
			return False
		syncType = response.get_int(1)

		return syncType

	def cmdSrcSyncType_wr( self, syncType ):
		cmd = Command(0x0A04, self.tx_header)
		cmd.put_int(1, syncType)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "SRC_RAW_SYNC_TYPE"):
			return False

		return True

	def cmdSrcPixClk_rd( self, port, digSrc ):
		cmd = Command(0x0A06, self.tx_header)
		cmd.put_int(1, port)
		cmd.put_int(1, digSrc)
		response = cmd.read(self.phy, 6)
		if not utils.check_response_and_print_error(response, False, "SRC_PXL_CLK"):
			return False
		PixelClock = response.get_int(2)
		PixelClockFreq = response.get_int(4)

		return PixelClock, PixelClockFreq

	def cmdSrcThresh_rd( self, port ):
		cmd = Command(0x0A08, self.tx_header)
		cmd.put_int(1, port)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "SRC_THRESHOLD"):
			return False
		threshold = response.get_int(2)

		return threshold

	def cmdSrcThresh_wr( self, port, Threshold ):
		cmd = Command(0x0A08, self.tx_header)
		cmd.put_int(1, port)
		cmd.put_int(2, Threshold)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "SRC_THRESHOLD"):
			return False

		return True

	def cmdSrcPorch_rd( self, port ):
		cmd = Command(0x0A09, self.tx_header)
		cmd.put_int(1, port)
		response = cmd.read(self.phy, 8)
		if not utils.check_response_and_print_error(response, False, "SRC_FR_BK_PORCH"):
			return False
		FrontPorch = response.get_int(4)
		BackPorch = response.get_int(4)

		return FrontPorch, BackPorch

	def cmdSrcStatus_rd( self, port ):
		cmd = Command(0x0A0A, self.tx_header)
		cmd.put_int(1, port)
		response = cmd.read(self.phy, 15)
		if not utils.check_response_and_print_error(response, False, "SRC_SRC_STATUS"):
			return False
		TotalLines = response.get_int(2)
		TotalSCLKsPerLine = response.get_int(4)
		VerticalFrequency = response.get_int(2)
		HorizontalFrequency = response.get_int(2)
		HSyncWidth = response.get_int(2)
		VSyncWidth = response.get_int(2)
		IsInterlaced = response.get_int(1)

		return TotalLines, TotalSCLKsPerLine, VerticalFrequency, HorizontalFrequency, HSyncWidth, VSyncWidth, IsInterlaced

	def cmdSrcCSC_rd( self, port ):
		cmd = Command(0x0A0B, self.tx_header)
		cmd.put_int(1, port)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "SRC_SRC_CSC"):
			return False
		index = response.get_int(2)

		return index

	def cmdSrcCSC_wr( self, port, index ):
		cmd = Command(0x0A0B, self.tx_header)
		cmd.put_int(1, port)
		cmd.put_int(1, index)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "SRC_SRC_CSC"):
			return False

		return True

	def cmdSrcDesc_rd( self ):
		cmd = Command(0x0A0C, self.tx_header)
		response = cmd.read(self.phy, 39)
		if not utils.check_response_and_print_error(response, False, "SRC_SRC_DESC"):
			return False
		srcDesc_sourceActive = response.get_int(1)
		srcDesc_okToDeinterlace = response.get_int(1)
		srcDesc_isVideo = response.get_int(1)
		srcDesc_isYUV = response.get_int(1)
		srcDesc_isHighDefinitionVideo = response.get_int(1)
		srcDesc_is3D = response.get_int(1)
		getRate = response.get_int(4)
		srcDesc_inputHeight = []
		srcDesc_inputHeight += response.get_arr(2)
		srcDesc_inputWidth = []
		srcDesc_inputWidth += response.get_arr(2)
		srcDesc_nativeHeight = []
		srcDesc_nativeHeight += response.get_arr(2)
		srcDesc_nativeWidth = []
		srcDesc_nativeWidth += response.get_arr(2)
		srcDesc_port = response.get_int(1)
		srcDesc_alcOffset_Red = []
		srcDesc_alcOffset_Red += response.get_arr(2)
		srcDesc_alcOffset_Green = []
		srcDesc_alcOffset_Green += response.get_arr(2)
		srcDesc_alcOffset_Blue = []
		srcDesc_alcOffset_Blue += response.get_arr(2)
		srcDesc_alcGain_Red = []
		srcDesc_alcGain_Red += response.get_arr(2)
		srcDesc_alcGain_Green = []
		srcDesc_alcGain_Green += response.get_arr(2)
		srcDesc_alcGain_Blue = []
		srcDesc_alcGain_Blue += response.get_arr(2)
		srcDesc_alcSampleClock = []
		srcDesc_alcSampleClock += response.get_arr(2)
		srcDesc_alcLeftPixel = []
		srcDesc_alcLeftPixel += response.get_arr(2)
		srcDesc_alcTopLine = []
		srcDesc_alcTopLine += response.get_arr(2)
		srcDesc_connector = response.get_int(1)
		srcDesc_activeDisplay = response.get_int(1)

		return srcDesc_sourceActive, srcDesc_okToDeinterlace, srcDesc_isVideo, srcDesc_isYUV, srcDesc_isHighDefinitionVideo, srcDesc_is3D, getRate, srcDesc_inputHeight, srcDesc_inputWidth, srcDesc_nativeHeight, srcDesc_nativeWidth, srcDesc_port, srcDesc_alcOffset_Red, srcDesc_alcOffset_Green, srcDesc_alcOffset_Blue, srcDesc_alcGain_Red, srcDesc_alcGain_Green, srcDesc_alcGain_Blue, srcDesc_alcSampleClock, srcDesc_alcLeftPixel, srcDesc_alcTopLine, srcDesc_connector, srcDesc_activeDisplay

	def cmdSrcDesc_wr( self, srcDesc_sourceActive, srcDesc_okToDeinterlace, srcDesc_isVideo, srcDesc_isYUV, srcDesc_isHighDefinitionVideo, srcDesc_is3D, setRate, srcDesc_inputHeight, srcDesc_inputWidth, srcDesc_nativeHeight, srcDesc_nativeWidth, srcDesc_port, srcDesc_alcOffset_Red, srcDesc_alcOffset_Green, srcDesc_alcOffset_Blue, srcDesc_alcGain_Red, srcDesc_alcGain_Green, srcDesc_alcGain_Blue, srcDesc_alcSampleClock, srcDesc_alcLeftPixel, srcDesc_alcTopLine, srcDesc_connector, srcDesc_activeDisplay ):
		cmd = Command(0x0A0C, self.tx_header)
		cmd.put_int(1, srcDesc_sourceActive)
		cmd.put_int(1, srcDesc_okToDeinterlace)
		cmd.put_int(1, srcDesc_isVideo)
		cmd.put_int(1, srcDesc_isYUV)
		cmd.put_int(1, srcDesc_isHighDefinitionVideo)
		cmd.put_int(1, srcDesc_is3D)
		cmd.put_int(4, setRate)
		cmd.put_int(2, srcDesc_inputHeight)
		cmd.put_int(2, srcDesc_inputWidth)
		cmd.put_int(2, srcDesc_nativeHeight)
		cmd.put_int(2, srcDesc_nativeWidth)
		cmd.put_int(1, srcDesc_port)
		cmd.put_int(2, srcDesc_alcOffset_Red)
		cmd.put_int(2, srcDesc_alcOffset_Green)
		cmd.put_int(2, srcDesc_alcOffset_Blue)
		cmd.put_int(2, srcDesc_alcGain_Red)
		cmd.put_int(2, srcDesc_alcGain_Green)
		cmd.put_int(2, srcDesc_alcGain_Blue)
		cmd.put_int(2, srcDesc_alcSampleClock)
		cmd.put_int(2, srcDesc_alcLeftPixel)
		cmd.put_int(2, srcDesc_alcTopLine)
		cmd.put_int(1, srcDesc_connector)
		cmd.put_int(1, srcDesc_activeDisplay)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "SRC_SRC_DESC"):
			return False

		return True

	def cmdLmpEnable_rd( self ):
		cmd = Command(0x0B00, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "LMP_ENABLE"):
			return False
		enable = response.get_int(1)

		return enable

	def cmdLmpEnable_wr( self, enable ):
		cmd = Command(0x0B00, self.tx_header)
		cmd.put_int(1, enable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "LMP_ENABLE"):
			return False

		return True

	def cmdLmpEnaRst_rd( self ):
		cmd = Command(0x0B01, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "LMP_ENABLERESET"):
			return False
		enable = response.get_int(1)

		return enable

	def cmdLmpEnaRst_wr( self, enable ):
		cmd = Command(0x0B01, self.tx_header)
		cmd.put_int(1, enable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "LMP_ENABLERESET"):
			return False

		return True

	def cmdLmpIsLit_rd( self ):
		cmd = Command(0x0B02, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "LMP_ISLIT"):
			return False
		LMP_IsLampLit = response.get_int(1)

		return LMP_IsLampLit

	def cmdLmpIsStab_rd( self ):
		cmd = Command(0x0B03, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "LMP_ISSTABLE"):
			return False
		LMP_IsLampLitStable = response.get_int(1)

		return LMP_IsLampLitStable

	def cmdLmpSyncType_rd( self ):
		cmd = Command(0x0B04, self.tx_header)
		response = cmd.read(self.phy, 3)
		if not utils.check_response_and_print_error(response, False, "LMP_SYNCTYPE"):
			return False
		syncType = response.get_int(1)
		negativePolarity = response.get_int(1)
		lampSyncSel = response.get_int(1)

		return syncType, negativePolarity, lampSyncSel

	def cmdLmpSyncType_wr( self, syncType, negativePolarity, lampSyncSel ):
		cmd = Command(0x0B04, self.tx_header)
		cmd.put_int(1, syncType)
		cmd.put_int(1, negativePolarity)
		cmd.put_int(1, lampSyncSel)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "LMP_SYNCTYPE"):
			return False

		return True

	def cmdLmpGetBin_rd( self ):
		cmd = Command(0x0B05, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "LMP_GETBIN"):
			return False
		bin = response.get_int(1)

		return bin

	def cmdLmpSyncCnt_rd( self ):
		cmd = Command(0x0B06, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "LMP_SYNCCOUNT"):
			return False
		syncCount = response.get_int(1)

		return syncCount

	def cmdLmpSyncCnt_wr( self, syncCount ):
		cmd = Command(0x0B06, self.tx_header)
		cmd.put_int(1, syncCount)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "LMP_SYNCCOUNT"):
			return False

		return True

	def cmdLmpEnaManBin_rd( self ):
		cmd = Command(0x0B07, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "LMP_ENABMAN_BIN"):
			return False
		LMP_IsManualLampBinEnabled = response.get_int(1)

		return LMP_IsManualLampBinEnabled

	def cmdLmpEnaManBin_wr( self, enable ):
		cmd = Command(0x0B07, self.tx_header)
		cmd.put_int(1, enable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "LMP_ENABMAN_BIN"):
			return False

		return True

	def cmdLmpSetMan_wr( self, bin_val ):
		cmd = Command(0x0B08, self.tx_header)
		cmd.put_int(1, bin_val)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "LMP_SETMAN_BIN"):
			return False

		return True

	def cmdLmpStrRstDly_rd( self ):
		cmd = Command(0x0B09, self.tx_header)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "LMP_STRKRST_DELAY"):
			return False
		delay = response.get_int(2)

		return delay

	def cmdLmpStrRstDly_wr( self, delay ):
		cmd = Command(0x0B09, self.tx_header)
		cmd.put_int(2, delay)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "LMP_STRKRST_DELAY"):
			return False

		return True

	def cmdLmpEnabDly_rd( self ):
		cmd = Command(0x0B0A, self.tx_header)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "LMP_ENAB_DELAY"):
			return False
		delay = response.get_int(2)

		return delay

	def cmdLmpEnabDly_wr( self, delay ):
		cmd = Command(0x0B0A, self.tx_header)
		cmd.put_int(2, delay)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "LMP_ENAB_DELAY"):
			return False

		return True

	def cmdLmpFanCtl_rd( self, fanNum, select ):
		cmd = Command(0x0B0B, self.tx_header)
		cmd.put_int(1, fanNum)
		cmd.put_int(1, select)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "LMP_FANCONTROL"):
			return False
		swFreq = response.get_int(1)
		dutyCycle = response.get_int(1)

		return swFreq, dutyCycle

	def cmdLmpFanCtl_wr( self, fanNum, swFreq, dutyCycle, select ):
		cmd = Command(0x0B0B, self.tx_header)
		cmd.put_int(1, fanNum)
		cmd.put_int(1, swFreq)
		cmd.put_int(1, dutyCycle)
		cmd.put_int(1, select)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "LMP_FANCONTROL"):
			return False

		return True

	def cmdVarLmp_EnableComms_rd( self ):
		cmd = Command(0x0B10, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "LMP_BLST_COMMUNICATIONS"):
			return False
		enable = response.get_int(1)

		return enable

	def cmdVarLmp_EnableComms_wr( self, enable ):
		cmd = Command(0x0B10, self.tx_header)
		cmd.put_int(1, enable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "LMP_BLST_COMMUNICATIONS"):
			return False

		return True

	def cmdVarLmp_GetWaveformIndex_rd( self ):
		cmd = Command(0x0B11, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "LMP_BLST_WAVEFORMINDEX"):
			return False
		waveform_index = response.get_int(1)

		return waveform_index

	def cmdVarLmp_SetWaveformIndex_wr( self, waveform_index ):
		cmd = Command(0x0B11, self.tx_header)
		cmd.put_int(1, waveform_index)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "LMP_BLST_WAVEFORMINDEX"):
			return False

		return True

	def cmdVarLmp_GetNumOfWaveForms_rd( self ):
		cmd = Command(0x0B12, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "LMP_BLST_GETNUMWAVEFORMS"):
			return False
		num_waveforms = response.get_int(1)

		return num_waveforms

	def cmdVarLmp_GetWaveformID_rd( self ):
		cmd = Command(0x0B13, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "LMP_BLST_GETWAVEFORMID"):
			return False
		waveform_id = response.get_int(1)

		return waveform_id

	def cmdVarLmp_GetWaveformGain_rd( self ):
		cmd = Command(0x0B14, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "LMP_BLST_WAVEFORMGAIN"):
			return False
		waveform_gain = response.get_int(1)

		return waveform_gain

	def cmdVarLmp_SetWaveformGain_wr( self, waveform_gain ):
		cmd = Command(0x0B14, self.tx_header)
		cmd.put_int(1, waveform_gain)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "LMP_BLST_WAVEFORMGAIN"):
			return False

		return True

	def cmdVarLmp_GetMinGain_rd( self ):
		cmd = Command(0x0B15, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "LMP_BLST_GETMINGAIN"):
			return False
		min_gain = response.get_int(1)

		return min_gain

	def cmdVarLmp_GetMaxGain_rd( self ):
		cmd = Command(0x0B16, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "LMP_BLST_GETMAXGAIN"):
			return False
		max_gain = response.get_int(1)

		return max_gain

	def cmdVarLmp_OpenMailbox_wr( self, StartAddr ):
		cmd = Command(0x0B17, self.tx_header)
		cmd.put_int(2, StartAddr)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "LMP_BLST_OPENMAILBOX"):
			return False

		return True

	def cmdVarLmp_WriteMailbox_wr( self, mbx_data ):
		cmd = Command(0x0B18, self.tx_header)
		cmd.put_int(1, mbx_data)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "LMP_BLST_WRITEMAILBOX"):
			return False

		return True

	def cmdVarLmp_ReadMailBox_rd( self ):
		cmd = Command(0x0B19, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "LMP_BLST_READMAILBOX"):
			return False
		data = response.get_int(1)

		return data

	def cmdVarLmp_CloseMailbox_wr( self ):
		cmd = Command(0x0B1A, self.tx_header)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "LMP_BLST_CLOSEMAILBOX"):
			return False

		return True

	def cmdVarLmp_GetMailboxStatus_rd( self ):
		cmd = Command(0x0B1B, self.tx_header)
		response = cmd.read(self.phy, 3)
		if not utils.check_response_and_print_error(response, False, "LMP_BLST_GETMAILBOXSTATUS"):
			return False
		address = response.get_int(2)
		err = response.get_int(1)

		return address, err

	def cmdVarLmp_GetManufactureID_rd( self ):
		cmd = Command(0x0B1C, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "LMP_BLST_GETMANUFACTUREID"):
			return False
		manufacturer_id = response.get_int(1)

		return manufacturer_id

	def cmdVarLmp_GetBallastID_rd( self ):
		cmd = Command(0x0B1D, self.tx_header)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "LMP_BLST_GETBALLASTID"):
			return False
		ballast_id = response.get_int(2)

		return ballast_id

	def cmdVarLmp_GetBallastStatus_rd( self ):
		cmd = Command(0x0B1E, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "LMP_BLST_GETBALLASTSTATUS"):
			return False
		ballast_status = response.get_int(1)

		return ballast_status

	def cmdVarLmp_GetLampStatus_rd( self ):
		cmd = Command(0x0B1F, self.tx_header)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "LMP_BLST_GETLAMPSTATUS"):
			return False
		safe_mode = response.get_int(1)
		error_code = response.get_int(1)

		return safe_mode, error_code

	def cmdLmpSyncDelay_wr( self, thisDelay ):
		cmd = Command(0x0B20, self.tx_header)
		cmd.put_int(2, thisDelay)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "LMP_SYNCDELAY"):
			return False

		return True

	def cmdLmpSyncDelay_rd( self ):
		cmd = Command(0x0B20, self.tx_header)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "LMP_SYNCDELAY"):
			return False
		thisDelay = response.get_int(2)

		return thisDelay

	def cmdReportLampInfo_rd( self, index ):
		cmd = Command(0x0B21, self.tx_header)
		cmd.put_int(1, index)
		response = cmd.read(self.phy, 4)
		if not utils.check_response_and_print_error(response, False, "LMP_REPORT_LAMPINFO"):
			return False
		info = response.get_int(4)

		return info

	def cmdReportLampModes_wr( self, index ):
		cmd = Command(0x0B22, self.tx_header)
		cmd.put_int(1, index)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "LMP_REPORT_LAMPMODES"):
			return False

		return True

	def cmdReportLampModes_rd( self, index ):
		cmd = Command(0x0B22, self.tx_header)
		cmd.put_int(1, index)
		response = cmd.read(self.phy, 4)
		if not utils.check_response_and_print_error(response, False, "LMP_REPORT_LAMPMODES"):
			return False
		mode = response.get_int(4)

		return mode

	def cmdLmpSetDynGain_wr( self, PowerGain ):
		cmd = Command(0x0B23, self.tx_header)
		cmd.put_int(1, PowerGain)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "LMP_BLST_DYNAMICGAIN"):
			return False

		return True

	def cmdLmpGetDynGainStatus_rd( self ):
		cmd = Command(0x0B24, self.tx_header)
		response = cmd.read(self.phy, 8)
		if not utils.check_response_and_print_error(response, False, "LMP_BLST_DYNAMICGAIN_STATUS"):
			return False
		PowerGain = response.get_int(1)
		MinGain = response.get_int(1)
		MaxGain = response.get_int(1)
		is_pulses_on = response.get_int(1)
		color_correction_index = response.get_int(1)
		cooling_gain = response.get_int(1)
		lamp_state = response.get_int(1)
		is_db_enabled = response.get_int(1)

		return PowerGain, MinGain, MaxGain, is_pulses_on, color_correction_index, cooling_gain, lamp_state, is_db_enabled

	def cmdLmpSetDynGainState( self, State ):
		cmd = Command(0x0B25, self.tx_header)
		cmd.put_int(1, State)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "LMP_BLST_DYNBLST_SETSTATE"):
			return False

		return True

	def cmdCWIndexPeriod_rd( self ):
		cmd = Command(0x0C03, self.tx_header)
		response = cmd.read(self.phy, 8)
		if not utils.check_response_and_print_error(response, False, "CW_IDXPERIOD"):
			return False
		period = response.get_int(4)
		frequency = response.get_int(4)

		return period, frequency

	def cmdCWBrake_wr( self ):
		cmd = Command(0x0C16, self.tx_header)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "CW_CMDBRAKE"):
			return False

		return True

	def cmdCWSetSpeed_wr( self, Speed ):
		cmd = Command(0x0C19, self.tx_header)
		cmd.put_int(2, Speed)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "CW_SET_SPEED"):
			return False

		return True

	def cmdCWSetDir_rd( self ):
		cmd = Command(0x0C1A, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "CW_SET_DIR"):
			return False
		cw1_direction = response.get_int(1)

		return cw1_direction

	def cmdCWSetDirection_wr( self, Dir ):
		cmd = Command(0x0C1A, self.tx_header)
		cmd.put_int(1, Dir)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "CW_SET_DIR"):
			return False

		return True

	def cmdCWIsDirSet_rd( self ):
		cmd = Command(0x0C1B, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "CW_IS_DIR_SET"):
			return False
		cw1_is_dir_set = response.get_int(1)

		return cw1_is_dir_set

	def cmdCWClockEnable_wr( self, ClkEnable ):
		cmd = Command(0x0C1C, self.tx_header)
		cmd.put_int(1, ClkEnable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "CW_CLOCK_ENABLE"):
			return False

		return True

	def cmdCWGetType_rd( self ):
		cmd = Command(0x0C1D, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "CW_TYPE"):
			return False
		CW_GetWheel = response.get_int(1)

		return CW_GetWheel

	def cmdCWType_wr( self, Type ):
		cmd = Command(0x0C1D, self.tx_header)
		cmd.put_int(1, Type)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "CW_TYPE"):
			return False

		return True

	def cmdCWMtrType_rd( self ):
		cmd = Command(0x0C1E, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "CW_MTR_TYPE"):
			return False
		CW_GetMotorType = response.get_int(1)

		return CW_GetMotorType

	def cmdCWMtrType_wr( self, Type ):
		cmd = Command(0x0C1E, self.tx_header)
		cmd.put_int(1, Type)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "CW_MTR_TYPE"):
			return False

		return True

	def cmdCWGetIndexPrecision_rd( self, Wheel ):
		cmd = Command(0x0C23, self.tx_header)
		cmd.put_int(1, Wheel)
		response = cmd.read(self.phy, 3)
		if not utils.check_response_and_print_error(response, False, "CW_INDEX_PRECISION"):
			return False
		DegreesInteger = response.get_int(2)
		DegreesFraction = response.get_int(1)

		return DegreesInteger, DegreesFraction

	def cmdCWIndexPrecision_wr( self, Wheel, DegreesInteger, DegreesFraction ):
		cmd = Command(0x0C23, self.tx_header)
		cmd.put_int(1, Wheel)
		cmd.put_int(2, DegreesInteger)
		cmd.put_int(1, DegreesFraction)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "CW_INDEX_PRECISION"):
			return False

		return True

	def cmdCWManVsync_wr( self, enable, freq ):
		cmd = Command(0x0C24, self.tx_header)
		cmd.put_int(1, enable)
		cmd.put_int(1, freq)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "CW_MAN_VSYNC"):
			return False

		return True

	def cmdCWSetDualTrackMode_wr( self, mode ):
		cmd = Command(0x0C25, self.tx_header)
		cmd.put_int(1, mode)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "CW_TRACK_MODE"):
			return False

		return True

	def cmdCWSetDualTrackMode_rd( self ):
		cmd = Command(0x0C25, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "CW_TRACK_MODE"):
			return False
		Mode = response.get_int(1)

		return Mode

	def cmdCWSetCW3_Period_wr( self, period ):
		cmd = Command(0x0C26, self.tx_header)
		cmd.put_int(4, period)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "CW_CW3_PERIOD"):
			return False

		return True

	def cmdCWSetCW3_Period_rd( self ):
		cmd = Command(0x0C26, self.tx_header)
		response = cmd.read(self.phy, 4)
		if not utils.check_response_and_print_error(response, False, "CW_CW3_PERIOD"):
			return False
		period = response.get_int(4)

		return period

	def cmdCWSetCW_IndexPol_wr( self, polarity1, polarity2, polarity3 ):
		cmd = Command(0x0C27, self.tx_header)
		cmd.put_int(1, polarity1)
		cmd.put_int(1, polarity2)
		cmd.put_int(1, polarity3)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "CW_INDEX_POLARITY"):
			return False

		return True

	def cmdCWSetCW_IndexPol_rd( self ):
		cmd = Command(0x0C27, self.tx_header)
		response = cmd.read(self.phy, 3)
		if not utils.check_response_and_print_error(response, False, "CW_INDEX_POLARITY"):
			return False
		polarity1 = response.get_int(1)
		polarity2 = response.get_int(1)
		polarity3 = response.get_int(1)

		return polarity1, polarity2, polarity3

	def cmdSEQEnable_rd( self ):
		cmd = Command(0x0D01, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "SEQ_ENABLE"):
			return False
		SEQ_IsEnabled = response.get_int(1)

		return SEQ_IsEnabled

	def cmdSeqEnable_wr( self, enable ):
		cmd = Command(0x0D01, self.tx_header)
		cmd.put_int(1, enable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "SEQ_ENABLE"):
			return False

		return True

	def cmdSEQEnableSpokeTest_rd( self ):
		cmd = Command(0x0D02, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "SEQ_ENABLESPOKETEST"):
			return False
		IsEnabled = response.get_int(1)

		return IsEnabled

	def cmdSeqEnableSpokeTest_wr( self, enable ):
		cmd = Command(0x0D02, self.tx_header)
		cmd.put_int(1, enable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "SEQ_ENABLESPOKETEST"):
			return False

		return True

	def cmdSEQConfigSpokeTest_rd( self ):
		cmd = Command(0x0D03, self.tx_header)
		response = cmd.read(self.phy, 3)
		if not utils.check_response_and_print_error(response, False, "SEQ_CONFIGSPOKETEST"):
			return False
		Param1 = response.get_int(1)
		Param2 = response.get_int(1)
		Param3 = response.get_int(1)

		return Param1, Param2, Param3

	def cmdSeqCfgSpokeTest_wr( self, Param1, Param2, Param3 ):
		cmd = Command(0x0D03, self.tx_header)
		cmd.put_int(1, Param1)
		cmd.put_int(1, Param2)
		cmd.put_int(1, Param3)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "SEQ_CONFIGSPOKETEST"):
			return False

		return True

	def cmdSEQGetRevision_rd( self ):
		cmd = Command(0x0D04, self.tx_header)
		response = cmd.read(self.phy, 4)
		if not utils.check_response_and_print_error(response, False, "SEQ_GETREVISION"):
			return False
		SEQ_GetRev = response.get_int(4)

		return SEQ_GetRev

	def cmdFrmParms_rd( self ):
		cmd = Command(0x0E01, self.tx_header)
		response = cmd.read(self.phy, 12)
		if not utils.check_response_and_print_error(response, False, "FRC_PARAMS"):
			return False
		RateIn = response.get_int(4)
		RateOut = response.get_int(4)
		FRCmode = response.get_int(4)

		return RateIn, RateOut, FRCmode

	def cmdFrmParms_wr( self, RateIn, RateOut, FRCmode ):
		cmd = Command(0x0E01, self.tx_header)
		cmd.put_int(4, RateIn)
		cmd.put_int(4, RateOut)
		cmd.put_int(4, FRCmode)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "FRC_PARAMS"):
			return False

		return True

	def cmdTpmSw_rd( self, SigNo ):
		cmd = Command(0x0F00, self.tx_header)
		cmd.put_int(1, SigNo)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "SW_TM_CFG"):
			return False
		SigType = response.get_int(1)

		return SigType

	def cmdTpmSw_wr( self, SigNo, SigType ):
		cmd = Command(0x0F00, self.tx_header)
		cmd.put_int(1, SigNo)
		cmd.put_int(1, SigType)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "SW_TM_CFG"):
			return False

		return True

	def cmdTpmHw_rd( self, SigNo ):
		cmd = Command(0x0F01, self.tx_header)
		cmd.put_int(1, SigNo)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "HW_TM_CFG"):
			return False
		SigType = response.get_int(1)

		return SigType

	def cmdTpmHw_wr( self, SigNo, SigType ):
		cmd = Command(0x0F01, self.tx_header)
		cmd.put_int(1, SigNo)
		cmd.put_int(1, SigType)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "HW_TM_CFG"):
			return False

		return True

	def cmdDispCfgPri_rd( self ):
		cmd = Command(0x1000, self.tx_header)
		response = cmd.read(self.phy, 17)
		if not utils.check_response_and_print_error(response, False, "DISP_CFGPRIMARY"):
			return False
		DisplayConfig_CroppedArea_FirstPixel = response.get_int(2)
		DisplayConfig_CroppedArea_FirstLine = response.get_int(2)
		DisplayConfig_CroppedArea_PixelsPerLine = response.get_int(2)
		DisplayConfig_CroppedArea_LinesPerFrame = response.get_int(2)
		DisplayConfig_DisplayArea_FirstPixel = response.get_int(2)
		DisplayConfig_DisplayArea_FirstLine = response.get_int(2)
		DisplayConfig_DisplayArea_PixelsPerLine = response.get_int(2)
		DisplayConfig_DisplayArea_LinesPerFrame = response.get_int(2)
		DisplayConfig_Centered = response.get_int(1)

		return DisplayConfig_CroppedArea_FirstPixel, DisplayConfig_CroppedArea_FirstLine, DisplayConfig_CroppedArea_PixelsPerLine, DisplayConfig_CroppedArea_LinesPerFrame, DisplayConfig_DisplayArea_FirstPixel, DisplayConfig_DisplayArea_FirstLine, DisplayConfig_DisplayArea_PixelsPerLine, DisplayConfig_DisplayArea_LinesPerFrame, DisplayConfig_Centered

	def cmdDispCfgPri_wr( self, DisplayConfig_CroppedArea_FirstPixel, DisplayConfig_CroppedArea_FirstLine, DisplayConfig_CroppedArea_PixelsPerLine, DisplayConfig_CroppedArea_LinesPerFrame, DisplayConfig_DisplayArea_FirstPixel, DisplayConfig_DisplayArea_FirstLine, DisplayConfig_DisplayArea_PixelsPerLine, DisplayConfig_DisplayArea_LinesPerFrame, DisplayConfig_Centered ):
		cmd = Command(0x1000, self.tx_header)
		cmd.put_int(2, DisplayConfig_CroppedArea_FirstPixel)
		cmd.put_int(2, DisplayConfig_CroppedArea_FirstLine)
		cmd.put_int(2, DisplayConfig_CroppedArea_PixelsPerLine)
		cmd.put_int(2, DisplayConfig_CroppedArea_LinesPerFrame)
		cmd.put_int(2, DisplayConfig_DisplayArea_FirstPixel)
		cmd.put_int(2, DisplayConfig_DisplayArea_FirstLine)
		cmd.put_int(2, DisplayConfig_DisplayArea_PixelsPerLine)
		cmd.put_int(2, DisplayConfig_DisplayArea_LinesPerFrame)
		cmd.put_int(1, DisplayConfig_Centered)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DISP_CFGPRIMARY"):
			return False

		return True

	def cmdDispPriSrc_rd( self ):
		cmd = Command(0x1001, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DISP_PRIMARYSRC"):
			return False
		source = response.get_int(1)

		return source

	def cmdDispPriSrc_wr( self, source ):
		cmd = Command(0x1001, self.tx_header)
		cmd.put_int(1, source)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DISP_PRIMARYSRC"):
			return False

		return True

	def cmdDispBckMd_rd( self ):
		cmd = Command(0x1002, self.tx_header)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "DISP_BACKGRNDMD"):
			return False
		Mode = response.get_int(1)
		Clr = response.get_int(1)

		return Mode, Clr

	def cmdDispBckMd_wr( self, Mode, Clr ):
		cmd = Command(0x1002, self.tx_header)
		cmd.put_int(1, Mode)
		cmd.put_int(1, Clr)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DISP_BACKGRNDMD"):
			return False

		return True

	def cmdDispScaleRing_rd( self ):
		cmd = Command(0x1004, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DISP_SCALERING"):
			return False
		enable = response.get_int(1)

		return enable

	def cmdDispScaleRing_wr( self, enable ):
		cmd = Command(0x1004, self.tx_header)
		cmd.put_int(1, enable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DISP_SCALERING"):
			return False

		return True

	def cmdDispScaleFilt_rd( self ):
		cmd = Command(0x1005, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DISP_SCALEFILT"):
			return False
		FtNum = response.get_int(1)

		return FtNum

	def cmdDispScaleFilt_wr( self, FtNum ):
		cmd = Command(0x1005, self.tx_header)
		cmd.put_int(1, FtNum)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DISP_SCALEFILT"):
			return False

		return True

	def cmdDispAnaEnable_rd( self ):
		cmd = Command(0x1006, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DISP_ANAENABLE"):
			return False
		enabled = response.get_int(1)

		return enabled

	def cmdDispAnaEnable_wr( self, status ):
		cmd = Command(0x1006, self.tx_header)
		cmd.put_int(1, status)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DISP_ANAENABLE"):
			return False

		return True

	def cmdDispAspect_rd( self ):
		cmd = Command(0x1007, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DISP_ASPECT"):
			return False
		aspect_ratio = response.get_int(1)

		return aspect_ratio

	def cmdDispAspect_wr( self, aspect_ratio ):
		cmd = Command(0x1007, self.tx_header)
		cmd.put_int(1, aspect_ratio)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DISP_ASPECT"):
			return False

		return True

	def cmdDispFlipH_rd( self ):
		cmd = Command(0x1008, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DISP_HORIZFLIP"):
			return False
		Flip = response.get_int(1)

		return Flip

	def cmdDispFlipH_wr( self, Flip ):
		cmd = Command(0x1008, self.tx_header)
		cmd.put_int(1, Flip)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DISP_HORIZFLIP"):
			return False

		return True

	def cmdDispFlipV_rd( self ):
		cmd = Command(0x1009, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DISP_VERTFLIP"):
			return False
		Flip = response.get_int(1)

		return Flip

	def cmdDispFlipV_wr( self, Flip ):
		cmd = Command(0x1009, self.tx_header)
		cmd.put_int(1, Flip)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DISP_VERTFLIP"):
			return False

		return True

	def cmdDispFreeze_rd( self ):
		cmd = Command(0x100A, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DISP_FREEZE"):
			return False
		freeze = response.get_int(1)

		return freeze

	def cmdDispFreeze_wr( self, freeze ):
		cmd = Command(0x100A, self.tx_header)
		cmd.put_int(1, freeze)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DISP_FREEZE"):
			return False

		return True

	def cmdDispKeyEna_rd( self ):
		cmd = Command(0x100B, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DISP_KEYENABLE"):
			return False
		is_keystone_enabled = response.get_int(1)

		return is_keystone_enabled

	def cmdDispKeyEna_wr( self, results ):
		cmd = Command(0x100B, self.tx_header)
		cmd.put_int(1, results)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DISP_KEYENABLE"):
			return False

		return True

	def cmdDispKeyAng_rd( self ):
		cmd = Command(0x100C, self.tx_header)
		response = cmd.read(self.phy, 6)
		if not utils.check_response_and_print_error(response, False, "DISP_KEYANGLE"):
			return False
		pitch = response.get_int(2)
		throwRatio = response.get_int(2)
		DMDOffset = response.get_int(2)

		return pitch, throwRatio, DMDOffset

	def cmdDispKeyAng_wr( self, pitch, throwRatio, DMD_Offset ):
		cmd = Command(0x100C, self.tx_header)
		cmd.put_int(2, pitch)
		cmd.put_int(2, throwRatio)
		cmd.put_int(2, DMD_Offset)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DISP_KEYANGLE"):
			return False

		return True

	def cmdDispKeyPit_rd( self ):
		cmd = Command(0x100D, self.tx_header)
		response = cmd.read(self.phy, 4)
		if not utils.check_response_and_print_error(response, False, "DISP_KEYPITCH"):
			return False
		maxPitch = response.get_int(2)
		minPitch = response.get_int(2)

		return maxPitch, minPitch

	def cmdDispManualScaleFilt_wr( self, num ):
		cmd = Command(0x1010, self.tx_header)
		cmd.put_int(1, num)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DISP_MANFILT"):
			return False

		return True

	def cmdSfgColor_rd( self ):
		cmd = Command(0x1100, self.tx_header)
		response = cmd.read(self.phy, 6)
		if not utils.check_response_and_print_error(response, False, "SFG_SETCOLOR"):
			return False
		red = response.get_int(2)
		grn = response.get_int(2)
		blu = response.get_int(2)

		return red, grn, blu

	def cmdSfgColor_wr( self, red, grn, blu ):
		cmd = Command(0x1100, self.tx_header)
		cmd.put_int(2, red)
		cmd.put_int(2, grn)
		cmd.put_int(2, blu)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "SFG_SETCOLOR"):
			return False

		return True

	def cmdSfgRes_rd( self ):
		cmd = Command(0x1102, self.tx_header)
		response = cmd.read(self.phy, 4)
		if not utils.check_response_and_print_error(response, False, "SFG_SETRES"):
			return False
		sfgResolution_Horz_Resolution = response.get_int(2)
		sfgResolution_Vert_Resolution = response.get_int(2)

		return sfgResolution_Horz_Resolution, sfgResolution_Vert_Resolution

	def cmdDeiFMode_rd( self ):
		cmd = Command(0x1400, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DEI_FILM_MODE"):
			return False
		mode = response.get_int(1)

		return mode

	def cmdDeiFMode_wr( self, mode ):
		cmd = Command(0x1400, self.tx_header)
		cmd.put_int(1, mode)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DEI_FILM_MODE"):
			return False

		return True

	def cmdDeiThresh_rd( self ):
		cmd = Command(0x1401, self.tx_header)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "DEI_LOCK_THRESH"):
			return False
		before_lock = response.get_int(1)
		before_unlock = response.get_int(1)

		return before_lock, before_unlock

	def cmdDeiThresh_wr( self, before_lock, before_unlock ):
		cmd = Command(0x1401, self.tx_header)
		cmd.put_int(1, before_lock)
		cmd.put_int(1, before_unlock)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DEI_LOCK_THRESH"):
			return False

		return True

	def cmdDeiStatus_rd( self ):
		cmd = Command(0x1402, self.tx_header)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "DEI_STATUS"):
			return False
		is_region_0_locked = response.get_int(1)
		is_region_1_locked = response.get_int(1)

		return is_region_0_locked, is_region_1_locked

	def cmdDeiEnable_rd( self ):
		cmd = Command(0x1403, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DEI_ENABLE"):
			return False
		DEI_IsEnabled = response.get_int(1)

		return DEI_IsEnabled

	def cmdDeiEnable_wr( self, status ):
		cmd = Command(0x1403, self.tx_header)
		cmd.put_int(1, status)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DEI_ENABLE"):
			return False

		return True

	def cmdDeiIntStr_rd( self ):
		cmd = Command(0x1405, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DEI_INTER_STREN"):
			return False
		DEI_GetIntraFieldInterpolationStrength = response.get_int(1)

		return DEI_GetIntraFieldInterpolationStrength

	def cmdDeiIntStr_wr( self, strength ):
		cmd = Command(0x1405, self.tx_header)
		cmd.put_int(1, strength)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DEI_INTER_STREN"):
			return False

		return True

	def cmdDeiMMode_rd( self ):
		cmd = Command(0x1406, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DEI_MOTION_MODE"):
			return False
		mode = response.get_int(1)

		return mode

	def cmdDeiMMode_wr( self, mode ):
		cmd = Command(0x1406, self.tx_header)
		cmd.put_int(1, mode)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DEI_MOTION_MODE"):
			return False

		return True

	def cmdDeiRegionEn_rd( self ):
		cmd = Command(0x1407, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DEI_REGION_ENABLE"):
			return False
		Region_Enable = response.get_int(1)

		return Region_Enable

	def cmdDeiRegionEn_wr( self, enable ):
		cmd = Command(0x1407, self.tx_header)
		cmd.put_int(1, enable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DEI_REGION_ENABLE"):
			return False

		return True

	def cmdDeiRegionArea_rd( self ):
		cmd = Command(0x1408, self.tx_header)
		response = cmd.read(self.phy, 8)
		if not utils.check_response_and_print_error(response, False, "DEI_REGION_AREA"):
			return False
		FilmRegion_FirstPixel = response.get_int(2)
		FilmRegion_FirstLine = response.get_int(2)
		FilmRegion_PixelsPerLine = response.get_int(2)
		FilmRegion_LinesPerFrame = response.get_int(2)

		return FilmRegion_FirstPixel, FilmRegion_FirstLine, FilmRegion_PixelsPerLine, FilmRegion_LinesPerFrame

	def cmdDeiRegionArea_wr( self, FilmRegion_FirstPixel, FilmRegion_FirstLine, FilmRegion_PixelsPerLine, FilmRegion_LinesPerFrame ):
		cmd = Command(0x1408, self.tx_header)
		cmd.put_int(2, FilmRegion_FirstPixel)
		cmd.put_int(2, FilmRegion_FirstLine)
		cmd.put_int(2, FilmRegion_PixelsPerLine)
		cmd.put_int(2, FilmRegion_LinesPerFrame)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DEI_REGION_AREA"):
			return False

		return True

	def cmdDeiSetUserInterpolationStrength_rd( self ):
		cmd = Command(0x1409, self.tx_header)
		response = cmd.read(self.phy, 16)
		if not utils.check_response_and_print_error(response, False, "USER_INTERPOLATION_STRENGTH"):
			return False
		UserInterpolationStrength_strength_0 = response.get_int(1)
		UserInterpolationStrength_strength_1 = response.get_int(1)
		UserInterpolationStrength_strength_2 = response.get_int(1)
		UserInterpolationStrength_strength_3 = response.get_int(1)
		UserInterpolationStrength_strength_4 = response.get_int(1)
		UserInterpolationStrength_strength_5 = response.get_int(1)
		UserInterpolationStrength_strength_6 = response.get_int(1)
		UserInterpolationStrength_strength_7 = response.get_int(1)
		UserInterpolationStrength_strength_8 = response.get_int(1)
		UserInterpolationStrength_strength_9 = response.get_int(1)
		UserInterpolationStrength_strength_10 = response.get_int(1)
		UserInterpolationStrength_strength_11 = response.get_int(1)
		UserInterpolationStrength_strength_12 = response.get_int(1)
		UserInterpolationStrength_strength_13 = response.get_int(1)
		UserInterpolationStrength_strength_14 = response.get_int(1)
		UserInterpolationStrength_strength_15 = response.get_int(1)

		return UserInterpolationStrength_strength_0, UserInterpolationStrength_strength_1, UserInterpolationStrength_strength_2, UserInterpolationStrength_strength_3, UserInterpolationStrength_strength_4, UserInterpolationStrength_strength_5, UserInterpolationStrength_strength_6, UserInterpolationStrength_strength_7, UserInterpolationStrength_strength_8, UserInterpolationStrength_strength_9, UserInterpolationStrength_strength_10, UserInterpolationStrength_strength_11, UserInterpolationStrength_strength_12, UserInterpolationStrength_strength_13, UserInterpolationStrength_strength_14, UserInterpolationStrength_strength_15

	def cmdDeiSetUserInterpolationStrength_wr( self, UserInterpolationStrength_strength_0, UserInterpolationStrength_strength_1, UserInterpolationStrength_strength_2, UserInterpolationStrength_strength_3, UserInterpolationStrength_strength_4, UserInterpolationStrength_strength_5, UserInterpolationStrength_strength_6, UserInterpolationStrength_strength_7, UserInterpolationStrength_strength_8, UserInterpolationStrength_strength_9, UserInterpolationStrength_strength_10, UserInterpolationStrength_strength_11, UserInterpolationStrength_strength_12, UserInterpolationStrength_strength_13, UserInterpolationStrength_strength_14, UserInterpolationStrength_strength_15 ):
		cmd = Command(0x1409, self.tx_header)
		cmd.put_int(1, UserInterpolationStrength_strength_0)
		cmd.put_int(1, UserInterpolationStrength_strength_1)
		cmd.put_int(1, UserInterpolationStrength_strength_2)
		cmd.put_int(1, UserInterpolationStrength_strength_3)
		cmd.put_int(1, UserInterpolationStrength_strength_4)
		cmd.put_int(1, UserInterpolationStrength_strength_5)
		cmd.put_int(1, UserInterpolationStrength_strength_6)
		cmd.put_int(1, UserInterpolationStrength_strength_7)
		cmd.put_int(1, UserInterpolationStrength_strength_8)
		cmd.put_int(1, UserInterpolationStrength_strength_9)
		cmd.put_int(1, UserInterpolationStrength_strength_10)
		cmd.put_int(1, UserInterpolationStrength_strength_11)
		cmd.put_int(1, UserInterpolationStrength_strength_12)
		cmd.put_int(1, UserInterpolationStrength_strength_13)
		cmd.put_int(1, UserInterpolationStrength_strength_14)
		cmd.put_int(1, UserInterpolationStrength_strength_15)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "USER_INTERPOLATION_STRENGTH"):
			return False

		return True

	def cmdDeiEnableMotionDetectionInChroma_rd( self ):
		cmd = Command(0x140A, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "CHROMA_DILATION"):
			return False
		enable = response.get_int(1)

		return enable

	def cmdDeiEnableMotionDetectionInChroma_wr( self, enable ):
		cmd = Command(0x140A, self.tx_header)
		cmd.put_int(1, enable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "CHROMA_DILATION"):
			return False

		return True

	def CMD_GetUartConfig( self, uPort ):
		cmd = Command(0x1500, self.tx_header)
		cmd.put_int(1, uPort)
		response = cmd.read(self.phy, 10)
		if not utils.check_response_and_print_error(response, False, "UART_CONFIG"):
			return False
		uConfig = []
		uConfig += response.get_arr(10)

		return uConfig

	def CMD_SetUartConfig( self, uPort, uConfig_PortEnable, uConfig_BaudRate, uConfig_DataBits, uConfig_StopBits, uConfig_Parity, uConfig_FlowControl, uConfig_RxTrigLevel, uConfig_TxTrigLevel, uConfig_RxDataPolarity, uConfig_RxDataSource ):
		cmd = Command(0x1500, self.tx_header)
		cmd.put_int(1, uPort)
		cmd.put_int(1, uConfig_PortEnable)
		cmd.put_int(1, uConfig_BaudRate)
		cmd.put_int(1, uConfig_DataBits)
		cmd.put_int(1, uConfig_StopBits)
		cmd.put_int(1, uConfig_Parity)
		cmd.put_int(1, uConfig_FlowControl)
		cmd.put_int(1, uConfig_RxTrigLevel)
		cmd.put_int(1, uConfig_TxTrigLevel)
		cmd.put_int(1, uConfig_RxDataPolarity)
		cmd.put_int(1, uConfig_RxDataSource)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "UART_CONFIG"):
			return False

		return True

	def cmdDM365_EnableAutoUpdate( self, enable ):
		cmd = Command(0x1509, self.tx_header)
		cmd.put_int(1, enable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "UART_DM365_AUTOUPDATE"):
			return False

		return True

	def cmdDB_Enable_rd( self ):
		cmd = Command(0x1600, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DB_ENABLE"):
			return False
		Enabled = response.get_int(1)

		return Enabled

	def cmdDB_Enable_wr( self, Enable ):
		cmd = Command(0x1600, self.tx_header)
		cmd.put_int(1, Enable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DB_ENABLE"):
			return False

		return True

	def cmdDB_AperturePos_rd( self ):
		cmd = Command(0x1601, self.tx_header)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "DB_APERTURE"):
			return False
		position = response.get_int(2)

		return position

	def cmdDB_AperturePos_wr( self, position ):
		cmd = Command(0x1601, self.tx_header)
		cmd.put_int(2, position)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DB_APERTURE"):
			return False

		return True

	def cmdDB_Init_wr( self ):
		cmd = Command(0x1602, self.tx_header)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DB_INIT"):
			return False

		return True

	def cmdDB_IsPresent_rd( self ):
		cmd = Command(0x1603, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DB_ISPRESENT"):
			return False
		present = response.get_int(1)

		return present

	def cmdDB_ApertureMinMax_rd( self ):
		cmd = Command(0x1604, self.tx_header)
		response = cmd.read(self.phy, 4)
		if not utils.check_response_and_print_error(response, False, "DB_APERTURE_MIN_MAX"):
			return False
		AptMin = response.get_int(2)
		AptMax = response.get_int(2)

		return AptMin, AptMax

	def cmdDB_ApertureMinMax_wr( self, AptMin, AptMax ):
		cmd = Command(0x1604, self.tx_header)
		cmd.put_int(2, AptMin)
		cmd.put_int(2, AptMax)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DB_APERTURE_MIN_MAX"):
			return False

		return True

	def cmdDB_Strength_rd( self ):
		cmd = Command(0x1605, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DB_STRENGTH"):
			return False
		Strength = response.get_int(1)

		return Strength

	def cmdDB_Strength_wr( self, Strength ):
		cmd = Command(0x1605, self.tx_header)
		cmd.put_int(1, Strength)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DB_STRENGTH"):
			return False

		return True

	def cmdDB_OperMode_rd( self ):
		cmd = Command(0x1606, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DB_OPERMODE"):
			return False
		mode = response.get_int(1)

		return mode

	def cmdDB_OperMode_wr( self, mode ):
		cmd = Command(0x1606, self.tx_header)
		cmd.put_int(1, mode)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DB_OPERMODE"):
			return False

		return True

	def cmdDB_ApertIndex_rd( self ):
		cmd = Command(0x1608, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DB_APERTUREINDEX"):
			return False
		idx = response.get_int(1)

		return idx

	def cmdDB_ApertIndex_wr( self, idx ):
		cmd = Command(0x1608, self.tx_header)
		cmd.put_int(1, idx)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DB_APERTUREINDEX"):
			return False

		return True

	def cmdDB_NumSteps_rd( self ):
		cmd = Command(0x1609, self.tx_header)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "DB_NUMSTEPS"):
			return False
		Steps = response.get_int(2)

		return Steps

	def cmdDB_NumSteps_wr( self, Steps ):
		cmd = Command(0x1609, self.tx_header)
		cmd.put_int(2, Steps)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DB_NUMSTEPS"):
			return False

		return True

	def cmdDB_ClipPixels_rd( self ):
		cmd = Command(0x160A, self.tx_header)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "DB_CLIPPIXELS"):
			return False
		ClipPixels = response.get_int(2)

		return ClipPixels

	def cmdDB_ClipPixels_wr( self, ClipPixels ):
		cmd = Command(0x160A, self.tx_header)
		cmd.put_int(2, ClipPixels)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DB_CLIPPIXELS"):
			return False

		return True

	def cmdDB_ApertSpeed_rd( self ):
		cmd = Command(0x160B, self.tx_header)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "DB_APERTURESPEED"):
			return False
		Speed = response.get_int(2)

		return Speed

	def cmdDB_ApertSpeed_wr( self, Speed ):
		cmd = Command(0x160B, self.tx_header)
		cmd.put_int(2, Speed)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DB_APERTURESPEED"):
			return False

		return True

	def cmdDB_BorderConfig_rd( self ):
		cmd = Command(0x160C, self.tx_header)
		response = cmd.read(self.phy, 8)
		if not utils.check_response_and_print_error(response, False, "DB_BORDERCONFIG"):
			return False
		Top = response.get_int(2)
		Bottom = response.get_int(2)
		Left = response.get_int(2)
		Right = response.get_int(2)

		return Top, Bottom, Left, Right

	def cmdDB_BorderConfig_wr( self, Top, Bottom, Left, Right ):
		cmd = Command(0x160C, self.tx_header)
		cmd.put_int(2, Top)
		cmd.put_int(2, Bottom)
		cmd.put_int(2, Left)
		cmd.put_int(2, Right)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DB_BORDERCONFIG"):
			return False

		return True

	def cmdDB_BorderWeight_rd( self ):
		cmd = Command(0x160D, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DB_BORDERWEIGHT"):
			return False
		BorderWeight = response.get_int(1)

		return BorderWeight

	def cmdDB_BorderWeight_wr( self, BorderWeight ):
		cmd = Command(0x160D, self.tx_header)
		cmd.put_int(1, BorderWeight)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DB_BORDERWEIGHT"):
			return False

		return True

	def cmdDB_Gain_rd( self ):
		cmd = Command(0x160E, self.tx_header)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "DB_GAIN"):
			return False
		Gain = response.get_int(2)

		return Gain

	def cmdDB_Gain_wr( self, DBgain ):
		cmd = Command(0x160E, self.tx_header)
		cmd.put_int(2, DBgain)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DB_GAIN"):
			return False

		return True

	def cmdDB_ManualMode_wr( self, enable ):
		cmd = Command(0x160F, self.tx_header)
		cmd.put_int(1, enable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DB_MANMODE"):
			return False

		return True

	def cmdDB_Histogram_rd( self ):
		cmd = Command(0x1610, self.tx_header)
		response = cmd.read(self.phy, 136)
		if not utils.check_response_and_print_error(response, False, "DB_HISTOGRAM"):
			return False
		HistPtr = []
		HistPtr += response.get_arr(136)

		return HistPtr

	def cmdDB_PWMPort_rd( self ):
		cmd = Command(0x1611, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "DB_PWMPORT"):
			return False
		DB_GetPWMPortUsed = response.get_int(1)

		return DB_GetPWMPortUsed

	def cmdDB_PWMPort_wr( self, port ):
		cmd = Command(0x1611, self.tx_header)
		cmd.put_int(1, port)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DB_PWMPORT"):
			return False

		return True

	def cmdDB_OpenCloseApert_wr( self, open ):
		cmd = Command(0x1613, self.tx_header)
		cmd.put_int(1, open)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "DB_OPENCLOSEAPERTURE"):
			return False

		return True

	def cmdDB_CurrentApertPos_rd( self ):
		cmd = Command(0x1614, self.tx_header)
		response = cmd.read(self.phy, 4)
		if not utils.check_response_and_print_error(response, False, "DB_CURRENTAPERTPOS"):
			return False
		position = response.get_int(4)

		return position

	def CMD_GetGpioPinCfg( self, pin ):
		cmd = Command(0x1701, self.tx_header)
		cmd.put_int(1, pin)
		response = cmd.read(self.phy, 3)
		if not utils.check_response_and_print_error(response, False, "CONFIG_PIN"):
			return False
		dir = response.get_int(1)
		state = response.get_int(1)
		odrain = response.get_int(1)

		return dir, state, odrain

	#Function parsing failed
	def CMD_GetGpioPinName( ):
		return False

	def CMD_SetGpioPinCfg( self, pin, dir, state, odrain ):
		cmd = Command(0x1701, self.tx_header)
		cmd.put_int(1, pin)
		cmd.put_int(1, dir)
		cmd.put_int(1, state)
		cmd.put_int(1, odrain)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "CONFIG_PIN"):
			return False

		return True

	def cmdGPIOX_Cfg_rd( self, pin ):
		cmd = Command(0x1702, self.tx_header)
		cmd.put_int(1, pin)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "CONFIG_XPIN"):
			return False
		test = response.get_int(1)
		test = response.get_int(1)

		return test, test

	def cmdGPIOX_Cfg_wr( self, pin, out, val ):
		cmd = Command(0x1702, self.tx_header)
		cmd.put_int(1, pin)
		cmd.put_int(1, out)
		cmd.put_int(1, val)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "CONFIG_XPIN"):
			return False

		return True

	def CMD_SetGpioCfgReg( self, Iod_Bits_31_0, Iod_Bits_63_32, Iod_Bits_95_64, Lv_Bits_31_0, Lv_Bits_63_32, Lv_Bits_95_64, Od_Bits_31_0, Od_Bits_63_32, Od_Bits_95_64 ):
		cmd = Command(0x1703, self.tx_header)
		cmd.put_int(4, Iod_Bits_31_0)
		cmd.put_int(4, Iod_Bits_63_32)
		cmd.put_int(4, Iod_Bits_95_64)
		cmd.put_int(4, Lv_Bits_31_0)
		cmd.put_int(4, Lv_Bits_63_32)
		cmd.put_int(4, Lv_Bits_95_64)
		cmd.put_int(4, Od_Bits_31_0)
		cmd.put_int(4, Od_Bits_63_32)
		cmd.put_int(4, Od_Bits_95_64)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "CONFIG_REG"):
			return False

		return True

	def CMD_GetGpioCfgReg( self ):
		cmd = Command(0x1703, self.tx_header)
		response = cmd.read(self.phy, 36)
		if not utils.check_response_and_print_error(response, False, "CONFIG_REG"):
			return False
		Iod_Bits_31_0 = response.get_int(4)
		Iod_Bits_63_32 = response.get_int(4)
		Iod_Bits_95_64 = response.get_int(4)
		Lv_Bits_31_0 = response.get_int(4)
		Lv_Bits_63_32 = response.get_int(4)
		Lv_Bits_95_64 = response.get_int(4)
		Od_Bits_31_0 = response.get_int(4)
		Od_Bits_63_32 = response.get_int(4)
		Od_Bits_95_64 = response.get_int(4)

		return Iod_Bits_31_0, Iod_Bits_63_32, Iod_Bits_95_64, Lv_Bits_31_0, Lv_Bits_63_32, Lv_Bits_95_64, Od_Bits_31_0, Od_Bits_63_32, Od_Bits_95_64

	def CMD_SetGpioPin( self, Pin, LogicValue ):
		cmd = Command(0x1704, self.tx_header)
		cmd.put_int(1, Pin)
		cmd.put_int(1, LogicValue)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "GPIO_SET_PIN"):
			return False

		return True

	def CMD_GetGpioPin( self, Pin ):
		cmd = Command(0x1704, self.tx_header)
		cmd.put_int(1, Pin)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "GPIO_SET_PIN"):
			return False
		LogicValue = response.get_int(1)

		return LogicValue

	def CMD_SetGpioPins( self, Sp_Bits_31_0, Sp_Bits_63_32, Sp_Bits_95_64, Bp_Bits_31_0, Bp_Bits_63_32, Bp_Bits_95_64 ):
		cmd = Command(0x1705, self.tx_header)
		cmd.put_int(4, Sp_Bits_31_0)
		cmd.put_int(4, Sp_Bits_63_32)
		cmd.put_int(4, Sp_Bits_95_64)
		cmd.put_int(4, Bp_Bits_31_0)
		cmd.put_int(4, Bp_Bits_63_32)
		cmd.put_int(4, Bp_Bits_95_64)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "GPIO_SET_PINS"):
			return False

		return True

	def CMD_GetGpioPins( self, Sp_Bits_31_0, Sp_Bits_63_32, Sp_Bits_95_64 ):
		cmd = Command(0x1705, self.tx_header)
		cmd.put_int(4, Sp_Bits_31_0)
		cmd.put_int(4, Sp_Bits_63_32)
		cmd.put_int(4, Sp_Bits_95_64)
		response = cmd.read(self.phy, 12)
		if not utils.check_response_and_print_error(response, False, "GPIO_SET_PINS"):
			return False
		Bp_Bits_31_0 = response.get_int(4)
		Bp_Bits_63_32 = response.get_int(4)
		Bp_Bits_95_64 = response.get_int(4)

		return Bp_Bits_31_0, Bp_Bits_63_32, Bp_Bits_95_64

	def cmdGPIO_SetConsPin_wr( self, Start_Pin, Total_Pins, Bp_Bits_31_0, Bp_Bits_63_32, Bp_Bits_95_64 ):
		cmd = Command(0x1706, self.tx_header)
		cmd.put_int(1, Start_Pin)
		cmd.put_int(1, Total_Pins)
		cmd.put_int(4, Bp_Bits_31_0)
		cmd.put_int(4, Bp_Bits_63_32)
		cmd.put_int(4, Bp_Bits_95_64)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "GPIO_SET_CONS_PIN"):
			return False

		return True

	def cmdGPIO_GetConsPin_rd( self, Start_Pin, Total_Pins ):
		cmd = Command(0x1706, self.tx_header)
		cmd.put_int(1, Start_Pin)
		cmd.put_int(1, Total_Pins)
		response = cmd.read(self.phy, 12)
		if not utils.check_response_and_print_error(response, False, "GPIO_SET_CONS_PIN"):
			return False
		Bp_Bits_31_0 = response.get_int(4)
		Bp_Bits_63_32 = response.get_int(4)
		Bp_Bits_95_64 = response.get_int(4)

		return Bp_Bits_31_0, Bp_Bits_63_32, Bp_Bits_95_64

	def CMD_SetGpioIntSrc( self, INT_Src, Pin ):
		cmd = Command(0x1707, self.tx_header)
		cmd.put_int(1, INT_Src)
		cmd.put_int(1, Pin)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "GPIO_SET_INT_SRC"):
			return False

		return True

	def CMD_GetGpioIntSrc( self, INT_Src ):
		cmd = Command(0x1707, self.tx_header)
		cmd.put_int(1, INT_Src)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "GPIO_SET_INT_SRC"):
			return False
		Pin = response.get_int(1)

		return Pin

	def CMD_GetGpioEnable( self, Pin ):
		cmd = Command(0x1708, self.tx_header)
		cmd.put_int(1, Pin)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "GPIO_ENABLE"):
			return False
		Enable = response.get_int(1)
		Alternate_1_2 = response.get_int(1)

		return Enable, Alternate_1_2

	def CMD_GpioEnableAltFunc( self, Function, Enable ):
		cmd = Command(0x1709, self.tx_header)
		cmd.put_int(1, Function)
		cmd.put_int(1, Enable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "GPIO_ENABLE_ALT"):
			return False

		return True

	def cmdGPIO_SetUSBPin_wr( self ):
		cmd = Command(0x170B, self.tx_header)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "GPIO_SET_USB_PIN"):
			return False

		return True

	def cmdGPIO_GetUSBPin_rd( self ):
		cmd = Command(0x170B, self.tx_header)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "GPIO_SET_USB_PIN"):
			return False

		return True

	def CMD_SetGpioIntEnable( self, Enable, IntNum ):
		cmd = Command(0x170C, self.tx_header)
		cmd.put_int(1, Enable)
		cmd.put_int(1, IntNum)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "GPIO_ENABLE_INT"):
			return False

		return True

	def CMD_GetGpioIntEnable( self, IntNum ):
		cmd = Command(0x170C, self.tx_header)
		cmd.put_int(1, IntNum)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "GPIO_ENABLE_INT"):
			return False
		GPIO_GetEnableInterrupt = response.get_int(1)

		return GPIO_GetEnableInterrupt

	def CMD_SetGpioIntCfg( self, INT_Src, Trig_Type, Trig_Polarity ):
		cmd = Command(0x170D, self.tx_header)
		cmd.put_int(1, INT_Src)
		cmd.put_int(1, Trig_Type)
		cmd.put_int(1, Trig_Polarity)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "GPIO_SET_INT_CFG"):
			return False

		return True

	def CMD_GetGpioIntCfg( self, INT_Src ):
		cmd = Command(0x170D, self.tx_header)
		cmd.put_int(1, INT_Src)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "GPIO_SET_INT_CFG"):
			return False
		Trig_Type = response.get_int(1)
		Trig_Polarity = response.get_int(1)

		return Trig_Type, Trig_Polarity

	def CMD_GetGpioIntStatus( self, IntSrc ):
		cmd = Command(0x170E, self.tx_header)
		cmd.put_int(1, IntSrc)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "GPIO_GET_INT_STATUS"):
			return False
		GPIO_GetIntStatus = response.get_int(1)

		return GPIO_GetIntStatus

	def cmdGdlRamInit_wr( self, begin ):
		cmd = Command(0x1800, self.tx_header)
		cmd.put_int(1, begin)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "GDL_RAMINIT"):
			return False

		return True

	#Function parsing failed
	def cmdGdlRamData_wr( ):
		return False

	def cmdGdlRamLoad_wr( self ):
		cmd = Command(0x1802, self.tx_header)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "GDL_RAMLOAD"):
			return False

		return True

	def cmdGdlRestore_wr( self ):
		cmd = Command(0x1804, self.tx_header)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "GDL_RESTORE"):
			return False

		return True

	def cmdGdlFromInit_wr( self ):
		cmd = Command(0x1810, self.tx_header)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "GDL_FROMINIT"):
			return False

		return True

	#Function parsing failed
	def cmdGdlFromData_wr( ):
		return False

	def cmdGdlFromLoad_wr( self, index ):
		cmd = Command(0x1812, self.tx_header)
		cmd.put_int(1, index)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "GDL_FROMLOAD"):
			return False

		return True

	#Function parsing failed
	def cmdGdlFromID_rd( ):
		return False

	def CMD_GetPwmOutCfg( self, Port ):
		cmd = Command(0x1900, self.tx_header)
		cmd.put_int(1, Port)
		response = cmd.read(self.phy, 6)
		if not utils.check_response_and_print_error(response, False, "PWM_OUTCFG"):
			return False
		ConfigData_FreqHz = response.get_int(4)
		ConfigData_DutyCycle = response.get_int(1)
		ConfigData_OutputEnabled = response.get_int(1)

		return ConfigData_FreqHz, ConfigData_DutyCycle, ConfigData_OutputEnabled

	def CMD_SetPwmOutCfg( self, Port, ConfigData_FreqHz, ConfigData_DutyCycle, ConfigData_OutputEnabled ):
		cmd = Command(0x1900, self.tx_header)
		cmd.put_int(1, Port)
		cmd.put_int(4, ConfigData_FreqHz)
		cmd.put_int(1, ConfigData_DutyCycle)
		cmd.put_int(1, ConfigData_OutputEnabled)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "PWM_OUTCFG"):
			return False

		return True

	def CMD_GetPwmInCfg( self, Port ):
		cmd = Command(0x1901, self.tx_header)
		cmd.put_int(1, Port)
		response = cmd.read(self.phy, 10)
		if not utils.check_response_and_print_error(response, False, "PWM_INCFG"):
			return False
		ConfigData_SampleRate = response.get_int(4)
		ConfigData_InCounterEnabled = response.get_int(1)
		hi = response.get_int(2)
		lo = response.get_int(2)
		dc = response.get_int(1)

		return ConfigData_SampleRate, ConfigData_InCounterEnabled, hi, lo, dc

	def CMD_SetPwmInCfg( self, Port, ConfigData_SampleRate, ConfigData_InCounterEnabled ):
		cmd = Command(0x1901, self.tx_header)
		cmd.put_int(1, Port)
		cmd.put_int(4, ConfigData_SampleRate)
		cmd.put_int(1, ConfigData_InCounterEnabled)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "PWM_INCFG"):
			return False

		return True

	def cmdSplashCaptureStatus_rd( self ):
		cmd = Command(0x2102, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "SPLASH_CAPTURE_STATUS"):
			return False
		capture_status = response.get_int(1)

		return capture_status

	def cmdSplashLoadImage_wr( self, SplashLoadType, address0, address1 ):
		cmd = Command(0x2100, self.tx_header)
		cmd.put_int(1, SplashLoadType)
		cmd.put_int(4, address0)
		cmd.put_int(4, address1)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "SPLASH_LOADIMAGE"):
			return False

		return True

	def cmdSplashCapture_wr( self, SplashCaptureAddress, Splash_Store_Immediate, SPLASH_Compression, SPLASH_CaptureFormat, capture_3d ):
		cmd = Command(0x2101, self.tx_header)
		cmd.put_int(4, SplashCaptureAddress)
		cmd.put_int(1, Splash_Store_Immediate)
		cmd.put_int(1, SPLASH_Compression)
		cmd.put_int(1, SPLASH_CaptureFormat)
		cmd.put_int(1, capture_3d)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "SPLASH_CAPTURE"):
			return False

		return True

	def cmdBC_PreviewINIT_wr( self ):
		cmd = Command(0xFE00, self.tx_header)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "BC_PREVIEW_INIT"):
			return False

		return True

	#Function parsing failed
	def cmdBC_Preview_wr( ):
		return False

	#Function parsing failed
	def cmdBC_Preview_rd( ):
		return False

	#Function parsing failed
	def cmdCMPSR_Passthru_wr( ):
		return False

	def cmdSspPassthru_rd( self, port, cs, read_cmd ):
		cmd = Command(0x2300, self.tx_header)
		cmd.put_int(1, port)
		cmd.put_int(1, cs)
		cmd.put_int(1, read_cmd)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "SSP_PASSTHRU"):
			return False
		data_from_ssp = response.get_int(1)

		return data_from_ssp

	def cmdSspPassthru_wr( self, port, cs, cmd_0, cmd_1 ):
		cmd = Command(0x2300, self.tx_header)
		cmd.put_int(1, port)
		cmd.put_int(1, cs)
		cmd.put_int(1, cmd_0)
		cmd.put_int(1, cmd_1)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "SSP_PASSTHRU"):
			return False

		return True

	def cmdEnable3D_wr( self, enable ):
		cmd = Command(0x2500, self.tx_header)
		cmd.put_int(1, enable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_3D_ENABLE"):
			return False

		return True

	def cmdEnable3D_rd( self ):
		cmd = Command(0x2500, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "_3D_ENABLE"):
			return False
		enabled = response.get_int(1)

		return enabled

	def cmdSrcConfig3D_wr( self, Src3DConfig_temp_Format, Src3DConfig_temp_LR_Reference, Src3DConfig_temp_FrameDominance, Src3DConfig_temp_LR_Encoding, Src3DConfig_temp_TB_Reference, Src3DConfig_temp_OE_Reference, Src3DConfig_temp_NumActiveBlankLines, Src3DConfig_temp_NumberOfEncodedLines, Src3DConfig_temp_LeftEncodedLineLocation, Src3DConfig_temp_RightEncodedLineLocation, Src3DConfig_temp_BlankingColor ):
		cmd = Command(0x2501, self.tx_header)
		cmd.put_int(1, Src3DConfig_temp_Format)
		cmd.put_int(1, Src3DConfig_temp_LR_Reference)
		cmd.put_int(1, Src3DConfig_temp_FrameDominance)
		cmd.put_int(1, Src3DConfig_temp_LR_Encoding)
		cmd.put_int(1, Src3DConfig_temp_TB_Reference)
		cmd.put_int(1, Src3DConfig_temp_OE_Reference)
		cmd.put_int(1, Src3DConfig_temp_NumActiveBlankLines)
		cmd.put_int(1, Src3DConfig_temp_NumberOfEncodedLines)
		cmd.put_int(2, Src3DConfig_temp_LeftEncodedLineLocation)
		cmd.put_int(2, Src3DConfig_temp_RightEncodedLineLocation)
		cmd.put_int(1, Src3DConfig_temp_BlankingColor)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_3D_SETSOURCECFG"):
			return False

		return True

	def cmdSrcConfig3D_rd( self ):
		cmd = Command(0x2501, self.tx_header)
		response = cmd.read(self.phy, 13)
		if not utils.check_response_and_print_error(response, False, "_3D_SETSOURCECFG"):
			return False
		Src3DConfig_Format = response.get_int(1)
		Src3DConfig_LR_Reference = response.get_int(1)
		Src3DConfig_FrameDominance = response.get_int(1)
		Src3DConfig_LR_Encoding = response.get_int(1)
		Src3DConfig_TB_Reference = response.get_int(1)
		Src3DConfig_OE_Reference = response.get_int(1)
		Src3DConfig_NumActiveBlankLines = response.get_int(1)
		Src3DConfig_NumberOfEncodedLines = response.get_int(1)
		Src3DConfig_LeftEncodedLineLocation = response.get_int(2)
		Src3DConfig_RightEncodedLineLocation = response.get_int(2)
		Src3DConfig_BlankingColor = response.get_int(1)

		return Src3DConfig_Format, Src3DConfig_LR_Reference, Src3DConfig_FrameDominance, Src3DConfig_LR_Encoding, Src3DConfig_TB_Reference, Src3DConfig_OE_Reference, Src3DConfig_NumActiveBlankLines, Src3DConfig_NumberOfEncodedLines, Src3DConfig_LeftEncodedLineLocation, Src3DConfig_RightEncodedLineLocation, Src3DConfig_BlankingColor

	def cmdSetRefPolarity3D_wr( self, Ref3D, OddEven, TopField, Invert ):
		cmd = Command(0x2502, self.tx_header)
		cmd.put_int(1, Ref3D)
		cmd.put_int(1, OddEven)
		cmd.put_int(1, TopField)
		cmd.put_int(1, Invert)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_3D_SETREFPOLARITY"):
			return False

		return True

	def cmdGetRefPolarity3D_rd( self ):
		cmd = Command(0x2502, self.tx_header)
		response = cmd.read(self.phy, 4)
		if not utils.check_response_and_print_error(response, False, "_3D_SETREFPOLARITY"):
			return False
		Ref3D = response.get_int(1)
		OddEven = response.get_int(1)
		TopField = response.get_int(1)
		Invert = response.get_int(1)

		return Ref3D, OddEven, TopField, Invert

	def cmdSetLRDisplay3D_wr( self, invert ):
		cmd = Command(0x2503, self.tx_header)
		cmd.put_int(1, invert)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_3D_SETLRDISPLAY"):
			return False

		return True

	def cmdGetLRDisplay3D_rd( self ):
		cmd = Command(0x2503, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "_3D_SETLRDISPLAY"):
			return False
		Invert = response.get_int(1)

		return Invert

	def cmdSetDetectConfig3D_wr( self, Src_3DDetectConfig_Format, Src_3DDetectConfig_LR_Encoding, Src_3DDetectConfig_NumFramesToDetect, Src_3DDetectConfig_NumFramesToLock, Src_3DDetectConfig_NumFramesToLoseLock, Src_3DDetectConfig_NumActiveBlankLines, Src_3DDetectConfig_NumberOfEncodedLines ):
		cmd = Command(0x2504, self.tx_header)
		cmd.put_int(1, Src_3DDetectConfig_Format)
		cmd.put_int(1, Src_3DDetectConfig_LR_Encoding)
		cmd.put_int(1, Src_3DDetectConfig_NumFramesToDetect)
		cmd.put_int(1, Src_3DDetectConfig_NumFramesToLock)
		cmd.put_int(1, Src_3DDetectConfig_NumFramesToLoseLock)
		cmd.put_int(1, Src_3DDetectConfig_NumActiveBlankLines)
		cmd.put_int(1, Src_3DDetectConfig_NumberOfEncodedLines)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_3D_SETDETECTCONFIG"):
			return False

		return True

	def cmdGetDetectConfig3D_rd( self ):
		cmd = Command(0x2504, self.tx_header)
		response = cmd.read(self.phy, 7)
		if not utils.check_response_and_print_error(response, False, "_3D_SETDETECTCONFIG"):
			return False
		Src_3DDetectConfig_Format = response.get_int(1)
		Src_3DDetectConfig_LR_Encoding = response.get_int(1)
		Src_3DDetectConfig_NumFramesToDetect = response.get_int(1)
		Src_3DDetectConfig_NumFramesToLock = response.get_int(1)
		Src_3DDetectConfig_NumFramesToLoseLock = response.get_int(1)
		Src_3DDetectConfig_NumActiveBlankLines = response.get_int(1)
		Src_3DDetectConfig_NumberOfEncodedLines = response.get_int(1)

		return Src_3DDetectConfig_Format, Src_3DDetectConfig_LR_Encoding, Src_3DDetectConfig_NumFramesToDetect, Src_3DDetectConfig_NumFramesToLock, Src_3DDetectConfig_NumFramesToLoseLock, Src_3DDetectConfig_NumActiveBlankLines, Src_3DDetectConfig_NumberOfEncodedLines

	def cmdSet3DDetectEnable3D_wr( self, enable ):
		cmd = Command(0x2505, self.tx_header)
		cmd.put_int(1, enable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_3D_ENABLEDETECTION"):
			return False

		return True

	def cmdGet3DDetectEnable3D_rd( self ):
		cmd = Command(0x2505, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "_3D_ENABLEDETECTION"):
			return False
		enabled = response.get_int(1)

		return enabled

	def cmdSetSignature3D_wr( self, Src_3DSignature_LeftEyeColor, Src_3DSignature_RightEyeColor, Src_3DSignature_UseAlternatingPattern, Src_3DSignature_SecondLeftEyeColor, Src_3DSignature_SecondRightEyeColor, Src_3DSignature_ResultThresholdPct, Src_3DSignature_UpperColorLimit, Src_3DSignature_LowerColorLimit ):
		cmd = Command(0x2506, self.tx_header)
		cmd.put_int(1, Src_3DSignature_LeftEyeColor)
		cmd.put_int(1, Src_3DSignature_RightEyeColor)
		cmd.put_int(1, Src_3DSignature_UseAlternatingPattern)
		cmd.put_int(1, Src_3DSignature_SecondLeftEyeColor)
		cmd.put_int(1, Src_3DSignature_SecondRightEyeColor)
		cmd.put_int(1, Src_3DSignature_ResultThresholdPct)
		cmd.put_int(2, Src_3DSignature_UpperColorLimit)
		cmd.put_int(2, Src_3DSignature_LowerColorLimit)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_3D_SETSIGNATURE"):
			return False

		return True

	def cmdGetSignature3D_rd( self ):
		cmd = Command(0x2506, self.tx_header)
		response = cmd.read(self.phy, 10)
		if not utils.check_response_and_print_error(response, False, "_3D_SETSIGNATURE"):
			return False
		Src_3DSignature_LeftEyeColor = response.get_int(1)
		Src_3DSignature_RightEyeColor = response.get_int(1)
		Src_3DSignature_UseAlternatingPattern = response.get_int(1)
		Src_3DSignature_SecondLeftEyeColor = response.get_int(1)
		Src_3DSignature_SecondRightEyeColor = response.get_int(1)
		Src_3DSignature_ResultThresholdPct = response.get_int(1)
		Src_3DSignature_UpperColorLimit = response.get_int(2)
		Src_3DSignature_LowerColorLimit = response.get_int(2)

		return Src_3DSignature_LeftEyeColor, Src_3DSignature_RightEyeColor, Src_3DSignature_UseAlternatingPattern, Src_3DSignature_SecondLeftEyeColor, Src_3DSignature_SecondRightEyeColor, Src_3DSignature_ResultThresholdPct, Src_3DSignature_UpperColorLimit, Src_3DSignature_LowerColorLimit

	def cmdInitDetect3D_wr( self ):
		cmd = Command(0x2507, self.tx_header)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_3D_INITDETECT"):
			return False

		return True

	def cmdEnableDisplay3D_wr( self, Enable ):
		cmd = Command(0x2508, self.tx_header)
		cmd.put_int(1, Enable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_3D_ENABLEDISPLAY"):
			return False

		return True

	def cmdGetStatus3D_rd( self ):
		cmd = Command(0x250A, self.tx_header)
		response = cmd.read(self.phy, 10)
		if not utils.check_response_and_print_error(response, False, "_3D_GETDETECTSTATUS"):
			return False
		Status_VSync_Cnt = response.get_int(2)
		Status_TotalVSyncCnt = response.get_int(2)
		Status_DetectCurrState = response.get_int(1)
		Status_LastDetectEvent = response.get_int(1)
		Status_TaskTimeInUsec = response.get_int(4)

		return Status_VSync_Cnt, Status_TotalVSyncCnt, Status_DetectCurrState, Status_LastDetectEvent, Status_TaskTimeInUsec

	def cmdGetMaxSample3D_rd( self ):
		cmd = Command(0x250B, self.tx_header)
		response = cmd.read(self.phy, 12)
		if not utils.check_response_and_print_error(response, False, "_3D_GETMAXRGBSAMPLE"):
			return False
		MaxRed = response.get_int(2)
		MaxGreen = response.get_int(2)
		MaxBlue = response.get_int(2)
		Dummy = response.get_int(2)
		Dummy = response.get_int(2)
		Dummy = response.get_int(2)

		return MaxRed, MaxGreen, MaxBlue, Dummy, Dummy, Dummy

	def cmdDisableDLPLinkPulse3D_wr( self, Enable ):
		cmd = Command(0x250C, self.tx_header)
		cmd.put_int(1, Enable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_3D_DISABLEDLPLINK"):
			return False

		return True

	def cmdDisableDLPLinkPulse3D_rd( self ):
		cmd = Command(0x250C, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "_3D_DISABLEDLPLINK"):
			return False
		Enabled = response.get_int(1)

		return Enabled

	def cmdViewingMode3D_wr( self, mode ):
		cmd = Command(0x250D, self.tx_header)
		cmd.put_int(1, mode)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_3D_VIEWINGMODE"):
			return False

		return True

	def cmdViewingMode3D_rd( self ):
		cmd = Command(0x250D, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "_3D_VIEWINGMODE"):
			return False
		mode = response.get_int(1)

		return mode

	def cmdAPIEventMessagesEna3D_wr( self, enable ):
		cmd = Command(0x250E, self.tx_header)
		cmd.put_int(1, enable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_3D_EVT_MSGS"):
			return False

		return True

	def cmdAPIEventMessagesEna3D_rd( self ):
		cmd = Command(0x250E, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "_3D_EVT_MSGS"):
			return False
		Enabled = response.get_int(1)

		return Enabled

	def cmdAPIDebugMessagesEna3D_wr( self, enable ):
		cmd = Command(0x250F, self.tx_header)
		cmd.put_int(1, enable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_3D_API_MSGS"):
			return False

		return True

	def cmdAPIDebugMessagesEna3D_rd( self ):
		cmd = Command(0x250F, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "_3D_API_MSGS"):
			return False
		Enabled = response.get_int(1)

		return Enabled

	def cmdSSIReadDriverInfo_rd( self ):
		cmd = Command(0x2600, self.tx_header)
		response = cmd.read(self.phy, 12)
		if not utils.check_response_and_print_error(response, False, "_SSI_GETDRIVERINFO"):
			return False
		SPI_DriverID_ManufacturerID = response.get_int(1)
		SPI_DriverID_HardwareID = response.get_int(1)
		SPI_DriverID_FirmwareID = response.get_int(1)
		SPI_DriverID_Type = response.get_int(1)
		SPI_DriverID_ManufacturerID = response.get_int(1)
		SPI_DriverID_HardwareID = response.get_int(1)
		SPI_DriverID_FirmwareID = response.get_int(1)
		SPI_DriverID_Type = response.get_int(1)
		SPI_DriverID_ManufacturerID = response.get_int(1)
		SPI_DriverID_HardwareID = response.get_int(1)
		SPI_DriverID_FirmwareID = response.get_int(1)
		SPI_DriverID_Type = response.get_int(1)

		return SPI_DriverID_ManufacturerID, SPI_DriverID_HardwareID, SPI_DriverID_FirmwareID, SPI_DriverID_Type, SPI_DriverID_ManufacturerID, SPI_DriverID_HardwareID, SPI_DriverID_FirmwareID, SPI_DriverID_Type, SPI_DriverID_ManufacturerID, SPI_DriverID_HardwareID, SPI_DriverID_FirmwareID, SPI_DriverID_Type

	def cmdSSISetRedCurrents_wr( self, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_RED_CHANNEL_RedDriveLevel, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_RED_CHANNEL_GreenDriveLevel, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_RED_CHANNEL_BlueDriveLevel, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_RED_CHANNEL_Sample1DriveLevel, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_RED_CHANNEL_Sample2DriveLevel, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_RED_CHANNEL_YellowDriveLevel, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_RED_CHANNEL_CyanDriveLevel, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_RED_CHANNEL_MagentaDriveLevel, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_RED_CHANNEL_WhiteDriveLevel, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_RED_CHANNEL_BlackDriveLevel ):
		cmd = Command(0x2601, self.tx_header)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_RED_CHANNEL_RedDriveLevel)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_RED_CHANNEL_GreenDriveLevel)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_RED_CHANNEL_BlueDriveLevel)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_RED_CHANNEL_Sample1DriveLevel)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_RED_CHANNEL_Sample2DriveLevel)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_RED_CHANNEL_YellowDriveLevel)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_RED_CHANNEL_CyanDriveLevel)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_RED_CHANNEL_MagentaDriveLevel)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_RED_CHANNEL_WhiteDriveLevel)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_RED_CHANNEL_BlackDriveLevel)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_SSI_SETREDCURRENT"):
			return False

		return True

	#Function parsing failed
	def cmdSSIGetRedCurrents_rd( ):
		return False

	def cmdSSISetGreenCurrents_wr( self, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_GREEN_CHANNEL_RedDriveLevel, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_GREEN_CHANNEL_GreenDriveLevel, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_GREEN_CHANNEL_BlueDriveLevel, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_GREEN_CHANNEL_Sample1DriveLevel, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_GREEN_CHANNEL_Sample2DriveLevel, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_GREEN_CHANNEL_YellowDriveLevel, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_GREEN_CHANNEL_CyanDriveLevel, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_GREEN_CHANNEL_MagentaDriveLevel, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_GREEN_CHANNEL_WhiteDriveLevel, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_GREEN_CHANNEL_BlackDriveLevel ):
		cmd = Command(0x2602, self.tx_header)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_GREEN_CHANNEL_RedDriveLevel)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_GREEN_CHANNEL_GreenDriveLevel)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_GREEN_CHANNEL_BlueDriveLevel)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_GREEN_CHANNEL_Sample1DriveLevel)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_GREEN_CHANNEL_Sample2DriveLevel)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_GREEN_CHANNEL_YellowDriveLevel)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_GREEN_CHANNEL_CyanDriveLevel)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_GREEN_CHANNEL_MagentaDriveLevel)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_GREEN_CHANNEL_WhiteDriveLevel)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_GREEN_CHANNEL_BlackDriveLevel)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_SSI_SETGREENCURRENT"):
			return False

		return True

	#Function parsing failed
	def cmdSSIGetGreenCurrents_rd( ):
		return False

	def cmdSSISetBlueCurrents_wr( self, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_BLUE_CHANNEL_RedDriveLevel, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_BLUE_CHANNEL_GreenDriveLevel, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_BLUE_CHANNEL_BlueDriveLevel, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_BLUE_CHANNEL_Sample1DriveLevel, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_BLUE_CHANNEL_Sample2DriveLevel, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_BLUE_CHANNEL_YellowDriveLevel, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_BLUE_CHANNEL_CyanDriveLevel, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_BLUE_CHANNEL_MagentaDriveLevel, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_BLUE_CHANNEL_WhiteDriveLevel, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_BLUE_CHANNEL_BlackDriveLevel ):
		cmd = Command(0x2603, self.tx_header)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_BLUE_CHANNEL_RedDriveLevel)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_BLUE_CHANNEL_GreenDriveLevel)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_BLUE_CHANNEL_BlueDriveLevel)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_BLUE_CHANNEL_Sample1DriveLevel)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_BLUE_CHANNEL_Sample2DriveLevel)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_BLUE_CHANNEL_YellowDriveLevel)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_BLUE_CHANNEL_CyanDriveLevel)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_BLUE_CHANNEL_MagentaDriveLevel)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_BLUE_CHANNEL_WhiteDriveLevel)
		cmd.put_int(2, DriveLevels_SPIDrivePacket_DriveLevel_SSI_DRV_COLOR_BLUE_CHANNEL_BlackDriveLevel)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_SSI_SETBLUECURRENT"):
			return False

		return True

	#Function parsing failed
	def cmdSSIGetBlueCurrents_rd( ):
		return False

	def cmdSSIGetDriverStatus_rd( self ):
		cmd = Command(0x2604, self.tx_header)
		response = cmd.read(self.phy, 3)
		if not utils.check_response_and_print_error(response, False, "_SSI_GETDRIVERSTATUS"):
			return False
		SPI_DriverStatus_Summary = response.get_int(1)
		SPI_DriverStatus_Summary = response.get_int(1)
		SPI_DriverStatus_Summary = response.get_int(1)

		return SPI_DriverStatus_Summary, SPI_DriverStatus_Summary, SPI_DriverStatus_Summary

	def cmdSSISetRedDriverTiming_wr( self, SPI_DriverTiming_Enable, SPI_DriverTiming_StrobeDelay, SPI_DriverTiming_StrobeOffset ):
		cmd = Command(0x2605, self.tx_header)
		cmd.put_int(1, SPI_DriverTiming_Enable)
		cmd.put_int(2, SPI_DriverTiming_StrobeDelay)
		cmd.put_int(1, SPI_DriverTiming_StrobeOffset)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_SSI_SETREDDRIVERTIMING"):
			return False

		return True

	def cmdSSIGetRedDriverTiming_rd( self ):
		cmd = Command(0x2605, self.tx_header)
		response = cmd.read(self.phy, 4)
		if not utils.check_response_and_print_error(response, False, "_SSI_SETREDDRIVERTIMING"):
			return False
		SPI_DriverTiming_Enable = response.get_int(1)
		SPI_DriverTiming_StrobeDelay = response.get_int(2)
		SPI_DriverTiming_StrobeOffset = response.get_int(1)

		return SPI_DriverTiming_Enable, SPI_DriverTiming_StrobeDelay, SPI_DriverTiming_StrobeOffset

	def cmdSSISetGreenDriverTiming_wr( self, SPI_DriverTiming_Enable, SPI_DriverTiming_StrobeDelay, SPI_DriverTiming_StrobeOffset ):
		cmd = Command(0x2606, self.tx_header)
		cmd.put_int(1, SPI_DriverTiming_Enable)
		cmd.put_int(2, SPI_DriverTiming_StrobeDelay)
		cmd.put_int(1, SPI_DriverTiming_StrobeOffset)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_SSI_SETGREENDRIVERTIMING"):
			return False

		return True

	def cmdSSIGetGreenDriverTiming_rd( self ):
		cmd = Command(0x2606, self.tx_header)
		response = cmd.read(self.phy, 4)
		if not utils.check_response_and_print_error(response, False, "_SSI_SETGREENDRIVERTIMING"):
			return False
		SPI_DriverTiming_Enable = response.get_int(1)
		SPI_DriverTiming_StrobeDelay = response.get_int(2)
		SPI_DriverTiming_StrobeOffset = response.get_int(1)

		return SPI_DriverTiming_Enable, SPI_DriverTiming_StrobeDelay, SPI_DriverTiming_StrobeOffset

	def cmdSSISetBlueDriverTiming_wr( self, SPI_DriverTiming_Enable, SPI_DriverTiming_StrobeDelay, SPI_DriverTiming_StrobeOffset ):
		cmd = Command(0x2607, self.tx_header)
		cmd.put_int(1, SPI_DriverTiming_Enable)
		cmd.put_int(2, SPI_DriverTiming_StrobeDelay)
		cmd.put_int(1, SPI_DriverTiming_StrobeOffset)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_SSI_SETBLUEDRIVERTIMING"):
			return False

		return True

	def cmdSSIGetBlueDriverTiming_rd( self ):
		cmd = Command(0x2607, self.tx_header)
		response = cmd.read(self.phy, 4)
		if not utils.check_response_and_print_error(response, False, "_SSI_SETBLUEDRIVERTIMING"):
			return False
		SPI_DriverTiming_Enable = response.get_int(1)
		SPI_DriverTiming_StrobeDelay = response.get_int(2)
		SPI_DriverTiming_StrobeOffset = response.get_int(1)

		return SPI_DriverTiming_Enable, SPI_DriverTiming_StrobeDelay, SPI_DriverTiming_StrobeOffset

	def cmdSSISetExtSensorXY_wr( self, EE_CalData_Red_x, EE_CalData_Red_y, EE_CalData_Red_L, EE_CalData_Green_x, EE_CalData_Green_y, EE_CalData_Green_L, EE_CalData_Blue_x, EE_CalData_Blue_y, EE_CalData_Blue_L, EE_CalData_C1_x, EE_CalData_C1_y, EE_CalData_C1_L, EE_CalData_C2_x, EE_CalData_C2_y, EE_CalData_C2_L, ExtValStoreToEEPROM ):
		cmd = Command(0x2608, self.tx_header)
		cmd.put_int(2, EE_CalData_Red_x)
		cmd.put_int(2, EE_CalData_Red_y)
		cmd.put_int(2, EE_CalData_Red_L)
		cmd.put_int(2, EE_CalData_Green_x)
		cmd.put_int(2, EE_CalData_Green_y)
		cmd.put_int(2, EE_CalData_Green_L)
		cmd.put_int(2, EE_CalData_Blue_x)
		cmd.put_int(2, EE_CalData_Blue_y)
		cmd.put_int(2, EE_CalData_Blue_L)
		cmd.put_int(2, EE_CalData_C1_x)
		cmd.put_int(2, EE_CalData_C1_y)
		cmd.put_int(2, EE_CalData_C1_L)
		cmd.put_int(2, EE_CalData_C2_x)
		cmd.put_int(2, EE_CalData_C2_y)
		cmd.put_int(2, EE_CalData_C2_L)
		cmd.put_int(1, ExtValStoreToEEPROM)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_SSI_SETEXTXY"):
			return False

		return True

	def cmdSSISetExtSensorXY_rd( self ):
		cmd = Command(0x2608, self.tx_header)
		response = cmd.read(self.phy, 31)
		if not utils.check_response_and_print_error(response, False, "_SSI_SETEXTXY"):
			return False
		cal_data_R_x = response.get_int(2)
		cal_data_R_y = response.get_int(2)
		cal_data_R_Y = response.get_int(2)
		cal_data_G_x = response.get_int(2)
		cal_data_G_y = response.get_int(2)
		cal_data_G_Y = response.get_int(2)
		cal_data_B_x = response.get_int(2)
		cal_data_B_y = response.get_int(2)
		cal_data_B_Y = response.get_int(2)
		cal_data_C1_x = response.get_int(2)
		cal_data_C1_y = response.get_int(2)
		cal_data_C1_Y = response.get_int(2)
		cal_data_C2_x = response.get_int(2)
		cal_data_C2_y = response.get_int(2)
		cal_data_C2_Y = response.get_int(2)
		ExtValStoreToEEPROM = response.get_int(1)

		return cal_data_R_x, cal_data_R_y, cal_data_R_Y, cal_data_G_x, cal_data_G_y, cal_data_G_Y, cal_data_B_x, cal_data_B_y, cal_data_B_Y, cal_data_C1_x, cal_data_C1_y, cal_data_C1_Y, cal_data_C2_x, cal_data_C2_y, cal_data_C2_Y, ExtValStoreToEEPROM

	def cmdSSIGetInternalSensorCal_wr( self, EE_CalData_Red_SensorValue, EE_CalData_Red_DriveLevel, EE_CalData_Green_SensorValue, EE_CalData_Green_DriveLevel, EE_CalData_Blue_SensorValue, EE_CalData_Blue_DriveLevel, EE_CalData_C1_SensorValue, EE_CalData_C1_DriveLevel, EE_CalData_C2_SensorValue, EE_CalData_C2_DriveLevel, IntValStoreToEEPROM ):
		cmd = Command(0x2609, self.tx_header)
		cmd.put_int(2, EE_CalData_Red_SensorValue)
		cmd.put_int(2, EE_CalData_Red_DriveLevel)
		cmd.put_int(2, EE_CalData_Green_SensorValue)
		cmd.put_int(2, EE_CalData_Green_DriveLevel)
		cmd.put_int(2, EE_CalData_Blue_SensorValue)
		cmd.put_int(2, EE_CalData_Blue_DriveLevel)
		cmd.put_int(2, EE_CalData_C1_SensorValue)
		cmd.put_int(2, EE_CalData_C1_DriveLevel)
		cmd.put_int(2, EE_CalData_C2_SensorValue)
		cmd.put_int(2, EE_CalData_C2_DriveLevel)
		cmd.put_int(1, IntValStoreToEEPROM)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_SSI_SETSENSORVALUECAL"):
			return False

		return True

	def cmdSSIGetInternalSensorCal_rd( self ):
		cmd = Command(0x2609, self.tx_header)
		response = cmd.read(self.phy, 21)
		if not utils.check_response_and_print_error(response, False, "_SSI_SETSENSORVALUECAL"):
			return False
		cal_data_R_S = response.get_int(2)
		cal_data_R_DriveLevel = response.get_int(2)
		cal_data_G_S = response.get_int(2)
		cal_data_G_DriveLevel = response.get_int(2)
		cal_data_B_S = response.get_int(2)
		cal_data_B_DriveLevel = response.get_int(2)
		cal_data_C1_S = response.get_int(2)
		cal_data_C1_DriveLevel = response.get_int(2)
		cal_data_C2_S = response.get_int(2)
		cal_data_C2_DriveLevel = response.get_int(2)
		IntValStoreToEEPROM = response.get_int(1)

		return cal_data_R_S, cal_data_R_DriveLevel, cal_data_G_S, cal_data_G_DriveLevel, cal_data_B_S, cal_data_B_DriveLevel, cal_data_C1_S, cal_data_C1_DriveLevel, cal_data_C2_S, cal_data_C2_DriveLevel, IntValStoreToEEPROM

	def cmdSSIGetInternalSensor_rd( self, IntSenseSubframe ):
		cmd = Command(0x260A, self.tx_header)
		cmd.put_int(1, IntSenseSubframe)
		response = cmd.read(self.phy, 11)
		if not utils.check_response_and_print_error(response, False, "_SSI_GETSENSORVALUE"):
			return False
		r = response.get_int(2)
		g = response.get_int(2)
		b = response.get_int(2)
		c1 = response.get_int(2)
		c2 = response.get_int(2)
		error = response.get_int(1)

		return r, g, b, c1, c2, error

	def cmdSSISetIntSensorTiming_wr( self, red_delay1, red_delay2, grn_delay2, blu_delay2, ylw_delay2, cyn_delay2 ):
		cmd = Command(0x260B, self.tx_header)
		cmd.put_int(2, red_delay1)
		cmd.put_int(2, red_delay2)
		cmd.put_int(2, grn_delay2)
		cmd.put_int(2, blu_delay2)
		cmd.put_int(2, ylw_delay2)
		cmd.put_int(2, cyn_delay2)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_SSI_SETSENSORTIMING"):
			return False

		return True

	def cmdSSISetIntSensorTiming_rd( self ):
		cmd = Command(0x260B, self.tx_header)
		response = cmd.read(self.phy, 13)
		if not utils.check_response_and_print_error(response, False, "_SSI_SETSENSORTIMING"):
			return False
		red_delay1 = response.get_int(2)
		red_delay2 = response.get_int(2)
		grn_delay2 = response.get_int(2)
		blu_delay2 = response.get_int(2)
		ylw_delay2 = response.get_int(2)
		cyn_delay2 = response.get_int(2)
		SensorType = response.get_int(1)

		return red_delay1, red_delay2, grn_delay2, blu_delay2, ylw_delay2, cyn_delay2, SensorType

	def cmdSSISetCCIMode_wr( self, Mode ):
		cmd = Command(0x260C, self.tx_header)
		cmd.put_int(1, Mode)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_SSI_CCIMODECONTROL"):
			return False

		return True

	def cmdSSISetCCIMode_rd( self ):
		cmd = Command(0x260C, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "_SSI_CCIMODECONTROL"):
			return False
		Mode = response.get_int(1)

		return Mode

	def cmdSSISetCCIEnable_wr( self, enable ):
		cmd = Command(0x260D, self.tx_header)
		cmd.put_int(1, enable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_SSI_CCIENABLECONTROL"):
			return False

		return True

	def cmdSSISetCCIEnable_rd( self ):
		cmd = Command(0x260D, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "_SSI_CCIENABLECONTROL"):
			return False
		Enable = response.get_int(1)

		return Enable

	def cmdSSISetPWMDriveLevels_wr( self, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelRed, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelGreen, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelBlue, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelC1, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelC2, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelSense ):
		cmd = Command(0x260E, self.tx_header)
		cmd.put_int(2, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelRed)
		cmd.put_int(2, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelGreen)
		cmd.put_int(2, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelBlue)
		cmd.put_int(2, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelC1)
		cmd.put_int(2, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelC2)
		cmd.put_int(2, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelSense)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_SSI_PWMDRIVELEVELS"):
			return False

		return True

	def cmdSSISetPWMDriveLevels_rd( self ):
		cmd = Command(0x260E, self.tx_header)
		response = cmd.read(self.phy, 12)
		if not utils.check_response_and_print_error(response, False, "_SSI_PWMDRIVELEVELS"):
			return False
		DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelRed = response.get_int(2)
		DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelGreen = response.get_int(2)
		DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelBlue = response.get_int(2)
		DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelC1 = response.get_int(2)
		DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelC2 = response.get_int(2)
		DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelSense = response.get_int(2)

		return DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelRed, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelGreen, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelBlue, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelC1, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelC2, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelSense

	def cmdSSISetPWMDriveLevels2_wr( self, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelRed, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelGreen, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelBlue, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelC1, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelC2, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelSense ):
		cmd = Command(0x260F, self.tx_header)
		cmd.put_int(2, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelRed)
		cmd.put_int(2, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelGreen)
		cmd.put_int(2, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelBlue)
		cmd.put_int(2, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelC1)
		cmd.put_int(2, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelC2)
		cmd.put_int(2, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelSense)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_SSI_PWMDRIVELEVELS2"):
			return False

		return True

	def cmdSSISetPWMDriveLevels2_rd( self ):
		cmd = Command(0x260F, self.tx_header)
		response = cmd.read(self.phy, 12)
		if not utils.check_response_and_print_error(response, False, "_SSI_PWMDRIVELEVELS2"):
			return False
		DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelRed = response.get_int(2)
		DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelGreen = response.get_int(2)
		DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelBlue = response.get_int(2)
		DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelC1 = response.get_int(2)
		DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelC2 = response.get_int(2)
		DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelSense = response.get_int(2)

		return DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelRed, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelGreen, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelBlue, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelC1, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelC2, DrivePacket_PWMDriveLevel_SSI_PWM_DriveLevelSense

	def cmdSSISaveBrightnessTableToEEPROM_wr( self ):
		cmd = Command(0x2610, self.tx_header)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_SSI_SAVEBRIGHTNESSTABLE"):
			return False

		return True

	def cmdSSIEnableCompensation_wr( self, enable ):
		cmd = Command(0x2611, self.tx_header)
		cmd.put_int(1, enable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_SSI_ENABLECOMPENSATION"):
			return False

		return True

	def cmdSSIEnableCompensation_rd( self ):
		cmd = Command(0x2611, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "_SSI_ENABLECOMPENSATION"):
			return False
		Enable = response.get_int(1)

		return Enable

	def cmdSSIDebugBrightnessTable_rd( self ):
		cmd = Command(0x2612, self.tx_header)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "_SSI_DEBUGBRIGHTNESSTABLE"):
			return False
		index = response.get_int(2)

		return index

	def cmdSSIGetDutyCycles_rd( self ):
		cmd = Command(0x2613, self.tx_header)
		response = cmd.read(self.phy, 20)
		if not utils.check_response_and_print_error(response, False, "_SSI_GETDUTYCYCLES"):
			return False
		DesiredRedDC = response.get_int(2)
		DesiredGreenDC = response.get_int(2)
		DesiredBlueDC = response.get_int(2)
		ActualDC_0 = response.get_int(2)
		ActualDC_1 = response.get_int(2)
		ActualDC_2 = response.get_int(2)
		ActualDC_3 = response.get_int(2)
		ActualDC_4 = response.get_int(2)
		ActualDC_5 = response.get_int(2)
		ActualDC_6 = response.get_int(2)

		return DesiredRedDC, DesiredGreenDC, DesiredBlueDC, ActualDC_0, ActualDC_1, ActualDC_2, ActualDC_3, ActualDC_4, ActualDC_5, ActualDC_6

	def cmdSSIGetDutyCycleSeqIndex_wr( self, index ):
		cmd = Command(0x2614, self.tx_header)
		cmd.put_int(2, index)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_SSI_GETDUTYCYCLESEQINDEX"):
			return False

		return True

	def cmdSSIGetDutyCycleSeqIndex_rd( self ):
		cmd = Command(0x2614, self.tx_header)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "_SSI_GETDUTYCYCLESEQINDEX"):
			return False
		Index = response.get_int(2)

		return Index

	def cmdSSIDebugGetDutyCycles_rd( self ):
		cmd = Command(0x2615, self.tx_header)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "_SSI_DEBUGGETDUTYCYCLE"):
			return False
		index = response.get_int(2)

		return index

	#Function parsing failed
	def cmdSSIrgbStrobeOverride_rd( ):
		return False

	def cmdSSIrgbStrobeOverride_wr( self, forceLEDOffRed, forceLEDOffGreen, forceLEDOffBlue ):
		cmd = Command(0x2617, self.tx_header)
		cmd.put_int(1, forceLEDOffRed)
		cmd.put_int(1, forceLEDOffGreen)
		cmd.put_int(1, forceLEDOffBlue)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_SSI_SETRGBSTROBEOVERRIDE"):
			return False

		return True

	def cmdSSISetMaxCurrent_rd( self ):
		cmd = Command(0x2618, self.tx_header)
		response = cmd.read(self.phy, 10)
		if not utils.check_response_and_print_error(response, False, "_SSI_SETMAXCURRENT"):
			return False
		RedMax = response.get_int(2)
		GreenMax = response.get_int(2)
		BlueMax = response.get_int(2)
		C1Max = response.get_int(2)
		C2Max = response.get_int(2)

		return RedMax, GreenMax, BlueMax, C1Max, C2Max

	def cmdSSISetMaxCurrent_wr( self, RedMax, GreenMax, BlueMax, C1Max, C2Max ):
		cmd = Command(0x2618, self.tx_header)
		cmd.put_int(2, RedMax)
		cmd.put_int(2, GreenMax)
		cmd.put_int(2, BlueMax)
		cmd.put_int(2, C1Max)
		cmd.put_int(2, C2Max)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_SSI_SETMAXCURRENT"):
			return False

		return True

	def cmdSSIZeroCrossingCurrent_rd( self ):
		cmd = Command(0x2619, self.tx_header)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "_SSI_ZEROCROSSINGCURRENT"):
			return False
		current = response.get_int(2)

		return current

	def cmdSSIZeroCrossingCurrent_wr( self, current ):
		cmd = Command(0x2619, self.tx_header)
		cmd.put_int(2, current)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_SSI_ZEROCROSSINGCURRENT"):
			return False

		return True

	def cmdSSIEnableRealTimeCalibration_rd( self ):
		cmd = Command(0x261A, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "_SSI_ENABLEREALTIMERAMP"):
			return False
		Enable = response.get_int(1)

		return Enable

	def cmdSSIEnableRealTimeCalibration_wr( self, Enable ):
		cmd = Command(0x261A, self.tx_header)
		cmd.put_int(1, Enable)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_SSI_ENABLEREALTIMERAMP"):
			return False

		return True

	def cmdSSISetNumSensorAverages_rd( self ):
		cmd = Command(0x261B, self.tx_header)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "_SSI_SETNUMSENSORAVERAGES"):
			return False
		NumAvg = response.get_int(1)

		return NumAvg

	def cmdSSISetNumSensorAverages_wr( self, NumAvg ):
		cmd = Command(0x261B, self.tx_header)
		cmd.put_int(1, NumAvg)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_SSI_SETNUMSENSORAVERAGES"):
			return False

		return True

	def cmdSSISetSensorBlackLevels_rd( self ):
		cmd = Command(0x261C, self.tx_header)
		response = cmd.read(self.phy, 10)
		if not utils.check_response_and_print_error(response, False, "_SSI_SETSENSORBLACKLEVELS"):
			return False
		Red = response.get_int(2)
		Green = response.get_int(2)
		Blue = response.get_int(2)
		C1 = response.get_int(2)
		C2 = response.get_int(2)

		return Red, Green, Blue, C1, C2

	def cmdSSISetSensorBlackLevels_wr( self, Red, Green, Blue, C1, C2 ):
		cmd = Command(0x261C, self.tx_header)
		cmd.put_int(2, Red)
		cmd.put_int(2, Green)
		cmd.put_int(2, Blue)
		cmd.put_int(2, C1)
		cmd.put_int(2, C2)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_SSI_SETSENSORBLACKLEVELS"):
			return False

		return True

	def cmdTEMPSENSEInit_wr( self ):
		cmd = Command(0x2900, self.tx_header)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_TEMPSENSE_INIT"):
			return False

		return True

	def cmdTEMPSENSESample_wr( self ):
		cmd = Command(0x2901, self.tx_header)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "_TEMPSENSE_SAMPLE"):
			return False

		return True

	def cmdTEMPSENSECurrent_rd( self ):
		cmd = Command(0x2902, self.tx_header)
		response = cmd.read(self.phy, 2)
		if not utils.check_response_and_print_error(response, False, "_TEMPSENSE_GETCURRENT"):
			return False
		temp_sensor_current = response.get_int(2)

		return temp_sensor_current

	def cmdPADReg_wr( self, reg, val ):
		cmd = Command(0x3100, self.tx_header)
		cmd.put_int(1, reg)
		cmd.put_int(1, val)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "PAD_REG_RW"):
			return False

		return True

	def cmdPADReg_rd( self, reg ):
		cmd = Command(0x3100, self.tx_header)
		cmd.put_int(1, reg)
		response = cmd.read(self.phy, 1)
		if not utils.check_response_and_print_error(response, False, "PAD_REG_RW"):
			return False
		val = response.get_int(1)

		return val
		
	def cmdOnTheFlyLoadSplashHeader( self, byte_arr ):
		cmd = Command(0x2106, self.tx_header)
		cmd.put_arr(byte_arr)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "cmdOnTheFlyLoadSplashData"):
			return False
		return True
	
	def cmdOnTheFlyLoadSplashData( self, byte_arr ):
		cmd = Command(0x2107, self.tx_header)
		cmd.put_arr(byte_arr)
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "cmdOnTheFlyLoadSplashData"):
			return False
		return True
		

