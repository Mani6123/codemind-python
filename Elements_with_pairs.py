n=int(input())
a=list(map(int,input().split()))
b=len(a)
if b%2==0:
    for i in range(b):
        print(a[i],end=' ')
else:
    a.append(0)
    for i in range(b+1):
        print(a[i],end=' ')