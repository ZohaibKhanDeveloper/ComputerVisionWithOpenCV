import cv2

img = cv2.imread("../images/cat.jpg",0)
ret, thresholded = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

cv2.imshow("Original Image",img)
cv2.imshow("Thresholded Image",thresholded)
cv2.waitKey(0)
cv2.destroyAllWindows()