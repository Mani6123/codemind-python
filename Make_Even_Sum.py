n=int(input())
a=list(map(int,input().split()))
tot=sum(a)
if tot%2==0:
    print("1")
else: 
    print("0")