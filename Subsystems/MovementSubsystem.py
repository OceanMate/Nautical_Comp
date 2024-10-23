from Subsystems.Subsystem import Subsystem
from Subsystems.Modules.ApisqueenMotor import ApisqueenMotor
from Subsystems.Modules.BilgePumpMotor import BilgePumpMotor

from Constants import Constants
from receive_commands import receive_commands
from time import sleep


class MovementSubsystem(Subsystem):
    def __init__(self):
        super().__init__()
        verticalMotors = []
        # Create vertical motors
        #verticalMotors[0] = ApisqueenMotor(Constants.frontVerticalMotorPin)
        #verticalMotors[1] = ApisqueenMotor(Constants.backVerticalMotorPin)

        horizontalMotors = {}
        # Create horizontal motors
        horizontalMotors[0] = BilgePumpMotor(Constants.mflForwardID, Constants.mflBackwardID, Constants.mflSpeedID)
        horizontalMotors[1] = BilgePumpMotor(Constants.mfrForwardID, Constants.mfrBackwardID, Constants.mfrSpeedID)
        #horizontalMotors[2] = BilgePumpMotor(Constants.mbrForwardID, Constants.mbrBackwardID, Constants.mbrSpeedID)
        #horizontalMotors[3] = BilgePumpMotor(Constants.mblForwardID, Constants.mblBackwardID, Constants.mblSpeedID)
        while True:
                i = 0
                while i < len(horizontalMotors):
                    horizontalMotors[i].set_power(1)
                    sleep(.001)
                    #horizontalMotors[i].set_power(0)
                    #sleep(.001)
                    i += 1
                    

    def periodic(self):
        motorData = receive_commands().motorData

        # Set the speed of the vertical motors from the motor data
        i = 0
        while i < self.verticalMotors.length:
            self.verticalMotors[i].set_power(motorData[i])
            i += 1

        # Set the speed of the horizontal motors from the motor data
        i = 0
        while i < len(self.horizontalMotors):
            self.horizontalMotors[i].set_power(motorData[i + 2])
            i += 1
            


