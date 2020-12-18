import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  # os.path

html = Template(Path('./email/index.html').read_text())

# https://habr.com/ru/sandbox/128490/
email = EmailMessage()

email['from'] = 'sergei'
email['to'] = 'loginTo'
email['subject'] = 'fsadf'

email.set_content(html.substitute({'name': 'TinTIn'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('loginFrom', 'passwordFrom')
    smtp.send_message(email)
    print('OK')
