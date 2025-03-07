# n보다 크거나 같은 자연수 x에 대해 ax+b<=c*x

a,b=map(int,input().split())  #ax+b
c=int(input())                #cx
n=int(input())                
if a==c:
    if b<=0:
        print(1)
    else:
        print(0)
elif a<c:
    if b/(c-a) <= n:
        print(1)
    else:
        print(0)
else:
    print(0)