numbers = input("Enter integers: ").split()
positive = []
for n in numbers:
    if int(n) > 0:
        positive.append(int(n))
print(positive)        

n=int(input("Enter N: "))
squares=[i*i for i in range(1,n+1)]
print(squares)

word=input("enter a word to find vowels:")
vowels=[ch for ch in word if ch in "aeiouAEIOU"]
print(vowels)

word=input("Enter a word to find ordinary values of each character:")
values=[ord(ch)for ch in word]
print(values)

