def prime(k):
    if k==1:
        return False
    else:
        for i in range(2,int(k**0.5)+1):
            if k%i==0:
                return False
                break
        else:
            return True
n=int(input())
c=0
if prime(n):
    s=[int(i) for i in str(n)]
    for i in s:
        if prime(int(i)):
            c+=1
    if c==len(s):
        print("Mega Prime")
    else:
        print('Not Mega Prime')
else:
    print('Not Mega Prime')
        