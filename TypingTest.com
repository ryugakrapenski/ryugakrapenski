#NOTE THIS IS HIGHLY WIP, BUG FIXES ALONG WItH MANY OTHER FEATURES ARE STILL WORK IN PROGRESS

#FIRST TRIAL YOUTUBE LINK https://youtu.be/5RARMxSvRr8

import pytesseract
import pyautogui
from PIL import Image, ImageGrab
from pytesseract import *
import time
import keyboard


pytesseract.tesseract_cmd  = r'C:\Users\the80\AppData\Local\Programs\Tesseract-OCR\\tesseract'

time.sleep(5)

print('Finished waiting')


screenshot = ImageGrab.grab(bbox=(555, 130, 1230, 430)).convert('L')

output = pytesseract.image_to_string(screenshot)
matchfound = str(output)

print(matchfound)

keyboard.write(matchfound, 0.01)

time.sleep(2)

while True:

    if keyboard.is_pressed('delete'):
        exit(3)

    else:
        screenshot = ImageGrab.grab(bbox=(550, 230, 1230, 380)).convert('L')

        output = pytesseract.image_to_string(screenshot)
        matchfound = str(output)

        print(matchfound)

        keyboard.write(matchfound, 0.01)

        time.sleep(0.3)
