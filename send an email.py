# send an email

import smtplib

sender ="fadiabdf5@gmail.com"
receiver ="fido050505bdf@gmail.com"
password ="dxqkmnmdeiwqbous"# mot de passe générer
subject = "Python email test"
body ="I wrote an email! :D "
#header
# to hundele multiple line of text we use this " three times
message = f"""From: Fadia Boudiaf {sender}
To:Faten boudiaf{receiver}
Subject:{subject}\n
{body}
"""
# server object
server = smtplib.SMTP("smtp.gmail.com",587)# the default port number
server.starttls()

try:

    server.login(sender,password)
    print("Logged in...")
    server.sendmail(sender,receiver, message)
    print("Email has been sent!")
except smtplib.SMTPAuthenticationError:
    print("unable to sign in")

# you may have this error
'''
smtplib.SMTPAuthenticationError: (534, b'5.7.9 Application-specific password required. Learn more at\n5.7.9  https://support.google.com/mail/?p=InvalidSecondFactor l11-20020adff48b000000b0031c3ee933b5sm4599218wro.108 - gsmtp')
you may visit less secure app access, just write in search section : accès aux applications moins sécurisé then generer un mot de passe pour la messagerie
'''

