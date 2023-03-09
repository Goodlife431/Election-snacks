import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
with open("password.txt", "r") as f:
    password = f.read()

server.login("oduwolejohn431@gmail.com", password)

msg = MIMEMultipart()
msg['from'] = "Python"
msg['To'] = "seunjohn431@gmail.com"
msg['Subject'] = "Body"

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = "twitter profile.jpeg"
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('oduwolejohn431@gmail.com', 'seunjohn431@gmail.com', text)

