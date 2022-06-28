a=str(input())
b=a.split()
c=[]
for i in range(len(b)):
    d=list(b[i])
    c.append(len(d))
print(min(c))