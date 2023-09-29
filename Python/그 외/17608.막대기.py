import sys
input = sys.stdin.readline

stack = []
N = int(input())
arr = [int(input()) for _ in range(N)]
for l in arr:
    while True:
        if stack:
            if l < stack[-1]:
                stack.append(l)
                break
            else:
                stack.pop()
                continue
        else:
            stack.append(l)
            break
            
print(len(stack))