N = int(input())
arr = set()
for _ in range(N):
    name, cmd = input().split()
    if cmd == "enter":
        arr.add(name)
    elif cmd == "leave":
        arr.remove(name)
print('\n'.join(sorted(list(arr), reverse=True)))