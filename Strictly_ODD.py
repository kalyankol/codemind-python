n=int(input())
a=list(map(int,input().split()))
c=0
c1=0
for i in range(len(a)):
    if a[i]%2!=0:
        c+=1
        if i%2!=0:
            c1+=1
if c==c1:
    print(True)
else:
    print(False)

            