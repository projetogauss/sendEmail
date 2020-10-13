import yagmail

receiver = 'tiago.sampaio@equatorialenergia.com.br'
body = 'Hello from Yagmail'
filename = 'contacts.csv'

try:
    yag = yagmail.SMTP('tyagosampaio@gmail.com')
    yag.send(
        to=receiver,
        subject='Yagmail test with attachment',
        contents=body,
        attachments=filename,

    )
except Exception as e:
    print(e)