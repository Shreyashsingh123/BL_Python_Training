
# write is to write text to file
file2=open("data1.txt",'w')
file2.write("hello python")
file2.close()
# writelines is to write in the form of list

# read  entire file
file=open("data1.txt",'r')
print(file.read())


# read one line at a time
# print(file.readline())

#readlines is to read all lines into list amd add /n after every elements
# print(file.readlines())



# using with and append data
with open("data1.txt",'r') as file3:
    cont=file3.read()
    print(cont)
    
with open("data1.txt","a") as file4:
    cont=file4.write("Hii")
    
with open ("data1.txt",'r') as v:
    print(v.read())

