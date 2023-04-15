import sys
input = sys.stdin.readline
print = sys.stdout.write
def floyd_warshall():
    for k in range(n):
        for i in range(n):
            if i == k or dists[i][k] == 0:
                continue
            for j in range(n):
                if i == j or j == k or dists[k][j] == 0:
                    continue
                if dists[i][j] == 0:
                    dists[i][j] = dists[i][k] + dists[k][j]
                dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])

n = int(input())
m = int(input())

dists = [[0 for _ in range(n)]for _ in range(n)]
for _ in range(m):
    a, b, c = map(int,input().split())
    if dists[a-1][b-1] == 0:
        dists[a-1][b-1] = c
    else :
        dists[a-1][b-1] = min(dists[a-1][b-1], c)

floyd_warshall()

for line in dists:
    print(' '.join(map(str,line))+'\n')