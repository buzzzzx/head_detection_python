import cv2

face_cascade = cv2.CascadeClassifier(
    'F:/Python/PycharmProjects/day01/OpenCVTest/featurelib/615_15stages_head_detection.xml')

# get a frame
while True:
    ret, img = cv2.imread()
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度转换
    ret, thresh2 = cv2.threshold(grayimg, 30, 255, cv2.THRESH_BINARY)

    faces_rect = face_cascade.detectMultiScale(
         thresh2, 1.2, 3)  # 得到一个矩形，faces是多个矩形（一个脸一个）

    faces_rect = face_cascade.detectMultiScale(img, 1.2, 3)  # 得到一个矩形，faces是多个矩形（一个脸一个）
    font = cv2.FONT_HERSHEY_SIMPLEX

    # 将多个脸用框画出来
    for (x, y, w, h) in faces_rect:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, "opencv", (10, 500), font, 4, (255, 255, 255), 2)


    cv2.imshow('FaceDetect', img)
    #cv2.imwrite('pics1.jpg', img)
    key = cv2.waitKey(10)
    # cv2.imwrite('pics/%s.header.jpg' % (str(num)), img)
    # num = num + 1
cap.release()
cv2.destroyAllWindows()
