A=[]
M=0
for _ in range(5):
    temp=list(input())
    A.append(temp)
    M=max(len(temp),M)

for i in range(5):
    while len(A[i]) < M:
        A[i].append(' ')

transpose_A = list(map(list, zip(*A)))

for i in range(M):
    for j in range(5):
        if(transpose_A[i][j]==' '):
            pass
        else:
            print(transpose_A[i][j],end='')