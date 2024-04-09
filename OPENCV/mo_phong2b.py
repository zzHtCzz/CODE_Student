import cv2 as cv
import numpy as np

frame = cv.imread("Picture1.png", cv.IMREAD_COLOR)
img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
hsv=cv.cvtColor(frame, cv.COLOR_BGR2HSV)

_, threshold = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
contours,_ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
cap = cv.VideoCapture(0)
# font
font = cv.FONT_HERSHEY_SIMPLEX


# fontScale
fontScale = 0.5

# Blue color in BGR
color = (255, 51, 255)

# Line thickness of 2 px
thickness = 2

for c in contours:
    M = cv.moments(c)
    cX = int(M['m10']/M['m00'])
    cY = int(M['m01']/M['m00'])
    approx = cv.approxPolyDP(c, 0.01*cv.arcLength(c, True), True)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    pixel_center = hsv[cY, cX]
    hue_value = pixel_center[0]

    if len(approx) == 3 and 80<hue_value<100:
        cv.drawContours(frame, [approx], -1, (0, 255, 0), 3)
        cv.putText(frame, "tam giac", (x, y), font, fontScale, color, thickness, cv.LINE_AA)
        cv.putText(frame, "XANH DUONG", (cX, cY), font, fontScale, color, thickness, cv.LINE_AA)
cv.imshow("Anh", frame)
cv.imshow("Threashold", threshold)
cv.waitKey(0)
cv.destroyAllWindows()

