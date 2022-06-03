def pal(n):
    s=[int(i) for i in str(n)]
    m=s[::-1]
    y=''.join([str(i) for i in m])
    x=int(y)
    return x
n=int(input())
p=pal(n)
if p==n:
    print(True)
else:
    print(False)

