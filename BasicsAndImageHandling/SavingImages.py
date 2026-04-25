import cv2

img = cv2.imread('../images/cat.jpg')

cv2.imshow('Cat Image Orginal',img)
cv2.imshow('Gray Scale Cat Image',img[0:,0:,0])
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Writting or saving Grayscale image...")
cv2.imwrite('../images/catgray.png',img[0:,0:,0])