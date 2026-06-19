from time import sleep

# import gpiozero 
import odometry
import pidcontroller
from gpiostepper import Stepper
import main

target_decceleration = 0

motor = Stepper([4, 17, 27, 22],  64)

full_brake = 5000
full_release = -5000

def set_position(position):
    motor.step(position - motor.step_number)

def get_position():
    return motor.step_number

def set_speed(speed):
    motor.set_speed(speed)

while True:
    if odometry.get_error() < 1.5:
        set_position(full_brake) 
        sleep(5)
        if(odometry.get_acceleration < 0.1):
            set_position(full_brake - 1000)
            if abs(main.cX) < 10 and abs(main.cY) < 10:
                set_position(full_brake)  # Adjust the threshold as needed
            sleep(0.01)
    # elif odometry.get_error() < 3:
    #     target_decceleration = odometry.get_velocity() / ((odometry.get_error() - 1) / odometry.get_velocity())
    #     pid = pidcontroller(0, 0, 0, target_decceleration)
    #     set_position(pid.update(odometry.get_acceleration(), 0.01))
    #     sleep(0.01) 
    
