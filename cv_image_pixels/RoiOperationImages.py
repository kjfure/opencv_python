import cv2
import numpy as np
img = cv2.imread("image.jpg")
cv2.imshow('image',img)

print(img.shape)
imgRoi = img[280:340, 330:390]

#Splitting and Merging Image Channels
b = imgRoi[:,:,0]
print(b)
imgRoi[:,:,2] = 0

cv2.imshow('imageRoi',imgRoi)

#MakeBorder
BLUE=[255,0,0]
constant= cv2.copyMakeBorder(imgRoi,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
cv2.imshow('imageRoi',constant)

cv2.waitKey(0)
cv2.destroyAllWindows()
