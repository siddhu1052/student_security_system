import cv2
import scipy.misc as sp
# from scipy.misc import toimage, imsave
import matplotlib.pyplot as plt
import numpy as np
# img=cv2.imread(".\\Student_images\\pxfuel.jpg")

# printing image in new window
# while True :
#     cv2.imshow('result',img)
#     if cv2.waitKey(2)==27 :
# 	    break

# cv2.destroyAllWindows()
haar_data = cv2.CascadeClassifier(".\data1.xml")

# find face using haar cascade data
# while True :
#     faces=haar_data.detectMultiScale(img)
#     for x,y,w,h in faces :
# 	    cv2.rectangle(img, (x,y), (x+w,y+h), (10,5,2), 5)
#     cv2.imshow('result',img)
#     if cv2.waitKey(2)==27 :
# 	    break
# cv2.destroyAllWindows()

new_roll_number="1_20_FET_BCS_139"
final_path=".//Student_images//"+new_roll_number+".png"

capture= cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:
    face,img=capture.read();
    faces=haar_data.detectMultiScale(img)
    for x,y,w,h in faces :
        cv2.rectangle(img, (x,y), (x+w,y+h), (225,0,225), 2)
        face=img[y:y+h,x:x+w,:]
        # face=cv2.resize(face,(50,50))
        # print(len(data))
    cv2.imshow('result',img)
    if cv2.waitKey(2)==32 :
        cv2.imwrite(final_path,face)
        break;
cv2.destroyAllWindows()