from Subsystem import Subsystem
from Modules.ApisqueenMotor import ApisqueenMotor
from Constants import Constants
from receive_commands import receive_commands

class MovementSubsystem(Subsystem):
    def __init__(self):
        super().__init__()
        verticalMotors = []
        verticalMotors[0] = ApisqueenMotor(Constants.frontVerticalMotorPin)
        verticalMotors[1] = ApisqueenMotor(Constants.backVerticalMotorPin)
        

    def periodic(self):
        
        self.verticalMotors[0].set_pulse_width(2000)
        self.verticalMotors[1].set_pulse_width(2000)

        return
