import RPi.GPIO as GPIO
from time import sleep
from Constants import Constants

class ApisqueenMotor:
    def __init__(self, id):
        self.id = id
        
        GPIO.setup(self.id, GPIO.OUT)
        self.pwm = GPIO.pwm(self.id,100)
        self.pwm.start(0)
        #Apisqueen Motors need to be set up to there neutral position
        self.stop()
        sleep(1)
       

    # input power is a number between -1 and 1
    def set_power(self, power):
        speed = Constants.map(abs(power), -1, 1, 10, 20);
        # pulse_width is in microseconds
        # pulse_width should be between 1000 and 2000
        self.GPIO.output(self.id, speed)

    def stop(self):
        self.set_power(0)


    
 
