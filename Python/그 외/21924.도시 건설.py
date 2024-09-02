import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edge = sorted([tuple(map(int, input().split()))
              for _ in range(M)], key=lambda x: x[2])


def findParent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = findParent(parent, parent[x])
    return parent[x]


def unionParent(parent, v1, v2):
    v1 = findParent(parent, v1)
    v2 = findParent(parent, v2)

    if v1 < v2:
        parent[v2] = v1
    else:
        parent[v1] = v2


def isConnect(parent):
    a = findParent(parent, 0)
    for b in parent:
        b = findParent(parent, b)
        if a != b:
            return False
    return True


parent = [i for i in range(N)]
total = sum(x[2] for x in edge)

for v1, v2, w in edge:
    v1 -= 1
    v2 -= 1
    if findParent(parent, v1) == findParent(parent, v2):
        continue
    unionParent(parent, v1, v2)
    total -= w

if isConnect(parent):
    print(total)
else:
    print(-1)
