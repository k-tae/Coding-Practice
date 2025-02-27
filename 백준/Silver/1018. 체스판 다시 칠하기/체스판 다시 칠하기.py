N,M=map(int,input().split())
Matrix = [list(input()) for _ in range(N)]
W_Matrix=[]
B_Matrix=[]
Min=100
for i in range(8):
    temp=[]
    for j in range(8):
        if (i+j)%2 == 0:
            temp.append('W')
        else:
            temp.append('B')
    W_Matrix.append(temp)
for i in range(8):
    temp=[]
    for j in range(8):
        if (i+j)%2 == 0:
            temp.append('B')
        else:
            temp.append('W')
    B_Matrix.append(temp)

for i in range(N-7):
    for j in range(M-7):
        w_count = 0
        b_count = 0
        for x in range(8):
            for y in range(8):
                if Matrix[i+x][j+y] != W_Matrix[x][y]:
                    w_count += 1
                if Matrix[i+x][j+y] != B_Matrix[x][y]:
                    b_count += 1
        Min = min(Min, w_count, b_count)

print(Min)