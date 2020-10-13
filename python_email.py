import smtplib, ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

smtp_server = 'smtp.gmail.com'
# port for gmail with ssl
port = 465
#port to gmail without ssl
# port = 587
sender = 'tyagosampaio@gmail.com'
password = input('Enter your password here:')
context = ssl.create_default_context()

receiver = 'tyagosampaio@gmail.com'

message = MIMEMultipart('alternative')
message['Subject'] = 'Test Image!'
message['From']    = sender
message['To']      = receiver
text = """\
    Hi There!
    This message  was sent from Python"""

html = """\
    <html>
    <body>
        <p>Hi, <br>
        How are you?<br>
        <a href="http://www.realpython.com">Real Python</a> has many great tutorials. </p>
    </body>
    </html>    
"""

part1  = MIMEText(text, 'plain')
part2  = MIMEText(html, 'html')

filename = 'img.png'

with open(filename,'rb') as attachment:
    part_a = MIMEBase('application','octet-stream')
    part_a.set_payload(attachment.read())

encoders.encode_base64(part_a)

part_a.add_header(
    'Content-Disposition',
    f'attachment; filename={filename}')
message.attach(part1)
message.attach(part2)
message.attach(part_a)

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    #send email
    server.sendmail(sender,receiver, message.as_string())
    print('It worked')

#conection unsecurity with server without ssl
"""
try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender, password)
    #send email
    print('Its Worked!')
except Exception as e:
    print(e)
finally:
    server.quit()
"""