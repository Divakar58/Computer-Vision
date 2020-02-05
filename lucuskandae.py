
import numpy as np
import matplotlib.pyplot as plt
import cv2
try:
    #corner detetction for goodfeaturetrack
    corner_track_params=dict(maxCorners=20,qualityLevel=0.09,minDistance=7,blockSize=7) #maxcorner to detect 
    #Lucus kanada parameter
    lk_params=dict(winSize=(200,200),maxLevel=2,criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,0.03))#pyramid detection

    capture=cv2.VideoCapture(0)

    ret,prev_frame=capture.read(0)

    #convert to gray scale

    pre_gray=cv2.cvtColor(prev_frame,cv2.COLOR_BGR2GRAY)

    #pts to track
    prevPts=cv2.goodFeaturesToTrack(image=pre_gray,mask=None,**corner_track_params) #maxCorner qualityLevel,minDistance, blockSize

    mask=np.zeros_like(prev_frame,dtype=np.uint8)

    while True:
        ret,frame=capture.read(0)
        frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        nextPts,status,err=cv2.calcOpticalFlowPyrLK(prevImg=pre_gray,nextImg=frame_gray,prevPts=prevPts,nextPts=None,**lk_params)#winSize, maxLevel, criteria
        
        good_new=nextPts[status==1]
        good_prev=prevPts[status==1]
        
        for i,(nextpts,prevpts) in enumerate(zip(good_new,good_prev)):
            x_new,y_new=nextpts.ravel()
            x_pre,y_new=prevpts.ravel()
            mask=cv2.line(mask,(x_new,y_new),(x_pre,y_new),color=(0,255,0),thickness=2)
            frame=cv2.circle(frame,(x_new,y_new),radius=5,color=(0,255,255),thickness=-1)
        img=cv2.add(mask,frame)
        cv2.imshow("tracking",img)
        
        #reassign new to previous of continous trackin
        pre_gray=frame_gray
        prevPts=good_new.reshape(-1,1,2)
        
        k=cv2.waitKey(1)    
        if k==27:
            break
            
except Exception as e:
    print(e)
    cv2.destroyAllWindows()   
    capture.release()     
cv2.destroyAllWindows()   
capture.release()