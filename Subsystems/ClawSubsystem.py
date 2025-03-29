from Subsystems.Subsystem import Subsystem
from Subsystems.Modules.Servo import Servo

from Constants import Constants
from transmission.ComsThread import ComsThread
import board
import busio
import adafruit_pca9685

class ClawSubsystem(Subsystem):
    def __init__(self):
        super().__init__()
        
        i2c = busio.I2C(board.SCL, board.SDA)
        pca = adafruit_pca9685.PCA9685(i2c)
        pca.frequency = 50
        
        # Initialize claw motors here
        self.clampMotor = Servo(Constants.clawMotorPin, pca)
        self.rollMotor = Servo(Constants.rollMotorPin, pca)
        
        self.clawMotor.set_power(0)  # Set initial power to 0
        self.rollMotor.set_power(0)  # Set initial power to 0
        
        self.server = ComsThread()

    def periodic(self):
        clamp_power = self.server.get_claw_clamp()
        roll_power = self.server.get_claw_roll()
        
        # Update claw motor state if needed
        self.clampMotor.set_power(clamp_power)
        self.rollMotor.set_power(roll_power)
        
    def end(self):
        self.stop_claw()  # Ensure claw is stopped when ending the subsystem
        pass