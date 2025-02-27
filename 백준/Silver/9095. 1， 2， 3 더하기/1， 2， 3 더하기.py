def OTT(N):
    if N==1:
        return 1
    elif N==2:
        return 2
    elif N==3:
        return 4
    else:
        return OTT(N-1)+OTT(N-2)+OTT(N-3)
    
T=int(input())
for _ in range(T):
    N=int(input())
    print(OTT(N))