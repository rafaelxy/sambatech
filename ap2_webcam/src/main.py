# -*- coding: UTF-8 -*-

"""
Created on 22 Dec 2012

@author: rcampos
"""

import cv2.cv as cv

OUTFILE = "output-webcam.avi"
WND_NAME = "Aperte qualquer tecla para fechar"
WAIT = 1
NO_KEY = -1
CAM_IX = 0

capture = cv.CaptureFromCAM(CAM_IX)
image = cv.QueryFrame(capture)

writer = cv.CreateVideoWriter(OUTFILE,
                              fourcc = 0,
                              fps = 8.0,
                              frame_size = cv.GetSize(image),
                              is_color = 1)

while cv.WaitKey(WAIT) == NO_KEY:
    image = cv.QueryFrame(capture)
    cv.WriteFrame(writer, image)
    cv.ShowImage(WND_NAME, image)

cv.DestroyWindow(WND_NAME)    

#import cv2.cv as cv
#
#cv.NamedWindow("camera", 1)
#capture = cv.CaptureFromCAM(0)
#
#while True:
#    img = cv.QueryFrame(capture)
#    cv.ShowImage("camera", img)
#    if cv.WaitKey(10) == 27:
#        break
#    
#    
#cv.DestroyWindow("camera")


"""
import cv

cv.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)
camera_index = 0
capture = cv.CaptureFromCAM(camera_index)

gx = gy = 1
grayscale = blur = canny = False

def repeat():
    global capture #declare as globals since we are assigning to them now
    global camera_index
    global gx, gy, grayscale, canny, blur
    frame = cv.QueryFrame(capture)
    # import pdb; pdb.set_trace()

    if grayscale:
        gray = cv.CreateImage(cv.GetSize(frame), frame.depth, 1)
        cv.CvtColor(frame, gray, cv.CV_RGB2GRAY)
        frame = gray
        
    if blur:
        g = cv.CreateImage(cv.GetSize(frame), cv.IPL_DEPTH_8U, frame.channels)
        cv.Smooth(frame, g, cv.CV_GAUSSIAN, gx, gy)
        frame = g
    
    if grayscale and canny:
        c = cv.CreateImage(cv.GetSize(frame), frame.depth, frame.channels)
        cv.Canny(frame, c, 10, 100, 3)
        frame = c
    cv.ShowImage("w1", frame)

    c = cv.WaitKey(10)
    if c==ord('='): #in "n" key is pressed while the popup window is in focus
        gx += 2
        gy += 2
    elif c == ord('-'):
        gx = max(1, gx-2)
        gy = max(1, gy-2)
    elif c == ord('x'):
        gx += 2
    elif c == ord('X'):
        gx = max(1, gx-2)
    elif c == ord('q'):
        exit(0)

    elif c == ord('b'):
        blur = not blur
    elif c == ord('g'):
        grayscale = not grayscale
    elif c == ord('c'):
        canny = not canny
    



while True:
    repeat()
"""


"""
import cv

cv.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)
camera_index = 0
capture = cv.CaptureFromCAM(camera_index)

def repeat():
    global capture #declare as globals since we are assigning to them now
    global camera_index
    frame = cv.QueryFrame(capture)
    cv.ShowImage("w1", frame)
    c = cv.WaitKey(10)
    if(c=="n"): #in "n" key is pressed while the popup window is in focus
        camera_index += 1 #try the next camera index
        capture = cv.CaptureFromCAM(camera_index)
        if not capture: #if the next camera index didn't work, reset to 0.
            camera_index = 0
            capture = cv.CaptureFromCAM(camera_index)


if __name__ == '__main__':
    while True:
        repeat()
"""
        
"""        
import sys;
#import Image;
import cv;
 
camcapture = cv.CreateCameraCapture(0)
cv.SetCaptureProperty(camcapture,cv.CV_CAP_PROP_FRAME_WIDTH, 640)
cv.SetCaptureProperty(camcapture,cv.CV_CAP_PROP_FRAME_HEIGHT, 480);
 
if not camcapture:
        print "Err or opening WebCAM"
        sys.exit(1)
 
while 1:
    frame = cv.QueryFrame(camcapture)
    if frame is None:
        break
    cv.ShowImage('Camera', frame)
    k=cv.WaitKey(10);
"""