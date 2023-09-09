from collections import deque
import sys

input = sys.stdin.readline
result = []
arr = deque([])
N = int(input())
for _ in range(N):
    cmd = input().split()
    if cmd[0] == "1":
        arr.appendleft(cmd[1])
    elif cmd[0] == "2":
        arr.append(cmd[1])
    elif cmd[0] == "3":
        if arr:
            result.append(arr.popleft())
        else:
            result.append(-1)
    elif cmd[0] == "4":
        if arr:
            result.append(arr.pop())
        else:
            result.append(-1)
    elif cmd[0] == "5":
        result.append(len(arr))
    elif cmd[0] == "6":
        if arr:
            result.append(0)
        else:
            result.append(1)
    elif cmd[0] == "7":
        if arr:
            result.append(arr[0])
        else:
            result.append(-1)
    elif cmd[0] == "8":
        if arr:
            result.append(arr[-1])
        else:
            result.append(-1)
print('\n'.join(map(str,result)))