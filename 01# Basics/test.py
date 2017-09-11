# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import cv2

def main():
    
    cap = cv2.VideoCapture(0)
    
    while True:
        
        ret, frame = cap.read()
        
        frame = 5 * frame * frame + 4 * frame  + 4
        
        cv2.imshow('Test', frame)
        
        
        
        if cv2.waitKey(1) == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()