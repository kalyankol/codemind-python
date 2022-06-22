a,b=map(int,input().split())
s=[int(i) for i in str(a)]
m=s[:b]
n=s[-b:]
i=''.join([str(k) for k in m])
j=''.join([str(k) for k in n])
print(abs(int(i)-int(j)))
