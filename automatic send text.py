import pyautogui
import time
a=1
while a<=4:
    time.sleep(1)
    pyautogui.typewrite("This project  automatically send some text to someone")

    time.sleep(1)
    pyautogui.press('enter')
    a+=1
