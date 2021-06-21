import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
s = smtplib.SMTP('smtp.gmail.com', 587)
sender_email_id = 'likhokapesi04@gmail.com'
f = open('ithuba_details_file.txt', '+r')
line = f.readlines()
reciever_email_id = 'fullstackdeveloper1969@gmail.com'
password = input("Enter senders password: ")
subject = "Hello All"
msg = MIMEMultipart()
msg['from'] = sender_email_id
msg['To'] = reciever_email_id
msg['Subject'] = subject
body = "Felicitations!\n"
body = body + "you have won! a prize from ITHUBA National Lottery of South Africa"

msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
s.starttls()
s.login(sender_email_id, password)

s.sendmail(sender_email_id, reciever_email_id, text)
s.quit()
