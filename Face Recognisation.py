# import threading
import threading

import cv2  
# used for working with image and video processing

from deepface import DeepFace  

# face recognisation and facial attribute analysis


# for the purpose of videocapture
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# to give width size
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# to give width height

counter = 0
# initial counter set to zero
face_match = False# if face doesnot matches then false

reference_img = cv2.imread("reference.jng")


def check_face(frame):
    global face_match

    try:
        if deepface.verify(frame, reference_img.copy())["verified"]:
            face_match = True# if face matches then true

        else:
            face_match = False

    except ValueError:# exception handling
        face_match=False





while True:
    ret, frame = cap_read()

    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass

        counter += 1

        if face_match:# condition used
            cv2.putText(frame, "MATCH", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

        else:
            cv2.putText(frame, "MATCH", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.inshow("video", frame)

    key = cv2.waitkey(1)

    if key == ord("q"):
        break

cv2.destroyAllWindows()
