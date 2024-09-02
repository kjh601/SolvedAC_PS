import sys
input = sys.stdin.readline

N, M = map(int, input().split())


def findParent(parent, x):
    if parent[x] == x:
        return parent[x]
    parent[x] = findParent(parent, parent[x])
    return parent[x]


def unionParent(parent, a, b):
    a = findParent(parent, parent[a])
    b = findParent(parent, parent[b])

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


edge = [tuple(map(int, input().split()))
        for _ in range(M+1)]

parent = [i for i in range(N+1)]
count1 = N
for v1, v2, w in sorted(edge, key=lambda x: x[2]):
    if findParent(parent, v1) == findParent(parent, v2):
        continue

    unionParent(parent, v1, v2)
    count1 -= w

parent = [i for i in range(N+1)]
count2 = N
for v1, v2, w in sorted(edge, key=lambda x: -x[2]):
    if findParent(parent, v1) == findParent(parent, v2):
        continue

    unionParent(parent, v1, v2)
    count2 -= w

print(count1**2 - count2**2)
