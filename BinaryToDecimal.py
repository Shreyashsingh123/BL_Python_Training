bin=input("enter a binary number : ")
l=len(bin)
l-=1
ans=0
i=0
while(l>=0):
   if(bin[i]!='0'):
    ans+= 2**l
    i+=1
    l-=1
   else:
     i+=1
     l-=1

print(ans)

