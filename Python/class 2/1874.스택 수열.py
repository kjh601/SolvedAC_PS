import sys
input = sys.stdin.readline

n = int(input())
stack = list()
cmds = list()
flag = True
k = 1
for _ in range(n):
    num = int(input())
    while k<=num:
        stack.append(k)
        cmds.append('+')
        k+=1
    result = stack.pop()
    cmds.append('-')
    if result != num:
        flag = False
        break
if flag:
    print('\n'.join(cmds))
else:
    print('NO')