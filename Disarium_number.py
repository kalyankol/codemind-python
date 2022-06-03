n=int(input())
s=[int(i) for i in str(n)]
a=[]
b=0
sum=0
for i in range(len(s)):
    b=s[i]**(i+1)
    if b!=0:
        a.append(b)
for i in a:
    sum=sum+i
if sum==n:
    print(True)
else:
    print(False)
    
    
    
    
