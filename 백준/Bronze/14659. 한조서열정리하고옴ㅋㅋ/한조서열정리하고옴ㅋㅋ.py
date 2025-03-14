import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

stack = []
result = [0] * N  # 각 위치에서 보이는 건물 수 저장

for i in range(N - 1, -1, -1):  # 오른쪽에서 왼쪽으로 스캔
    count = 0
    while stack and stack[-1][0] < A[i]:
        count += stack.pop()[1] + 1  # 스택에 있는 건물들을 하나씩 제거하며 개수 누적
    result[i] = count
    stack.append((A[i], count))  # (건물 높이, 현재 위치에서 볼 수 있는 건물 수) 저장

print(max(result))
