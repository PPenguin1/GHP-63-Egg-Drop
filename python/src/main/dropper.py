import gpiozero
import odometry
import main

motor = gpiozero.Servo(18)

while True:
    if abs(main.cX) < 10 and abs(main.cY) < 10:
        motor.max()
    else:
        motor.min()
