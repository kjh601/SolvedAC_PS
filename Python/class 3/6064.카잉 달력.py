def gcd(n, m):
    while m > 0:
        n, m = m, n % m
    return n

def find_x(M, N, x, y):
    g = gcd(M, N)
    if (y-x) % g != 0:
        return -1
    lcm = M*N // g
    k = ((y-x) // g * pow(M//g, -1, N//g)) % (N//g)
    return k*M + x if k*M + x <= lcm else -1

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(find_x(M, N, x, y))