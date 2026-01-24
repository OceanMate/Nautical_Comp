from Subsystems.Subsystem import Subsystem

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
import adafruit_bno055
import board
from transmission.ComsThread import ComsThread

class IMU(Subsystem):
    def __init__(self):
        
        i2c = board.I2C() # uses board.SCL and board.SDA
        self.sensor = adafruit_bno055.BNO055_I2C(i2c)

        self.acceleration = []
        self.gyro = []
        self.comsThead = ComsThread()

    def periodic(self):
        raw_quat = self.sensor.quaternion
        
        # reorder from (w, x, y, z) to (x, y, z, w)
        quanterion = (raw_quat[1], raw_quat[2], raw_quat[3], raw_quat[0])
        self.comsThead.set_IMU_data(quanterion)
           
    def end(self):
        pass