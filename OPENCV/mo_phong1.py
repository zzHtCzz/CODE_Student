import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
# font
font = cv.FONT_HERSHEY_SIMPLEX

# org
org = (50, 450)

# fontScale
fontScale = 1

# Blue color in BGR
color = (255, 51, 255)

# Line thickness of 2 px
thickness = 2
text = "Tran Cong Hoa"
while True:
    ret, frame = cap.read()
    print(ret)
    frame = cv.rectangle(frame, (250, 250), (450, 300), (0, 255, 0))
    cv.putText(frame, text, org, font,
                fontScale, color, thickness, cv.LINE_AA)
    cv.imshow("Anh", frame)
    if cv.waitKey(1) == ord("q"):
        break
cv.destroyAllWindows()
