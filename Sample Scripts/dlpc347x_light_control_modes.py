# ######################################################
# Sample Script to run through Sensing Operating Modes #
# 1. Internal Pattern                                  #
# 2. Splash Pattern                                    #
# 3. External Pattern                                  #
# ######################################################

from dlpc347x.commands import *
from System.Threading import *

def SetUpExternalPatterns():
    # Configure the pattern to be 1-bit external pattern
    print ("Configuring Pattern to 1-bit_mono_ external streaming, 1 pattern, illum time = 3800...")
    global PatternConfiguration
    PatternConfiguration = PatternConfiguration()
    PatternConfiguration.SequenceType               = SequenceType.OneBitMono
    PatternConfiguration.NumberOfPatterns           = 1
    PatternConfiguration.RedIlluminator             = IlluminatorEnable.Disable
    PatternConfiguration.GreenIlluminator           = IlluminatorEnable.Enable
    PatternConfiguration.BlueIlluminator            = IlluminatorEnable.Disable
    PatternConfiguration.IlluminationTime           = 3800
    PatternConfiguration.PreIlluminationDarkTime    = 170
    PatternConfiguration.PostIlluminationDarkTime   = 30
    WritePatternConfiguration(PatternConfiguration)

    # Set mode to External Pattern Streaming
    WriteOperatingModeSelect(OperatingMode.SensExternalPattern)
    Thread.Sleep(1500)
    
def SetUpSplashPatterns():
    # Define splash screen index and display size parameters
    splash_index = 1
    first_pixel = 0
    first_line = 0

    # Configure the pattern to be 8-bit_mono_splash type
    print ("Configuring Pattern to 8-bit_mono_splash type, 2 patterns, illum time = 7736...")
    Summary, PatConfig = ReadPatternConfiguration()
    PatConfig.NumberOfPatterns = 2
    PatConfig.SequenceType = SequenceType.EightBitMono
    PatConfig.RedIlluminator = IlluminatorEnable.Disable
    PatConfig.GreenIlluminator = IlluminatorEnable.Enable
    PatConfig.BlueIlluminator = IlluminatorEnable.Disable
    PatConfig.IlluminationTime = 7737
    PatConfig.PreIlluminationDarkTime = 170
    PatConfig.PostIlluminationDarkTime = 30
    Summary = WritePatternConfiguration(PatConfig)

    # Set Splash image index and read the header information
    Summary = WriteSplashScreenSelect(splash_index)
    Summary, SplashScreenHeader = ReadSplashScreenHeader(splash_index)

    # Set image input and display to the size of the Splash image in flash
    Summary = WriteDisplaySize(first_pixel,first_line,SplashScreenHeader.WidthInPixels, SplashScreenHeader.HeightInPixels)
    Summary = WriteImageCrop(0,0,SplashScreenHeader.WidthInPixels, SplashScreenHeader.HeightInPixels)
    Summary = WriteInputImageSize(SplashScreenHeader.WidthInPixels, SplashScreenHeader.HeightInPixels)

    # Set the source to Splash Patterns
    Summary = WriteOperatingModeSelect(OperatingMode.SensSpaceCodedPattern)

    # Load and Display the Splash image
    print ("Displaying Splash Index %s...", splash_index)
    Summary = WriteSplashScreenExecute()
    # Wait for the Splash Image to be loaded from flash
    Thread.Sleep(500)
    
def SetUpInternalPatterns():
    # Configure the Pattern Order Table
    # This step is not necessary if the system already has a
    # Pattern Order Table defined in flash
    PatEntry = PatternOrderTableEntry()
    PatEntry.PatSetIndex = 0
    PatEntry.NumberOfPatternsToDisplay = 8
    PatEntry.RedIlluminator = IlluminatorEnable.Enable
    PatEntry.GreenIlluminator = IlluminatorEnable.Disable
    PatEntry.BlueIlluminator = IlluminatorEnable.Disable
    PatEntry.PatternInvertLsword = 0
    PatEntry.PatternInvertMsword = 0
    PatEntry.IlluminationTime = 401
    PatEntry.PreIlluminationDarkTime = 171
    PatEntry.PostIlluminationDarkTime = 31
    #Summary = WritePatternOrderTableEntry(WriteControl.Start, PatEntry)

    # Configure Trigger In
    # Trigger In Enable = Trigger In Mode
    # Trigger In Disable = Free Running Mode
    print ("Configuring TriggerIn...")
    WriteTriggerInConfiguration(TriggerEnable.Disable, TriggerPolarity.ActiveHi)

    # Configure Pattern Ready output
    print ("Configuring Pattern Ready...")
    WritePatternReadyConfiguration(TriggerEnable.Enable, TriggerPolarity.ActiveHi)

    # Set the source to Internal Streaming
    print ("Setting source to Internal Patterns...")
    Summary = WriteOperatingModeSelect(OperatingMode.SensInternalPattern)
    Thread.Sleep(500)

    # Start the Pattern Streaming process
    print ("Starting the Pattern Streaming process...")
    repeatCount = 255
    WriteInternalPatternControl(PatternControl.Start, repeatCount)
    Thread.Sleep(5000)

    # Use WriteInternalPatternControl command to Stop internal patterns before switching to a different mode
    WriteInternalPatternControl(PatternControl.Stop, 0)

# Define trigger delays
trig1_delay = 0
trig2_delay = 0

# Configure the output triggers
print ("Configuring TriggerOut 1 and 2...")
Summary = WriteTriggerOutConfiguration(TriggerType.Trigger1,TriggerEnable.Enable,TriggerInversion.NotInverted,trig1_delay)
Summary = WriteTriggerOutConfiguration(TriggerType.Trigger2,TriggerEnable.Enable,TriggerInversion.NotInverted,trig2_delay)

# Set up each of the Light Control modes for 5000ms each
SetUpInternalPatterns()

SetUpSplashPatterns()
Thread.Sleep(5000)

SetUpExternalPatterns()
Thread.Sleep(5000)

# Switch to Standby mode
print ("Switching to Standby mode...")
WriteOperatingModeSelect(OperatingMode.Standby)
