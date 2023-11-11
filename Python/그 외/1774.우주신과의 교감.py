import sys
input = sys.stdin.readline

N,M = map(int,input().split())

def calDistance(v1, v2):
    if (v1+1,v2+1) in connectVertex or (v2+1, v1+1) in connectVertex:
        return 0
    return ((vertex[v1][0]-vertex[v2][0])**2 + (vertex[v1][1] - vertex[v2][1])**2)**0.5

vertex = [tuple(map(int,input().split())) for _ in range(N)]

connectVertex = {tuple(map(int,input().split())) for _ in range(M)}

edge = sorted([(i,j,calDistance(i, j)) for i in range(N) for j in range(i+1, N)], key=lambda x:x[2])

parent = [i for i in range(N)]

def findParent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, v1, v2):
    v1 = findParent(parent, v1)
    v2 = findParent(parent, v2)
    
    if v1 < v2:
        parent[v2] = v1
    else :
        parent[v1] = v2

total = 0
for v1, v2, w in edge:
    v1 -= 1
    v2 -= 1
    if findParent(parent, v1) == findParent(parent, v2):
        continue
    unionParent(parent, v1, v2)
    total += w
print('{:.2f}'.format(total))