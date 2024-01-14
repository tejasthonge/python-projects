
'''
Depndance :pip install secure-smtplib
'''

import smtplib as s

obj = s.SMTP('smtp.gmail.com',587)   #587 is gmail port 

obj.ehlo()
obj.starttls()

obj.login('amarthonge6767@gmail.com','AMAR7558667986@6767')
subject="Test by pyhton"
body="this is test email by python"
massage = "subject:{}\n\n{}".format(subject,body)


#resiver email
listEmail =["dev@tejasthonge.tech","tejasthonge.sits.entc@gmail.com"]

obj.sendmail('amrthonge6767@gmail.com',listEmail,massage)
print("Done sending")

ob.quit()
