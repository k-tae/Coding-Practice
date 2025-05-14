def dfs(v,visited,adj_list):
    visited[v] = True
    count=1

    for i in adj_list[v]:
        if not visited[i]:
            count+=dfs(i,visited, adj_list)

    return count

N=int(input())
C=int(input())
D={}
for i in range(N):
    D[i+1] = []
for _ in range(C):
    a,b=map(int,input().split())
    D[a].append(b)
    D[b].append(a)

visited = [False] * (N+1)
a=dfs(1, visited, D)
print(a-1)
