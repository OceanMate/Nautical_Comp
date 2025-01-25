from gpiozero import LED
from gpiozero import PWMLED
from Constants import Constants


class BilgePumpMotor:
    def __init__(self, motorIDs):
        self.forwardID = motorIDs.forward
        self.backwardID = motorIDs.backward
        self.speedID = motorIDs.speed
         
        # I hate gpiozero need to make everything a pwmled for some reason
        # led doesn't work
        self.forward = PWMLED(self.forwardID)
        self.backward = PWMLED(self.backwardID)
        self.speed = PWMLED(self.speedID)
        
    


    # input power is a number between -1 and 1
    def set_power(self, power):
        # set the direction of the motor
        if power < 0:
            self.forward.value = 0
            self.backward.value = 1
        else:
            self.forward.value = 1
            self.backward.value = 0

        # set the speed of the motor
        power = abs(power)
        self.speed.value = power
        
