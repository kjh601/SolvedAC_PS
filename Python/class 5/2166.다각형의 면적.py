import sys
input = sys.stdin.readline

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

ret = 0.00
i = N-1
for j in range(N):
    ret += points[i][0] * points[j][1] - points[j][0] * points[i][1]
    i = j

print(round(abs(ret)/2, 1))
