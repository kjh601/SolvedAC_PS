import sys
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())

matrix = [list(input().split()) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if matrix[i][k]=='1' and matrix[k][j]=='1':
                matrix[i][j] = '1'

for line in matrix:
    print(' '.join(line)+'\n')