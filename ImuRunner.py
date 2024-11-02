import time
import board
import busio
from adafruit_lsm6ds.lsm6ds33 import LSM6DS33
from IMU import IMU

i2c = busio.I2C(board.SCL, board.SDA)
sensor = LSM6DS33(i2c)

imu = IMU

imu.classes

while True:
    
    imu.runLoop
    
    time.sleep(0.5)