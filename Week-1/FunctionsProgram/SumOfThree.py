n = int(input("Enter number of integers: "))
arr = []
print("Enter the integers:")
for i in range(n):
    num = int(input())
    arr.append(num)

count = 0

print("\nDistinct Triplets:")

for i in range(n):
    for j in range(i+1,n):
        for k in range (j+1,n):
            if arr[i]+arr[j]+arr[k]==0:
                print(arr[i],arr[j],arr[k])
                count+=1
print("Total triplets are:",count)
