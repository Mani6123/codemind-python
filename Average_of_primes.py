def prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
a=list(map(int,input().split()))
p=0
s=0
for i in a:
    if prime(i):
        p+=1
        s+=i
ave=s/p
print('{:.2f}'.format(ave))