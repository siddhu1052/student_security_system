import smtplib as sm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
import ssl
import csv
import datetime
def timer():
 data=""
 current_time = datetime.datetime.now()
 data=current_time
#  print(current_time)
 return data



def send_mails():
    
    sender ="sender@gmail.com"

    reciever="reciever@gmail.com"

    password='**************'

    subject="Entery time in campus(MRIIRS)"
    data="Your ward has entered the college at :"
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
    
    
    
def send_mails(data):
    with open('Student Details.csv',mode="r") as file :
        reader=csv.reader(file)
        for row in reader :
            if row[0] == data:
                r=row[3]
                break
    sender ="sender@gmail.com"
# reciever="varunkapasia51@gmail.com"
    reciever="sender@gmail.com"
# reciever="9900arya@gmail.com"
    password='rdcmzgpgbbituhne'

    subject="Entery time in campus(MRIIRS)"
    data="Your ward has entered the college at :"
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

send_mails("1/20/FET/BCS/139")