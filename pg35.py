def interest(p, t, senior):
    r = 12 if senior == "yes" else 10
    return (p * r * t) / 100

p = float(input("Enter principal: "))
t = float(input("Enter time: "))
senior = input("Senior citizen? (yes/no): ")

print("Simple Interest =", interest(p, t, senior.lower()))


