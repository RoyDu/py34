from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib


def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))

# input Email id and pwd
from_addr = 'duzhuoqi@outlook.com'  #input('From: ')
pwd = input('Password: ')
to_addr = input('To: ')
smtp_server = 'smtp-mail.outlook.com'    #input('SMTP server: ')

msg = MIMEMultipart()

msg['From'] = _format_addr('Python user <%s>' % from_addr)
msg['To'] = _format_addr('管理 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候...','utf-8').encode()

msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    #'<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8'))

with open('C:\\aaa.png', 'rb') as f:
	mime = MIMEBase('image','png', filename='aaa.png')
	mime.add_header('Content-Disposition','attachment', filename='aaa.png')
	mime.add_header('Content-ID','<0>')
	mime.add_header('X-Attachment-Id','0')	
	mime.set_payload(f.read())
	encoders.encode_base64(mime)
	msg.attach(mime)


server = smtplib.SMTP(smtp_server, 587)
server.set_debuglevel(1)
server.ehlo()
server.starttls()     #tls encryption
server.login(from_addr, pwd)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit() 