n=int(input())
a=list(map(int,input().split()))
#b=''.join([str(i) for i in a])
#c=int(b)
b=a[::-1]
s=0
for i in range(len(b)):
    s=s+(b[i]*2**i)
print(s)    
    