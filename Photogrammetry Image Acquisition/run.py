import pyautogui
import time

# Used for https://www.heroforge.com/


# Type in your start position of the cursor (X, Y)
posX = 881
posY = 459

# Put in the position of the upper left corner of the desired screenshot area and the width / height
screenRegionX = 499
screenRegionY = 120
screenRegionWidth = 1321
screenRegionHeight = 820

# Comment out when done getting coordinates
while True:
    print(pyautogui.position())

i = 0
time.sleep(2)
pyautogui.FAILSAFE = True
while i < 70:

    screenshot = pyautogui.screenshot(region=(screenRegionX, screenRegionY, screenRegionWidth, screenRegionHeight)).save(
        'scanImage' + str(i) + '.jpg')
    i += 1

    # time.sleep(0.2)

    pyautogui.moveTo(posX, posY, 0.2)
    pyautogui.dragTo(posX + 120, posY + 3, 0.2)
