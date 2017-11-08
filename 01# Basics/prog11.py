# importing needed libraries

import cv2

def main():
    events = [i for i in dir(cv2) if 'EVENT' in i]
    print(events)

if __name__ == "__main__":
    main()