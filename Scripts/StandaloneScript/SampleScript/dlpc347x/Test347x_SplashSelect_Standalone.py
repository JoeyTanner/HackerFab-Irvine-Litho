# ############################################
# Sample Script to run through Splash Images #
# ############################################

import struct
import time

from enum import Enum

from CommandScript.dlpc347x import *
from DriverScript.cypress import *

def main():
    with Cypress(0x36) as dev, LightCrafterDisplay(dev) as lcd:
    
        protocoldata = ProtocolData()
        
        def WriteCommand (writebytes, protocoldata):
            # print ("writebytes ", [hex(x) for x in writebytes])
            dev.write(writebytes)

        def ReadCommand(readbytecount, writebytes, protocoldata):
            # print ("writebytes ", [hex(x) for x in writebytes])
            readbytes = dev.read(readbytecount, writebytes)
            # print ("readbytes ", [hex(x) for x in readbytes])
            return readbytes
            
        DLPC347Xinit(ReadCommand, WriteCommand)

        # Read and store the Display settings
        Summary, source = ReadOperatingModeSelect ()
        Summary, CropStartPixel, CropStartLine, CropPixels, CropLines = ReadImageCrop()
        Summary, InputPixels, InputLines = ReadInputImageSize()
        Summary, StartPixel, StartLine, Pixels, Lines = ReadDisplaySize()
        
        # Set the source to Splash 
        Summary = WriteOperatingModeSelect(OperatingMode.SplashScreen)
        
        for splash_index in range(0,3+1):
            # Set Splash image index and read the header information
            Summary = WriteSplashScreenSelect(splash_index)
            Summary, SplashScreenHeader = ReadSplashScreenHeader(splash_index)
            first_pixel = 0
            first_line = 0
            dmd_pixels = 854
            dmd_lines = 480

            # Set image input and display to the size of the Splash image in flash
            #Summary = WriteDisplaySize(first_pixel,first_line,SplashScreenHeader.WidthInPixels, SplashScreenHeader.HeightInPixels)
            Summary = WriteDisplaySize(first_pixel, first_line, dmd_pixels, dmd_lines)
            Summary = WriteImageCrop(0,0,SplashScreenHeader.WidthInPixels, SplashScreenHeader.HeightInPixels)
            Summary = WriteInputImageSize(SplashScreenHeader.WidthInPixels, SplashScreenHeader.HeightInPixels)
            
            # Load and Display the Splash Image 
            print ("   Displaying Splash Index %s...", splash_index)
            Summary = WriteSplashScreenExecute()
            time.sleep(5)
            
        # Restore Display sizes and restore the source 
        print ("   Restoring Source to %s...", source)
        Summary = WriteDisplaySize(StartPixel,StartLine,dmd_pixels,dmd_lines)
        time.sleep(5)
        Summary = WriteImageCrop(CropStartPixel,CropStartLine,CropPixels,CropLines)
        time.sleep(5)
        Summary = WriteInputImageSize(InputPixels,InputLines)
        time.sleep(5)
        Summary = WriteOperatingModeSelect(source)
        time.sleep(10)
        
# main program for t2_SplashSelect.py
if __name__ == "__main__" : main()
