01122import cv2
import numpy as np
import matplotlib.pyplot as plt
from warnings import filterwarnings
filterwarnings('ignore')


def select_tracker():
    print("Welcome What tracking API would you like to use?")
    print("Enter 0 for BOOSTING: ")
    print("Enter 1 for MIL: ")
    print("Enter 2 for KCF: ")
    print("Enter 3 for TLD: ")
    print("Enter 4 for  MEDIANFLOW: ")
    choice=input("select tracking API: ")
    print(choice)
    if choice=='0':
        tracker=cv2.TrackerBoosting_create()
    if choice=='1':
        tracker=cv2.TrackerMIL_create()
    if choice=='2':
        tracker=cv2.TrackerKCF_create()
    if choice=='3':
        tracker=cv2.TrackerTLD_create()
    if choice=='4':
        tracker=cv2.TrackerMedianFlow_create()
    return tracker

tracker=select_tracker()

tracker_name=str(tracker).split()[0][1:]

capture=cv2.VideoCapture(0)

ret,frame=capture.read()

# region of interest
roi=cv2.selectROI(frame,False)

ret=tracker.init(frame,roi)

while True:
    ret,frame=capture.read()
    # update tracker
    success,roi=tracker.update(frame)
    (x,y,w,h)=tuple(map(int,roi))
    if success:
        cv2.rectangle(frame,(x,y),(x+w,y+h),color=(255,0,0),thickness=3)
    else:
        cv2.putText(frame,"Failure to Detect Tracking",org=(100,200),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=2,thickness=3,color=(0,0,255))
    
    cv2.putText(frame,tracker_name,org=(20,400),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,thickness=3,color=(0,255,0))

    cv2.imshow('Traking API',frame)
    k=cv2.waitKey(1) & 0xFF

    if k==27:
        break

cv2.destroyAllWindows()
capture.release()








   



