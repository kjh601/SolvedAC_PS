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


m = int(input())
matrix = [list(map(int, input().split())) for _ in range(m)]

edge = sorted([(i, j, matrix[i][j]) for i in range(m)
              for j in range(i+1, m)], key=lambda x: x[2])

parent = [i for i in range(m)]

total = 0
for v1, v2, w in edge:
    if findParent(parent, v1) == findParent(parent, v2):
        continue
    unionParent(parent, v1, v2)
    total += w

write(str(total))
