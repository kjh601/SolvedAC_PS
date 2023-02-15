from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    visited = set()
    queue = deque([start])
    result = 0
    while queue:
        output = queue.popleft()
        if output[0] in visited:
            continue
        visited.add(output[0])
        result += output[1]
        for node in matrix[output[0]]:
            queue.append((node,output[1]+1))

    return result

N,M = map(int,input().split())

matrix = [[]for _ in range(N+1)]
for _ in range(M):
    num1, num2 = map(int,input().split())
    matrix[num1].append(num2)
    matrix[num2].append(num1)

min_num = 100
for i in range(1,N+1):
    num = bfs((i,0))
    if num < min_num:
        min_num = num
        idx = i
print(idx)
