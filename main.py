import cv2 as cv
import numpy as np
from vision import Vision
from controls import *
import dxcam

#initializes video
camera = dxcam.create()

#Creates an instances of the Vision class from vision.py
vision = Vision()

camera.start(target_fps=60)  # threaded

while True:

    # Get raw pixels from the screen, save it to a Numpy array
    #This is the screenshot data. Updates everytime the while loop runs
    img = np.array(camera.get_latest_frame(), dtype="uint8")

    # Display the picture
    #Calls the class from vision.py
    vision.find(img)




    
    '''CODE ADD HERE'''







    # Press "q" to quit
    if cv.waitKey(15) & 0xFF == ord("q"):
        cv.destroyAllWindows()
        camera.stop()
        break
