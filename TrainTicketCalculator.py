distance=int(input("ENter distance :  "))
age=int(input("Enter age:  "))

fare=distance*2
if(age>=60):
    disc=fare*0.3
    fare-=disc
elif(age<12):
   disc=fare*0.5
   fare-=disc

print(fare)
