str=input("Enter a string:  ")

str=str.lower()
c=0
vowels=['a','e','i','o','u']
for i in range(len(str)-1):
    if str[i] in vowels:
        c+=1
print(c)

