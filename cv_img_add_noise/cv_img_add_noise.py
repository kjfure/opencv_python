from numpy import *
from scipy import *
import numpy as np
import cv2

img_src = cv2.imread('1.jpg')
cv2.imshow('1.jpg',img_src)

x,y,z= img_src.shape
print(x,y,z)

#椒盐噪声
SP_NoiseImg=img_src
SP_NoiseNum=int(0.01*x*y)
for i in range(SP_NoiseNum):
    randx=random.random_integers(0,x-1)
    randy=random.random_integers(0,y-1)
    if random.random_integers(0,1)==0: 
        SP_NoiseImg[randx,randy]=(0,0,0) 
    else:
        SP_NoiseImg[randx,randy]=(255,255,255) 

cv2.imshow('noise.jpg',SP_NoiseImg)

cv2.waitKey(0)
cv2.destroyAllWindows()


