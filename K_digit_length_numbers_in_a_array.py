n,k=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in a:
    j=str(abs(i))
    if len(j)==k:
        c+=1
print(c)        
#print(a,k)