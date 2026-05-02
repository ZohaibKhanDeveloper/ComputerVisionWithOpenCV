import cv2

img = cv2.imread("../images/car.jpg",0)
edges = cv2.Canny(img,50,255)

cv2.imshow("Original Image",img)
cv2.imshow("Edges Image",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()