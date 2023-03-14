import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
total = [[0 for _ in range(N+1)]for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        total[i][j] = matrix[i-1][j-1] + total[i-1][j] + \
            total[i][j-1] - total[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(total[x2][y2] - total[x1-1][y2] -
          total[x2][y1-1] + total[x1-1][y1-1])
