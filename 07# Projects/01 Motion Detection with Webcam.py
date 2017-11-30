import cv2
import numpy as np

def main():
    
    w = 800
    h = 600
    
    
    cap = cv2.VideoCapture(0)
    
    cap.set(3, w)
    cap.set(4, h)
    
#    print(cap.get(3))
#    print(cap.get(4))
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    ret, frame1 = cap.read()
    ret, frame2 = cap.read()


    while ret:
        
        d = cv2.absdiff(frame1, frame2)
        
        grey = cv2.cvtColor(d, cv2.COLOR_BGR2GRAY)
        
        blur = cv2.GaussianBlur(grey, (5, 5), 0)
        
        ret, th = cv2.threshold( blur, 20, 255, cv2.THRESH_BINARY)
    
        dilated = cv2.dilate(th, np.ones((3, 3), np.uint8), iterations=1 )
        
        eroded = cv2.erode(dilated, np.ones((3, 3), np.uint8), iterations=1 )
        
        img, c, h = cv2.findContours(eroded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(frame1, c, -1, (0, 0, 255), 2)

        cv2.imshow("Original", frame2)
        cv2.imshow("Output", frame1)
        if cv2.waitKey(1) == 27: # exit on ESC
            break
        
        frame1 = frame2
        ret, frame2 = cap.read()

    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    main()