import sys
input = sys.stdin.readline


def gcd(a, b):
    while (b != 0):
        n = a % b
        a = b
        b = n
    return a


N = int(input())

s = int(input())
b = int(input())
r = b-s
for _ in range(N-2):
    a = b
    b = int(input())
    r = gcd(r, b-a)

print(int((b-s)/r)-N+1)
