a=str(input())
b=str(input())
c=list(a)
d=list(b)
for i in range(len(c)):
    if c[i]==d[0]:
        print(True)
        print(c.index(d[0]))
        break
else:
    print(False)