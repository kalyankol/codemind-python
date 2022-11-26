def gl(s,i):
    s=list(s)
    v="aeiouAEIOU"
    m="ma"
    for j in range(i+1):
        m+='a'
    if s[0] in v:    
        s+=m
    else:
        a=s
        s=""
        for j in range(len(a)):
            if j!=0:
                s+=a[j]
        s+=a[0]
        s+=m
    s="".join(s)
    return s
n=list(map(str,input().split()))
for i in range(len(n)):
    print(gl(n[i],i),end=" ")