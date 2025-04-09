import board
import busio
import adafruit_pca9685

class Constants:
    # vertical motor pins
    frontVerticalMotorPin = 2
    backVerticalMotorPin = 1

    # horizontal motor pins
    frontLeftMotorPin = 4
    frontRightMotorPin = 3
    backLeftMotorPin = 5
    backRightMotorPin = 6
    
    # claw motor pins
    clawRollMotorPin = 7
    clawClampMotorPin = 0
    
    i2c = busio.I2C(board.SCL, board.SDA)
    pca = adafruit_pca9685.PCA9685(i2c)
    pca.frequency = 50

    # math scaling function 
    def map(x: float, in_min: float, in_max: float, out_min: float, out_max: float) -> float:
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    
    def clamp(n, smallest, largest): return max(smallest, min(n, largest))
