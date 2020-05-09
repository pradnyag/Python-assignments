import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from PIL import Image

username='pradorockss@gmail.com'
password='prado@123'

def send_mail(text= 'Email Body',subject='Hello World',from_email='Pradnya Gade <pradorockss@gmail.com>',to_emails=
None,):
    assert isinstance(to_emails,list)
    msg = MIMEMultipart("alternative")
    msg['From']= from_email
    msg['To']= ", ".join(to_emails)
    msg['Subject']= subject

    txt_part= MIMEText(text,'plain')
    msg.attach(txt_part)

    html_part= MIMEText("<h1>This is working</h1>",'html')
    msg.attach(html_part)

    img  = Image.open(r"C:\Users\Prado\Desktop\Projects\Practice\SMTP_module\image.jpg")  
    
    img_part=MIMEImage(img.tobytes(),'jpg')
    msg.attach(img_part)

    msg_str= msg.as_string()

    #login to smtp server
    server= smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(from_email,to_emails,msg_str)
    server.quit()

    # with smtplib.SMTP() as server:
    #     pass

if __name__ == "__main__":
    send_mail(to_emails=['pradorockss@gmail.com']) 
