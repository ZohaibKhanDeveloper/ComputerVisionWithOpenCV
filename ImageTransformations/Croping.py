import cv2 

img = cv2.imread('../images/cat.jpg',0)

print(f"Image Shape: {img.shape}")

cropped_img = img[190:700,0:]

cv2.imshow("Cropped Cat Image",cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()