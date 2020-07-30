import cv2
import numpy as np
def sketch(image):

    #converting image to gray scale
    img_gray = cv2.cvtcolor(image,cv2.COLOR_BGR2GRAY)

    #blurring image to remove noise
    img_blur = cv2.GassianBlur(img_gray,(3,3),0)

    #extracting edges
    edges= cv2.Canny(img_blur,10,80)

    #applying threshold inverse
    ret,mask=cv2.threshold(edges,50,255,cv2.THRESH_BINARY_INV)
    return mask
#capturing video from webcam
cap=cv2.VideoCapture(0)

#constant image capture from video
while True:
    ret,frame=cap.read()
    cv2.imshow('origginal',frame)
    cv2.imshow('Live_Sketch',sketch(frame))
    #key13==enter_key
    if cv2.waitKey(1)==13:
        break
#releasing webcam
cap.release()
#destroying window
cv2.destroyAllWindows()
