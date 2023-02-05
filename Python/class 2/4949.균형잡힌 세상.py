import sys

while True:
    arr = []
    line = sys.stdin.readline()[:-1]
    flag = True
    if line == '.':
        break
    for ch in line:
        if ch in ('(','['):
            arr.append(ch)
        elif ch == ')' :
            if arr and arr[-1] == '(':
                arr.pop()
            else:
                flag = False
                break
        elif ch == ']':
            if arr and arr[-1] == '[':
                arr.pop()
            else:
                flag = False
                break
    if flag and not arr:
        print("yes")
    else :
        print("no")
