import sys
input = sys.stdin.readline
write = sys.stdout.write

T = int(input())


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


def solve():
    N, M, p, q = map(int, input().split())
    parent = [i for i in range(N+1)]
    edge = sorted([tuple(map(int, input().split()))
                  for _ in range(M)], key=lambda x: x[2])

    is_connect = False
    for u, v, w in edge:
        if findParent(parent, u) == findParent(parent, v):
            continue

        if {u, v} == {p, q}:
            is_connect = True
        unionParent(parent, u, v)

    if is_connect:
        write("YES\n")
    else:
        write("NO\n")


for _ in range(T):
    solve()
