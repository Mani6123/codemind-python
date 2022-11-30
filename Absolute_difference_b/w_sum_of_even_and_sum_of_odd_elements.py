n=int(input())
l=list(map(int,input().split()))
ev=od=0
for i in l:
    if i%2==0:
        ev+=i
    else:
        od+=i
print(abs(ev-od))