import cv2
from numpy import *

# 初始化
cap = cv2.VideoCapture(0)
num = 0

face_cascade = cv2.CascadeClassifier(
    'F:/Python/PycharmProjects/day01/OpenCVTest/featurelib/lbpcascade_frontalface.xml')
"""
face_cascade = cv2.CascadeClassifier(
    'G:/head/data1/cascade.xml')
"""
people_num = []


#########################################

while True:
    # get a frame
    ret, img = cap.read()

    ####################### 检测人脸代码 #####################
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度转换
    faces_rect = face_cascade.detectMultiScale(
        grayimg, 1.2, 3)  # 得到一个矩形，faces是多个矩形（一个脸一个）

    people_num.append(len(faces_rect))

    # 将多个脸用框画出来
    for (x, y, w, h) in faces_rect:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # roi_gray = grayimg[y:y + h, x:x + w]
        # roi_color = img[y:y + h, x:x + w]

    cv2.imshow('FaceDetect', img)
    key = cv2.waitKey(10)
    cv2.imwrite('pics/%s.header.jpg' % (str(num)), img)
    num = num + 1
    ############################################

    if key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
