from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = deque()
for _ in range(N):
    cmd = input().split()
    if cmd[0] == "push_front":
        arr.appendleft(cmd[1])
    elif cmd[0] == "push_back":
        arr.append(cmd[1])
    elif cmd[0] == "pop_front":
        if arr:
            print(arr.popleft())
        else :
            print(-1)
    elif cmd[0] == "pop_back":
        if arr:
            print(arr.pop())
        else :
            print(-1)
    elif cmd[0] == "size":
        print(len(arr))
    elif cmd[0] == "empty":
        if arr:
            print(0)
        else :
            print(1)
    elif cmd[0] == "front":
        if arr:
            print(arr[0])
        else :
            print(-1)
    elif cmd[0] == "back":
        if arr:
            print(arr[-1])
        else :
            print(-1)