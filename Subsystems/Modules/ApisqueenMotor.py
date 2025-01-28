from time import sleep
from gpiozero import PWMLED

class ApisqueenMotor:
    def __init__(self, id):
        self.id = id
        
        self.motor = PWMLED(pin=self.id, frequency=50)
        print(self.motor.frequency)
        #Apisqueen Motors need to be set up to there neutral position
        self.stop()
        sleep(3)
       

    # input power is a number between -1 and 1
    def set_power(self, power):
        # pulse_width is in microseconds
        # pulse_width should be between 1000 and 2000
        
        # map power from -1 to 1 to 0.05 to 0.1
        map_power = (power + 1) / 2 * 0.025 + 0.05
        
        self.motor.value = map_power

    def stop(self):
        self.set_power(0.075)


    
 
