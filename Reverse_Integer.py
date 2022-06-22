n=int(input())
if n<0:
    q=-n
else:
    q=n
s=[int(i) for i in str(q)]
for i in range(len(s)):
    if s[-1]==0:
        s.remove(0)
m=s[::-1]
k=''.join([str(i) for i in m])
if n>0:
    print(int(k))
else:
    print(-int(k))