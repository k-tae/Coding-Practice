M,N=map(int,input().split())
U,L,R,D=map(int,input().split())
A=[]
for _ in range(M):
    A.append(input())
for i in range(M+U+D): # 가로줄
    for j in range(N+L+R): # 세로줄
        if i>=U and i<M+U and j>=L and j<N+L:
            print(A[i-U][j-L],end='')
        elif (i+j)%2 == 0:
            print('#',end='')
        else:
            print('.',end='')
    print('')