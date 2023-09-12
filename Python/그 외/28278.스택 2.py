import sys
input = sys.stdin.readline

stack = []


def solve(cmd):
    if cmd[0] == "1":
        stack.append(cmd[1])
    elif cmd[0] == "2":
        if stack:
            return stack.pop()
        else:
            return "-1"
    elif cmd[0] == "3":
        return str(len(stack))
    elif cmd[0] == "4":
        if stack:
            return "0"
        else:
            return "1"
    elif cmd[0] == "5":
        if stack:
            return (stack[-1])
        else:
            return "-1"


result = []
for _ in range(int(input())):
    value = solve(input().split())
    if value:
        result.append(value)
print('\n'.join(result))
