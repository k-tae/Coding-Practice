h,m,s=map(int,input().split())
q=int(input())
for _ in range(q):
    A=list(map(int,input().split()))
    if len(A)==2:
        A[1]=A[1]%86400
    if A[0]==1:
        sh=A[1]//3600
        temp=A[1]%3600
        sm=temp//60
        ss=temp%60
        h+=sh
        m+=sm
        s+=ss
        if s>=60:
            s-=60
            m+=1
        if m>=60:
            m-=60
            h+=1
        if h>=24:
            h-=24
    elif A[0]==2:
        sh=A[1]//3600
        temp=A[1]%3600
        sm=temp//60
        ss=temp%60
        h-=sh
        m-=sm
        s-=ss
        if s<0:
            s+=60
            m-=1
        if m<0:
            m+=60
            h-=1
        if h<0:
            h+=24
    else:
        print(h,m,s)