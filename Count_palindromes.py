def pal(n):
    s=[int(i) for i in str(n)]
    m=s[::-1]
    if s==m:
        return True
    else:
        return False
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if pal(i):
        c+=1
print(c)        
    