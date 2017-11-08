import cv2
import matplotlib.pyplot as plt

def main():
    
    imgpath = "D:\\Youtube Code\\Python\\Python OpenCV3\\Python-OpenCV3\\Dataset\\4.2.04.tiff"
    img = cv2.imread(imgpath, 1)
    
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    plt.imshow(img)
    plt.title('Color Image BGR')
    plt.xticks([])
    plt.yticks([])
    plt.show()
 
    
    plt.imshow(img1)
    plt.title('Color Image RGB')
    plt.xticks([])
    plt.yticks([])
    plt.show()
 
if __name__ == "__main__":
    main()