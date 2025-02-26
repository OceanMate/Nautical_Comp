# This file contains the constants used in the project 
# So that they can be easily changed in one place
class BilgeMotorIDs:
    def __init__(self, forward: int, backward: int, speed: int):
        self.forward = forward
        self.backward = backward
        self.speed = speed


class Constants:
    # Could you have mupltiple classes for each subsystem?
    # Might be overly complicated
    
    # vertical motor pins
    frontVerticalMotorPin = 0
    backVerticalMotorPin = 0

    # rasberry pi ports x,y motors are connected to
    # Forward and backwards are digital pins and speeds are anolog pins
    mfl = BilgeMotorIDs(17, 27, 1)
    mfr = BilgeMotorIDs(22, 10, 2)
    mbr = BilgeMotorIDs(5, 6, 3)
    mbl = BilgeMotorIDs(13, 19, 4)

    # math scaling function 
    def map(x: float, in_min: float, in_max: float, out_min: float, out_max: float) -> float:
        return (x -in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
    
    def clamp(n, smallest, largest): return max(smallest, min(n, largest))
