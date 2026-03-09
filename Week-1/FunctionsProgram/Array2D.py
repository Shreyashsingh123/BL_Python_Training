n=int(input("number of rows::"))
m=int(input("number of columns:"))

array1=[]
for i in range(0,n):
    row=[]
    for j in range(0,m):
        value=int(input())
        row.append(value)
    array1.append(row)



def show(array1):
    for i in range(0,n):
        for j in range(0,m):
            print(array1[i][j]," ")
show(array1)