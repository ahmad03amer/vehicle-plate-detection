import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('count.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
pytesseract

#############################################
#### Detecting Characters  ######
#############################################
hImg, wImg,_ = img.shape
boxes = pytesseract.image_to_data(img)
for x,b in enumerate(boxes.splitlines()):
      if x!=0:
            b = b.split()
            print(b)
            if len(b)==12:
                x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                cv2.putText(img,b[11],(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
                cv2.rectangle(img, (x,y), (x+w, y+h), (50, 50, 255), 2)
cv2.imshow('img', img)
cv2.waitKey(0)