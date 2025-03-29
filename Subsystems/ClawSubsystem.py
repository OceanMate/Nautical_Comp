from Subsystems.Subsystem import Subsystem
from Subsystems.Modules.Servo import Servo

from Constants import Constants
from transmission.ComsThread import ComsThread

class ClawSubsystem(Subsystem):
    def __init__(self):
        super().__init__()
        
        pca = Constants.pca
        
        print("am here")
        # Initialize claw motors here
        #self.clampMotor = Servo(Constants.clawClampMotorPin, pca)
        self.rollMotor = Servo(Constants.clawRollMotorPin, pca)
        print("am here")
        
        #self.clampMotor.set_power(0)  # Set initial power to 0
        self.rollMotor.set_power(0)  # Set initial power to 0
        
        self.server = ComsThread()

    def periodic(self):
        clamp_power = self.server.get_claw_clamp()
        roll_power = self.server.get_claw_roll()
        
        clamp_power  =1
        roll_power =1
         
        # Update claw motor state if needed
        #self.clampMotor.set_power(clamp_power)
        self.rollMotor.set_power(roll_power)
        
    def end(self):
        self.stop_claw()  # Ensure claw is stopped when ending the subsystem
        pass