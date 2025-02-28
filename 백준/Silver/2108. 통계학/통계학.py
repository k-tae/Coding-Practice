import sys
from collections import Counter

# 빠른 입력
input = sys.stdin.readline

# 1. 입력받기
N = int(input().strip())
A = [int(input().strip()) for _ in range(N)]

# 2. 산술평균 (반올림)
print(round(sum(A) / N))

# 3. 중앙값 (정렬 후 중간값)
A.sort()
print(A[N // 2])

# 4. 최빈값 (Counter 사용)
counter = Counter(A)
max_freq = max(counter.values())  # 가장 큰 빈도수 찾기
modes = sorted([k for k, v in counter.items() if v == max_freq])  # 최빈값 리스트 정렬

# 최빈값이 여러 개라면 두 번째로 작은 값 출력
if len(modes) > 1:
    print(modes[1])
else:
    print(modes[0])

# 5. 범위 (최댓값 - 최솟값)
print(max(A) - min(A))
