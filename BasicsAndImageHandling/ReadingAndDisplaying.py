import cv2

img = cv2.imread("../images/cat.jpg")

cv2.imshow("Cat image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread("../images/cat.jpg",0)

cv2.imshow("Cat image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread("../images/cat.jpg",1)

cv2.imshow("Cat image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()