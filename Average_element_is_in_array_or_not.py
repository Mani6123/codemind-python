n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(n):
    s=s+a[i]
ave=s//(len(a))
c=0
for i in range(n):
    if ave==a[i]:
        c+=1
if c==0:
    print('False')
else:
    print('True')