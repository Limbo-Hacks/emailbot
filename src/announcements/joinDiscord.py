import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465
sender_mail = input("Enter the mail address of limbohacks: ")
password = input("Input the password of limbohacks mail: ")
no_hacker_mails = int(input("Input the no of hacker emails: "))
hacker_mails = []

for i in range(0, no_hacker_mails):
    no = i
    no += 1
    up = repr(no)
    no -= 1
    statement = "Enter the mail no " + up + ": "
    ele = input(statement)
    hacker_mails.append(ele)


message = MIMEMultipart("Limbo Hacks")
message["Subject"] = "Join Discord"
message["From"] = sender_mail
message["To"] = ", ".join(hacker_mails)

head = """\
    LimboHacks
    """
html = """\
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
<style>
body {
  background-color: black;
  text-align: center;
  color: white;
}
</style>
</head>
<body>

<h1>Join our Discord</h1>
<p>Join our <a href="https://discord.gg/8XJSzmtWPp">Discord</a> and meet amazing hackers and judge from globe</p>

</body>
</html>
"""

div1 = MIMEText(head, "plain")
div2 = MIMEText(html, "html")

message.attach(div1)
message.attach(div2)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
    server.login(sender_mail, password)
    server.sendmail(sender_mail, hacker_mails, message.as_string())
    print("Discord announcement sent")
