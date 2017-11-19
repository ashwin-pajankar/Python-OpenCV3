import cv2

def main():
    
    windowName = ['Binary', 'Binary Inv', 'Zero', 'Zero Inv', 'Trunc']
    
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False


    while ret:
    
        ret, frame = cap.read()
        
        th = 127
        max_val = 255
    
        ret, o1 = cv2.threshold(frame, th, max_val, cv2.THRESH_BINARY)
        ret, o2 = cv2.threshold(frame, th, max_val, cv2.THRESH_BINARY_INV)
        ret, o3 = cv2.threshold(frame, th, max_val, cv2.THRESH_TOZERO)
        ret, o4 = cv2.threshold(frame, th, max_val, cv2.THRESH_TOZERO_INV)
        ret, o5 = cv2.threshold(frame, th, max_val, cv2.THRESH_TRUNC)
        
        cv2.imshow(windowName[0], o1)
        cv2.imshow(windowName[1], o2)
        cv2.imshow(windowName[2], o3)
        cv2.imshow(windowName[3], o4)
        cv2.imshow(windowName[4], o5)
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    main()