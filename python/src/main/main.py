import cv2
import keyboard
import matplotlib.widgets as widgets
import matplotlib.pyplot as plt


feed = cv2.VideoCapture(0)

imageSizeX = 640
imageSizeY = 480

# feed = cv2.resize(feed, (imageSizeX, imageSizeY))

hueMin = 0
hueMax = 37.2
saturationMin = 0
saturationMax = 73.1
valueMin = 40
valueMax = 255

# hueMinAx = plt.axes([0.25, 0.1, 0.65, 0.03])
# hueMaxAx = plt.axes([0.25, 0.15, 0.65, 0.03])
# saturationMinAx = plt.axes([0.25, 0.2, 0.65, 0.03])
# saturationMaxAx = plt.axes([0.25, 0.25, 0.65, 0.03])
# valueMinAx = plt.axes([0.25, 0.3, 0.65, 0.03])
# valueMaxAx = plt.axes([0.25, 0.35, 0.65, 0.03])

# hueMin = widgets.Slider(hueMinAx, 'Hue Min', 0, 255)
# hueMax = widgets.Slider(hueMaxAx, 'Hue Max', 0, 255)
# saturationMin = widgets.Slider(saturationMinAx, 'Saturation Min', 0, 255)
# saturationMax = widgets.Slider(saturationMaxAx, 'Saturation Max', 0, 255)
# valueMin = widgets.Slider(valueMinAx, 'Value Min', 0, 255)
# valueMax = widgets.Slider(valueMaxAx, 'Value Max', 0, 255)
while True:
    plt.ion()
    plt.show()
    plt.pause(0.001)
    if(keyboard.is_pressed('q')):
        break;

    _, frame = feed.read();

    frame = cv2.resize(frame, (imageSizeX, imageSizeY))

    if not _:
        print("Error: Could not read frame from camera feed.")
        continue;

    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frameHSV, (hueMin, saturationMin, valueMin), (hueMax, saturationMax, valueMax))
    # mask = cv2.inRange(frameHSV, (hueMin.val, saturationMin.val, valueMin.val), (hueMax.val, saturationMax.val, valueMax.val))

    contr = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    objectCntsAreas = []

    for i in contr[0]:
        M = cv2.moments(i)

        objectCntsAreas.append(M["m00"])

    if len(objectCntsAreas) > 0:
        # Find the largest (and theoretically closest) object
        maxValue = max(objectCntsAreas)

        maxObjectCntsIndex = objectCntsAreas.index(maxValue)

        # Find pixel position of object
        M = cv2.moments(contr[0][maxObjectCntsIndex])

        cX = int((M["m10"] / (M["m00"] + 0.001))) - (imageSizeX / 2)
        cY = int((M["m01"] / (M["m00"] + 0.001))) - (imageSizeY / 2)
        print("Object Position: " + str(cX) + ", " + str(cY))


    cv2.imshow("Mask", mask)
    cv2.imshow("Frame", frame)
    cv2.imshow("Frame HSV", frameHSV)
    cv2.waitKey(5);