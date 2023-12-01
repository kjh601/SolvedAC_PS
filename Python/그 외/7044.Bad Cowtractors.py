import sys
input = sys.stdin.readline

N, M = map(int, input().split())


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, u, v):
    u = find(parent, u)
    v = find(parent, v)

    if u < v:
        parent[v] = u
    else:
        parent[u] = v


edge = sorted([tuple(map(int, input().split()))
              for _ in range(M)], key=lambda x: -x[2])
parent = [i for i in range(N+1)]
total = 0
count = 0
for u, v, w in edge:
    if find(parent, u) == find(parent, v):
        continue

    union(parent, u, v)
    total += w
    count += 1

if count == N-1:
    print(total)
else:
    print(-1)
