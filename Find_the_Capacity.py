s,t,b=map(int,input().split())
cap=2*s*t*b*512
c=cap//1024
print('{}KB'.format(c))