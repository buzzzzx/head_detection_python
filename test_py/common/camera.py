# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/11/29 下午7:56'

import cv2
import sys
import pymysql
import time

t1 = time.time()


class Camera(object):
    def __init__(self, index=0):
        self.cap = cv2.VideoCapture(index)
        self.openni = index in (cv2.CAP_OPENNI, cv2.CAP_OPENNI2)
        self.fps = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.release()

    def release(self):
        if not self.cap: return
        self.cap.release()
        self.cap = None

    def capture(self, callback, gray=True):

        # add
        face_cascade = cv2.CascadeClassifier(
            '618_17stages_head_detection.xml')

        if not self.cap:
            sys.exit('The capture is not ready')

        while True:
            t = cv2.getTickCount()

            # Kinect camera
            if self.openni:
                if not self.cap.grab():
                    sys.exit('Grabs the next frame failed')
                ret, depth = self.cap.retrieve(cv2.CAP_OPENNI_DEPTH_MAP)
                ret, frame = self.cap.retrieve(cv2.CAP_OPENNI_GRAY_IMAGE
                                               if gray else cv2.CAP_OPENNI_BGR_IMAGE)

                # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces_rect = face_cascade.detectMultiScale(
                    depth, 1.2, 3)

                # show head
                for (x, y, w, h) in faces_rect:
                    frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(frame, "Head No." + str(len(faces_rect)), (x, y),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                cv2.imshow('HeadDetect', frame)
                key = cv2.waitKey(10)

                t2 = time.time()
                if int(t2 - t1) == 15:
                    people_num = len(faces_rect)
                    time_rec = time.strftime('%X', time.localtime(t2))
                    data_one = cur.execute(
                        'insert into detection_peoplecount(time_join, people_count) values(%s, %s)',
                        (time_rec, people_num))
                    conn.commit()

                    t1 = t2

                if key & 0xFF == ord('q'):
                    break

                if callback:
                    callback(frame, depth, self.fps)

            # PC camera
            else:
                ret, frame = self.cap.read()
                if not ret:
                    sys.exit('Reads the next frame failed')
                if gray:
                    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faces_rect = face_cascade.detectMultiScale(
                        img, 1.2, 3)

                    # show head
                    for (x, y, w, h) in faces_rect:
                        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        cv2.putText(frame, "Head No." + str(len(faces_rect)), (x, y),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                    cv2.imshow('HeadDetect', img)
                    key = cv2.waitKey(10)

                    t2 = time.time()
                    if int(t2 - t1) == 15:
                        people_num = len(faces_rect)
                        time_rec = time.strftime('%X', time.localtime(t2))
                        data_one = cur.execute(
                            'insert into detection_peoplecount(time_join, people_count) values(%s, %s)',
                            (time_rec, people_num))
                        conn.commit()

                        t1 = t2

                    if key & 0xFF == ord('q'):
                        break

                if callback:
                    callback(frame, self.fps)

            t = cv2.getTickCount() - t
            self.fps = cv2.getTickFrequency() / t

            # esc, q
            ch = cv2.waitKey(10) & 0xFF
            if ch == 27 or ch == ord('q'):
                break

    def fps(self):
        return self.fps

    def get(self, prop_id):
        return self.cap.get(prop_id)

    def set(self, prop_id, value):
        self.cap.set(prop_id, value)


if __name__ == '__main__':
    # mysql connect
    conn = pymysql.connect(host='127.0.01', port=3306,
                           user='root', passwd='batman123', db='head_detection')
    cur = conn.cursor()

    callback = lambda gray, fps: cv2.imshow('gray', gray)

    with Camera(0) as cam:
        print("Camera: %dx%d, %d" % (
            cam.get(cv2.CAP_PROP_FRAME_WIDTH),
            cam.get(cv2.CAP_PROP_FRAME_HEIGHT),
            cam.get(cv2.CAP_PROP_FPS)))
        cam.capture(callback)

    cv2.destroyAllWindows()
