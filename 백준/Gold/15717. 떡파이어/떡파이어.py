N = int(input())
MOD = 10**9 + 7

if N == 0:
    print(1)  # 0세로 죽는 방법은, 아무 것도 안 먹고 죽는 1가지
else:
    print(pow(2, N - 1, MOD))
