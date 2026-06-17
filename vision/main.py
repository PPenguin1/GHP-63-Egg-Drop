import cv2
import keyboard
import numpy as np
#import matplotlib.pyplot as plt


feed = cv2.VideoCapture(0)

hueMin = 0
hueMax = 255
saturationMin = 0
saturationMax = 255
valueMin = 0
valueMax = 255

while True:
    if(keyboard.is_pressed('q')):
        break;

    _, frame = feed.read();

    if not _:
        print("Error: Could not read frame from camera feed.")
        continue;

    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frameHSV, (hueMin, saturationMin, valueMin), (hueMax, saturationMax, valueMax))
    cv2.imshow("Mask", mask)
    cv2.imshow("Frame", frame)

    cv2.waitKey(5);
