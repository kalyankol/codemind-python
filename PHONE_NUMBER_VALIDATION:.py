n=int(input())
s=[int(i) for i in str(n)]
if s[0]!='0' and len(s)==10:
    print("Valid")
else:
    print("Invalid")