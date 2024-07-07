import cv2 as cv
import numpy as np
import time
from vision import Vision
import dxcam

#initializes video
camera = dxcam.create()

#Creates an instances of the Vision class from vision.py
vision = Vision()

camera.start(target_fps=60)  # threaded

while True:

    #Captures the time at the start of the loop
    last_time = time.time()

    # Get raw pixels from the screen, save it to a Numpy array
    img = np.array( camera.get_latest_frame())

    # Display the picture
    #Calls the class from vision.py
    vision.find(img)




    
    '''CODE ADD HERE'''





    #Prints FPS
    print(f"fps: {1 / (time.time() - last_time)}")

    # Press "q" to quit
    if cv.waitKey(30) & 0xFF == ord("q"):
        cv.destroyAllWindows()
        camera.stop()
        break
