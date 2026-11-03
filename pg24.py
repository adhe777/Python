d1 = {}
d2 = {}

n = int(input("Enter number of items: "))

for i in range(n):
    k = input("Enter key for first dictionary: ")
    v = input("Enter value: ")
    d1[k] = v

for i in range(n):
    k = input("Enter key for second dictionary: ")
    v = input("Enter value: ")
    d2[k] = v

d1.update(d2)
print("Merged dictionary:", d1)
