n=str(input())
c='aeiouAEIOU'
b=list(n)
d=[]
e=[]
for i in b:
    if i in c:
        d.append(i)
for i in d:
    if i not in e:
        e.append(i)
if len(e)>0:
    print(*e)
else:
    print('-1')