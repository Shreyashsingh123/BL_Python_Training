balance=int(input("Enter the Availabe balance"))
a=int(input("Enter number of times withdrawal request"))

while(a!=0):
    amt=int(input("Enter amount to withdraw"))
    if(amt<=balance and amt%100==0):
        balance-=amt
        print("Success")
    else:
        print("Failed")
    a-=1
print(balance)