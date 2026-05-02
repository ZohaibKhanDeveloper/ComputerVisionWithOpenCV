import cv2

img = cv2.imread("../images/circle.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
countours,heirarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img_copy = img.copy()
cv2.drawContours(img_copy,countours,1,(0,0,200),2)

cv2.imshow("Countours Image",img_copy)
cv2.imshow("Original Image",img)
cv2.imshow("Grayscale Image",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()