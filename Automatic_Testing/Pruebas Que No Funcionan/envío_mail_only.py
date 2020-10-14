import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

emailfrom = "sistemasgobstore@gmail.com"
emailto = "axolotlcode@gmail.com"
fileToSend = "allreports.html"
username = "sistemasgobstore@gmail.com"
password = input("Escribe tu contraseña por favor: ")

msg = MIMEMultipart()
msg["From"] = emailfrom
msg["To"] = emailto
msg["Subject"] = "Resultados de pruebas automatizadas"
msg.preamble = "Pruebas automatizadas de python"

variabledeTexto= "50 esta variable es una variabel chidas"

text = "Espero que estés teniendo un excelente día, te dejo un resumen de las pruebas automatizadas"

strTable = "<html><table><tr><th>Nombre de prueba</th><th>Totales</th><th>Pasadas</th><th>Errores</th></tr>"
lista1=['osqui','micho','tuti','ola']
lista2=[10,10,9,8]
lista3=[0,0,1,2]
lista4=[1,2,3,4]
for i in range(0,len(lista1)):
 #symb = chr(num)
 strRW = "<tr><td>"+str(lista1[i])+ "</td><td>"+str(lista2[i])+"</td><td>"+str(lista3[i])+"</td><td>"+str(lista4[i])+"</td></tr>"
 strTable = strTable+strRW
 
strTable = strTable+"</table></html>"
# ponemos las variables de MIME como texto plano y como html para poderle hacer attach al .msg
part1 = MIMEText(text, 'plain')
#part2 = MIMEText(html, 'html')
part2 = MIMEText(strTable, 'html')
ctype, encoding = mimetypes.guess_type(fileToSend)
if ctype is None or encoding is not None:
    ctype = "application/octet-stream"

maintype, subtype = ctype.split("/", 1)

if maintype == "text":
    fp = open(fileToSend)
    # Note: we should handle calculating the charset
    attachment = MIMEText(fp.read(), _subtype=subtype)
    fp.close()
elif maintype == "image":
    fp = open(fileToSend, "rb")
    attachment = MIMEImage(fp.read(), _subtype=subtype)
    fp.close()
elif maintype == "audio":
    fp = open(fileToSend, "rb")
    attachment = MIMEAudio(fp.read(), _subtype=subtype)
    fp.close()
else:
    fp = open(fileToSend, "rb")
    attachment = MIMEBase(maintype, subtype)
    attachment.set_payload(fp.read())
    fp.close()
    encoders.encode_base64(attachment)
attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
msg.attach(attachment)
msg.attach(part1)
msg.attach(part2)
server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(username,password)
#el sendmail tiene tres argumentos (de donde sale, a donde va y el mensaje)
server.sendmail(emailfrom, emailto, msg.as_string())

print("mensaje enviado")
server.quit()
