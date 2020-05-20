n=int(input("Enter the size of the array: "))
x=[]
for i in range(n):
    a=input("enter the element of array: ")
    x.append(a)
for i in range(0,n-1):
    x[i]=max(x[i+1:])
print("Final array is:", x)
