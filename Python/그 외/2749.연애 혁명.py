import sys
input = sys.stdin.readline


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


N, M = map(int, input().split())

total = 0
edge = []
parent = [i for i in range(N+1)]
for _ in range(M):
    a, b, c, d = map(int, input().split())
    if d:
        unionParent(parent, a, b)
    else:
        edge.append((a, b, c))
        total += c

edge.sort(key=lambda x: -x[2])

for u, v, w in edge:
    if findParent(parent, u) == findParent(parent, v):
        continue

    unionParent(parent, u, v)
    total -= w

print(total)
