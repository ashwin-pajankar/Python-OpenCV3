# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

def main():
    
    imgpath = "D:\\Youtube Code\\Python\\Python OpenCV3\\Python-OpenCV3\\Dataset\\4.2.04.tiff"
    img = cv2.imread(imgpath, 0)
    
    outpath = "D:\\Youtube Code\\Python\\Python OpenCV3\\Python-OpenCV3\\Output\\4.2.04.jpg"
    
    cv2.imshow('Lena', img)
    cv2.imwrite(outpath, img)
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')
    
    
    
if __name__ == "__main__":
    main()