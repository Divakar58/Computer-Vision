import cv2
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

road=cv2.imread('DATA/road_image.jpg')

road_copy=road.copy()

plt.imshow(road)

road.shape

#creating marker image
marker_image=np.zeros(road.shape[:2],dtype=np.int32) #black image of size 600,800

#creating segements
segments=np.zeros(road.shape,dtype=np.uint8) #black image of size same as road image 600,800,3

#to create color using colormap cm based on index
def create_marker(i):
    return tuple(np.array(cm.tab10(i)[:3])*255)

colors=[]
for i in range(10):
    colors.append(create_marker(i))


##Global variables
marker_color_updated=False
current_marker_index=1
n_markers=10 #0-9

#call back function
def mouse_button_clicked(event,x,y,flags,param):
    global marker_color_updated

    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(marker_image,(x,y),10,(current_marker_index),thickness=-1)
        cv2.circle(road_copy,(x,y),10,colors[current_marker_index],thickness=-1)
        marker_color_updated=True

cv2.namedWindow('Road image')
cv2.setMouseCallback('Road image',mouse_button_clicked)


while True:
    
    cv2.imshow('Road image',road_copy)
    cv2.imshow('Road image results',segments)
    k=cv2.waitKey(1)
    #to break 
    if k==27:
        break
    #to clear segmented image and road copy (to reset all)
    elif k==ord('c'): 
        road_copy=road.copy()
        marker_image=np.zeros(road.shape[:2],dtype=np.int32)
        segments=np.zeros(road.shape,dtype=np.uint8)
    #color marker update
    elif k>0 and chr(k).isdigit():
        current_marker_index=int(chr(k))

    if marker_color_updated:
        marker_image_copy=marker_image.copy()
        cv2.watershed(road,marker_image_copy)
        
        segments=np.zeros(road.shape,dtype=np.uint8)

        for color_index in range(n_markers):
            #coloring segments

            segments[marker_image_copy==(color_index)]=colors[color_index]
        
        marker_color_updated=False
        
        
cv2.destroyAllWindows()
    