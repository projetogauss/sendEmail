from O365 import Account

# In this case, you will need to be used of the client_id and cliente_secree generated in your Azure Cloud account
credentials = ('client_id', 'client_secret')

account = Account(credentials)
m = account.new_message()
m.to.add('to_example@example.com')
m.subject = 'Testing!'
m.body = "This message was sent by python 0395 lib"
m.send()