# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Written by Owen Miller 2015 ©

#import numpy as np
import cv2
import argparse
#import sys

def countBlobs(img):
    # threshold image then call findCountours()
    _, mask = cv2.threshold(img, 0, 1, cv2.THRESH_BINARY | cv2.THRESH_OTSU);
    contours, _ =  cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE);
    return len(contours);


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Give me an image and I'll count how many blobs \
        I see. For this version, you must use a dark background. Watch out that you're \
        not using lossy compression (eg JPEG) that could be changing the colour of your blobs!");
    parser.add_argument("inputFile", help="The image to be processed",type=str);
    parser.add_argument("--batch", help="Look for surrounding files with similar names and process \
        those too (not supported yet).", action='store_true', default=False);

    args = parser.parse_args();

    if(args.inputFile != None):
        src = cv2.imread(args.inputFile, cv2.CV_LOAD_IMAGE_GRAYSCALE);
        if(args.batch):
            # loop
            pass; #todo
        count = countBlobs(src);
        if count == 1:
            print("{0:d} blob".format(count));
        else:
            print("{0:d} blobs".format(count));