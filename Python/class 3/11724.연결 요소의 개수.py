import sys
input = sys.stdin.readline

def dfs(start):
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited :
            continue
        visited.add(node)
        stack.extend(matrix[node])

N, M = map(int,input().split())
visited = set()
matrix = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int,input().split())
    matrix[u].append(v)
    matrix[v].append(u)

count = 0
for i in range(1,N+1):
    if i in visited:
        continue
    dfs(i)
    count += 1

print(count)