from collections import Counter
T=int(input())
for _ in range(T):
    N=int(input())
    A=[]
    for _ in range(N):
        a,b=input().split()
        A.append(b)
    a=Counter(A)
    Count=list(a.values())
    ans=1
    for i in range(len(Count)):
      ans=ans*(Count[i]+1)
    print(ans-1)