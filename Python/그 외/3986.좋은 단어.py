import sys
input = sys.stdin.readline

count = 0
for _ in range(int(input())):
    stack = ['C']

    for ch in input().rstrip():
        if stack[-1] == ch:
            stack.pop()
            continue
        stack.append(ch)

    if stack == ['C']:
        count += 1

print(count)
