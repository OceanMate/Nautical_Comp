import RPi.GPIO as GPIO
from Constants import Constants



class BilgePumpMotor:
    def __init__(self, motorIDs):
        GPIO.setmode(GPIO.BCM)
        self.forwardID = motorIDs.forward
        self.backwardID = motorIDs.backward
        self.speedID = motorIDs.speed
        
        GPIO.setup(self.forwardID, GPIO.OUT)
        GPIO.setup(self.backwardID, GPIO.OUT)
        GPIO.setup(self.speedID, GPIO.OUT)
        # Set up the PWM on pin #speedID at 50Hz
        self.pwm = GPIO.PWM(self.speedID, 500)
        self.pwm.start(0)
    


    # input power is a number between -1 and 1
    def set_power(self, power):
        # set the direction of the motor
        if power < 0:
            GPIO.output(self.forwardID, GPIO.LOW)
            GPIO.output(self.backwardID, GPIO.HIGH)
        else:
            GPIO.output(self.forwardID, GPIO.HIGH)
            GPIO.output(self.backwardID, GPIO.LOW)

        # set the speed of the motor
        speed = Constants.map(abs(power), 0, 1, 0, 100);
        self.pwm.ChangeDutyCycle(speed)
        
