# -*- coding: UTF-8 -*-

"""
Created on 22 Dec 2012

@author: rcampos
"""

import cv2.cv as cv

class Capture():
    def __init__(self, outfile, wnd_name):
        self.__outfile = outfile
        self.__wnd_name = wnd_name
        
        """Opções da captura"""
        self.WAIT = 1
        self.NO_KEY = -1
        self.CAM_IX = 0
        
        """Opções do video"""
        self.__fourcc = 0
        self.__fps = 8.0
        self.__is_color = 1

    def capture(self):
        capture = cv.CaptureFromCAM(self.CAM_IX)
        image = cv.QueryFrame(capture)
        
        writer = cv.CreateVideoWriter(self.__outfile,
                                      self.__fourcc,
                                      self.__fps,
                                      frame_size = cv.GetSize(image),
                                      is_color = 1)
        
        self.__read_cam(capture, writer)
        
        
    def __read_cam(self, capture, writer):
        while cv.WaitKey(self.WAIT) == self.NO_KEY:
            image = cv.QueryFrame(capture)
            cv.WriteFrame(writer, image)
            cv.ShowImage(self.__wnd_name, image)
        
        cv.DestroyWindow(self.__wnd_name)
