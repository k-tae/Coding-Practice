import sys

N = sys.stdin.readline().strip()
if len(N) == 1:
    N = '0' + N

ans = N
count = 0

while True:
    count += 1
    temp_sum = int(N[0]) + int(N[1])
    N = N[1] + str(temp_sum % 10) 

    if N == ans:  
        print(count)
        break
