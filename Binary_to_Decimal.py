n=int(input())
for i in range(n):
    a=int(input())
    sum=0
    m=[int(i) for i in str(a)]
    s=m[::-1]
    for i in range(len(s)):
        sum=sum+int(s[i])*2**i
    print(sum)    
    