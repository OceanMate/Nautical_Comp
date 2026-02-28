import time
from Subsystems.Subsystem import Subsystem
from Subsystems.Modules.ApisqueenMotor import ApisqueenMotor

from Constants import Constants
from transmission.ComsThread import ComsThread

class MovementSubsystem(Subsystem):
    def __init__(self):
        super().__init__()
        
        print("Setting up motors")
        pca = Constants.pca
        print("PCA setup complete")

        self.verticalMotors = []
        # Create vertical motors
        try:
            self.verticalMotors.append(ApisqueenMotor(Constants.frontLeftVerticalMotorPin, pca))
            self.verticalMotors.append(ApisqueenMotor(Constants.frontRightVerticalMotorPin, pca))
            self.verticalMotors.append(ApisqueenMotor(Constants.backVerticalMotorPin, pca))
        except:
            print("Error setting up vertical motors")

        self.horizontalMotors = []
        # Create horizontal motors
        try:
            self.horizontalMotors.append(ApisqueenMotor(Constants.frontLeftMotorPin, pca))
        except:
            print("Error setting up front left motor")
        try:
            self.horizontalMotors.append(ApisqueenMotor(Constants.frontRightMotorPin, pca))
        except:
            print("Error setting up front right motor")
        try:
            self.horizontalMotors.append(ApisqueenMotor(Constants.backRightMotorPin, pca))
        except:
            print("Error setting up back right motor")
        try:
            self.horizontalMotors.append(ApisqueenMotor(Constants.backLeftMotorPin, pca))
        except:
            print("Error setting up back left motor")
        

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
            #motor.set_power(1)
            motor.update()
            i += 1
            
        i = 0
        for motor in self.horizontalMotors:
            motor.set_power(linearSpeeds[i])
            #motor.set_power(1)
            motor.update()
            i += 1
        
            
            
    def end(self):
        for motor in self.verticalMotors:
            motor.emergency_stop()
        for motor in self.horizontalMotors:
            motor.emergency_stop()




