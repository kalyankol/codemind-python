a=str(input())
b=a.split()
c=[]
e=[]
for i in range(len(b)):
    c.append(b[i])
d=(c[::-1])
for j in range(len(d)):
    m=d[j][::-1]
    e.append(m)
print(*e)