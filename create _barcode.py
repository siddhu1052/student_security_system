from barcode import Code128
import cv2
import matplotlib.pyplot as plt
from barcode.writer import ImageWriter

# Input of roll number
No=input("Enter the Roll No :")
new_roll_no=No.replace("/","_")

# creation of barcode 
b=Code128(No,writer=ImageWriter())
final_path="C:\\Users\\rpnih\\Desktop\\manav rachna\\6th Sem\\cloud project\\barcodes\\"+new_roll_no
# b.save (new_roll_no);
b.save (final_path);

# with open('C:\\Users\\rpnih\\Desktop\\manav rachna\\6th Sem\\cloud project\\barcodes','a') as folder:
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