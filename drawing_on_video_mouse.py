import cv2

capture=cv2.VideoCapture(0)

#call back function
def draw_rec(event,x,y,flags,param):
    global pt1,pt2,topLeftClicked,bottomRightClicked
    if event==cv2.EVENT_LBUTTONDOWN:
        #   check if the rectangle is already present if yes reset
        if topLeftClicked and bottomRightClicked:
            pt1=(0,0)
            pt2=(0,0)
            topLeftClicked=False
            bottomRightClicked=False
        ##check if left mouse is clicked
        if topLeftClicked==False:
            pt1=(x,y)
            topLeftClicked=True
        ##check if right mouse is clicked    
        elif bottomRightClicked==False:
            pt2=(x,y)
            #print("bottom",x,y)
            bottomRightClicked=True
    
#global variables
pt1=(0,0)
pt2=(0,0)
topLeftClicked=False
bottomRightClicked=False

cv2.namedWindow('my player')
cv2.setMouseCallback('my player',draw_rec)

while True:
    ret,frame=capture.read()

    if topLeftClicked:
        cv2.circle(frame,pt1,color=(0,0,255),radius=2,thickness=-1)
    if topLeftClicked and bottomRightClicked:
        cv2.rectangle(frame,pt1,pt2,color=(0,0,255),thickness=3)
    cv2.imshow('my player',frame)
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break

capture.release()
cv2.destoryAllWindows()