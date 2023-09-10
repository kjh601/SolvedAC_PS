from sys import stdin
input = stdin.readline


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solve(n):
    while True:
        if is_prime(n):
            return n
        n += 1


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
