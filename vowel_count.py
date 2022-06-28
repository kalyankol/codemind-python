n=str(input())
c='aeiouAEIOU'
b=list(n)
d=[]
e=[]
for i in b:
    if i in c:
        d.append(i)
if len(d)>0:
    print(len(d))
else:
    print('0')
#for i in d:
#    if i not in e:
#        e.append(i)
#if len(e)>0:
#    print(len(e))
#else:
#    print('0')