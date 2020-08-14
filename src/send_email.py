import markdown
import codecs
import os

os.system("python src/functions.py")
# Login
service = service_account_login()

# Elementos del email
EMAIL_FROM    = ''
EMAIL_TO      = 'angel.r.chicote@gmail.com'
EMAIL_SUBJECT = 'Hello  from Lyfepedia!'
EMAIL_CONTENT = read_markdownfile(file_md = "markdown/message.md")

# Generamos el mensaje y enviamos
message = create_message(EMAIL_FROM, EMAIL_TO, EMAIL_SUBJECT, EMAIL_CONTENT)
sent    = send_message(service, 'me', message)

