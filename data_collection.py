#1 Importing the CSV module
import csv

with open('Student Details.csv',"a", newline="") as file:
    myFile = csv.writer(file)
    

    # myFile.writerow(["Roll no.","Name","DEPT", \
    #                 "Student_mail","Parent_mail","Mentor Mail Id"])


    noOfstudentLevels = int(input("Enter how many student levels you want: "))

    for i in range(noOfstudentLevels):
        roll = input("student "+ str(i+1) +": Enter Roll Number: ")
        name = input("student "+ str(i+1) +": Enter Name: ")
        dept = input("student "+ str(i+1) +": Enter Department: ")
        mails = input("student "+ str(i+1) +": Enter Student_mail: ")
        mailp = input("student "+ str(i+1) +": Enter Parent_mail: ")
        mailm = input("student "+ str(i+1) +": Enter Mentor_mail: ")
        myFile.writerow([roll, name,dept, mails, mailp,mailm])