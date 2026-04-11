import board
import RPi.GPIO as GPIO
from Constants import Constants 
from transmission.ComsThread import ComsThread

class Subsystem:
    def __init__(self):
        pass


class WaterSensor(Subsystem):

    def __init__(self, pin):
        super().__init__()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Constants.waterSensorPin, GPIO.IN)
        self.comsThead = ComsThread()

    def is_water_detected(self):
        print("Water detected: " + str(GPIO.input(Constants.waterSensorPin)))
        return GPIO.input(Constants.waterSensorPin)
    
    def periodic(self):
        self.comsThead.set_water_data(self.is_water_detected())

    def end(self):
        GPIO.cleanup()