n=int(input())
m=n**2
a=[int(i) for i in str(n)]
b=[int(i) for i in str(m)]
c=len(a)
d=b[-c::]
if d==a:
    print("Automorphic Number")
else:
     print("Not an Automorphic Number")