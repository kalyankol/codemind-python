n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if i!=1:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            c+=1
print(c)            
            