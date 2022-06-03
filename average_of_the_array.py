n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    s=s+i
m=s/n
avg='{:.2f}'.format(m)
print(avg)