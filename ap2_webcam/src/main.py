'''
Created on 22 Dec 2012

@author: rcampos
'''

import cv2.cv as cv

capture=cv.CaptureFromCAM(0)
image=cv.QueryFrame(capture)
writer=cv.CreateVideoWriter("output-webcam.avi", 0, 8.0, cv.GetSize(image), 1)

count=0
while count<100:
    image=cv.QueryFrame(capture)
    cv.WriteFrame(writer, image)
    cv.ShowImage('Image_Window',image)
    cv.WaitKey(1)
    count+=1
