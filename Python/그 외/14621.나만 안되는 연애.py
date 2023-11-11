N, M = map(int,input().split())

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

def is_all_connect(parent):
    a = findParent(parent, parent[0])
    for b in parent[1:]:
        if a != findParent(parent, parent[b]):
            return False
    return True

univ = input().split()

parent = [i for i in range(N)]

edge = sorted([tuple(map(int,input().split())) for _ in range(M)], key = lambda x : x[2])
total = 0
for v1, v2, w in edge:
    v1 -= 1
    v2 -= 1
    if univ[v1] == univ[v2]:
        continue
    if findParent(parent, v1) == findParent(parent, v2):
        continue
    
    unionParent(parent, v1, v2)
    total += w

if is_all_connect(parent):
    print(total)
else:
    print(-1)