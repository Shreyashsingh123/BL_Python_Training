#operation should be 1 only 
#  :x**2  lambda x,y,a,s...can be multiple argument nut 
# for single number use direct lambda but for list and all use map,filter,reduce 

num=[1,2,3,4,5]
# square list using lambda
sq=list(map(lambda x:x**2,num))
print(sq)

# even number
ev=list(map(lambda x:x%2==0,num))
print(ev)

# filter even number from list num
ev2=list(filter(lambda x:x%2==0,num))
print(ev2)
odd=list(filter(lambda x:x%2!=0,num))
print(odd)

# sort list based on alphabetical character
ls=["apple","zbanana","orange","date"]
print(sorted(ls))

#  sort list based on alphabetical character and length
print(sorted(ls,key=lambda x:len(x)))  #based on key sort it

det=[
    {"name":"shreyash","age":21},
    {"name":"ayush","age":28},
    {"name":"shreya","age":22}
]
print(sorted(det,key=lambda x:(x["age"],x["name"])))
# sort based on age and name(key of dict)
# first priority age and if not sorted using it then sort based n name

# max age in ls
print(max(det,key=lambda x:x["age"]))