K, N = map(int, input().split())
A = [int(input()) for _ in range(K)]

start = 1
end = max(A)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = sum(i // mid for i in A)

    if total >= N:
        result = mid  # 가능한 최대 길이 저장
        start = mid + 1
    else:
        end = mid - 1

print(result)
