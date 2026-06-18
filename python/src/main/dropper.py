import gpiozero
import odometry

motor = gpiozero.Motor(0, 0)

while True:
    if odometry.is_at_target():
        motor.forward()

