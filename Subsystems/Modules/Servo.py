from Constants import Constants

class Servo:
    def __init__(self, id, pca):
        self.motor_channel = pca.channels[id]
    
    def set_power(self, power):
        # pulse_width is in microseconds
        # pulse_width should be between 1000 and 2000
        Constants.clamp(power, -1, 1)
        
        # map power from -1 to 1 to 0.025 to 0.125
        map_power = (power + 1) * 0.05 + 0.025
                
        # convert map_power to a 16-bit value
        map_power_16bit = int(map_power * 65535)
        
        self.motor_channel.duty_cycle = map_power_16bit
        
    def stop(self):
        self.motor_channel.duty_cycle = 0
