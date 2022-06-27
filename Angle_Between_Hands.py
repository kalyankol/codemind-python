a,b=map(int,input().split(':'))
n=abs(30*a-(11/2)*b)
m=360-(n)
if n>m:
    print(m)
else:
    print(n)