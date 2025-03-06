import sys

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(2, limit + 1) if is_prime[i]]

def prime_factorization(N):
    if N == 1:
        return
    
    limit = int(N ** 0.5)
    primes = sieve(limit)
    
    for p in primes:
        while N % p == 0:
            print(p)
            N //= p
        if N == 1:
            return

    if N > 1:
        print(N)
N = int(sys.stdin.readline().strip())
prime_factorization(N)