# coding=utf-8
import cv2
from numpy import *
from PIL import Image
import os
import glob

cap = cv2.VideoCapture(0)
cap.set(3, 20)
cap.set(4, 20)
num = 0

while True:
    ret, img = cap.read()
    cv2.imshow("capture", img)
    key = cv2.waitKey(10)

    if key & 0xFF == ord('z'):
        cv2.imwrite('pics_ori/%sheader.jpg' % (str(num)), img)
        num = num + 1

    if key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# 处理图片
f = glob.glob(r'F:\Python\PycharmProjects\day01\OpenCVTest\pics_ori\*.jpg')
for files in f:
    filepath, filename = os.path.split(files)
    filtername, ext = os.path.splitext(filename)
    op = 'F:\\Python\\PycharmProjects\\day01\\OpenCVTest\\pics_deal\\'
    img = Image.open(files)
    im_deal = img.resize((64, 64), Image.ANTIALIAS)
    im_deal.save(op + filtername + '.jpg')

print("ok")