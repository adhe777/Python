l1 = input("Enter colors: ").split()
l2 = input("Enter colors: ").split()
for x in l1:
    if x not in l2:
        print(x)
