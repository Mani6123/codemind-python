def add_digts(n):
    a=0
    while n>0:
        r=n%10
        a+=r**2
        n=n//10
        if a>9 and n==0:
            n=a
            a=0
    if a==1 or a==7:
        print('True') 
    else:
        print('False')
        
n=int(input())
add_digts(n)