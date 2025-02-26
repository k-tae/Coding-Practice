T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    U=M
    D=N
    for i in range(N-1):
        U=U*(M-1-i)
        D=D*(N-1-i)
    print(int(U/D))