import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    path = "D:\\Youtube Code\\Python\\Python OpenCV3\\Python-OpenCV3\\Dataset\\"
    imgpath =  path + "4.2.07.tiff"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    
    k = np.array(np.ones((11, 11), np.float32))/121
    
    k = np.array(([0, -1, 0], [-1, 5, -1], [0, -1, 0]), np.float32)
    
    print(k)
    

    output = cv2.filter2D(img, -1, k)
    
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title('Original Image')
    
    plt.subplot(1, 2, 2)
    plt.imshow(output)
    plt.title('Filtered Image')
    
    plt.show()

if __name__ == "__main__":
    main()