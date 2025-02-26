import time
from Subsystems.Subsystem import Subsystem
from Subsystems.Modules.ApisqueenMotor import ApisqueenMotor

from Constants import Constants
from transmission.ComsThread import ComsThread

class MovementSubsystem(Subsystem):
    def __init__(self):
        super().__init__()

        self.verticalMotors = []
        # Create vertical motors
        self.verticalMotors.append(ApisqueenMotor(Constants.frontVerticalMotorPin))
        #self.verticalMotors.append(ApisqueenMotor(Constants.backVerticalMotorPin))

        self.horizontalMotors = []
        # Create horizontal motors
        self.horizontalMotors.append(ApisqueenMotor(Constants.frontLeftMotorPin))
        self.horizontalMotors.append(ApisqueenMotor(Constants.frontRightMotorPin))
        self.horizontalMotors.append(ApisqueenMotor(Constants.backRightMotorPin))
        self.horizontalMotors.append(ApisqueenMotor(Constants.backLeftMotorPin))
        

        # Set the speed of the motors to 0 and wait to unlock the motors
        for motor in self.verticalMotors:
            motor.set_power(0)

        for motor in self.horizontalMotors:
            motor.set_power(0)
        
        time.sleep(5)
            
        self.server = ComsThread()       
        
                    

    def periodic(self):
        #rint(self.server.get_horizontal_motors())
        linearSpeeds = self.server.get_horizontal_motors()
        verticalSpeeds = self.server.get_vertical_motors()
        
        # Set the speed of the vertical motors from the motor data
       # self.verticalMotors[0].set_power(1)
        for motor in self.verticalMotors:
            motor.set_power(0.5)
            
        i = 0
        for motor in self.horizontalMotors:
            motor.set_power(0.5)
            i += 1   
        
        
            
            
    def end(self):
        pass
        
            


