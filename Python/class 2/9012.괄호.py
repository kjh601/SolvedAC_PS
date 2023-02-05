import sys

N = int(input())
for _ in range(N):
    arr = []
    line = sys.stdin.readline()[:-1]
    flag = True
    for ch in line:
        if ch == '(':
            arr.append(ch)
        elif ch == ')' :
            if arr and arr[-1] == '(':
                arr.pop()
            else:
                flag = False
                break
    if flag and not arr:
        print("YES")
    else :
        print("NO")
