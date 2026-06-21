from mpu6050 import mpu6050 
import io
from time import sleep

velocity = 0
position = 0
accel = mpu6050(0x68)

file = io.open("accel_data.txt", "w")

target_decceleration = 0

target_position = 9

def get_acceleration():
    return accel.get_accel_data()

def get_gyro():
    return accel.get_gyro_data()

def get_error():
    return target_position - position

def is_at_target():
    return abs(get_error()) < 0.1

def get_position():
    return position

def get_velocity():
    return velocity

while True:
    accel_data = get_acceleration()
    velocity += accel_data['x'] * 0.01
    position += velocity * 0.01 
    file.write(f"{accel_data['x']}, {velocity}, {position}\n")
    sleep(0.01)

