from collections import deque
def bfs(start,end):
    queue = deque([start])
    visited = set()
    while queue :
        node = queue.popleft()
        if node[0] == end:
            return node[1]
        if  node[0] in visited:
            continue
        visited.add(node[0])
        for i in [(node[0]-1,node[1]+1),(node[0]+1,node[1]+1),(node[0]*2,node[1]+1)]:
            if 0<=i[0]<=K*2:
                queue.append(i)
    
N, K = map(int, input().split())
if K < N:
    print(N-K)
else :
    print(bfs((N,0),K))