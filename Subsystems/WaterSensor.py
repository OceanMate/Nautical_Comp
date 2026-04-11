import board
import RPi.GPIO as GPIO
from Constants import Constants 
from transmission.ComsThread import ComsThread

class Subsystem:
    def __init__(self):
        pass


class WaterSensor(Subsystem):

    def __init__(self):
        super().__init__()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Constants.waterSensorPin, GPIO.IN)
        self.comsThead = ComsThread()
        print("Water sensor initialized")

    def is_water_detected(self):
        print("Water detected: ")
        print(str(GPIO.input(Constants.waterSensorPin)))
        return GPIO.input(Constants.waterSensorPin)
    
    def periodic(self):
        try:
            GPIO.setmode(GPIO.BCM)
            # GPIO.setup(Constants.waterSensorPin, GPIO.IN)
            self.comsThead.set_water_data(self.is_water_detected())
        except Exception as e:
            print("Error occurred while setting water data: " + str(e))

    def end(self):
        GPIO.cleanup()