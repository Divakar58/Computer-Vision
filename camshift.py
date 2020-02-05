import cv2
import numpy as np
import matplotlib.pyplot as plt

#capture video to detect image
capture=cv2.VideoCapture(0)

#read frame
ret,frame=capture.read()

#face classifier
faceCascade=cv2.CascadeClassifier('DATA/haarcascades/haarcascade_frontalface_default.xml')
#detect face
face_rect=faceCascade.detectMultiScale(frame,scaleFactor=1.2,minNeighbors=5)
#change the detected face dimension to a tuple
(face_x,face_y,w,h)=tuple(face_rect[0])
#put them in track window to be used in meanshift to track it later
track_window=(face_x,face_y,w,h)
#region of interest in the image (face)
roi=frame[face_y:face_y+h,face_x:face_x+w]
#convert to hsv
hsv_roi=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
#getting the hist of the roi
roi_hist=cv2.calcHist([hsv_roi],[0],None,[255],[0,255])
#normalized the values to range(0,255)
roi_hist_norm=cv2.normalize(roi_hist,None,0,255,cv2.NORM_MINMAX)
#creating a criteria
term_criteria=(cv2.TERM_CRITERIA_EPS | cv2.TermCriteria_COUNT,10,1)

#capturing video to track image
while True:
    #capture video to track image in it
    ret,frame=capture.read()
    if ret==True:
        #convert current video image to hsv
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #create a backproject using current image and previous roi hist 
        dst=cv2.calcBackProject([hsv],[0],roi_hist_norm,[0,255],1)
        #perform camshift using track window to resize window based on the detection in video
        ret,track_window=cv2.CamShift(dst,track_window,term_criteria)

        #get pts from the ret
        pts=cv2.boxPoints(ret)
        #converting to int from float
        pts=np.int0(pts)
        #draw polylines (which resizes)
        frame=cv2.polylines(img=frame,pts=[pts],isClosed=True,color=(255,0,0),thickness=5)
        #show image
        cv2.imshow('cam shift',frame)
        #wait for the image to be pressed
        k=cv2.waitKey(1)
        if k==27:
            break
    else:
        break
#destory windows
cv2.destroyAllWindows()
capture.release()




