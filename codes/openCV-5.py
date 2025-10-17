import cv2
import numpy as np

print(cv2.__version__)

while True:
    frame = np.zeros([250, 250], dtype = np.uint8)
    cv2.imshow('My Window', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
