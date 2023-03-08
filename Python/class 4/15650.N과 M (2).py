import sys
write = sys.stdout.write


def backtracking(st):
    if len(arr) == M:
        print(" ".join(map(str, arr)))
        return
    for i in range(st, N+1):
        arr.append(i)
        backtracking(i+1)
        arr.pop()


N, M = map(int, input().split())
arr = []
backtracking(1)
