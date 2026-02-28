import board
import busio
import adafruit_pca9685

class Constants:
    # horizontal motor pins
    frontLeftMotorPin = 0
    frontRightMotorPin = 1
    backLeftMotorPin = 2
    backRightMotorPin = 3
    
    # vertical motor pins
    frontLeftVerticalMotorPin = 4
    frontRightVerticalMotorPin = 5
    backVerticalMotorPin = 6
    
    # claw motor pins
    clawRollMotorPin = 7
    clawClampMotorPin = 8
    
    #i2c = busio.I2C(board.SCL, board.SDA)
    #pca = adafruit_pca9685.PCA9685(i2c)
    #pca.frequency = 50

    # math scaling function 
    @staticmethod
    def map(x: float, in_min: float, in_max: float, out_min: float, out_max: float) -> float:
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    
    @staticmethod
    def clamp(n, smallest, largest): return max(smallest, min(n, largest))
