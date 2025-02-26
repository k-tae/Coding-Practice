T=int(input())
A=[int(n) for n in input().split()]
for i in A:
    a=0
    for j in range(i-1):
        if i%(j+1)==0:
            a=a+j+1
    if a==i:
        print("Perfect")
    elif a<i:
        print("Deficient")
    else:
        print("Abundant")