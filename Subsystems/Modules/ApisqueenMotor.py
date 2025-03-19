from Constants import Constants
import time


class ApisqueenMotor:
    def __init__(self, id, pca):
        self.motor_channel = pca.channels[id]
        
        # acceleration smoothing variables
        self.actualPower = 0
        self.desiredPower = 0
        
        self.time_between_steps = 0.001
        self.change_per_second = 2
        self.lastStep = time.time()

        
    # input power is a number between -1 and 1
    def set_power(self, power):
        self.desiredPower = Constants.clamp(power,-1,1)
    
    def _set_power_real(self, power):
        # pulse_width is in microseconds
        # pulse_width should be between 1000 and 2000
        self.desiredPower = Constants.clamp(power,-1,1)
        
        # map power from -1 to 1 to 0.05 to 0.1
        map_power = (power + 1) * 0.025 + 0.05
        
        # print(map_power)
        
        # convert map_power to a 16-bit value
        map_power_16bit = int(map_power * 65535)
        
        self.motor_channel.duty_cycle = map_power_16bit

    def update(self):
        # acceleration smoothing for the motor
        # using time to update based on time not cycles
        if time.time() - self.lastStep >= self.time_between_steps:
            step_change = self.change_per_second * (time.time() - self.lastStep)
            if abs(self.desiredPower - self.actualPower) < step_change:
                self.actualPower = self.desiredPower
            elif self.actualPower < self.desiredPower:
                self.actualPower += step_change
            elif self.actualPower > self.desiredPower:
                self.actualPower -= step_change
            self.lastStep = time.time()
            self._set_power_real(self.actualPower)

    def emergency_stop(self):
        self._set_power_real(0)

