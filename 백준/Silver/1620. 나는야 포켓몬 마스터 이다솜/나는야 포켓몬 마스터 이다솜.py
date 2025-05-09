import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokemon = {}
reverse_pokemon = {}

for i in range(1, N + 1):
    name = input().strip()
    pokemon[name] = i
    reverse_pokemon[i] = name

for _ in range(M):
    A = input().strip()
    if A.isdigit():
        print(reverse_pokemon[int(A)])
    else:
        print(pokemon[A])
