import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    path = "D:\\Youtube Code\\Python\\Python OpenCV3\\Python-OpenCV3\\Dataset\\"
    imgpath1 =  path + "4.2.01.tiff"
    img1 = cv2.imread(imgpath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    
    rows, columns, channels = img1.shape
    
    point1 = np.float32([[100, 100], [300, 100], [100, 300]])
    point2 = np.float32([[200, 150], [400, 150], [200, 400]])
    
    A = cv2.getAffineTransform(point1, point2)
    
    print(A)
    
    
    output = cv2.warpAffine(img1, A, (columns, rows))
    
    
    plt.imshow(output)
    plt.title('Transformed Image')
    plt.show()

if __name__ == "__main__":
    main()