import cv2 as cv
from controls import *
import numpy as np
import dxcam
from windows_capture import WindowsCapture, Frame, InternalCaptureControl





#Load Trained Model
MarioCascade = cv.CascadeClassifier("Mario/Cascade/cascade.xml")


camera = dxcam.create()

camera.start(target_fps=60)


while True:


    #Reads the frames of the video.
    FrameData = np.array(camera.get_latest_frame())


    #Simpifies the Algorithim. Turns video to grayscale
    #GrayFrameData = cv.cvtColor(FrameData, cv.COLOR_BGR2GRAY)



    rect = MarioCascade.detectMultiScale(
        FrameData,
        scaleFactor=1.1,
        minNeighbors=1000,
        minSize=(30, 30),
        flags=cv.CASCADE_SCALE_IMAGE
    )
    

    for (x, y, w, h) in rect:
        cv.rectangle(FrameData, (x, y), (x+w, y+h), (0, 255, 0), 2)


    
    '''CODE ADD HERE'''






    FrameData = cv.cvtColor(FrameData, cv.COLOR_BGR2RGB)

    cv.imshow("Frame_final", FrameData)



    # Press "q" to quit
    if cv.waitKey(1) & 0xFF == ord("q"):
        cv.destroyAllWindows()
        camera.stop()
        break
