import cv2 as cv
import numpy
import time
from vision import findClickPositions
import dxcam


camera = dxcam.create()

while True:

    #Captures the time at the start of the loop
    last_time = time.time()

    # Get raw pixels from the screen, save it to a Numpy array
    img = numpy.array(camera.grab())
    img = cv.cvtColor(img, cv.COLOR_BGRA2BGR)
    img = img[...,:3]

    # Display the picture
    #cv.imshow("OpenCV/Numpy normal", img)
    findClickPositions("NEW.jpg", img, 0.4, 'rectangles')

    #Prints FPS
    print(f"fps: {1 / (time.time() - last_time)}")


    

    
    '''CODE ADD HERE'''






    # Press "q" to quit
    if cv.waitKey(25) & 0xFF == ord("q"):
        cv.destroyAllWindows()
        break
