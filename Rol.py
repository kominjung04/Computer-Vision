import cv2
import numpy as np

capture = cv2.VideoCapture(0)
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")
    
title = "homework"
x, y, w, h = 200, 100, 100, 200
while True:
    ret,frame = capture.read()
    if not ret: break

    roi = frame[y:y+h, x:x+w]

    roi[:, :, 1] = np.clip(roi[:, :, 1] + 30, 0, 255)

    frame[y:y+h, x:x+w] = roi

    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)


    cv2.imshow(title, frame)
    if cv2.waitKey(30) >= 0:
        break
    
cv2.destroyAllWindows()
capture.release()