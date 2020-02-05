import cv2

pic=cv2.imread(r'DATA/00-puppy.jpg')

while True:
    cv2.imshow('Puppy',pic)
    #iif we waited fro 1 ms and if we pressed Esc(27) key  custom keys ord('q)
    if cv2.waitKey(1) & 0xFF==27:
        break

cv2.destoryAllWindows()