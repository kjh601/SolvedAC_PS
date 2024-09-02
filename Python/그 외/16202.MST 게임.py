import sys
input = sys.stdin.readline
write = sys.stdout.write

N, M, K = map(int, input().split())

edge = [list(map(int, input().split()))+[i]
        for i in range(1, M+1)]


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


def isAllConnect(parent):
    a = findParent(parent, 1)
    for i in range(2, N+1):
        if a != findParent(parent, i):
            return False
    return True


for i in range(K):
    parent = [j for j in range(N+1)]

    total = 0
    for v1, v2, w in edge[i:]:
        if findParent(parent, v1) == findParent(parent, v2):
            continue
        unionParent(parent, v1, v2)
        total += w

    if isAllConnect(parent):
        write(str(total)+" ")
    else:
        write("0 ")
