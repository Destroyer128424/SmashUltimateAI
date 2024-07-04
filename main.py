import cv2 as cv
import numpy
import time
import mss



with mss.mss() as sct:

    # Part of the screen to capture
    monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}


    while True:

        #Captures the time at the start of the loop
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(monitor))

        # Display the picture
        cv.imshow("OpenCV/Numpy normal", img)

        #Prints FPS
        print(f"fps: {1 / (time.time() - last_time)}")





        '''CODE ADD HERE'''






        # Press "q" to quit
        if cv.waitKey(25) & 0xFF == ord("q"):
            cv.destroyAllWindows()
            break
