def self(n):
    t=n
    c=0
    s=str(n)
    l=len(s)
    while n>0:
        r=n%10
        if r==0:
            break
        elif t%r==0:
            c+=1
            n=n//10
        else:
            n=n//10
    if c==l:
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if self(i)==True:
        print(i,end=' ')