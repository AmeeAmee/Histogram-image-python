import cv2

img = cv2.imread("gradient.png")

thresh_img, temp1 = cv2.threshold(img,150,255,cv2.THRESH_BINARY)

thresh_img_invers, temp2 = cv2.threshold(img,150,255,cv2.THRESH_BINARY_INV)

thresh_img_trunc, temp3 = cv2.threshold(img,150,255,cv2.THRESH_TRUNC)

cv2.imshow('Original img', img)
# cv2.imshow('threshold img', thresh_img)
cv2.imshow('temp', temp1)
    
