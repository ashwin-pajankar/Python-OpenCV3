import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "D:\\Youtube Code\\Python\\Python OpenCV3\\Python-OpenCV3\\Dataset\\"
    
    imgpath1 =  path + "4.2.01.tiff"
#    imgpath2 =  path + "4.2.04.tiff"
    
    img1 = cv2.imread(imgpath1, 1)
#    img2 = cv2.imread(imgpath2, 1)
    
#    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
#    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    
    output = cv2.resize(img1, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    
    titles = ['Image 1', 'Resised']
    images = [img1, output]
    
    cv2.imshow('Upscale', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
if __name__ == "__main__":
    main()