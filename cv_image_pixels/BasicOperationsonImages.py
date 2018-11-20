import cv2
import numpy as np

img = cv2.imread('image.jpg')
cv2.imshow('1',img)

#get pixel
px = img[100,100]
print(px)
blue = img[100,100,0]
print(blue)
green = img[100,100][1]
print(green)

#modify
img[100,100]=[1,2,3]
px = img[100,100]
print(px)

red=img.item(100,100,2)
print(red)
img.itemset((100,100,2),100)
red=img.item(100,100,2)
print(red)

#image size
shape = img.shape
print(shape)
size = img.size
print(size)
print(img.dtype)




