N=int(input())
count=0
for _ in range(N):
    d=int(input())
    if d%2!=0:
        count+=1
print(count)