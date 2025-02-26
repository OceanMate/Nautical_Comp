
class Constants:
    # vertical motor pins
    frontVerticalMotorPin = 0
    backVerticalMotorPin = 1

    # horizontal motor pins
    frontLeftMotorPin = 2
    frontRightMotorPin = 3
    backLeftMotorPin = 4
    backRightMotorPin = 5

    # math scaling function 
    def map(x: float, in_min: float, in_max: float, out_min: float, out_max: float) -> float:
        return (x -in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
    
    def clamp(n, smallest, largest): return max(smallest, min(n, largest))
