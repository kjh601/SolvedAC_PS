import sys
input = sys.stdin.readline
output = sys.stdout.write
T = int(input())
for _ in range(T):
    state = False
    p = input().rstrip()
    n = int(input())
    arr = input().rstrip()
    nums = arr[1:-1].split(',')
    if nums[0] == '':
        nums = []
    st = 0
    ed = n-1
    for cmd in p:
        if cmd == 'R':
            tmp = st
            st = ed
            ed = tmp
            state = not state
        elif cmd == 'D':
            if not state and st <= ed:
                st += 1
            elif state and st >= ed:
                st -= 1
            else :
                state = 'error'
                break
                
    if state == 'error':
        output('error\n')
    elif state:
        if st < ed:
            output('[]\n')
            continue
        output('[')
        for i in range(st,ed,-1):
            output(nums[i]+',')
        output(nums[ed]+']\n')
    else :
        if st > ed:
            output('[]\n')
            continue
        output('[')
        for i in range(st,ed):
            output(nums[i]+',')
        output(nums[ed]+']\n')