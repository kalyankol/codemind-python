def rev(n):
    s=[int(i) for i in str(n)]
    m=s[::-1]
    p=''.join([str(i) for i in m])
    k=int(p)
    return k
n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    b.append(rev(i))
print(*b)    