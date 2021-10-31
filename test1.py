from types import FrameType
import cv2 as cv

def face_detect_demo(img):
    gary = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    face_detect = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    face = face_detect.detectMultiScale(gary)
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
    cv.imshow('result',img)


cap = cv.VideoCapture() 

while True:
    frame = cap.read()
    face_detect_demo(frame)
    if ord('q') == cv.waitKey(0):
        break
cv.destroyAllWindows()
cap.release()