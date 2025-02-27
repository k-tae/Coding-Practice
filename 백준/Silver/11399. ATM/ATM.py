N=int(input())
L=[int(i) for i in input().split()]
L.sort()
for i in range(len(L)):
    L[len(L)-1-i]=L[len(L)-1-i]*(i+1)
print(sum(L))