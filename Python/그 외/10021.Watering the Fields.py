from heapq import heappush, heappop
from sys import stdin


def findParent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = findParent(parent, parent[x])
    return parent[x]


def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)

    if a == b:
        return False
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return True


N, C = map(int, stdin.readline().split())
node = []
for i in range(N):
    node.append(tuple(map(int, stdin.readline().split())))

edge = []
for i in range(N-1):
    for j in range(i+1, N):
        a, c = node[i]
        b, d = node[j]
        weight = (a-b)**2+(c-d)**2
        if weight < C:
            continue
        heappush(edge, (weight, i, j))

parent = [i for i in range(N)]
total = 0
count = 0
while edge and count < N-1:
    w, v1, v2 = heappop(edge)
    if not unionParent(parent, v1, v2):
        continue
    total += w
    count += 1

if count == N-1:
    print(total)
else:
    print(-1)
