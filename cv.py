#   OpenCV   #
import cv2
import numpy as np
import random

#   CASCADE   #
face_cascade = cv2.CascadeClassifier('xml/front.xml')
eye_cascade = cv2.CascadeClassifier('xml/eye.xml')

num = random.randint(10, 100)

#   SET CAPTURE TO CAM 0   #
cap = cv2.VideoCapture(0)
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (107, 255, 0), 4)
        cv2.putText(img, 'Person {0}'.format(num), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 255, 255), 2, cv2.LINE_AA)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        print("Detectet Person")
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (65, 0, 255), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
