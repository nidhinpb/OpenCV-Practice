import numpy as np
import cv2
def cir_pic(events,x,y,flags,param):
    if events==cv2.EVENT_RBUTTONDOWN:
        cv2.circle(fix_img,(x,y),50,color=(0,0,255),thickness=10)    
cv2.namedWindow(winname="Puppy")
cv2.setMouseCallback("Puppy",cir_pic)
fix_img= cv2.imread('D:\Python CV_Course\Computer-Vision-with-Python\DATA\dog_backpack.jpg')
while True:
    cv2.imshow("Puppy",fix_img)
    if cv2.waitKey(20) & 0xFF==27:
        break
cv2.destroyAllWindows()