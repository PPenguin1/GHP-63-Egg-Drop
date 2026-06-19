from time import sleep

import gpiozero 
import odometry
import pidcontroller
from gpiostepper import Stepper

target_decceleration = 0

motor = Stepper([2, 3, 4, 17],  64)


def set_position(position):
    motor.step(position - motor.step_number)

def get_position():
    return motor.step_number

def set_speed(speed):
    motor.set_speed(speed)

while True:
    if odometry.get_error < 3:
        target_decceleration = odometry.get_velocity() / ((odometry.get_error() - 1) / odometry.get_velocity())
        pid = pidcontroller(0, 0, 0, target_decceleration)
        set_position(pid.update(odometry.get_acceleration(), 0.01))
        sleep(0.01)
        

