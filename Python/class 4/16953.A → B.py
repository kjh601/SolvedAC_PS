from collections import deque


def bfs(start):
    curr = deque([start])
    left = deque()
    count = 1
    while curr:
        output = curr.popleft()
        if output == B:
            return count
        if output*2 <= B:
            left.append(output*2)
        if output*10+1 <= B:
            left.append(output*10+1)
        if not curr:
            curr = left
            left = deque()
            count += 1
    return -1


A, B = map(int, input().split())
print(bfs(A))
