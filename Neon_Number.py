n=int(input())
s=n**2
sum=0
a=[int(i) for i in str(s)]
for i in a:
    sum=sum+i
if n==sum:
    print("Neon Number")
else:
    print("Not Neon Number")
