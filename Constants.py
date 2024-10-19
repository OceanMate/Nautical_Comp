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
    mflForwardID = -1, mflBackwardID = -1, mflSpeedID = -1
    mfrForwardID = -1, mfrBackwardID = -1, mfrSpeedID = -1
    mbrForwardID = -1, mbrBackwardID = -1, mbrSpeedID = -1
    mblForwardID = -1, mblBackwardID = -1, mblSpeedID = -1

    def map(x: float, in_min: float, in_max: float, out_min: float, out_max: float) -> float:
        return (x -in_min) * (out_max - out_min) / (in_max - in_min) + out_min;