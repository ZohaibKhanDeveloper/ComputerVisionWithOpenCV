import cv2 

img = cv2.imread('../images/cat.jpg')

fliped_v = cv2.flip(img,0)
fliped_h = cv2.flip(img,1)
fliped_both = cv2.flip(img,-1)

cv2.imshow("Flipped Vertically",fliped_v)
cv2.imshow("Flipped Horizontally",fliped_h)
cv2.imshow("Flipped Both Side",fliped_both)
cv2.waitKey(0)
cv2.destroyAllWindows()