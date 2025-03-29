import time
from Subsystems.Subsystem import Subsystem
from Subsystems.Modules.ApisqueenMotor import ApisqueenMotor

from Constants import Constants
from transmission.ComsThread import ComsThread

class MovementSubsystem(Subsystem):
    def __init__(self):
        super().__init__()
        
        pca = Constants.pca

        self.verticalMotors = []
        # Create vertical motors
        self.verticalMotors.append(ApisqueenMotor(Constants.frontVerticalMotorPin, pca))
        #self.verticalMotors.append(ApisqueenMotor(Constants.backVerticalMotorPin, pca))

        self.horizontalMotors = []
        # Create horizontal motors
        self.horizontalMotors.append(ApisqueenMotor(Constants.frontLeftMotorPin, pca))
        self.horizontalMotors.append(ApisqueenMotor(Constants.frontRightMotorPin, pca))
        self.horizontalMotors.append(ApisqueenMotor(Constants.backRightMotorPin, pca))
        self.horizontalMotors.append(ApisqueenMotor(Constants.backLeftMotorPin, pca))
        

        # Set the speed of the motors to 0 and wait to unlock the motors
        for motor in self.verticalMotors:
            motor.emergency_stop()
        for motor in self.horizontalMotors:
            motor.emergency_stop()
        
        time.sleep(5)
        print("motor should be unlocked")
            
        self.server = ComsThread()       
        
                    

    def periodic(self):
        # print(self.server.get_horizontal_motors())
        linearSpeeds = self.server.get_horizontal_motors()
        verticalSpeeds = self.server.get_vertical_motors()
        
        # Set the speed of the vertical motors from the motor data
        i = 0
        for motor in self.verticalMotors:
            motor.set_power(verticalSpeeds[i])
            motor.update()
            i += 1
            
        i = 0
        for motor in self.horizontalMotors:
            motor.set_power(linearSpeeds[i])
            motor.update()
            i += 1
        
            
            
    def end(self):
        for motor in self.verticalMotors:
            motor.emergency_stop()
        for motor in self.horizontalMotors:
            motor.emergency_stop()




