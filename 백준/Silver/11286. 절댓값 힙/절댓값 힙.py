import sys
import heapq
input = sys.stdin.readline
N=int(input())
hq=[]
for _ in range(N):
    a=int(input())
    if a!=0:
        heapq.heappush(hq, (abs(a),a))
    else:
        if hq==[]:
            print(0)
        else:
            print(heapq.heappop(hq)[1])