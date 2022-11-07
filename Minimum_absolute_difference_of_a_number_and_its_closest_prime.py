def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
x=int(input())
temp=x
while True:
    if is_prime(x)==True:
        print(0)
    else:
        y=x-1
        z=x+1
        while True:
            if is_prime(y)==True:
                break
            y-=1
        while True:
            if is_prime(z)==True:
                break
            z+=1
        a=abs(temp-y)
        b=abs(temp-z)
        print(min(a,b))
    break