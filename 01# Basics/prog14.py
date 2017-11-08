import cv2
import matplotlib.pyplot as plt

def main():
    
    imgpath = "D:\\Youtube Code\\Python\\Python OpenCV3\\Python-OpenCV3\\Dataset\\4.2.04.tiff"
    img = cv2.imread(imgpath, 1)
    
    
    plt.imshow(img, cmap='gray')
    plt.title('Gray Colormap')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    plt.imshow(img)
    plt.title('Default Colormap')
    plt.xticks([])
    plt.yticks([])
    plt.show()  
 
if __name__ == "__main__":
    main()