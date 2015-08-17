# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Written by Owen Miller 2015
# Apache 2.0 License

from gimpfu import *
import os
import cv2

def countingBlobs(img, layer):
    print("Je suis ici");
    
register(
     "Count_blobs",
     "This script counts the number of blobs in a layer",
     "",
     "Owen Miller",
     "kokociel.com",
     "August 2015",
     "<Image>/Python-Fu/_Machine Vision/_Count Blobs",
     "",
     [
      (PF_STRING, "img", "Input name", ""),
      (PF_STRING, "layer", "Blob layer","")
      ],
     [],
     countingBlobs)

main()