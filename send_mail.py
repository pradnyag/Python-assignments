import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

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


    #Attaching image 
    img_path=r'C:\Users\Prado\Desktop\Projects\Practice\SMTP_module\image.jpg'
    
    img_part=MIMEImage(open(img_path,'rb').read(),'jpg',name='image')
    img_part.add_header('Content-ID','animal image')
    msg.attach(img_part)


    # Attaching html part

    html_content= """\
    <html>
    <head></head>
    <body>
        <p>Hi!<br>
        Here is the <a href="https://www.python.org">link</a> you wanted.<br>
        <img src="{{url_for('static',filename=img_path)}} alt="Smiley face" width="100" height="100" align="middle" style="margin:0px 50px">
    </body>
    </html>
    """

    html_part= MIMEText(html_content,'html')
    msg.attach(html_part)

    
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
