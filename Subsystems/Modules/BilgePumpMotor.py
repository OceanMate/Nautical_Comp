from gpiozero import LED
from gpiozero import PWMOutputDevice
from Constants import Constants
import time
import board
import busio
import adafruit_pca9685


class BilgePumpMotor:
    def __init__(self, motorIDs):
        self.forwardID = motorIDs.forward
        self.backwardID = motorIDs.backward
        self.speedID = motorIDs.speed
         
        # I hate gpiozero need to make everything a pwmled for some reason
        # led doesn't work
        self.forward = PWMOutputDevice(self.forwardID)
        self.backward = PWMOutputDevice(self.backwardID)
        
        i2c = busio.I2C(board.SCL, board.SDA)
        self.pca = adafruit_pca9685.PCA9685(i2c)
        self.pca.frequency = 100

        self.speed_channel = self.pca.channels[self.speedID]
        
        # acceleration smoothing variables
        self.actualPower = 0
        self.time_between_steps = 0.05
        self.lastStep = time.time()
        
    
    def update(self):
        # acceleration smoothing for the motor
        # using time to update based on time not cycles
        if(time.time() - self.lastStep >= self.time_between_steps):
            if(abs(self.desiredPower)-abs(self.actualPower) < 0.1):
                self.actualPower = self.desiredPower
            elif(self.actualPower < self.desiredPower):
                self.actualPower += 0.1
            elif(self.actualPower > self.desiredPower):
                self.actualPower -= 0.1
            self.lastStep = time.time()
            self.set_power_real(self.actualPower)
        pass
    
    def set_power(self, power):
        power = Constants.clamp(power,-1,1)
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
        power_16bit = int(power * 65535)

        self.speed_channel.duty_cycle = power_16bit
        
