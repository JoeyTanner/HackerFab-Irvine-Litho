###########################################################################################################################################################################
# Texas Instruments DLP LightCrafter 230NP EVM Python Support Code - sample02_splash.py - Last Updated May 8th, 2020
# This script is intended to be used with the DLPDLCR230NP EVM on a Raspberry Pi 4 (or compatible)
# It is recommended to consult the DLPDLCR230NPEVM User's Guide for more detailed information on the operation of this EVM
# For technical support beyond what is provided in the above documentation, direct inquiries to TI E2E Forums (http://e2e.ti.com/support/dlp)
###########################################################################################################################################################################
import struct
import time

from enum import Enum

import sys, os.path
python_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(python_dir)
from api.dlpc343x_xpr4 import *
from linuxi2c import *
import i2c

class Set(Enum):
    Disabled = 0
    Enabled = 1

def main():
        '''
        This script cycles through available splash screens on the DLPDLCR230NPEVM.
        Raspberry Pi automatically configures each splash screen via I2C.
        System will await user input before cycling through each splash screen.
        Splash screens are saved on DLPC3436 flash device. Flash is accessed on splash screen switch.
        Please review the DLPC3436 Programmer's Guide for more information.
        '''

        protocoldata = ProtocolData()
        
        def WriteCommand(writebytes, protocoldata):
            '''
            Issues a command over the software I2C bus to the DLPDLCR230NP EVM.
            Set to write to Bus 7 by default
            '''
            # print ("Write Command writebytes ", [hex(x) for x in writebytes])
            i2c.write(writebytes)       
            return

        def ReadCommand(readbytecount, writebytes, protocoldata):
            '''
            Issues a read command over the software I2C bus to the DLPDLCR230NP EVM.
            Set to read from Bus 7 by default
            '''
            # print ("Read Command writebytes ", [hex(x) for x in writebytes])
            i2c.write(writebytes) 
            readbytes = i2c.read(readbytecount)
            return readbytes

        def PrintRegister(ReadData):
            '''
            Helper function; prints the contents of a register data block read via I2C.
            '''
            filtered_dict = [ (key, value) for key, value in vars(ReadData).items() if not (key.startswith("__") and key.endswith("__"))]
            print("{" + "\n".join("{!r}: {!r},".format(k, v) for k, v in filtered_dict) + "}")
        
        def InitGPIO():
            '''
            Initializes the GPIO pins on the Raspberry Pi for use with the DLPDLCR230NP EVM in Video mode.
            Standard GPIO functionality is as follows:
            BCM #0  - 21 --> ALT2            (RGB666 DPI Output)
            BCM #22 - 23 --> I2C-7           (SW-based I2C Bus)
            BCM #24      --> SPI_SELECT_ASIC (Flash select line, Tri-Stated for Video mode)
            BCM #25      --> RGB_BUFFER_SEL  (RGB666 Buffer Enable, Drive High for Video mode)
            BCM #26      --> SPI_SELECT_FPGA (Flash select line, Tri-Stated for Video mode)
            NOTE: Do NOT attempt to enable RGB666 buffers and access ASIC/FPGA flash devices simultaneously. Damage to flash devices may occur.
            '''
            print("Initializing Raspberry Pi Default Settings for DLPC3436...")
            os.system("raspi-gpio set 0 op pn")
            os.system("raspi-gpio set 1-27 ip pn")
            time.sleep(1)
            os.system("gpio drive 0 5")
            os.system("raspi-gpio set 22 op pn")
            os.system("raspi-gpio set 23 op pn")
            os.system("raspi-gpio set 0-21 a2 pn")
            os.system("raspi-gpio set 25 op dh")
            time.sleep(1)

        # ##### ##### Initialization for I2C ##### #####
        # register the Read/Write Command in the Python library
        DLPC343X_XPR4init(ReadCommand, WriteCommand)
        i2c.initialize()
        InitGPIO()
        # ##### ##### Command call(s) start here ##### #####  

        print("Cycling Splash Screens on DLPC3436...")
        Summary = WriteDisplayImageCurtain(1,Color.Black)
        Summary = WriteFpgaTestPatternSelect(Set.Disabled,  FpgaTestPatternColor.Black,   FpgaTestPattern.SolidField,  0)
        Summary = WriteSourceSelect(Source.FpgaTestPattern, Set.Disabled)
        Summary = WriteInputImageSize(1920, 1080)
        time.sleep(2)
        Summary = WriteDisplayImageCurtain(0,Color.Black)
        
        for splash_index in range(0,3+1):
            print("Displaying Splash Screen",splash_index,"...")
            Summary = WriteSplashScreenSelect(splash_index)
            Summary = WriteSourceSelect(Source.SplashScreen, Set.Disabled)
            Summary,SplashScreenHeader = ReadSplashScreenHeader(splash_index)	
            input("Press ENTER to continue to next splash screen")
            Summary = WriteSourceSelect(Source.FpgaTestPattern, Set.Disabled)
            time.sleep(1)

        print("Restoring Raspberry Pi Video Display")
        Summary = WriteDisplayImageCurtain(1,Color.Black)
        Summary = WriteSourceSelect(Source.ExternalParallelPort, Set.Disabled)
        Summary = WriteInputImageSize(1920, 1080)
        Summary = WriteExternalVideoSourceFormatSelect(ExternalVideoFormat.Rgb666)
        time.sleep(2)
        Summary = WriteDisplayImageCurtain(0,Color.Black)

        # ##### ##### Command call(s) end here ##### #####
        i2c.terminate()


if __name__ == "__main__" : main()


