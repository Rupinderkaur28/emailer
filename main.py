from emailer.input import User
from emailer.mail_attachment import sent_mail_attach
from emailer.pdf import create_pdf


def main():
    input= User('abcdefr','xyzgr',34)
    data=input.user_input()
    is_valid= input.input_validation(data)
    if is_valid:
        print("ok")
    else:
        raise Exception("ERROR")
    create_pdf('test.pdf',data)
    sent_mail_attach('your email','to email','filename','password')



main()