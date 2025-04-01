from Subsystems.Subsystem import Subsystem
from Subsystems.Modules.Servo import Servo

from Constants import Constants
from transmission.ComsThread import ComsThread

class ClawSubsystem(Subsystem):
    def __init__(self):
        super().__init__()
        
        pca = Constants.pca
                # Initialize claw motors here
        self.clampMotor = Servo(Constants.clawClampMotorPin, pca)
        self.rollMotor = Servo(Constants.clawRollMotorPin, pca)
        
        self.clampMotor.stop()
        self.rollMotor.stop()
        
        self.server = ComsThread()

    def periodic(self):
        clamp_power = self.server.get_claw_clamp()
        roll_power = self.server.get_claw_roll()
                 
        # Update claw motor state if needed
        self.clampMotor.set_power(clamp_power)
        self.rollMotor.set_power(roll_power)
        
    def end(self):
        self.clampMotor.stop()
        self.rollMotor.stop()