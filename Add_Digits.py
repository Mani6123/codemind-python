def add_digts(n):
    a=0
    while n>0:
        r=n%10
        a+=r
        n=n//10
        if a>9 and n==0:
            n=a
            a=0
    print(a)
n=int(input())
add_digts(n)
