# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 16:00:10 2018

@author: hp
"""

import urllib.request
import cv2
import numpy as np

url='http://192.168.10.41:8080/shot.jpg'

while True:
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)

    # all the opencv processing is done here
    cv2.imshow('test',img)
    if cv2.waitKey(10)==ord('q'):
        
        exit(0)
  
