num=int(input("Enter a number:  "))
ans=0
temp=num
while(temp>9):
    num=temp
    ans=0
    while(num>0):
        r=num%10
        num//=10
        ans+=r
    temp-=ans
print(temp)
