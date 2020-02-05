import cv2
capture=cv2.VideoCapture(0)
width=int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)) # to capture the width of the video image ex: 720.0
height=int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)) # to capture the height of the video image
frames=int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
print(frames)
output=cv2.VideoWriter('myvideo.mp4',cv2.VideoWriter_fourcc(*'DIVX'),30,(width,height))

while True:
    ret,frame=capture.read()
    #frame1=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #operations
    output.write(frame)
    cv2.imshow('Frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
capture.release()
output.release()
cv2.destroyAllWindows()