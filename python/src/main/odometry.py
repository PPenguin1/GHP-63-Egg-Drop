import mpu6050 
from time import sleep

accelerometer = mpu6050(0x68)

velocity = 0
position = 0

target_position = 10

def get_acceleration():
    return accelerometer.get_accel_data()

def get_gyro():
    return accelerometer.get_gyro_data()

def get_error():
    return target_position - position

def is_at_target():
    return abs(get_error()) < 0.1

while True:
    accel_data = get_acceleration()
    velocity += accel_data['x'] * 0.01  # Assuming a time step of 0.01 seconds
    position += velocity * 0.01  # Update position based on velocity
    sleep(0.01)
