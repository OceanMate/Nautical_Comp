from Constants import Constants
from Subsystems.Modules.ApisqueenMotor import ApisqueenMotor

class main:
    def __init__(self):
        motor = ApisqueenMotor(Constants.frontVerticalMotorPin)
        motor.writeMicroseconds(1500)

    