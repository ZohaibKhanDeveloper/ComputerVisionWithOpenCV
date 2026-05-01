import cv2

camera = cv2.VideoCapture(0)

fwidth = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
fheight = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID')
recorded = cv2.VideoWriter("video.avi",codec,60,(fwidth,fheight))

while camera.isOpened():
    ret, frame = camera.read()

    if ret:
        recorded.write(frame)
        cv2.imshow("Recording...",frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

camera.release()
recorded.release()
cv2.destroyAllWindows()        