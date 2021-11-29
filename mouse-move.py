import pyautogui
import time
i=0
while True:
    if i%2==0:
        pyautogui.moveRel(0,10)
    else:
        pyautogui.move.Rel(0,-10)
    i=i+1
    time.sleep(5)