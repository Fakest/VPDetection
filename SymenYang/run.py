import cv2

filename = "data/"
img = cv2.imread(filename)
vp = (509, 451)
red = [0,0,255]
cv2.circle(img, vp, 1, red, 10)

cv2.imshow('img', img)
size = 100
for i in range(size):
    img = cv2.imread(filename + i.jpg)
    vp = (509, 451)
    red = [0, 0, 255]
    cv2.circle(img, vp, 1, red, 10)
    cv2.imwrite("", img)
#cv2.waitKey(0)