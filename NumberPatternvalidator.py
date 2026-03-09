num=int(input("Enter a number:  "))
nums=[]
i=0
while(num>0):
    r=num%10
    num//=10
    nums.append(r)
ans=True
nums.reverse()
# for i in range(5):
#     print(i)
for i in range(len(nums)-1):
    if({nums[i]<nums[i+1]}):
        ans=True
        continue
    else:
        ans=False
        break
if(ans):
    print("YES")
else:
    print("NO")

    
