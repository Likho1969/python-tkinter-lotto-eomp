
import smtplib
from tkinter import *


s = smtplib.SMTP('smtp.gmail.com', 587)
sender_email_id = 'likhokapesi04@gmail.com'
receiver_email_id = ['godwin@lifechoices.co.za', 'thapelo@lifechoices.gmail.co.za', 'fullstackdeveloper1969@gmail.com', 'likhokapesi135@gmail.com']
password = input("Enter senders email password: ")
# start TLS for security
s.starttls()
# Authentication
s.login(sender_email_id, password)
# message to be sent
message = "Felicitations!\n"
message = message + "you have won! a prize from ITHUBA National Lottery of South Africa"
# sending the mail
s.sendmail(sender_email_id, receiver_email_id, message)
# terminating the session
s.quit()
