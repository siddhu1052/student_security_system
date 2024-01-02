import csv
from barcode import Code128
import cv2
import matplotlib.pyplot as plt
from barcode.writer import ImageWriter
import matplotlib.pyplot as plt
import numpy as np
import scipy.misc as sp

################### TAKE PICTURE ######################################################################

def image_capturing(no):
    haar_data = cv2.CascadeClassifier(".\data1.xml")
    new_roll_no=no.replace("/","_")
    final_path=".//Student_images//"+new_roll_no+".png"

    capture= cv2.VideoCapture(0,cv2.CAP_DSHOW)
    while True:
        face,img=capture.read();
        faces=haar_data.detectMultiScale(img)
        for x,y,w,h in faces :
            cv2.rectangle(img, (x,y), (x+w,y+h), (225,0,225), 2)
            face=img[y:y+h,x:x+w,:]
            # face=cv2.resize(face,(50,50))
        
        cv2.imshow('result',img)
        if cv2.waitKey(2)==32 :
            cv2.imwrite(final_path,face)
            break;
    cv2.destroyAllWindows()

################### CREATE BARCODE ############################################################
def barcode_maker(No):
    new_roll_no=No.replace("/","_")

# creation of barcode 
    b=Code128(No,writer=ImageWriter())
    final_path=".\\barcodes\\"+new_roll_no
# b.save (new_roll_no);
    b.save (final_path);

# with open('.\\barcodes','a') as folder:
#     folder.write(b)
# print karne ke lie 
# new_roll_no+='.png'

    final_path+='.png';
    img = cv2.imread(final_path)
    while True :
        cv2.imshow('result',img)
        if cv2.waitKey(2)==27 :
	        	break

# print (first_step)
    
############## ASKING FOR DETAILS ######################################################################################

with open('Student Details.csv',"a", newline="") as file:
    myFile = csv.writer(file)
    

    # myFile.writerow(["Roll no.","Name","DEPT", \
    #                 "Student_mail","Parent_mail","Mentor Mail Id"])


    noOfstudentLevels = int(input("Enter number of entries to do : "))

    for i in range(noOfstudentLevels):
        roll = input("student "+ str(i+1) +": Enter Roll Number: ")
        name = input("student "+ str(i+1) +": Enter Name: ")
        
        
        dept = input("student "+ str(i+1) +": Enter Department: ")
        mails = input("student "+ str(i+1) +": Enter Student_mail: ")
        mailp = input("student "+ str(i+1) +": Enter Parent_mail: ")
        mailm = input("student "+ str(i+1) +": Enter Mentor_mail: ")
        myFile.writerow([roll, name,dept, mails, mailp,mailm])
        barcode_maker(roll)
        print("Click a picture");
        image_capturing(roll)
        
#############################################################################################################################
'''
1/20/FET/BCS/139
Siddharth Singh
FET
siddhussingh@gmail.com
siddhussingh@gmail.com
siddharthmentor@gmail.com

1/20/FET/BCS/133
Varun Kapasia
FET
varunkapasia51@gmail.com
varunkapasia8010@gmail.com
varunmentor@gmail.com

1/20/FET/BCS/142
Deepanshu Choudhary
FET
ppkkcc2@gmail.com
ppkkcc2@gmail.com
deepanshuofficial4@gmail.com


1/20/FET/BCS/141
Tushar Saini
FET
tusharto0511@gmail.com
arcsuper16@gmail.com
boy298011@gmail.com

1/20/FET/BCS/202
Aman Negi
FET
anegi9643@gmail.com
negia9848@gmail.com
boy298011@gmail.com

'''