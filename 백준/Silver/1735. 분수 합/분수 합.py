#최대 공약수 구하기
def gcd(a,b):
  if a>b:
    temp=a
    a=b
    b=temp
  while b%a!=0:
    r=b%a
    b=a
    a=r
  return a

A,B=map(int,input().split())
a,b=map(int,input().split())
D=(B*b)//gcd(B,b)
U=A*D//B+a*D//b
if gcd(D,U)==1:
    print(U,D)
else:
    print(U//gcd(D,U),D//gcd(D,U))