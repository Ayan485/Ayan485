import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

recipients = ''' + str(input("Enter E-mail IDs ")) + '''

email_user = 'ennmeemayan.2971.11Sc@gmail.com'
email_password = 'Ennmeemayan'
email_send = recipients

sub =  str(input("Enter the Subject"))

subject = sub

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

bd = str(input("Enter The Mail"))

body = bd
msg.attach(MIMEText(body,'plain'))

filename=r"C:\Users\Ayan\Pictures\Saved Pictures\do-a-simple-but-cool-profile-pic-or-logo-for-u.jpeg"
attachment  =open(filename,"rb")

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+ filename)

msg.attach(part)

#msg = 'Hi how are you?'
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit()
