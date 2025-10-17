import numpy as np


frame = np.array([[0,0,0],[0,0,0],[0,0,0]])

print (frame[1,2])

frame [1,2] = 1 # frame [1,2] = 255 
print ("\n", frame)

frame [1,2] = 255 
print("\n", frame)

frame = np.zeros([5, 5], dtype = np.uint8)
print("\n", frame)

frame[1, 1] = 125
print("\n", frame)

frame[0:2, 0:5] = 10
frame[0:2, 0:5] = 100

print("\n", frame)