import smtplib

def send_email(email, content):
    sender = "sender@email.com"
    recipient = email
    subject = "Email with abstracted information"
    body = content

    message = "Subject: {}\n\n{}".format(subject, body)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.
