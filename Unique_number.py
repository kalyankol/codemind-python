n=int(input())
c=0
a=[int(i) for i in str(n)]
for i in a:
    if a.count(i)==1:
        c+=1
if c==len(a):
    print('Unique Number')
else:
    print('Not Unique Number')
    