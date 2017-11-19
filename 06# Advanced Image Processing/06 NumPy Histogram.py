import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    path = "D:\\Youtube Code\\Python\\Python OpenCV3\\Python-OpenCV3\\Dataset\\"
    impath = path  + "4.2.07.tiff"
    img = cv2.imread(impath, 0)

    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Image')
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(1, 2, 2)
    hist, bins = np.histogram(img.ravel(), 256, [0,255])
    plt.xlim([0, 255])
    plt.ylim([0, 3000])
    plt.plot(hist)
    plt.title('Histogram')
    plt.show()

if __name__ == "__main__":
    main()