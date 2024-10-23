# This file contains the constants used in the project 
# So that they can be easily changed in one place
class Constants:
    # Could you have mupltiple classes for each subsystem?
    # Might be overly complicated
    
    # vertical motor pins
    frontVerticalMotorPin = -1
    backVerticalMotorPin = -1

    # rasberry pi ports x,y motors are connected to
    # Forward and backwards are digital pins and speeds are anolog pins
    mflForwardID = 17
    mflBackwardID = 27
    mflSpeedID = 4
    mfrForwardID = 22
    mfrBackwardID = 10
    mfrSpeedID = 9
    mbrForwardID = 5
    mbrBackwardID = 6
    mbrSpeedID = 11
    mblForwardID = 13
    mblBackwardID = 19
    mblSpeedID = 26

    def map(x: float, in_min: float, in_max: float, out_min: float, out_max: float) -> float:
        return (x -in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
