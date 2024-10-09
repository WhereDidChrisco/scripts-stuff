# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import pyautogui as py
import time
import board
import adafruit_MPU6050

# i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
mpu = adafruit_MPU6050.MPU6050(i2c)  #


def mousePosition():
    centerPosition = py.center((0, 0, 1920, 1080))  # Finds the center of a 1920x1080 screen
    print(centerPosition)  # Prints the center of the screen


def mouseLeft():  # Moves mouse cursor to the left until desired
    position = py.position()  # Gets current mouse position
    print(position)
    xPosition = position[0] + 100
    print(xPosition)
    py.moveTo(str(position[0]+100))


while True:
    mpu_accel = '%.2f, %.2f, %.2f' % mpu.acceleration
    mpu_a = '%.2f' % mpu.acceleration[0]
    mpu_b = '%.2f' % mpu.acceleration[1]
    mpu_c = '%.2f' % mpu.acceleration[2]

    mpu_gyro = '%.2f, %.2f, %.2f' % mpu.gyro
    mpu_d = '%.2f' % mpu.gyro[0]
    mpu_e = '%.2f' % mpu.gyro[1]
    mpu_f = '%.2f' % mpu.gyro[2]

    mpu_temp = '%.2f C' % mpu.temperature

    print(mpu_accel)
    time.sleep(2)
    print(mpu_a, mpu_b, mpu_c)
    time.sleep(2)
    print(mpu_gyro)
    time.sleep(2)
    print(mpu_d, mpu_e, mpu_f)
    time.sleep(2)
    print(mpu_temp)
    time.sleep(2)

    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % mpu.acceleration)
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % mpu.gyro)
    print("Temperature: %.2f C" % mpu.temperature)
    print("")
    time.sleep(5)
