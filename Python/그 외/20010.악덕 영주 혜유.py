import sys
input = sys.stdin.readline


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


def findFarthestNode(graph, node):
    stack = [(node, 0)]
    visited = {node}
    farthest_node = node
    farthest_length = 0
    while stack:
        now, length = stack.pop()
        for vertex, w in graph[now]:
            if vertex in visited:
                continue

            newLength = length+w
            stack.append((vertex, newLength))
            visited.add(vertex)
            if farthest_length < newLength:
                farthest_length = newLength
                farthest_node = vertex
    return farthest_node, farthest_length


N, K = map(int, input().split())

parent = [i for i in range(N)]
edge = sorted([tuple(map(int, input().split()))
              for _ in range(K)], key=lambda x: x[2])

total = 0
graph = [[] for _ in range(N)]
for v1, v2, w in edge:
    if findParent(parent, v1) == findParent(parent, v2):
        continue

    unionParent(parent, v1, v2)
    total += w
    graph[v1].append((v2, w))
    graph[v2].append((v1, w))


print(total)
print(findFarthestNode(graph, findFarthestNode(graph, 0)[0])[1])
