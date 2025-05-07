N = int(input())
A = [0] * N
left, right = 0, N - 1

for i in range(1, N + 1):
    val = i
    if i % 2 == 0:
        A[right] = val
        right -= 1
    else:
        A[left] = val
        left += 1

print(*A)