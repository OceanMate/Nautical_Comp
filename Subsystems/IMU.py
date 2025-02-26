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

    def getGyroData(self):
        return self.sensor.gyro

    def periodic(self):
        #FOR DEBUG
        #print("Gyro X:%.2f, Y: %.2f, Z: %.2f radians/s" % (self.getGyroData()))
        
        self.comsThead.set_IMU_data(self.getGyroData())
           
    def end(self):
        pass