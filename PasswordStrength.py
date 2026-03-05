password=input("Enter Password")
upper=False
digit=False
lower=False
for i in password:
 if(i.isupper()):
    upper=True
 elif(i.isdigit()):
    digit=True
 elif(i.islower()):
    lower=True
if(upper and digit and lower):
    print("Strong Password")
else:
    print("Weak Password")

    
 