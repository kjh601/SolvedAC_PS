import sys
input = sys.stdin.readline


def backtracking(st):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
    else:
        for i in range(st, N):
            arr.append(nums[i])
            backtracking(i)
            arr.pop()


N, M = map(int, input().split())
nums = list(sorted(set(map(int, input().split()))))
N = len(nums)
arr = []
backtracking(0)
