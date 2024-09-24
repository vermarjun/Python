import smtplib
from email.mime.text import MIMEText

# Define SMTP server and authentication details
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = input('Enter email: ')
smtp_password = input('Enter password: ') ##ENTER APP PASSWORD!!

# Create an email message
message = MIMEText('This is a test email')
message['Subject'] = 'Test Email'
message['From'] = 'vermarjun26@gmail.com'
message['To'] = 'vermarjun26@gmail.com'

# Establish a connection to the SMTP server
smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
smtp_connection.starttls()

# Log in to the SMTP server
smtp_connection.login(smtp_username, smtp_password)

# Send the email
for x in range(10):
    smtp_connection.send_message(message)

# Close the SMTP connection
smtp_connection.quit()