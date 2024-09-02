import sys
input = sys.stdin.readline

n, m = map(int, input().split())
connected_edge = [tuple(map(int, input().split())) for _ in range(m)]
matrix = [list(map(int, input().split())) for _ in range(n)]

edge = sorted([(i, j, matrix[i][j]) for i in range(1, n-1)
              for j in range(i+1, n)], key=lambda x: x[2])


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


parent = [i for i in range(n)]
for v1, v2 in connected_edge:
    unionParent(parent, v1-1, v2-1)

total = 0
new_edge = []
for v1, v2, w in edge:
    if findParent(parent, v1) == findParent(parent, v2):
        continue

    unionParent(parent, v1, v2)
    total += w
    new_edge.append((v1, v2))

print(total, len(new_edge))
for v1, v2 in new_edge:
    print(v1+1, v2+1)
