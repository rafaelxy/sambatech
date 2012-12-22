# -*- coding: UTF-8 -*-

"""
Created on 22 Dec 2012

@author: rcampos
"""

import cv2.cv as cv
import traceback

OUTFILE = "output-webcam.avi"
WND_NAME = "Aperte qualquer tecla para fechar"
WAIT = 1
NO_KEY = -1
CAM_IX = 0

try:
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
except:
    print traceback.format_exc()