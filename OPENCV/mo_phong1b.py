import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# font
font = cv2.FONT_HERSHEY_SIMPLEX

# org
org = (50, 450)

# fontScale
fontScale = 1

# Blue color in BGR
color = (255,255, 255)

# Line thickness of 2 px
thickness = 2
text = "Tran Cong Hoa"

# Tạo một ảnh đen với kích thước 512x512
img = np.zeros((512,512,3), np.uint8)

# Tọa độ các đỉnh của ngũ giác
pts = np.array([[250,150],[300,192],[280,250],[220,250],[200,192]], np.int32)
pts1 = np.array([[350,225],[300,192],[250,230],[270,280],[330,280]], np.int32)
pts2 = np.array([[310,340],[330,280],[280,250],[230,280],[260,340]], np.int32)
pts3 = np.array([[200,340],[180,280],[220,250],[270,280],[260,340]], np.int32)
pts4 = np.array([[160,230],[180,280],[230,280],[250,230],[200,192]], np.int32)

# Để vẽ một hình ngũ giác, ta sử dụng hàm cv2.polylines
# Tham số thứ hai là tập hợp các tọa độ của đỉnh
# Tham số thứ ba là True nếu muốn nối điểm cuối cùng đến điểm đầu tiên
# Tham số thứ tư là màu và độ dày của đường vẽ
cv2.polylines(img,[pts],True,(255,0,0),1)
cv2.polylines(img,[pts1],True,(255,0,0),1)
cv2.polylines(img,[pts2],True,(255,0,0),1)
cv2.polylines(img,[pts3],True,(255,0,0),1)
cv2.polylines(img,[pts4],True,(255,0,0),1)

cv2.putText(img, text, org, font,
                fontScale, color, thickness, cv2.LINE_AA)
# Hiển thị ảnh
cv2.imshow("Pentagon",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
