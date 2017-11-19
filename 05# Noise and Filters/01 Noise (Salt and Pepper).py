import cv2
import matplotlib.pyplot as plt
import numpy as np
import random

def main():
    
    path = "D:\\Youtube Code\\Python\\Python OpenCV3\\Python-OpenCV3\\Dataset\\"
    imgpath =  path + "4.2.02.tiff"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    

  
    plt.imshow(img)
    plt.title('Image with Salt and Pepper Noise')
    plt.show()

if __name__ == "__main__":
    main()