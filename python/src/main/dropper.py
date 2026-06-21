import gpiozero
import main

motor = gpiozero.Servo(18)

while True:
    if abs(main.cX) < 100 and abs(main.cY) < 100:
        motor.max()
    else:
        motor.min()
