import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    path = "D:\\Youtube Code\\Python\\Python OpenCV3\\Python-OpenCV3\\Dataset\\"
    imgpath1 =  path + "4.2.01.tiff"
    img1 = cv2.imread(imgpath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    
    rows, columns, channels = img1.shape
    
    point1 = np.float32([[0, 0], [400, 0], [0, 400], [400, 400]])
    point2 = np.float32([[0, 0], [500, 0], [0, 500], [500, 500]])
    
    P = cv2.getPerspectiveTransform(point1, point2)
    
    print(P)
    
    
    output = cv2.warpPerspective(img1, P, (700, 700))
    
    
    plt.imshow(output)
    plt.title('Changed Perspective')
    plt.show()

if __name__ == "__main__":
    main()