import sys
input = sys.stdin.readline


def mul(a, b):
    result = [[0 for _ in range(N)]for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += a[i][k] * b[k][j]
                result[i][j] %= 1000
    return result


def pow(matrix, n):
    if n == 1:
        return matrix
    else:
        x = pow(matrix, n//2)
        if n % 2:
            return mul(mul(x, x), matrix)
        else:
            return mul(x, x)


N, B = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        A[i][j] %= 1000

for line in pow(A, B):
    sys.stdout.write(' '.join(map(str, line))+'\n')
