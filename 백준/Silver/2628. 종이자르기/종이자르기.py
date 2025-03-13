garo, sero = map(int, input().split())
n = int(input())

garo_cuts = [0, garo] 
sero_cuts = [0, sero] 

for _ in range(n):
    direction, num = map(int, input().split())
    if direction:
        garo_cuts.append(num)
    else:
        sero_cuts.append(num)
garo_cuts.sort()
sero_cuts.sort()

max_garo = max(garo_cuts[i] - garo_cuts[i - 1] for i in range(1, len(garo_cuts)))
max_sero = max(sero_cuts[i] - sero_cuts[i - 1] for i in range(1, len(sero_cuts)))

print(max_garo * max_sero)
