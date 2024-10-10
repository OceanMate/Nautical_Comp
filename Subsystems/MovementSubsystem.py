from Subsystem import Subsystem
from Modules.ApisqueenMotor import ApisqueenMotor
from Constants import Constants
from receive_commands import receive_commands

class MovementSubsystem(Subsystem):
    def __init__(self):
        super().__init__()
        verticalMotors = []
        # Create vertical motors
        verticalMotors[0] = ApisqueenMotor(Constants.frontVerticalMotorPin)
        verticalMotors[1] = ApisqueenMotor(Constants.backVerticalMotorPin)
        

    def periodic(self):
        motorData = receive_commands.motorData

        # Set the speed of the vertical motors from the motor data
        i = 0
        while i < self.verticalMotors.length:
            self.verticalMotors[i].set_pulse_width(motorData[i])
            i += 1

