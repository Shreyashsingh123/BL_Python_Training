battery=100
drain=int(input("enter drains per minute:  "))
ans=0
while(battery>=0):
    battery-=drain
    ans+=1
print(ans)