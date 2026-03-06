seats=int(input("Enter seats avilable:  "))
req=int(input("ENter number of request:  "))
Seatreq=req
c=0
while(req!=0):
    a=int(input("Enter requested seats :  "))
    if(a<=seats):
        seats-=a
        c+=1
    req-=1
for i in range(c):
    print("CONFIRMED")
Seatreq-=c
for i in range(Seatreq):
    print("WAITLISTED")