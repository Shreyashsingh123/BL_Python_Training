class student:
    def __init__(self,*args):
        # *args is positional argument use to take multiple elemnt as a tuple
        if len(args)==1:
            self.name=args[0]
        elif len(args)==2:
            self.name=args[0]
            self.age=args[1]
        elif len(args)==3:
            self.name=args[0]
            self.age=args[1]
            self.city=args[2]
Student1=student("harsh")
Student2=student("Shreyash",21)
Student3=student("Shreyash",21,"varanasi")

print(Student1.name) #first if executed as only one parameter is there
print(Student2.name,", ",Student2.age)  # two parameter is there so elif get executed
print(Student3.name,",",Student3.age,",",Student3.city)  # three argument is there so second elif executed and similarly next conditions will be there

# practice 2

def info(name, *marks):
    print("Name is:", name)
    print("Marks is:", marks)

info("Rahul", 80, 85, 90)
print("Added more marks ")
info("Rahul", 80, 85, 90,95,98)

def display(*args):
    for item in args:
        print(item)

display("Python", "Java", "C++")

# third code

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers(1, 2, 3))
print(add_numbers(5, 10, 15, 20))


