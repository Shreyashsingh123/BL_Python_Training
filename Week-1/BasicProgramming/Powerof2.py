num=int(input("Enter the number:"))
i=0
power=1
while(i<=num and num<31):
    print("2^", i, " is =", power)
    power*= 2
    i += 1
