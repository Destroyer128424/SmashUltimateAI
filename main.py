import cv2 as cv
import numpy
import time
from vision import Vision
import dxcam


camera = dxcam.create()
vision = Vision('Mario.jpg')
camera.start(target_fps=60)  # threaded

while True:

    #Captures the time at the start of the loop
    last_time = time.time()

    # Get raw pixels from the screen, save it to a Numpy array
    img = numpy.array( camera.get_latest_frame())
    img = cv.cvtColor(img, cv.COLOR_BGRA2BGR)
    img = img[...,:3]

    # Display the picture
    #cv.imshow("OpenCV/Numpy normal", img)
    points = vision.find(img, 0.7, 'rectangles')

    #Prints FPS
    print(f"fps: {1 / (time.time() - last_time)}")


    
    '''CODE ADD HERE'''



    # Press "q" to quit
    if cv.waitKey(25) & 0xFF == ord("q"):
        cv.destroyAllWindows()
        camera.stop()
        break
