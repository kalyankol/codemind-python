a,b,c=map(int,input().split())
d=2*a*b*c*512
cap=d//1024
f=str(cap)
g=list(f)
g.append('KB')
print(''.join([str(i) for i in g]))
