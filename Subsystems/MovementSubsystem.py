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

        horizontalMotors = []
        # Create horizontal motors
        horizontalMotors[0] = ApisqueenMotor(Constants.mflForwardID, Constants.mflBackwardID, Constants.mflSpeedID)
        horizontalMotors[1] = ApisqueenMotor(Constants.mfrForwardID, Constants.mfrBackwardID, Constants.mfrSpeedID)
        horizontalMotors[2] = ApisqueenMotor(Constants.mbrForwardID, Constants.mbrBackwardID, Constants.mbrSpeedID)
        horizontalMotors[3] = ApisqueenMotor(Constants.mblForwardID, Constants.mblBackwardID, Constants.mblSpeedID)
        

    def periodic(self):
        motorData = receive_commands().motorData

        # Set the speed of the vertical motors from the motor data
        i = 0
        while i < self.verticalMotors.length:
            self.verticalMotors[i].set_power(motorData[i])
            i += 1

        # Set the speed of the horizontal motors from the motor data
        i = 0
        while i < self.horizontalMotors.length:
            self.horizontalMotors[i].set_power(motorData[i + 2])
            i += 1
            


