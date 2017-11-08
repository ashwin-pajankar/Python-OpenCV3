import cv2
import numpy as np

def main():
    
    img1 = np.zeros((512, 512, 3), np.uint8)
    
    cv2.line(img1, (0, 99), (99, 0), (255, 0, 0), 2)
    cv2.rectangle(img1, (100, 60), (200, 170), (0, 255, 0), 2)
    cv2.circle(img1, (60, 60), 50, (0, 0, 255), -1)
    cv2.ellipse(img1, (160, 260), (50, 20), 0, 0, 360, (127, 127, 127), -1)
    
    points = np.array([[80, 2], [125, 0], [179, 0], [230, 5], [30, 50]], np.int32)
    points = points.reshape((-1, 1, 2))
    cv2.polylines(img1, [points], True, (0, 255, 255))
    
    text1 = 'Test Text'
    cv2.putText(img1, text1, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 0))
       
    cv2.imshow('Lena', img1)
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')
    
if __name__ == "__main__":
    main()