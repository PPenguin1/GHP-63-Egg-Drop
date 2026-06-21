from time import sleep

import odometry
from gpiostepper import Stepper
import main

target_decceleration = 0

motor = Stepper([4, 17, 27, 22],  64)

full_brake = 2500
full_release = -5000

def set_position(position):
    motor.step(position - motor.step_number)

def get_position():
    return motor.step_number

def set_speed(speed):
    motor.set_speed(speed)

set_position(2500)
while True:
    if odometry.get_error() < 1.5:
        set_position(full_brake) 
        sleep(5)
        if(odometry.get_acceleration < 0.1):
            set_position(-1000)
            if abs(main.cX) < 10 and abs(main.cY) < 10:
                set_position(full_brake)  # Adjust the threshold as needed
            sleep(0.01)
    
