CorrectPin=input("Enter correct pin:  ")
ans=False
i=0
while(i<3):
    attempt=input("Enter pin:  ")
    if(attempt==CorrectPin):
        ans=True
        break
    i+=1
# print(ans)
if(ans):
     print("ACCESS GRANTED")
else:
     print("ACCESS DENIED")