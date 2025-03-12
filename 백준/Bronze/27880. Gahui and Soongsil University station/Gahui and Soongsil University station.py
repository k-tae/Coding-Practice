ans=0
for _ in range(4):
    A,B=input().split()
    if A=="Es":
        ans+=int(B)*21
    else:
        ans+=int(B)*17
print(ans)