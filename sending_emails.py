from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# email messages to send emails in python


message = MIMEMultipart()
message["from"] = "Vinicius Pinho"
message["to"] = "vinicius.pinho@elsys.com.br"
message["subject"] = "This is a tes"
message.attach(MIMEText("Body"))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("vinicius.mpinho@gmail.com", "130277vcx1977")
    smtp.send_message(message)
    print("sent....")
