import cv2
import numpy as np

def main():
    windowName = "Preview"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False


    while ret:
    
        ret, frame = cap.read()
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Green Color
#        low = np.array([40, 50, 50])
#        high = np.array([80, 255, 255])
        
        # Blue Color
        low = np.array([100, 50, 50])
        high = np.array([140, 255, 255])
        
        # Red Color
        low = np.array([140, 150, 0])
        high = np.array([180, 255, 255])
        
        image_mask = cv2.inRange(hsv, low, high)
        
        output = cv2.bitwise_and(frame, frame, mask = image_mask)
        
        cv2.imshow("Original", frame)
        cv2.imshow("Mask", image_mask)
        cv2.imshow(windowName, output)
        if cv2.waitKey(1) == 27: # exit on ESC
            break

    cv2.destroyAllWindows()
    cap.release()
    
main()