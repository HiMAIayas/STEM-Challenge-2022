import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

ImgFileName = 'STEMVISION\code\imageprocessing\camimages\cam1.png'
with open(ImgFileName, 'rb') as f:
    img_data = f.read()

msg = MIMEMultipart()
msg['Subject'] = 'ก๊อกๆๆ พัสดุมาส่งแล้วจ้า'
msg['From'] = '_YOUR_EMAIL_1'
msg['To'] = '_YOUR_EMAIL_2'

text = MIMEText('ชื่อผู้รับพัสดุ: ')
msg.attach(text)
image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
msg.attach(image)

context = ssl.create_default_context()

s = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
s.login('_YOUR_EMAIL_1', 'ykgivwgegernlbch')
s.sendmail(msg['From'], msg['To'], msg.as_string())
