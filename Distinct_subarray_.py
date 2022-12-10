a=int(input())
b=int(input())
c=[]
for i in range(a,b+1):
    c.append(i)
c1=0
for i in range(len(c)):
    for j in range(len(c)):
        c2=0
        for k in range(i,j+1):
            c2+=c[k]
        if c2%2!=0:
            c1+=1
print(c1) 
