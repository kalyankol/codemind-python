a=str(input())
b='aeiouAEIOU'
f='aeiou'
g='AEIOU'
lc=0
uc=0
c=list(a)
d=[]
for i in a:
    if i in b:
        d.append(i)
e=set(d)
for i in e:
    if i in f:
        lc=lc+1
    elif i in g:
        uc=uc+1
if uc==len(g) or lc==len(f):
    print(True)
else:
    print(False)