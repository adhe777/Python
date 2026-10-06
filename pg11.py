n=int(input("Enter number of names:"))
names=[]
for i in range(n):
    name=input("Enter name:")
    names.append(name)
count=0
for name in names:
    count += name.lower().count('a')
    print("Number of occurrences of 'a':",count)
