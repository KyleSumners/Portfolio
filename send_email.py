import smtplib, ssl
import os

host = "smtp.gmail.com"
port = 465

username = "kylesumners242@gmail.com"
password = os.getenv("PASSSWORD")


receiver = "kylesumners242@gmail.com"
context = ssl.create_default_context()

message = """
Subject: Hi!
Hi!
How are you?
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)