numbers=input("Enter numbers: ").split()
result=[]
for n in numbers:
    if int(n) % 2 != 0:
        result.append(n)
print(result)
