import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)
position1 = pt.locateOnScreen("D:\Projects\PYTHON/smile.JPG", confidence=.8)
x = position1[0]
y = position1[1]


# gets message

def get_message():
    global x, y

    position = pt.locateOnScreen("D:\Projects\PYTHON/smile.JPG", confidence=.8)

    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=0.03)


get_message()
