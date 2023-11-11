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

T = int(input())
for _ in range(T):
    N, M = map(int,input().split())
    parent = [i for i in range(N)]
    edge = [tuple(map(int,input().split())) for _ in range(M)]
    
    count = 0
    for v1, v2 in edge:
        v1 -= 1
        v2 -= 1
        if findParent(parent, v1) == findParent(parent, v2):
            continue
        count += 1
        unionParent(parent, v1, v2)
    write(str(count)+'\n')