def ami(n):
    c=0
    for i in range(1,n):
        if n%i==0:
            c+=i
    return c
    
a=int(input())
b=int(input())
if ami(a)==b and ami(b)==a :
    print('Amicable')
else:
    print('Not Amicable')