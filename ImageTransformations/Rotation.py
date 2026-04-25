import cv2 

img = cv2.imread('../images/cat.jpg')

rotated_90 = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
rotated_180 = cv2.rotate(img,cv2.ROTATE_180)
rotated_90_cc = cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("Rotated 90 Degree Clockwise Image",rotated_90)
cv2.imshow("Rotated 180 Degree Image",rotated_180)
cv2.imshow("Rotated 90 Degree Couter Clockwise Image",rotated_90_cc)
cv2.imshow("Original Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

m = cv2.getRotationMatrix2D((img.shape[1]//2,img.shape[0]//2),90,1.0)
rotated_image = cv2.warpAffine(img,m,(img.shape[1],img.shape[0]))
cv2.imshow("Rotated Image",rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
