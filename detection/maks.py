import cv2


class FaceDetection(object):

    def __init__(self):
        self.count = 0

    def face_detection(self):
        video = cv2.VideoCapture(0)
        face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        while True:
            ret, frame = video.read()
            faces = face_detect.detectMultiScale(frame, 1.3, 5)
            for x, y, w, h in faces:
                count = self.count + 1
                name = './images/face_without_mask/' + str(count) + '.jpg'
                print(f"Creating images.............. {name}")
                cv2.imwrite(name, frame[y:y + h, x:x + w])
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.imshow('frame', frame)
            k = cv2.waitKey(1)

            # if k == ord('q'):
            if self.count > 50:
                break

        video.release()
        cv2.destroyAllWindows()


face_dec = FaceDetection()
face_dec.face_detection()
