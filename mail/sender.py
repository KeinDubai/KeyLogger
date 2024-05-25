from os import getenv
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib

load_dotenv()

class EmailSender:
    def __init__(self, mailFrom:str, password:str, mailTo:str, subject:str, body:str) -> None:
        self.mailFrom = mailFrom
        self.password = password
        self.mailTo = mailTo
        self.subject = subject
        self.body = body

    def __createEmail(self) -> EmailMessage:
        em = EmailMessage()
        em["From"] = self.mailFrom
        em["To"] = self.mailTo
        em["Subject"] = self.subject
        em.set_content(self.body)
        return em

    def sendEmail(self) -> None:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.mailFrom, self.password)
            smtp.sendmail(self.mailFrom, self.mailTo, self.__createEmail().as_string())

if __name__ == "__main__":
    mailFrom = 'dragonball.xd.lol@gmail.com'
    password = getenv("PASSWORD")
    mailTo = 'gustavo.dela.fuente@hotmail.com'
    subject = 'Keylogger Test'
    body = 'Test'

    email_sender = EmailSender(mailFrom, password, mailTo, subject, body)
    email_sender.sendEmail()
