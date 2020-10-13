import yagmail

receiver = 'youremail@gmail.com'
body = 'Hello from Yagmail'
filename = 'contacts.csv'

try:
    yag = yagmail.SMTP('youremail@gmail.com')
    yag.send(
        to=receiver,
        subject='Yagmail test with attachment',
        contents=body,
        attachments=filename,

    )
except Exception as e:
    print(e)