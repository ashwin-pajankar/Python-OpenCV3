import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "D:\\Youtube Code\\Python\\Python OpenCV3\\Python-OpenCV3\\Dataset\\"
    imgpath =  path + "7.1.02.tiff"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    edgesx = cv2.Scharr(img, -1, dx=1, dy=0, scale=1,
                       delta=0, borderType=cv2.BORDER_DEFAULT)
    
    edgesy = cv2.Scharr(img, -1, dx=0, dy=1, scale=1,
                       delta=0, borderType=cv2.BORDER_DEFAULT)
    
    edges = edgesx + edgesy

    output = [img, edgesx, edgesy, edges]
    titles = ['Original', 'dx=1 dy=0', 'dx=0 dy=1', 'Edges']
    
    for i in range(4):
        plt.subplot(2, 2, i+1)
        plt.imshow(output[i], cmap = 'gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()