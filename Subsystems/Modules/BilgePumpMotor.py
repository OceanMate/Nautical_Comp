from gpiozero import LED
from gpiozero import PWMLED
from Constants import Constants
import time


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
        
        # acceleration smoothing variables
        self.actualPower = 0
        self.time_between_steps = 0.1
        self.lastStep = time.time()
        
    
    def update(self):
        # acceleration smoothing for the motor
        # using time to update based on time not cycles
        if(time.time() - self.lastStep >= self.time_between_steps):
            
            if(self.actualPower < self.desiredPower):
                self.actualPower += 0.01
            elif(self.actualPower > self.desiredPower):
                self.actualPower -= 0.01
            self.lastStep = time.time()
            self.set_power_real(self.actualPower)
        pass
    
    def set_power(self, power):
        power = Constants.clamp(power,0,1)
        self.desiredPower = power

    # input power is a number between -1 and 1
    def set_power_real(self, power):
        # set the direction of the motor
        if power < 0:
            self.forward.value = 0
            self.backward.value = 1
        else:
            self.forward.value = 1
            self.backward.value = 0

        # set the speed of the motor
        power = abs(power)
        power = Constants.clamp(power,0,1)
        self.speed.value = power
        
