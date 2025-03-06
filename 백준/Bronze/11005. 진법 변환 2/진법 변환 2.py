N,B=map(int,input().split())
A=[]
while N>=B:
    temp=N%B
    N=N//B
    if temp>9:
        temp=chr(temp+55)
    A.append(temp)
if N>9:
    N=chr(N+55)
A.append(N)
A.reverse()
for i in range(len(A)):
    print(A[i],end='')