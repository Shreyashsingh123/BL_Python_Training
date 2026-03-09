import math
num1=int(input("Enter the value: "))
num2=int(input("Enter the value: "))

def calculate(num1,num2):
    return math.sqrt(num1*num1 + num2*num2)

sum=calculate(num1,num2)
print("The eucledian distance is:",sum)