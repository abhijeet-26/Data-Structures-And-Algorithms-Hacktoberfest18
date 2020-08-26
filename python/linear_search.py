arr=[]
n=int(input("Enter the length of arr: "))
for i in range(n):
    x=int(input("enter the next element: "))
    arr.append(x)
search=int(input("Enter the value to be searched: "))
k=0
for j in arr:
    if j==search:
        print("the index value is ",k)
        break
    k+=1
else:
    print("element not found")

print("Thank you for using our code!!!")