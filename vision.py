import cv2 as cv
import gradio as gr
import numpy as np
import matplotlib.pyplot as plt
import dxcam


class Vision:


    def __init__(self):
        pass


    def find(self, img):

        #OpenCV prefers BGR
        img = cv.cvtColor(img, cv.COLOR_BGRA2BGR)
        #Removes alpha channels
        #img = img[...,:3] 





        """CODE HERE"""








        # Display the resulting frame
        cv.imshow("Frame_final", img)
