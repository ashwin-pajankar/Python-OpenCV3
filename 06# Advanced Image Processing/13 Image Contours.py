import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "D:\\Youtube Code\\Python\\Python OpenCV3\\Python-OpenCV3\\Dataset\\"

    imgpath1 =  path + "4.2.07.tiff"
    

    img = cv2.imread(imgpath1, 1)
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    ret, thresh = cv2.threshold(gray, 75, 255, 0)
    
    img2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#    print(contours)
#    print(hierarchy)
    
    cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
    
    original = cv2.imread(imgpath1, 1)
    
    original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
    
    output = [original, img]
    titles = ['Original', 'Contours']
    
    
    for i in range(2):
        plt.subplot(1, 2, i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()  

if __name__ == "__main__":
    main()