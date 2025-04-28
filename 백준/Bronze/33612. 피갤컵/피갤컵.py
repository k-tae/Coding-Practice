N=int(input())
Y,M=2024, 8+7*(N-1)
while M>12:
    M=M-12
    Y=Y+1
print(Y, M)