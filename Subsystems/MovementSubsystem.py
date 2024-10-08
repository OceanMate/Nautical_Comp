from Subsystem import Subsystem
from Modules.ApisqueenMotor import ApisqueenMotor
from Constants import Constants

class MovementSubsystem(Subsystem):
    def __init__(self):
        super().__init__()
        verticalMotors = []
        verticalMotors[0] = ApisqueenMotor(Constants.frontVerticalMotorPin)
        verticalMotors[1] = ApisqueenMotor(Constants.backVerticalMotorPin)

    def onEnable(self):
        return

    def periodic(self):
        return

    def onDisable(self):
        for motor in self.verticalMotors:
            motor.stop()
        return