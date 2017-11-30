import cv2
from numpy import *
import time
import pymysql

# initial
cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(
    '618_17stages_head_detection.xml')

conn = pymysql.connect(host='127.0.01', port=3306,
                       user='root', passwd='batman123', db='head_detection')
cur = conn.cursor()

t1 = time.time()

while True:
    # get a frame
    ret, img = cap.read()

    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces_rect = face_cascade.detectMultiScale(
        grayimg, 1.2, 3)

    # show head
    for (x, y, w, h) in faces_rect:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, "Head No." + str(len(faces_rect)), (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow('HeadDetect', img)
    key = cv2.waitKey(10)

    # t2 = time.time()
    # if int(t2 - t1) == 15:
    #     people_num = len(faces_rect)
    #     date_rec = time.strftime('%Y-%m-%d', time.localtime(t2))
    #     time_rec = time.strftime('%X', time.localtime(t2))
    #     data_one = cur.execute(
    #         'insert into head_count(people_count, date, time) values(%s, %s, %s)', (people_num, date_rec, time_rec))
    #     conn.commit()
    #
    #     t1 = t2

    if key & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
cur.close()
conn.close()
