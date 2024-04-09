import cv2 as cv
import numpy as np

frame = cv.imread("Picture1.png")
img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

_, threshold = cv.threshold(img, 0, 255, cv.THRESH_BINARY)
contours,_ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_TC89_KCOS)
# font
font = cv.FONT_HERSHEY_SIMPLEX


# fontScale
fontScale = 0.5

# Blue color in BGR
color = (255, 51, 255)

# Line thickness of 2 px
thickness = 2

for c in contours:
    approx = cv.approxPolyDP(c, 0.01*cv.arcLength(c, True), True)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx) == 1:
        continue
    elif len(approx) == 2:
        continue
    elif len(approx) == 3:
        continue
    elif len(approx) == 4:
        continue
    elif len(approx) == 5:
        continue
    elif len(approx) == 6:
        continue
    elif len(approx) == 7:
        continue
    elif len(approx) == 8:
        cv.drawContours(frame, [approx], -1, (0, 255, 0), 2)
        cv.putText(frame, "Mten", (x, y), font, fontScale, color, thickness, cv.LINE_AA)
    elif len(approx) == 8:
        continue
    elif len(approx) == 9:
        continue
    elif len(approx) == 10:
        continue
    elif len(approx) == 11:
        continue
    elif len(approx) == 12:
        continue
    else:
        cv.drawContours(frame, [approx], -1, (0, 255, 0),2)
        cv.putText(frame, "tron", (x, y), font, fontScale, color, thickness, cv.LINE_AA)
    
cv.imshow("Anh", frame)
cv.imshow("Threashold", threshold)
cv.waitKey(0)
cv.destroyAllWindows()

