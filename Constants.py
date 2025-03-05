
class Constants:
    # vertical motor pins
    frontVerticalMotorPin = 4
    backVerticalMotorPin = 5

    # horizontal motor pins
    frontLeftMotorPin = 0
    frontRightMotorPin = 1
    backLeftMotorPin = 2
    backRightMotorPin = 3

    # math scaling function 
    def map(x: float, in_min: float, in_max: float, out_min: float, out_max: float) -> float:
        return (x -in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
    
    def clamp(n, smallest, largest): return max(smallest, min(n, largest))
