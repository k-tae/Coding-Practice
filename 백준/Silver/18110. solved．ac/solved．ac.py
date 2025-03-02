import sys
def roun(num):
    return int(num + 0.5)

input=sys.stdin.readline

N=int(input())
cut=roun(N*0.15)
A=[]
for _ in range(N):
    A.append(int(input()))
A.sort()
A=A[cut:N-cut]
print(roun(sum(A)/len(A)) if len(A)!=0 else 0)