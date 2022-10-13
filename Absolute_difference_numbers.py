n,c=map(int,input().split())
s=n%(10**c)
rev=rev1=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
m=rev%(10**c)
while m>0:
    d=m%10
    rev1=rev1*10+d
    m=m//10
t=rev1-s
a=abs(t)
print(a)