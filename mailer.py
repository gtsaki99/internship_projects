import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import stdiomask   #will need pip install stdiomask beforehand if to be run from command line
import requests    #will need pip install requests beforehand if to be run from command line
import os


path = r'' #insert path you want

def do():
    if os.path.exists(path):
        #getting sender's email address, receiver's address and structural info of email(message and subject)
        sender = input("Please enter sender's email address: ")
        #get password of user by covering the characters with an asterisk
        pwd = stdiomask.getpass(prompt="Please enter the senders password: ", mask = '*')
        #rest of the info
        receiver = input("Please enter the receivers address: ")
        subject = input("Please enter the subject that you want to be included in the email: ")
        body = input("Please write any message that you want to be written in the email: ")
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = subject

        #creating the body of the email
        msg.attach(MIMEText(body, 'plain'))
        attachment = open(path, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload(attachment.read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename = %s" % path.replace(r'__', "")) #replace __ with all the initial path except the file name
        msg.attach(p)
        text = msg.as_string()

        #getting sender's smtp server address and port number using sender's email address
        info = requests.get("https://emailsettings.firetrust.com/settings?q=" + sender)
        temp, useful = info.text.split('"SMTP","address":"')
        server, useful1 = useful.split('","port":')
        portNo, useful2 = useful1.split(',"secure":"')
        protocol, temp1 = useful2.split('","username"')
        # delete useless variables
        del temp, temp1, useful1, useful2

        #user warning message
        if server == "smtp.mail.yahoo.com" or server == "smtp.gmail.com":
            print("Services like gmail or yahoo will require access to less secure apps for this program to work. If not enable please enable it and restart this program. For instructions visit these websites: https://support.google.com/accounts/answer/6010255?hl=en for gmail and: https://support.reolink.com/hc/en-us/articles/360004195474-How-to-Allow-Less-Secure-Apps-to-Access-Your-Yahoo-Mail")

        #attempting connection using each smtp server's protocol
        if protocol == 'TLS':
            s = smtplib.SMTP(server, portNo)
            s.starttls()
        else:
            s = smtplib.SMTP_SSL(server + ':' + portNo)
        s.login(sender, pwd)
        s.sendmail(sender, receiver, text)
        s.quit()
        print("Email sent successfully.")
    else:
        print(r'File does not exist in __. Try creating it or putting it in this path and then run program again') #__ as above

do()
#lastModTime = 0                                to run the program every time the file in path gets updated
#while True:
#    if os.path.getmtime(path) != lastModTime:
#        do()
#        lastModTime = os.path.getmtime(path)