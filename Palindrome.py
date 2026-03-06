num=int(input("Enter a number"))
temp=num
ans=0
while(num>0):
    rem=num%10
    num//=10
    ans=(ans*10)+rem
if(ans==temp):
    print("PALINDROME")
else:
    print("NOT PALINDROME")
