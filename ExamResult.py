marks=[]
avg=0
for i in range(5):
    m=int(input("Enter marks"))
    marks.append(m)
    if(m<35):
        print("FAIL")
        break
    else:
        avg+=m
# below else executes if break not occur in for loop
else:
 avg/=5
 if(avg>=75):
    print("DISTINCTION")
 else:
    print("PASS")

