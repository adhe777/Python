s=input("Enter a string:")
result=""
for ch in s:
        if ch not in result:
                print(ch,":",s.count(ch))
                result +=ch
