d ={}
n= int(input("Enter number of items:"))

for i in range(n):
    k = input("Enter a key: ")
    v = int(input("Enter values: "))
    d[k] = v
print("Ascending:",dict(sorted(d.items())))
print("Descending:",dict(sorted(d.items(),reverse=True)))
