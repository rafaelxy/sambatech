# -*- coding: UTF-8 -*-

"""
Created on 22 Dec 2012

@author: rcampos
"""


import traceback
import cam.write

OUTFILE = "output-webcam.avi"
WND_NAME = "Capturando Imagem - Aperte qualquer tecla para fechar"

try:
    cap = cam.write.Capture(OUTFILE, WND_NAME)
    cap.capture()
except:
    print traceback.format_exc()