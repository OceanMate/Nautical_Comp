import pigpio
from time import sleep

class ApisqueenMotor:
    def __init__(self, id):
        self.id = id
        self.pi = pigpio.pi()
        if not self.pi.connected:
            raise Exception("Could not connect to pigpio daemon")
        #Apisqueen Motors need to be set up to there neutral position
        self.stop()
        sleep(1)
       

    # pulse_width is in microseconds
    # pulse_width should be between 1000 and 2000
    def set_pulse_width(self, pulse_width):
        self.pi.set_servo_pulsewidth(self.id, pulse_width)

    def stop(self):
        self.pi.set_servo_pulsewidth(self.id, 1500)
        self.pi.stop()


    
 