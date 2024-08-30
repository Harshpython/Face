# imoort threading used for User Interface Responsiveness
import threading

import cv2  #used for working with image and videoprocessing

from deepface import DeepFace

#face recognisation and facial attribute analysis 
# for the purpose of videocapture
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# for reading csv

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)# setting up the camera width and height

counter = 0

face_match = False # if face doesnot match then no occurence

reference_img = cv2.imread("reference.jng")

def check_face(frame):
    global face_match# face detection

    try:
        if DeepFace.verify(frame, reference_img.copy())["verified"]:
            face_match=True

        else:
            face_match=False

    except ValueError:
        pass # used to run the function




while True:
    ret, frame = cap_read()

    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass

        counter += 1

        if face_match:# defined
            cv2.putText(frame,"MATCH",(20,450),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3) 


        

        else:
            cv2.putText(frame, "MATCH", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.inshow("video",frame)# to show the face






    key = cv2.waitkey(1)

    if key == ord("q"):
        break

cv2.destroyAllWindows()
