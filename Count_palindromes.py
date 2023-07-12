def pal(n):
    t=n
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    if rev==t:
        return True
    return False
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if pal(i)==True:
        c+=1
print(c)