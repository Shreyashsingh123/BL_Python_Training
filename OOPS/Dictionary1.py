# dictionary is used to store key value pairs 
# key unique,value may duplicate
# mutable in nature

student={
    "name":"Harsh",
    "age":20,
    "course":"Btech"
}

print(student["name"])
# accessing values using key
print(student["age"])

# adding new item
student["city"]="varanasi"
print(student)

# updating
student["age"]=25
print(student)

# deleting
del student["age"]
print(student)


# pop is use to remove value using key  and return that corresponding value of key
print(student.pop("name"))
print(student)

