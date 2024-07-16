import re

def isValidEmail(email):
    # regex expression for the validation of the email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if(re.fullmatch(regex, email)):
        return True
    else:
        return False
    
email = input('hello, input email address: ')

    
if isValidEmail(email):
        username = email[0:email.index('@')]
        domain = email[email.index('@')+1:]
        print('Username : ', username)
        print('Domain is: ' , domain)
else:
     print('Invalid email')