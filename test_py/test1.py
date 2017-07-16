# coding=utf-8
import cv2
import numpy as np

img = cv2.imread('F:\Python\PycharmProjects\day01\OpenCVTest\pics\zz.jpg')
GrayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh2 = cv2.threshold(GrayImage, 50, 255, cv2.THRESH_BINARY)
# OpenCV定义的结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# 腐蚀图像
eroded = cv2.erode(thresh2, kernel)
# 显示腐蚀后的图像
cv2.imshow("Eroded Image", eroded)

# 膨胀图像
dilated = cv2.dilate(thresh2, kernel)
# 显示膨胀后的图像
cv2.imshow("Dilated Image", dilated)
# 原图像
cv2.imshow("Origin", img)

# NumPy定义的结构元素
NpKernel = np.uint8(np.ones((3, 3)))
Nperoded = cv2.erode(thresh2, NpKernel)
# 显示腐蚀后的图像
cv2.imshow("Eroded by NumPy kernel", Nperoded)

cv2.waitKey(0)
cv2.destroyAllWindows()