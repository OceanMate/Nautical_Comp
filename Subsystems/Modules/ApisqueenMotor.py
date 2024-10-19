import pigpio
from time import sleep
from Constants import Constants

class ApisqueenMotor:
    def __init__(self, id):
        self.id = id
        # Set up the pigpio 
        self.pi = pigpio.pi()
        if not self.pi.connected:
            raise Exception("Could not connect to pigpio daemon")
        #Apisqueen Motors need to be set up to there neutral position
        self.stop()
        sleep(1)
       

    # input power is a number between -1 and 1
    def set_power(self, power):
        speed = Constants.map(abs(power), -1, 1, 1000, 2000);
        # pulse_width is in microseconds
        # pulse_width should be between 1000 and 2000
        self.pi.set_servo_pulsewidth(self.id, speed)

    def stop(self):
        self.pi.set_servo_pulsewidth(self.id, 1500)


    
 