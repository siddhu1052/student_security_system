import cv2
import csv
import pandas as pd
from pyzbar import pyzbar
import matplotlib.pyplot as plt
# from deepface import DeepFace
import smtplib as sm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
import ssl
import datetime
import face_recognition
from PIL import Image, ImageDraw
# import face_recognition as fr  


cap = cv2.VideoCapture(0)
#########################################################################################################################
def load_and_encode_image(image_path):
    image = face_recognition.load_image_file(image_path)
    face_encoding = face_recognition.face_encodings(image)
    if face_encoding:
        return face_encoding[0]
    return None

def compare_faces(image_path1, image_path2):
    # Load and encode faces
    face_encoding1 = load_and_encode_image(image_path1)
    face_encoding2 = load_and_encode_image(image_path2)

    if face_encoding1 is None or face_encoding2 is None:
        return False  # Unable to find faces in one or both images

    # Compare faces
    results = face_recognition.compare_faces([face_encoding1], face_encoding2)
    return results[0]

def draw_rectangle_on_face(image_path, face_location):
    image = face_recognition.load_image_file(image_path)
    pil_image = Image.fromarray(image)
    draw = ImageDraw.Draw(pil_image)

    top, right, bottom, left = face_location
    draw.rectangle([left, top, right, bottom], outline="red", width=2)
    pil_image.show()

#############################################################################################################
def timer():
    data=""
    current_time = datetime.datetime.now()
    data=current_time
#  print(current_time)
    return data


# #############################################################################
# def face_comparision(path1,path2):
    
    

########################################################################################################
def send_mails(data):
    with open('Student Details.csv',mode="r") as file :
        reader=csv.reader(file)
        for row in reader :
            if row[0] == data:
                r=row[4]
                break
    sender ="sender@gmail.com"
    reciever=r
    password='**************'

    subject="Entery time in campus(MRIIRS)"
    data="Your ward "+ row[1] + " has entered the college at :"
    time=timer()

#print(type(time));
    body=data+str(time)
# body+=data+time

    em=EmailMessage()
    em['From']=sender;
    em['To']=reciever
    em['Subject']=subject
    em.set_content(body)

    context=ssl.create_default_context()
    server=sm.SMTP_SSL("smtp.gmail.com",465)
# server.starttls()
    server.login(sender,password)
    server.sendmail(sender,reciever,em.as_string())
    print("Done");

        
    
####################################################################################################################
while True:
    ret, frame = cap.read()
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        data = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (10,5,2), 2)
        path=str(data)
        path=path.replace("/","_")
        extension=".png";
        b="Student_images\\"
        path=b+path+extension
        print(data)
        print(path);
        img = cv2.imread(path);
        plt.imshow(img)
        haar_data = cv2.CascadeClassifier(".\data1.xml")
        final_path='Student_images\\temp.png'
        while True :
            cv2.imshow('result',img)
            
            while True:
                face,img=cap.read();
                faces=haar_data.detectMultiScale(img)
                for x,y,w,h in faces :
                    cv2.rectangle(img, (x,y), (x+w,y+h), (225,0,225), 2)
                    face=img[y:y+h,x:x+w,:]
                cv2.imshow('result',img)
                cv2.imwrite(final_path,face)
                
                if compare_faces(final_path, path):
                    send_mails(data)
                    break;
                if cv2.waitKey(2)==32 :
                    break;
            cv2.destroyAllWindows();
            break;
            
        
        
    cv2.imshow("Barcode Scanner", frame)
    if cv2.waitKey(1)==27:
        break
cap.release()

cv2.destroyAllWindows()