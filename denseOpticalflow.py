
import numpy as np
import matplotlib.pyplot as plt
import cv2
try:
    capture=cv2.VideoCapture(0)

    ret,frame1=capture.read()

    #convert to gray scale

    frame1_gray=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)


    hsv_mask=np.zeros_like(frame1,dtype=np.uint8)
    hsv_mask[:,:,1]=255

    while True:
        ret,frame2=capture.read(0)
        frame2_gray=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
        
        flow=cv2.calcOpticalFlowFarneback(prev=frame1_gray,next=frame2_gray,flow=None,pyr_scale=0.5,levels=3,winsize=15,iterations=3,poly_n=5,poly_sigma=1.2,flags=0)#winSize, maxLevel, criteria
        mag,angle=cv2.cartToPolar(flow[:,:,0],flow[:,:,1],angleInDegrees=True)
        hsv_mask[:,:,0]=angle
        hsv_mask[:,:,2]=cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
        
        bgr=cv2.cvtColor(hsv_mask,cv2.COLOR_HSV2BGR)

        cv2.imshow("dense optical flow",bgr)
        
        #reassign new to previous of continous trackin
        frame1_gray=frame2_gray
        
        k=cv2.waitKey(1)    
        if k==27:
            break
            
except Exception as e:
    print(e)
    cv2.destroyAllWindows()   
    capture.release()     
cv2.destroyAllWindows()   
capture.release()