import sys
input = sys.stdin.readline
write = sys.stdout.write


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def edge_maker(R, C):
    edge = []
    node_num = 0
    for _ in range(R):
        weight = list(map(int, input().split()))

        for w in weight:
            edge.append((node_num, node_num+1, w))
            node_num += 1
        node_num += 1

    node_num = 0
    for _ in range(R-1):
        weight = list(map(int, input().split()))
        for w in weight:
            edge.append((node_num, node_num+C, w))
            node_num += 1

    edge.sort(key=lambda x: x[2])
    return edge


def solve():
    R, C = map(int, input().split())
    edge = edge_maker(R, C)
    parent = [i for i in range(R*C)]

    total = 0
    for u, v, w in edge:
        if find(parent, u) == find(parent, v):
            continue

        union(parent, u, v)
        total += w
    write(str(total)+'\n')


T = int(input())
for _ in range(T):
    solve()
