import cv2
import numpy as np

def main():
    
    w = 160
    h = 120
    
    
    cap = cv2.VideoCapture(0)
    
    cap.set(3, w)
    cap.set(4, h)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False


    while ret:
    
        ret, frame = cap.read()
    
        Z = frame.reshape((-1,3))
        Z = np.float32(Z)
    
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    
        K=32
        ret, label1, center1 = cv2.kmeans(Z, K, None,
                                      criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        center1 = np.uint8(center1)
        res1 = center1[label1.flatten()]
        output1 = res1.reshape((frame.shape))
    
        cv2.imshow("Original", frame)
        cv2.imshow("Quantized", output1)
        if cv2.waitKey(1) == 27: # exit on ESC
            break

    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    main()