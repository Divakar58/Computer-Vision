import cv2
import time
capture =cv2.VideoCapture('myvideo.mp4')

if not(capture.isOpened()):
    print("Error in opening video file")
while True:
    ret,frame=capture.read()
    if ret:
        time.sleep(1/30) #30 is the number of frames the video recorded 
        cv2.imshow('My video player',frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break
capture.release()
cv2.destroyAllWindows()
