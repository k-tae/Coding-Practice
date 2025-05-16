while True:
    N, M, K = map(int, input().split())
    
    if N == 0 and M == 0 and K == 0:
        break

    A = N - M - K
    majority = (N // 2) + 1  # 과반수 기준
    needed = majority - M  # 최소 확보해야 할 무소속 의원 수

    if needed <= 0:
        print(0)
    elif needed > A:  # 무소속 의원이 부족하면 법안 통과 불가
        print(-1)
    else:
        print(needed)
