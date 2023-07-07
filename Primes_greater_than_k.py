def prime(n):
    e=0
    for i in range(1,n+1):
        if n%i==0:
            e+=1
    if (e==2):
        return 1
    return 0
n=int(input())
a=list(map(int,input().split()))
k=int(input())
d=0
for i in range(n):
    if (prime(a[i])):
        if (a[i]>=k):
            d+=1
print(d)