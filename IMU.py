import time
import board
import busio
from adafruit_lsm6ds.lsm6ds33 import LSM6DS33

i2c = busio.I2C(board.SCL, board.SDA)
sensor = LSM6DS33(i2c)

class IMU:
    
    def classes(self):
        
        self.acceleration = []
        self.gyro = []

    def runLoop(self):
 
        print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (sensor.acceleration))
        print("Gyro X:%.2f, Y: %.2f, Z: %.2f radians/s" % (sensor.gyro))
        
        self.gyro.pop[0]
        self.acceleration.pop[0]
        
        self.gyro.append [sensor.acceleration]
        self.acceleration.append[sensor.gyro]
        
        print("")