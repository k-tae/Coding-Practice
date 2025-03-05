a,b,n,w=map(int,input().split())
count=0
for i in range(1,n):
    k=a*i+b*(n-i)
    if w==k:
        count+=1
        ans=[i,n-i]
if count==1:
    print(ans[0],ans[1])
else:
    print(-1)