import cv2
import numpy as np

# Tạo một ảnh đen với kích thước 512x512
img = np.zeros((200,200))


cv2.imshow("Pentagon",img)
cv2.waitKey(0)
cv2.destroyAllWindows()






