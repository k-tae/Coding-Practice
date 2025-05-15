import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

counter = Counter(A)  # A의 각 수의 등장 횟수를 dict 형태로 저장

for num in B:
    print(counter[num], end=' ')
