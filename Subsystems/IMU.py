import time
import board as board
import busio
from adafruit_lsm6ds.lsm6ds33 import LSM6DS33
from Subsystem import Subsystem



class IMU(Subsystem):
    
    def __init__(self):
        #INCLUDE THIS IN MAIN FUNCTION
        i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = LSM6DS33(i2c)

        self.acceleration = []
        self.gyro = []

    def periodic(self):
        #FOR DEBUG
        print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (self.sensor.acceleration))
        print("Gyro X:%.2f, Y: %.2f, Z: %.2f radians/s" % (self.sensor.gyro))
        
        #destroys info in array (hopefully)
        self.gyro.pop[0,1,2]
        self.acceleration.pop[0,1,2]
        
        #adds new info into array
        self.gyro.append [self.sensor.acceleration]
        self.acceleration.append[self.sensor.gyro]
        
        #(DEBUG) prints blank line for formatting
        print("")
        
        #sleep to stop from running too much
        time.sleep(0.02)
        
    def end(self):
        #nothing yet
        print("uhoh stinky")