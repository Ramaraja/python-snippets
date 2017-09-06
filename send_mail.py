# Python code to Sending mail 
# from your Gmail account 
import smtplib
 
# list of email_ids
li = ["xxxxx@gmail.com", "yyyyy@gmail.com"]
 
for i in range(len(li)):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("sender_email_id", "sender_email_id_password")
    message = "This a test mail from Python"
    s.sendmail("sender_email_id", li[i], message)
    s.quit()
