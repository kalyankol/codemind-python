def r(n):
    s=[int(i) for i in str(n)]
    w=s[::-1]
    m=''.join([str(i) for i in w])
    j=int(m)
    return j
n=int(input())#12
s=n**2#144
q=r(n)#21
h=q**2#441
k=r(h)#144
if k==s:
    print(True)
else:
    print(False)
