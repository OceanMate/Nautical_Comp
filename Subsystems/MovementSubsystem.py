from Subsystems.Subsystem import Subsystem
from Subsystems.Modules.ApisqueenMotor import ApisqueenMotor
from Subsystems.Modules.BilgePumpMotor import BilgePumpMotor

from Constants import Constants
from receive_commands import receive_commands
import RPi.GPIO as GPIO

class MovementSubsystem(Subsystem):
    def __init__(self):
        super().__init__()

        GPIO.setmode(GPIO.BCM)
        verticalMotors = []
        # Create vertical motors
        #verticalMotors.append(ApisqueenMotor(Constants.frontVerticalMotorPin))
        #verticalMotors.append(ApisqueenMotor(Constants.backVerticalMotorPin))

        self.horizontalMotors = []
        # Create horizontal motors
        self.horizontalMotors.append(BilgePumpMotor(Constants.mflForwardID, Constants.mflBackwardID, Constants.mflSpeedID))
        self.horizontalMotors.append(BilgePumpMotor(Constants.mfrForwardID, Constants.mfrBackwardID, Constants.mfrSpeedID))
        self.horizontalMotors.append(BilgePumpMotor(Constants.mbrForwardID, Constants.mbrBackwardID, Constants.mbrSpeedID))
        self.horizontalMotors.append(BilgePumpMotor(Constants.mblForwardID, Constants.mblBackwardID, Constants.mblSpeedID))
        
        # Set the speed of the motors to 0
        for motor in self.verticalMotors:
            motor.set_power(0)

        for motor in self.horizontalMotors:
            motor.set_power(0)
            
        
                        
                    

    def periodic(self):
        #motorData = receive_commands().motorData

        # Set the speed of the vertical motors from the motor data
        #for motor in self.verticalMotors:
        #    motor.set_power(1)

        for motor in self.horizontalMotors:
            motor.set_power(1)
            
        
            
            
    def end(self):
        GPIO.cleanup()
        
            


