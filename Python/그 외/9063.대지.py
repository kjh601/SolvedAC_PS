import sys
input = sys.stdin.readline
INF = sys.maxsize

min_x = INF
max_x = -INF
min_y = INF
max_y = -INF

for _ in range(int(input())):
    x, y = map(int,input().split())
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

print(abs(min_x-max_x)*abs(min_y-max_y))