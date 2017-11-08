import cv2
import numpy as np

def main():
    
    imgpath = "D:\\Youtube Code\\Python\\Python OpenCV3\\Python-OpenCV3\\Dataset\\4.2.04.tiff"
    img1 = cv2.imread(imgpath, 0)
    
#    print(img1)
    print(type(img1))
    print(img1.dtype)
    
    print(img1.shape)
    print(img1.ndim)
    print(img1.size)
    
#    cv2.imshow('Lena', img1)
#    cv2.waitKey(0)
#    cv2.destroyWindow('Lena')
    
if __name__ == "__main__":
    main()