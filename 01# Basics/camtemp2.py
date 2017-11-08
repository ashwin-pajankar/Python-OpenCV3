import cv2

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
        
        output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        cv2.imshow(windowName, output)
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyWindow(windowName)
    cap.release()
    
main()