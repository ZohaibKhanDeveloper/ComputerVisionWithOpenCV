import cv2

img = cv2.imread('../images/cat.jpg')


cv2.line(img,(30,30),(500,30),(0,0,255),2)
cv2.rectangle(img,(40,40),(500,250),(0,255,0),2)
cv2.circle(img,(368,552),150,(255,0,0),2)

cv2.imshow("Cat Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()