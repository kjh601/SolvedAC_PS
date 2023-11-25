import sys
input = sys.stdin.readline
write = sys.stdout.write

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]


def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]


def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [i for i in range(N)]
edge = []

total = 0
for i in range(N-1):
    for j in range(i+1, N):
        if matrix[i][j] < 0:
            unionParent(parent, i, j)
            total -= matrix[i][j]
        else:
            edge.append((i, j, matrix[i][j]))
edge.sort(key=lambda x: x[2])

new_railroad = []
for v1, v2, w in edge:
    if findParent(parent, v1) == findParent(parent, v2):
        continue

    unionParent(parent, v1, v2)
    new_railroad.append((v1, v2))
    total += w

print(total, len(new_railroad))
for v1, v2 in new_railroad:
    write(str(v1+1)+' '+str(v2+1)+'\n')
