import cv2

def main():
    windowName = "OpenCV Video Player"
    cv2.namedWindow(windowName)
    
    filename = 'D:\\Youtube Code\\Python\\Python OpenCV3\\Python-OpenCV3\\Output\\Output.avi'
    cap = cv2.VideoCapture(filename)
    
    
    while (cap.isOpened()):
    
        ret, frame = cap.read()
        
        print(ret)
        
        if ret:
            cv2.imshow(windowName, frame)
            if cv2.waitKey(17) == 27:
                break
        else:
            break

    cv2.destroyAllWindows()    
    cap.release()

if __name__ == "__main__":
    main()