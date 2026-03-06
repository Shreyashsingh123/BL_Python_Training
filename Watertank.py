capacity=1000
n=5
c=0
ans=0
while(n!=0):
    a=int(input("Enter inflow water amount:  "))
    if(ans<capacity):
        c+=1
        ans+=a
    
    n-=1
print(c)
