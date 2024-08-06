# import smtplib as smtp
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText


# server = smtp.SMTP('smtp.gmail.com',587)
# server.ehlo()
# server.starttls()
# server.login('getpc2022@gmail.com','minimal8')
# emailadd = 'cretivox.de@gmail.com'
# # print(body)
# msg = 'test email from getpc'
# server.sendmail("getpc2022@gmail.com",emailadd,msg)
# print("Success Send")
# server.quit()


# import smtplib, ssl
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.application import MIMEApplication
# import pandas as pd



# email_from = 'getpc2022@gmail.com'
# password = 'ogjnoeylpyxgqxrb'
# email_to = 'cretivox.dev@gmail.com'

# email_message = MIMEMultipart()
# email_message['From'] = email_from
# email_message['To'] = email_to
# email_message['Subject'] = 'Hi {}, this is test from getpc2022'.format(email_to)
# print(email_to)
# # Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
# # email_message.attach(MIMEText(html, "html"))

# email_string = email_message.as_string()

# # Connect to the Gmail SMTP server and Send Email
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL("smtp.gmail.com", 1025, context=context) as server:
#     server.login(email_from, password)
#     server.sendmail(email_from, email_to, email_string)

# import smtplib
# import ssl

# # Setup port number and servr name

# smtp_port = 587                 # Standard secure SMTP port
# smtp_server = "smtp.gmail.com"  # Google SMTP Server

# email_from = "getpc2022@gmail.com"
# email_to = "cretivox.dev@gmail.com"

# pswd = "ogjnoeylpyxgqxrb"

# # content of message

# message = "Dr!!!"

# # Create context
# simple_email_context = ssl.create_default_context()


# try:
#     # Connect to the server
#     print("Connecting to server...")
#     TIE_server = smtplib.SMTP(smtp_server, smtp_port)
#     TIE_server.starttls(context=simple_email_context)
#     TIE_server.login(email_from, pswd)
#     print("Connected to server :-)")
    
#     # Send the actual email
#     print()
#     print(f"Sending email to - {email_to}")
#     TIE_server.sendmail(email_from, email_to, message)
#     print(f"Email successfully sent to - {email_to}")

# # If there's an error, print it out
# except Exception as e:
#     print(e)

# # Close the port
# finally:
#     TIE_server.quit()


"""
######################################################################
Email With Attachments Python Script
Coded By "The Intrigued Engineer" over a coffee
Thanks For Watching!!!
######################################################################
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
import os

# Setup port number and server name

smtp_port = 587                 # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

email_from = "getpc2022@gmail.com"

pswd = "ogjnoeylpyxgqxrb"


# name the email subject
subject = "New email from TIE with attachments!!"



# Define the email function (dont call it email!)
person = "rhohim27@gmail.com"
# Make the body of the email
body = f'''Subject: A plain text email
To: {''.join(person)}
This is a new test email sent by Python.'''

# make a MIME object to define parts of the email
msg = MIMEMultipart()
msg['From'] = email_from
msg['To'] = person
msg['Subject'] = subject

# Define the file to attach
filename = "15701-30854-1-SM.pdf"

# Attach the body of the message
msg.attach(MIMEText(body, 'plain'))

# with open(filenamepdf,'rb') as file:
# # Attach the file with filename to the email
#     msg.attach(MIMEApplication(file.read(), Name=filenamepdf))

# pdf = MIMEApplication(open(filenamepdf, 'rb').read())
# pdf.add_header('Content-Disposition', 'attachment', filename = filenamepdf)
# msg.attach(pdf)
    
# Open the file in python as a binary
attachment= open(filename, 'rb')  # r for read and b for binary

# Encode as base 64
attachment_package = MIMEBase('application', 'octet-stream')
attachment_package.set_payload((attachment).read())
encoders.encode_base64(attachment_package)
attachment_package.add_header('Content-Disposition', "attachment; filename= " + filename)
msg.attach(attachment_package)

# Cast as string
text = msg.as_string()

# Connect with the server
print("Connecting to server...")
TIE_server = smtplib.SMTP(smtp_server, smtp_port)
TIE_server.starttls()
TIE_server.login(email_from, pswd)
print("Succesfully connected to server")
print()


# Send emails to "person" as list is iterated
print(f"Sending email to: {person}...")
TIE_server.sendmail(email_from, person, text)
print(f"Email sent to: {person}")
print()

# Close the port
TIE_server.quit()


# Run the function
