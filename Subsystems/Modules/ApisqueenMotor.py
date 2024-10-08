import RPi.GPIO as GPIO

from time import sleep

class ApisqueenMotor:
    def __init__(self,id):
        
        # Stops all warnings from appearing
        GPIO.setwarnings(False)
        # We name all the pins on BOARD mode
        GPIO.setmode(GPIO.BOARD)
        # Set an output for the PWM Signal
        GPIO.setup(id, GPIO.OUT)
        # Set up the  PWM on pin #16 at 50Hz
        self.pwm = GPIO.PWM(id, 50)


    
    def writeMicroseconds(self, microseconds):
        period = 20  # Period in milliseconds for 50Hz
        duty_cycle = (microseconds / 1000) / period * 100  # Convert to percentage
        self.pwm.ChangeDutyCycle(duty_cycle)