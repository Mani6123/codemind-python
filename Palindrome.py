def pal(n):
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev

num=int(input())
if num==pal(num):
    print('True')
else:
    print('False')