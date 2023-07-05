n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(n):
    s+=a[i]
ave=s//(len(a))
c=0
for j in range(n):
    if a[j]>=ave:
        c+=1
print(c)