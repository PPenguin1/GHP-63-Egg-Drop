import gpiozero
import odometry

motor = gpiozero.Servo(18)

while True:
    if odometry.is_at_target():
        motor.max()
    else:
        motor.min()
