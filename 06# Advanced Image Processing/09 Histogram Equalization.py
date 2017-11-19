import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "D:\\Youtube Code\\Python\\Python OpenCV3\\Python-OpenCV3\\Dataset\\"
    imgpath =  path + "4.2.04.tiff"

    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    R, G, B = cv2.split(img)
    
    output1_R = cv2.equalizeHist(R)
    output1_G = cv2.equalizeHist(G)
    output1_B = cv2.equalizeHist(B)
    
    output1 = cv2.merge((output1_R, output1_G, output1_B))

#    clahe = cv2.createCLAHE()
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

    output2_R = clahe.apply(R)
    output2_G = clahe.apply(G)
    output2_B = clahe.apply(B)
    
    output2 = cv2.merge((output2_R, output2_G, output2_B))


    output = [img, output1, output2]
    titles = ['Original Image', 'Adjusted Histogram', 'CLAHE']
    
    for i in range(3):
        plt.subplot(1, 3, i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()