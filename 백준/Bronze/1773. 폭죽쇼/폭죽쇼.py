import sys
input = sys.stdin.readline

N, C = map(int, input().split())
fireworks = set()  # 터지는 시간을 저장할 집합

for _ in range(N):
    k = int(input().strip())  # 개행 문자 제거
    fireworks.update(range(k, C + 1, k))  # 배수들을 한 번에 추가

print(len(fireworks))  # 중복을 제거한 개수 출력
