import cv2 

img = cv2.imread('../images/cat.jpg')

resized_img = cv2.resize(img,(300,300))
resized_scaled_img = cv2.resize(img,None,fx=0.3,fy=0.3)

cv2.imshow("Original Image",img)
cv2.imshow("Resized 300x300 Image",resized_img)
cv2.imshow("Resized Scaled Image",resized_scaled_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
