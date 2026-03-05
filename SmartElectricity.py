unit=int(input("Enter the number of units Contotaled :"))
total=0
if(unit<=100 and unit>0):
    total=100*3
elif(unit<=200):
    total=100*3+(unit-100)*5
else:
    total=100*3+100*5+(unit-200)*8

if(unit>300):
    total=total+(total*10)/100
print("Electricity bill is :",total)