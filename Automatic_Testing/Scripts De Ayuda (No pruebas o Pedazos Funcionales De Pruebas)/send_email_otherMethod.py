import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "sistemasgobstore@gmail.com"
password = input("Type your password and press enter: ")
#password.encode('utf-8')

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    #server = smtplib.SMTP(smtp_server,port)
    server = smtplib.SMTP(smtp_server,port,None,30)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    server.sendmail("sistemasgobstore@gmail.com","alejandro.elara@gmail.com","hole muneecote, te lo envio desde paiton")
    print("Correo enviado exitosamente")
    # TODO: Send email here
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 
