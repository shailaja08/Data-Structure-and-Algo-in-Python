def LinearSearch(a,n,x):
    for i in range(0,n):
        if a[i]>x:
            break
        if a[i]==x:
            return i
    return -1


n=int(input("Enter the number of nodes:"))
a=[None]*n
for i in range(0,n):
    a[i]=int(input("Enter the value in sorted order"))

x=int(input("Enter the number you want to search"))
Index=LinearSearch(a,n,x)
if Index==-1:
    print("The number is not found in the list")
else:
    print("The number is at the index",Index)
