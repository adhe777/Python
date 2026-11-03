S = input("Enter a string:")
if S.endswith("ing"):
    S +="ly"
else:
    S+="ing"
print(S)
