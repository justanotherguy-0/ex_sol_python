d=str((0,1,2,3,4,5,6,7,8,9))
password=input("Password testing. Write your password: ")

def number_detector(p):
    a=False
    for i in p:
        if d.count(i)>0:
            a=True    
    return a        
if not password.islower() and not password.isupper() and number_detector(p):
    print('I can\'t hack you')
else:
    print('Your bank account is mine( and so is your wife :v)')