from collections import deque
import sys
input = sys.stdin.readline

left = deque(input().rstrip())
right = deque()

N = int(input())
for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'L':
        if not left:
            continue
        right.append(left.pop())
    elif cmd[0] == 'D':
        if not right:
            continue
        left.append(right.pop())
    elif cmd[0] == 'B':
        if not left:
            continue
        left.pop()
    elif cmd[0] == 'P':
        left.append(cmd[1])

print(''.join(left)+''.join(reversed(right)))
