import cv2
import urllib.request
import os
from django.conf import settings

class VideoCamera(object):
    def __init__(self):
        self.video=cv2.VideoCapture(0)
    def __del__(self):
        self.video.release()
    def frame(self):
        while True:
            px ,image=VideoCamera.__init__(self)
            cv2.imshow('Text detection',image)
            if cv2.waitKey(1)& 0xFF==ord('s'):
                cv2.imwrite('text1.png',image)
                break
            VideoCamera.__del__(self)

