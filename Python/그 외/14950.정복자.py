import sys
input = sys.stdin.readline

N, M, t = map(int, input().split())
edge = sorted([tuple(map(int, input().split()))
              for _ in range(M)], key=lambda x: x[2])


def findParent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = findParent(parent, parent[x])
    return parent[x]


def unionParent(parent, a, b):
    a = findParent(parent, parent[a])
    b = findParent(parent, parent[b])

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [i for i in range(N+1)]
total = 0
tmp = 0
for v1, v2, w in edge:
    if findParent(parent, v1) == findParent(parent, v2):
        continue
    unionParent(parent, v1, v2)
    total += w
print(total+t*(N-1)*(N-2)//2)
