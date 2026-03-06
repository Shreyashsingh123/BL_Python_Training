num=int(input("Enter a number:  "))
temp=num
ans=0
while(num>0):
    r=num%10
    num//=10
    ans+=(r**3)
print(ans==temp)