while (1):
    N=int(input())
    A=[]
    if N==-1:
        break
    else:
        for i in range(1,N):
            if N%i ==0:
                A.append(i)
        if N==sum(A):
            print(N,'=',end=' ')
            for i in range(len(A)):
                if i==len(A)-1:
                    print(A[i])
                else:
                    print(A[i],'+',end=' ')
        else:
            print(N,'is NOT perfect.')