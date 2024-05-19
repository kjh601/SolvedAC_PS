from collections import deque
N = int(input())

arr = deque()
for i in range(N,0,-1):
    arr.append(i)
    for _ in range(i):
        arr.append(arr.popleft())
print(' '.join(map(str,reversed(arr))))