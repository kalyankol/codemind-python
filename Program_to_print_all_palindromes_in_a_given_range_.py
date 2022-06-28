def is_pali(i):
    t=i
    rev=0
    while i!=0:
        r=i%10
        rev=rev*10+r
        i=i//10
    if rev==t:
        return True
    else:
        return False
n=int(input())
m=int(input())
for i in range(n,m+1):
    if is_pali(i):
        print(i,end=' ')