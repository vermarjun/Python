##JOSE POTILLAS CODE, IDK WAS GETTING SOME ERRORS!

import smtplib #Importing SMTP LIBRARY
import getpass #Get password from user in a safe way so that you dont have to store it as raw string!
#Create an smtp_object from the library, in SMTP(), it is expecting a str(What host you want to use), port num(available ports are 587, 465)
smtp_obj = smtplib.SMTP('smtp.gmail.com',587)
#This .ehlo() connects you to the server, it returns something like this --> (250, b'smtp.gmail.com at your service) which means connected to the server
x = smtp_obj.ehlo()
print(x)
#PORT 587 uses an encryption method TLS, while 465 uses SSL. By this line we are just activating encryption
x = smtp_obj.starttls()
print(x)
email = input('Enter your email: ') #Safe way to get email from user
password = input('Enter your password: ') #Safe way to get password from user
x = smtp_obj.login(email,password)
print(x) 
from_adress = input('Enter whom you want to send email as: ')
to_adress = input('Enter who you want to send email to: ')
subject = input('Enter a subject for email: ')
message = input('Enter a message for email: ')
msg = 'Subject: '+ subject + '\n', message
x =  smtp_obj.sendmail(from_adress, to_adress, msg)
print(x)
smtp_obj.quit()