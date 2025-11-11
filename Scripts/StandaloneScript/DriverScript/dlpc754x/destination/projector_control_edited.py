	
#!/cygdrive/c/Python27/python
# ******************************************************************************
# 
#   Copyright (c) 2018-2019 Texas Instruments
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

class ProjectorControlEdited:
    
	DESTINATION_VALUE = 2
	NUM_CMD_BYTES = 2

	def __init__(self, phy, use_seq, use_len, use_checksum):
		self.tx_header = TxHeader(ProjectorControlEdited.DESTINATION_VALUE, ProjectorControlEdited.NUM_CMD_BYTES, use_seq, use_len, use_checksum)
		self.phy = phy

	def cmdApp_Versions_rd( self ):
		cmd = Command(0x0205, self.tx_header)
		response = cmd.read(self.phy, 80)
		if not utils.check_response_and_print_error(response, False, "APP_VERSIONS"):
			return False
		AppVersion_Patch = response.get_int(2)
		AppVersion_Minor = response.get_int(1)
		AppVersion_Major = response.get_int(1)
		EepromVersion_Subminor = response.get_int(1)
		Reserved = response.get_int(1)
		EepromVersion_Minor = response.get_int(1)
		EepromVersion_Major = response.get_int(1)
		APIVersion_Patch = response.get_int(2)
		APIVersion_Minor = response.get_int(1)
		APIVersion_Major = response.get_int(1)
		Supported_LayoutRevision = response.get_int(2)
		Supported_LayoutHash = []
		Supported_LayoutHash += response.get_arr(32)
		Programmed_LayoutRevision = response.get_int(2)
		Programmed_LayoutHash = []
		Programmed_LayoutHash += response.get_arr(32)

		return AppVersion_Patch, AppVersion_Minor, AppVersion_Major, EepromVersion_Subminor, EepromVersion_Minor, EepromVersion_Major, APIVersion_Patch, APIVersion_Minor, APIVersion_Major, Supported_LayoutRevision, Supported_LayoutHash, Programmed_LayoutRevision, Programmed_LayoutHash

	def cmdApp_Signature_rd( self, LibIndex ):
		cmd = Command(0x0247, self.tx_header)
		cmd.put_int(1, LibIndex)
		response = cmd.read(self.phy, 62)
		if not utils.check_response_and_print_error(response, False, "APP_GETSIGNATURE"):
			return False
		LibName = []
		LibName += response.get_arr(21)
		Changeset = []
		Changeset += response.get_arr(41)

		return LibName, Changeset
		
	def cmdApp_I2CPass_rd( self, port, is7bit, hasSubaddr, sclRate, devAddr, subAddr, byteCount):
		cmd = Command(0x020A, self.tx_header)
		cmd.put_int(1, port)
		cmd.put_int(1, is7bit)
		cmd.put_int(1, hasSubaddr)
		cmd.put_int(4, sclRate)
		cmd.put_int(2, devAddr)
		cmd.put_int(1, subAddr)
		cmd.put_int(2, byteCount)
		response = cmd.read(self.phy, byteCount)
		#if not utils.check_response_and_print_error(response, False, "APP_I2C_PASS_RD"):
			#return False
		PT_DataArray = []
		PT_DataArray += response.get_arr(byteCount)

		return PT_DataArray

	def cmdApp_I2CPass_wr( self, port, is7bit, hasSubaddr, sclRate, devAddr, subAddr, *args):
		cmd = Command(0x020A, self.tx_header)
		cmd.put_int(1, port)
		cmd.put_int(1, is7bit)
		cmd.put_int(1, hasSubaddr)
		cmd.put_int(4, sclRate)
		cmd.put_int(2, devAddr)
		cmd.put_int(1, subAddr)
		for data in args:
			cmd.put_int(1, data)
			print data
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "APP_I2C_PASS_WR"):
			return False

		return True
    
      	# Not auto generated because of macro
        def CMD_GetGpioPinName(self, pin):
        	cmd = Command(0x170F, self.tx_header)
        	cmd.put_int(1, pin)
        
        	response = cmd.read(self.phy, 32)
	        if not utils.check_response_and_print_error(response, False, "READ_GPIO_PIN_NAME"):
       			return False

        	str = []
        	str += response.get_arr(32)
          	str1 = "".join(map(chr, str))
        	return str1
	
	def cmdOSD_EnableOSD(self, enable):
		cmd = Command(0x3200, self.tx_header, True)
		cmd.put_int(1,1) #case 1 in osdCmd_write
		cmd.put_int(1,enable)
		
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "OSD_ENABLE_FAIL"):
			return False
		return True
	
	def cmdOSD_LoadMenu(self, menuId, displayEnable):
		cmd = Command(0x3200, self.tx_header, True)
		cmd.put_int(1,7) #case 7 in osdCmd_write
		cmd.put_int(2, menuId)
		cmd.put_int(1, displayEnable)
		
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "OSD_LOAD_MENU_FAIL"):
			return False
		return True 
	
	def cmdOSD_DisplayMenu(self, menuId, displayEnable):
		cmd = Command(0x3200, self.tx_header, True)
		cmd.put_int(1,8) #case 8 in osdCmd_write
		cmd.put_int(2, menuId)
		cmd.put_int(1, displayEnable) # Display true/false
		
		response = cmd.write(self.phy, True)
		if not utils.check_response_and_print_error(response, False, "OSD_DISPLAY_MENU_FAIL"):
			return False
		return True
		
	def cmdOSD_SetMenuPos(self, menuId, horizPos, vertPos):
		cmd = Command(0x3200, self.tx_header)
		cmd.put_int(1,9) #case 9 in osdCmd_write
		cmd.put_int(2, menuId)
		cmd.put_int(2, horizPos)
		cmd.put_int(2, vertPos)
		
		response = cmd.write(self.phy)
		if not utils.check_response_and_print_error(response, False, "OSD_SET_MENU_POSITION_FAIL"):
			return False
		return True
		
	def cmdOSD_SetSliderVal(self, feildId, val):
		cmd = Command(0x3200, self.tx_header)
		cmd.put_int(1,23) #case 23 in osdCmd_write
		cmd.put_int(2, feildId)
		cmd.put_int(2, val)
		
		response = cmd.write(self.phy)
		if not utils.check_response_and_print_error(response, False, "OSD_SET_SLIDER_VAL_FAIL"):
			return False
		return True
		
	def cmdOSD_SetMenuBlink(self, menuId, ena):
		cmd = Command(0x3200, self.tx_header)
		cmd.put_int(1,73) #case 73 in osdCmd_write
		cmd.put_int(2, menuId)
		cmd.put_int(2, ena)
		
		response = cmd.write(self.phy)
		if not utils.check_response_and_print_error(response, False, "OSD_SET_MENU_BLINK_FAIL"):
			return False
		return True
		
	def cmdDMD_WriteReg(self, regId, regVal):
		cmd = Command(0xFEFF, self.tx_header)
		cmd.put_int(1, 0x90) #pass thru command id
		cmd.put_int(2, 5) #expected bytes
		cmd.put_int(1, regId)
		cmd.put_int(4, regVal)
		
		response = cmd.write(self.phy)
		if not utils.check_response_and_print_error(response, False, "DMD_REG_WRITE_FAIL"):
			return False
		return True
		
	def cmdDMD_ReadReg(self, regId):		
		cmd = Command(0xFEFF, self.tx_header)
		cmd.put_int(1, 0x90) #pass thru command id
		cmd.put_int(2, 5) #expected bytes
		cmd.put_int(1, 1) #num of read params
		cmd.put_int(1, regId)
		
		response = cmd.read(self.phy, 5)
		if not utils.check_response_and_print_error(response, False, "DMD_REG_READ_FAIL"):
			return False
		
		cmdId = response.get_int(1)
		regVal = response.get_int(4)
		return cmdId,regVal
		
	def cmdFMT_WriteStructuredPatternBitplane(self, BP_Num, IsVertPat, ByteArray):
		ByteArrLen = len(ByteArray)
		
		cmd = Command(0x1003, self.tx_header, True)
		cmd.put_int(1,BP_Num)
		cmd.put_int(1, IsVertPat)
		cmd.put_int(2, ByteArrLen)
		cmd.put_arr(ByteArray[0:ByteArrLen])
		
		response = cmd.write(self.phy)
		if not utils.check_response_and_print_error(response, False, "Fsl Pattern Write Failed"):
			return FALSE
		
			
	def cmdApp_PADReg_rd( self, reg):
		cmd = Command(0x3100, self.tx_header)
		cmd.put_int(1, reg)
		response = cmd.read(self.phy,1)
		#if not utils.check_response_and_print_error(response, False, "APP_I2C_PASS_RD"):
			#return False
		data = response.get_int(1)

		return data

	def cmdApp_PADReg_wr( self, reg, val):
		cmd = Command(0x3100, self.tx_header)
                print reg
                print val
		cmd.put_int(1, reg)
		cmd.put_int(1, val)
		response = cmd.write(self.phy, True)
		# if not utils.check_response_and_print_error(response, False, "APP_I2C_PASS_WR"):
			# return False

		return True

	def CMD_WarpEnable(self, enable):
		cmd = Command(0xFF02, self.tx_header)
		cmd.put_int(1, enable)
		response = cmd.write(self.phy, True)
		return True
