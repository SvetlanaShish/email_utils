import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 
from sys import argv

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Svetlana'
email['to'] = 'shishmareva.2013@mail.ru'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login(input('Enter your mail'), input('Enter your password'))
  smtp.send_message(email)
  print('all good boss!')