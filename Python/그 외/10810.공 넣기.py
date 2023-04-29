import sys
input = sys.stdin.readline

N, M = map(int, input().split())
baskets = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for index in range(i-1, j):
        baskets[index] = k

for ball in baskets:
    print(ball, end=' ')