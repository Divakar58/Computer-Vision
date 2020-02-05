import cv2
import numpy as np

drawing=False
ix,iy=-1,-1

def draw_rec(event,x,y,flags,params):
    global ix,iy,drawing
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y
        #cv2.rectangle(img,x,y,color=(0,0,255),thickness=5)
    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.rectangle(img,(ix,iy),(x,y),color=(0,0,255),thickness=1)
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        cv2.rectangle(img,(ix,iy),(x,y),color=(0,0,255),thickness=1)

cv2.namedWindow('my_image')
cv2.setMouseCallback('my_image',draw_rec)



img=np.zeros(shape=(1024,1024,3))

while True:
    cv2.imshow('my_image',img)
    if (cv2.waitKey(1) & 0xFF==27):
        break

cv2.destoryAllWindows()

































# ##function
# def draw_circle(event,x,y,flags,param):
#     if event==cv2.EVENT_LBUTTONDOWN:
#         cv2.circle(black_img,(x,y),color=(255,255,0),radius=50,thickness=-1)
#     elif event==cv2.EVENT_RBUTTONDOWN:
#         cv2.circle(black_img,(x,y),color=(255,0,255),radius=50,thickness=-1)

# ## link the event
# cv2.namedWindow('drawing')
# cv2.setMouseCallback('drawing',draw_circle)

# black_img=np.zeros((1024,1024,3))
# ### show image
# while True:
#     cv2.imshow('drawing',black_img)
#     if cv2.waitKey(1) & 0xFF==27:
#         break
# cv2.destoryAllWindows()



