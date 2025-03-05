N=int(input())
k=N
d=5
for i in range(4):
    N=N*(k-i-1)
    d=d*(i+1)
print(N//d)