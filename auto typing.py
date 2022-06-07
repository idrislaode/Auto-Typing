import time 
import mss
import numpy
import pytesseract
import pyautogui

top = 260
left = 425
width = 1155
height = 60

area = {'top': top, 'left': left, 'width': width, 'height': 60}

time.sleep(5)

with mss.mss() as sct:
    while True:
        im = numpy.asarray(sct.grab(area)) 

        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
        
        text = pytesseract.image_to_string(im)
        
        xMouse, yMouse = pyautogui.position()
        
        if(xMouse<left):
            print(text)
            pyautogui.write(text, interval = 0.015)
            pyautogui.write(' ', interval = 0.015) 
            time.sleep(0.15)

