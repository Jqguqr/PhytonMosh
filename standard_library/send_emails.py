# email package from python standard library
# mine = multi porpuse internet mail extentions
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# To attache emage
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib


template = Template(Path("template.html").read_text())

message = MIMEMultipart()
# Headers
message["from"] = "Eduardo Estrada"
message["to"] = "eadrian10@live.com.mx"
message["subject"] = "This is a test"

# Body
# message.attach(MIMEText("Body", "plain"))
# body = template.substitute({"name": "John"})
body = template.substitute(name="John")
message.attach(MIMEText(body, "plain"))

# Get Image
try:
    message.attach(MIMEImage(Path("image.png").read_bytes()))
except ValueError:
    print("We can not find the image")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("eadrian10@live.com.mx", "password")
        smtp.send_message(message)
        print("Sent...")
    except ConnectionError:
        print("There is an error when sent the email")
