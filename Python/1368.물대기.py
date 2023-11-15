import sys
input = sys.stdin.readline

N = int(input())
dig_cost = [(i, -1, int(input())) for i in range(N)]

matrix = [tuple(map(int, input().split())) for _ in range(N)]

edge = sorted([(i, j, matrix[i][j]) for i in range(N)
               for j in range(i+1, N) if matrix[i][j]]+dig_cost, key=lambda x: x[2])


def findParent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = findParent(parent, parent[x])
    return parent[x]


def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [i for i in range(N+1)]

total = 0
for v1, v2, w in edge:
    if findParent(parent, v1) == findParent(parent, v2):
        continue
    unionParent(parent, v1, v2)
    total += w

print(total)
