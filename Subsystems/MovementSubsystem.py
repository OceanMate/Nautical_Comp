from Subsystems.Subsystem import Subsystem
from Subsystems.Modules.ApisqueenMotor import ApisqueenMotor
from Subsystems.Modules.BilgePumpMotor import BilgePumpMotor

from Constants import Constants
from server import ROVServer
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
        self.horizontalMotors.append(BilgePumpMotor(Constants.mfl))
        self.horizontalMotors.append(BilgePumpMotor(Constants.mfr))
        self.horizontalMotors.append(BilgePumpMotor(Constants.mbr))
        self.horizontalMotors.append(BilgePumpMotor(Constants.mbl))
        
        # Set the speed of the motors to 0
        for motor in self.verticalMotors:
            motor.set_power(0)

        for motor in self.horizontalMotors:
            motor.set_power(0)
            
        self.sever = ROVServer()
            
        
                        
                    

    def periodic(self):
        motorData = self.server.motor_data

        # Set the speed of the vertical motors from the motor data
        #for motor in self.verticalMotors:
        #    motor.set_power(1)
        i = 0;
        for motor in self.horizontalMotors:
            motor.set_power(motorData[i])
            i += 1
            
        
            
            
    def end(self):
        GPIO.cleanup()
        
            


