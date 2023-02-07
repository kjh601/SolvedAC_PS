import sys
input = sys.stdin.readline

N = int(input())
S = set()
all_S = set(i for i in range(1,21))
for _ in range(N):
    cmds = input().split()
    if len(cmds) == 2:
        cmds[1] = int(cmds[1])
    if cmds[0] == 'add':
        S.add(cmds[1])
    elif cmds[0] == 'remove':
        S.discard(cmds[1])
    elif cmds[0] == 'check':
        print(1 if cmds[1] in S else 0)
    elif cmds[0] == 'toggle':
        if cmds[1] in S:
            S.discard(cmds[1])
        else :
            S.add(cmds[1])
    elif cmds[0] == 'all':
        S = all_S
    elif cmds[0] == 'empty':
        S = set()
