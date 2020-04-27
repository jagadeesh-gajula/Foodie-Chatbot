import smtplib 
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login("gajulajagadeesh7@gmail.com", "!V!cky@pgdml@123")
message = "The details of all the restaurants you inquried \n \n"
global res
message = "hello this email is to check the code"
try:
    s.sendmail("gajulajagadeesh7@gmail.com", str("cherryjan96@gmail.com"), message)
    s.quit()
    print("email sent")
except:
    print("this is is not working")