
import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture

#Allows access to OS files
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Calls the Class that captures our screen from windowcapture.py
wincap = WindowCapture('yuzu 1734')


#Allows us to see FPS
loop_time = time()


#This loop captures 
while(True):


    #Screen Capture
    screenshot = wincap.get_screenshot()
    cv.imshow('Computer Vision', screenshot)

    #Shows us FPS
    print('FPS {}'.format(1/(time() - loop_time)))
    loop_time = time()


    #CODE ONLY QUITS IF 'q' IS PRESSED
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

    

#End
print('Done.')