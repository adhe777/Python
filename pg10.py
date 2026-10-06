n=int(input("Enter number of elements:"))
first=[]
for i in range(n):
    x=int(input("Enter value:"))
    if x>100:
        first.append("over")
    else:
        first.append(x)
    print("List:",first)
