#Author: Tiffany-Ellen Vo
#Description: Mass emailing for Baskin Day (and general use)

#Keep in mind, GMAIL restricts users to 500 emails per 24 hrs
#In order for this program to work, you need to change your gmail setting for security
#If not, you will receive an error because Google will block your device from logging in
#To do so, settings-> security-> less secure app access ON

import smtplib
 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# sender email address
email_user = 'SENDER_EMAIL'
 
# sender email passowrd for login purposes
email_password = 'SENDER_EMAIL_PASSWORD'

# list of users to whom email is to be sent
# enter list of emails in format ['email@gmail.com', 'sammyslug@gmail.com']
email_send = ['LIST_OF_RECIPIENTS']
subject = 'EMAIL_SUBJECT'
msg = MIMEMultipart()
msg['From'] = email_user

# converting list of recipients into comma separated string
# Email message is in HTML format to have more flexibility on how the email looks
# Please refer to HTML syntax to add whatever messages, images, etc., you want
msg['To'] = ", ".join(email_send)
msg['Subject'] = subject
body = """<html>
            <body>
              <p> START MESSAGE HERE </p>
              <p> <b> This email was sent from a python script. </b> </p>
            </body>
          </html>
       """
msg.attach(MIMEText(body, 'html'))
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)
server.sendmail(email_user,email_send,text)
server.quit()
