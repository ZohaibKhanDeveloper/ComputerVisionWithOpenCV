import cv2 

img = cv2.imread("../images/cat.jpg")

gblurred = cv2.GaussianBlur(img,(5,5),3)
mblurred = cv2.medianBlur(img, 5)

cv2.imshow("Original Image",img)
cv2.imshow("Guassian Blurred Image",gblurred)
cv2.imshow("Median Blurred Image",mblurred)
cv2.waitKey(0)
cv2.destroyAllWindows()