amount=int(input("Enter total order amount:  "))
discount=0
if(amount>=5000):
    discount=amount*0.2
elif(amount>=3000 and amount<5000):
    discount=amount*0.1
elif(amount>=1000 and amount<3000):
    discount=amount*0.05
else:
    discount=0
finalamount=amount-discount
print("Final payable amount is:",finalamount)