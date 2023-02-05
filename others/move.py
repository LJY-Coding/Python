import pyautogui as pag
import random
import time

while True:
    x = random.randint(600, 700)
    y = random.randint(200, 600)
    pag.moveTo(x, y, 0.5)
    pag.click(x, y, clicks=1, interval=10, button='left')
    time.sleep(10)