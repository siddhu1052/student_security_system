import smtplib as sm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
import ssl
import datetime
def timer():
 data=""
 current_time = datetime.datetime.now()
 data=current_time
#  print(current_time)
 return data




sender ="varunkapasia8010@gmail.com"
# reciever="varunkapasia51@gmail.com"
reciever="siddhussingh@gmail.com"
# reciever="9900arya@gmail.com"
password='emyxinuapcdfdtea'

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
