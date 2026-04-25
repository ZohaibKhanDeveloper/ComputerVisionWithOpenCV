import cv2

img = cv2.imread("../images/cat.jpg")

cv2.putText(img,"I love Cats",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)

cv2.imshow("Cat Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()