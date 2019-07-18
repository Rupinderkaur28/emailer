
import smtplib

def sendemail(from_addr, to_addr_list, subject, message,login, password,
              smtpserver='smtp.gmail.com:587'):
    header = 'From: %s ' % from_addr
    header += 'To: %s' % ', '.join(to_addr_list)
    header += 'Subject: %s' % subject
    message = header + message

    try:
        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(login, password)
        problems = server.sendmail(from_addr, to_addr_list, message)
        server.quit()
    except Exception as err:
        print(err)


