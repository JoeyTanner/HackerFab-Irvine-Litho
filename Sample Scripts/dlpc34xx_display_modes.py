######################################################################
# Sample Script that run through all the Operating Modes for .2 WVGA #
######################################################################

from dlpc347x.commands import *
import time

def configureForSplash(index, dmdPixels, dmdLines):
    rtnText = ""
    # Read and store the Display settings
    Summary, CropStartPixel, CropStartLine, CropPixels, CropLines = ReadImageCrop()
    if not Summary.Successful:
        rtnText = "Failed to Read Image Crop"

    Summary, InputPixels, InputLines = ReadInputImageSize()
    if not Summary.Successful:
        rtnText = "Failed to Read Input Image Size."

    Summary, StartPixel, StartLine, Pixels, Lines = ReadDisplaySize()
    if not Summary.Successful:
        rtnText = "Failed to Read Display Size."

    Summary = WriteSplashScreenSelect(index)
    if not Summary.Successful:
        rtnText = "Failed to Write Splash Screen Select."

    Summary, SplashScreenHeader = ReadSplashScreenHeader(index)
    if not Summary.Successful:
        rtnText = "Failed to Read Splash Screen Header."
        
    # Set image input and display to the size of the Splash image in flash
    first_pixel = 0
    first_line = 0
    Summary = WriteDisplaySize(first_pixel,first_line,854, 480)
    if not Summary.Successful:
        rtnText = "Failed to Write Display Size."
    
    Summary = WriteImageCrop(0,0,SplashScreenHeader.WidthInPixels, SplashScreenHeader.HeightInPixels)
    if not Summary.Successful:
            rtnText = "Failed to Write Image Crop."
    
    Summary = WriteInputImageSize(SplashScreenHeader.WidthInPixels, SplashScreenHeader.HeightInPixels)
    if not Summary.Successful:
        rtnText = "Failed to Write Image Crop."

    return rtnText

# Get the current operating mode to save for later restoration
Summary, CurrentOperatingMode = ReadOperatingModeSelect()
print ("Operating Mode ", CurrentOperatingMode)
Summary, CurrInputPixelsPerLine, CurrInputLinesPerFrame = ReadInputImageSize()
print ("input image size ", CurrInputPixelsPerLine, CurrInputLinesPerFrame)
Summary, CurrCropCaptureStartPixel, CurrCropCaptureStartLine, CurrCropPixelsPerLine, CurrCropLinesPerFrame = ReadImageCrop()
print ("image Crop ", CurrCropCaptureStartPixel, CurrCropCaptureStartLine, CurrCropPixelsPerLine, CurrCropLinesPerFrame)
Summary, CurrDispStartPixel, CurrDispStartLine, CurrDispPixelsPerLine, CurrDispLinesPerFrame = ReadDisplaySize()
print ("display size ", CurrDispStartPixel, CurrDispStartLine, CurrDispPixelsPerLine, CurrDispLinesPerFrame)

DmdWidth = 854
DmdHeight = 480

#---------------------------------------------------------------------------------------
# Operating Mode: Test Pattern
print ("Switching to Test Pattern Operating Mode")
Summary = WriteInputImageSize(DmdWidth, DmdHeight)
Summary = WriteImageCrop(0, 0, DmdWidth, DmdHeight)
Summary = WriteDisplaySize(0, 0, DmdWidth, DmdHeight)
gridlinevar = GridLines()
gridlinevar.Border = BorderEnable.Enable
gridlinevar.BackgroundColor = Color.Green
gridlinevar.ForegroundColor = Color.Magenta
gridlinevar.HorizontalForegroundLineWidth = 25
gridlinevar.HorizontalBackgroundLineWidth = 75
gridlinevar.VerticalForegroundLineWidth = 50
gridlinevar.VerticalBackgroundLineWidth = 100
WriteGridLines(gridlinevar)
WriteOperatingModeSelect(OperatingMode.TestPatternGenerator)       
time.sleep(2)
Summary, NewOperatingMode = ReadOperatingModeSelect()
time.sleep(2)

if (NewOperatingMode != OperatingMode.TestPatternGenerator):
    print("Test Pattern Generator Operating Mode cound not be set. Operating mode = %s", str(NewOperatingMode)) 

#---------------------------------------------------------------------------------------
# Operating Mode: Splash Screen
print ("Switching to Splash Screen Operating Mode")
rettext = configureForSplash(2, DmdWidth, DmdHeight)
if rettext != "":
    print ("Configure Splash Error ", rettext)
    
Summary = WriteOperatingModeSelect(OperatingMode.SplashScreen)
time.sleep(2)
Summary, NewOperatingMode = ReadOperatingModeSelect()
time.sleep(2)

if (NewOperatingMode != OperatingMode.SplashScreen):
    print("Splash Image Operating Mode cound not be set. Operating mode = %s", str(NewOperatingMode)) 

Summary = WriteSplashScreenExecute()
time.sleep(10)

# Restore Settings
print ("restore input image size ", CurrInputPixelsPerLine, CurrInputLinesPerFrame)
Summary = WriteInputImageSize(CurrInputPixelsPerLine, CurrInputLinesPerFrame)

print ("restore image Crop ", CurrCropCaptureStartPixel, CurrCropCaptureStartLine, CurrCropPixelsPerLine, CurrCropLinesPerFrame)
Summary = WriteImageCrop(CurrCropCaptureStartPixel, CurrCropCaptureStartLine, CurrCropPixelsPerLine, CurrCropLinesPerFrame)

print ("restore display size ", CurrDispStartPixel, CurrDispStartLine, CurrDispPixelsPerLine, CurrDispLinesPerFrame)
Summary = WriteDisplaySize(CurrDispStartPixel, CurrDispStartLine, CurrDispPixelsPerLine, CurrDispLinesPerFrame)

#---------------------------------------------------------------------------------------
# Operating Mode: External Video Port
print ("Switching to External Video Operating Mode")
Summary = WriteOperatingModeSelect(OperatingMode.ExternalVideoPort)
time.sleep(10)
Summary, NewOperatingMode = ReadOperatingModeSelect()
time.sleep(2)

if (NewOperatingMode != OperatingMode.ExternalVideoPort):
    print("External Video Operating Mode cound not be set. Operating mode = %s", str(NewOperatingMode)) 

#---------------------------------------------------------------------------------------
# Operating Mode: Standby
print ("Switching to Standby Operating Mode")
Summary = WriteOperatingModeSelect(OperatingMode.Standby)
time.sleep(2)
Summary, NewOperatingMode = ReadOperatingModeSelect()
time.sleep(2)

if (NewOperatingMode != OperatingMode.Standby):
    print("Stanby Operating Mode cound not be set. Operating mode = %s", str(NewOperatingMode)) 

#---------------------------------------------------------------------------------------
# Operating Mode: External Pattern Streaming
print ("Switching to External Pattern Streaming Operating Mode")

# Configure the pattern to be 1-bit_mono_splash type
PatConfig = PatternConfiguration()
PatConfig.NumberOfPatterns = 8
PatConfig.SequenceType = SequenceType.OneBitMono
PatConfig.RedIlluminator = IlluminatorEnable.Disable
PatConfig.GreenIlluminator = IlluminatorEnable.Enable
PatConfig.BlueIlluminator = IlluminatorEnable.Disable
PatConfig.IlluminationTime = 793
PatConfig.PreIlluminationDarkTime = 338
PatConfig.PostIlluminationDarkTime = 60

# Configure the output triggers
print ("       Configuring TriggerOut 1 and 2...")
Summary = WriteTriggerOutConfiguration(TriggerType.Trigger1, TriggerEnable.Enable, TriggerInversion.NotInverted, 0)
Summary = WriteTriggerOutConfiguration(TriggerType.Trigger2, TriggerEnable.Enable, TriggerInversion.NotInverted,0)
Summary = WritePatternConfiguration(PatConfig)

Summary = WriteOperatingModeSelect(OperatingMode.SensExternalPattern)
time.sleep(2)
Summary, NewOperatingMode = ReadOperatingModeSelect()
time.sleep(2)

if (NewOperatingMode != OperatingMode.SensExternalPattern):
    print("External Pattern Streaming Operating Mode cound not be set. Operating mode = %s", str(NewOperatingMode)) 

#---------------------------------------------------------------------------------------
# Operating Mode: Internal Pattern Streaming
print ("Switching to Internal Pattern Streaming Operating Mode")
Summary = WriteOperatingModeSelect(OperatingMode.SensInternalPattern)
time.sleep(2)
Summary, NewOperatingMode = ReadOperatingModeSelect()
time.sleep(2)

if (NewOperatingMode != OperatingMode.SensInternalPattern):
    print("External Pattern Streaming Operating Mode cound not be set. Operating mode = %s", str(NewOperatingMode)) 

Summary = WriteInternalPatternControl(PatternControl.Start, 255)
time.sleep(5)
Summary = WriteInternalPatternControl(PatternControl.Stop, 0)
time.sleep(2)

#---------------------------------------------------------------------------------------
# Operating Mode: Space Coded Pattern Streaming
print ("Switching to Space Coded Splash Pattern Streaming Operating Mode")
rettext = configureForSplash(0, DmdWidth, DmdHeight)
if rettext != "":
    print ("Configure Splash Error ", rettext)

# Configure the pattern to be 1-bit_mono_splash type
PatConfig = PatternConfiguration()
PatConfig.NumberOfPatterns = 8
PatConfig.SequenceType = SequenceType.OneBitMono
PatConfig.RedIlluminator = IlluminatorEnable.Disable
PatConfig.GreenIlluminator = IlluminatorEnable.Enable
PatConfig.BlueIlluminator = IlluminatorEnable.Disable
PatConfig.IlluminationTime = 793
PatConfig.PreIlluminationDarkTime = 338
PatConfig.PostIlluminationDarkTime = 60

# Configure the output triggers
print ("       Configuring TriggerOut 1 and 2...")
Summary = WriteTriggerOutConfiguration(TriggerType.Trigger1, TriggerEnable.Enable, TriggerInversion.NotInverted, 0)
Summary = WriteTriggerOutConfiguration(TriggerType.Trigger2, TriggerEnable.Enable, TriggerInversion.NotInverted,0)
Summary = WritePatternConfiguration(PatConfig)

Summary = WriteOperatingModeSelect(OperatingMode.SensSpaceCodedPattern)
time.sleep(2)
Summary, NewOperatingMode = ReadOperatingModeSelect()
time.sleep(2)

if (NewOperatingMode != OperatingMode.SensSpaceCodedPattern):
    print("Splash Pattern Operating Mode cound not be set. Operating mode = %s", str(NewOperatingMode)) 

# Load and Display the Splash image 
Summary = WriteSplashScreenExecute()
time.sleep(20)

# Restore Settings
print ("restore input image size ", CurrInputPixelsPerLine, CurrInputLinesPerFrame)
Summary = WriteInputImageSize(CurrInputPixelsPerLine, CurrInputLinesPerFrame)

print ("restore image Crop ", CurrCropCaptureStartPixel, CurrCropCaptureStartLine, CurrCropPixelsPerLine, CurrCropLinesPerFrame)
Summary = WriteImageCrop(CurrCropCaptureStartPixel, CurrCropCaptureStartLine, CurrCropPixelsPerLine, CurrCropLinesPerFrame)

print ("restore display size ", CurrDispStartPixel, CurrDispStartLine, CurrDispPixelsPerLine, CurrDispLinesPerFrame)
Summary = WriteDisplaySize(CurrDispStartPixel, CurrDispStartLine, CurrDispPixelsPerLine, CurrDispLinesPerFrame)

print ("Setting operating mode back to original mode...%s", str(CurrentOperatingMode))
Summary = WriteOperatingModeSelect(CurrentOperatingMode)

