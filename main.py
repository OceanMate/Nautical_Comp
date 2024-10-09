from Constants import Constants
from Subsystems.Modules.ApisqueenMotor import ApisqueenMotor
from Subsystems.MovementSubsystem import MovementSubsystem


class main:
    def __init__(self):
        motor = ApisqueenMotor(Constants.frontVerticalMotorPin)
        motor.writeMicroseconds(1500)
        subsystems = {}
        subsystems["Movement"] = MovementSubsystem()

    