salary=int(input("Enter salary: "))
latedays=int(input("Enter late days"))
absentdays=int(input("Enyter total absent days:"))
if(latedays>5 and latedays<=10):
    sum=salary*0.05
    salary-=sum
elif(latedays>10):
    sum=salary*0.1
    salary-=sum
if(absentdays>2):
    absent=salary*0.05
    salary-=absent
print("Final Slary is:",salary)