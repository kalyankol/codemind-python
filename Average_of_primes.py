n=int(input())
a=list(map(int,input().split()))
b=[]
s=0
avg=0
for i in a:
    if i!=1:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            b.append(i)
for i in b:
    s=s+i
avg=s/len(b)
print('{:.2f}'.format(avg))
    
        