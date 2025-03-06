import math
M=int(input())
N=int(input())
A=[]
for i in range(M,N+1):
    loop=math.floor(i**0.5)
    count=0
    for j in range(2,loop+1):
        if i%j==0:
            count+=1
    if count==0 and i!=1:
        A.append(i)
if A!=[]:
    print(sum(A))
    print(A[0])
else:
    print(-1)