n=int(input())
sum=0
mul=1
while n>0:
    rem=n%10
    sum=sum+rem
    mul=mul*rem
    n=n//10
print(mul-sum)