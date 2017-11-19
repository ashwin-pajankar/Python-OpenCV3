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
        
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.blur(frame, (15, 15))

#        circles = cv2.HoughCircles(blur, method=cv2.cv.CV_HOUGH_GRADIENT,
#                                   dp=1, minDist=200, param1=50, param2=13,
#                                   minRadius=30, maxRadius=175)
        
        cv2.imshow(windowName, blur)

        if cv2.waitKey(1) == 27: # exit on ESC
            break

    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    main()