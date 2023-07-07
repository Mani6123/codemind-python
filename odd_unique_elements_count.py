n=int(input())
a=list(map(int,input().split()))
b=list(set(a))
c=0
for i in range(len(b)):
    if b[i]%2!=0 and b[i]!=0:
        c+=1
l=len(a)
print(c)