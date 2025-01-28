from time import sleep
from gpiozero import PWMLED, PWMOutputDevice

class ApisqueenMotor:
    def __init__(self, id):
        self.id = id
        
        self.motor = PWMOutputDevice(pin=self.id, frequency=50)
        print(self.motor.frequency)
        #Apisqueen Motors need to be set up to there neutral position
        self.stop()
        sleep(3)

    # input power is a number between -1 and 1
    def set_power(self, power):
        # pulse_width is in microseconds
        # pulse_width should be between 1000 and 2000
        
        # map power from -1 to 1 to 0.05 to 0.1
        map_power = (power + 1) * 0.025 + 0.05
        
        self.motor.value = map_power

    def stop(self):
        self.set_power(0.075)

import pigpio
import time

pi = pigpio.pi() #create pigpio object
LED_PIN = 18 # Define the GPIO port to which the LED is connected.
PWM_FREQUENCY = 50 #define the PWM frequency in Hz
PWM_range = 1000
PWM_DUTYCYCLE = 0 # Define PWM duty cycle, value range 0 (2) 55,
pi.set_mode(LED_PIN, pigpio.OUTPUT) #Set the GPIO port to output mode
pi.set_PWM_frequency(LED_PIN, PWM_FREQUENCY) #set PWM frequency
pi.set_PWM_range(LED_PIN, PWM_range) # set range 1000

pi.set_PWM_dutycycle(LED_PIN, 75) # set PWM duty cycle 75/1000=7.5 per cent
time.sleep(3) # delay 3s unlock successful

pi.set_PWM_dutycycle(LED_PIN, 100)
# Positive rotation 7.5%-10% duty cycle, the larger the duty cycle, the faster the positive rotation speed
time.sleep(15)

pi.set_PWM_dutycycle(LED_PIN, 60)
# Reverse The closer the duty cycle is to 5%, the faster the reversal speed is
time.sleep(5)

pi.set_PWM_dutycycle(LED_PIN, 75)
# Duty cycle
time.sleep(5)

    
 
