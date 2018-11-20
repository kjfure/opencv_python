import cv2 as cv

img = cv.imread('image.jpg',-1)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
