import cv2
import numpy as np

# Load the image and convert it to grayscale
img = cv2.imread("Picture1.png", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian filter to reduce noise
gray = cv2.GaussianBlur(gray, (5, 5), 0)

# Threshold the image to separate background and foreground
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Detect circles using HoughCircles
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
                           param1=50, param2=30, minRadius=0, maxRadius=0)

# Draw the circles on the original image
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(img, (x, y), r, (0, 255, 0), 2)
        cv2.putText(img, "Circle", (x - 20, y - 20), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 2)

# Find contours in the thresholded image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Loop over the contours to find arrows
for cnt in contours:
    # Find the bounding rectangle of the contour
    x, y, w, h = cv2.boundingRect(cnt)
    # Ignore contours that are too small or too big
    if w < 20 or h < 20 or w > 200 or h > 200:
        continue
    # Compute the aspect ratio of the bounding rectangle
    aspect_ratio = w / float(h)
    # Ignore rectangles that are not sufficiently elongated
    if aspect_ratio < 2:
        continue
    # Draw the arrow on the original image
    cv2.rectangle(img, (x, y), (x + w, y + h))