T=int(input("ENter time"))
T%=90
if(T<=30):
    print("RED")
elif(T<=60 and T>30):
    print("YELLOW")
else:
    print("GREEN")