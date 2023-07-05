n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    if a[i]==0 or a[i]==1:
        c+=1
    else:
        print('False')
        break
if c==len(a):
    print('True')