
import smtplib # simple mail transfer protocol

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()  #tls = transport layer security

# input all the details
sender_email = input("enter sender email : ")
password = input("enter the password : ")

reciever_email = input("enter the reciever email : ")
message = input("enter the message to be sent : ")

#login
server.login(sender_email , password)

server.sendmail(sender_email, reciever_email , message)

print("mail sent successfully")
