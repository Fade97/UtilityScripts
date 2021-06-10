import pyautogui
import time

i = 0

# Type in your start position of the cursor (X, Y)
posX = 881
posY = 459

# Comment out when done getting coordinates
while True:
    print(pyautogui.position())

time.sleep(2)
pyautogui.FAILSAFE = True
while i < 70:

    # Put in the position of the upper left corner of the desired screenshot area and the width / height
    #                                         x    y    w     h
    screenshot = pyautogui.screenshot(region=(719, 113, 1000, 900)).save(
        'scanImage' + str(i) + '.jpg')
    i += 1

    # time.sleep(0.2)

    pyautogui.moveTo(posX, posY, 0.2)
    pyautogui.dragTo(posX + 120, posY + 3, 0.2)
