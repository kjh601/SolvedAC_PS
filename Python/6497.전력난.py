import sys
input = sys.stdin.readline
write = sys.stdout.write


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


while (True):
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    edge = sorted([tuple(map(int, input().split()))
                   for _ in range(n)], key=lambda x: x[2])

    parent = [i for i in range(m)]

    total = sum(t[-1] for t in edge)
    for v1, v2, w in edge:
        v1 -= 1
        v2 -= 1
        if findParent(parent, v1) == findParent(parent, v2):
            continue
        unionParent(parent, v1, v2)
        total -= w

    write(str(total)+'\n')
