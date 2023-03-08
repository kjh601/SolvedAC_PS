def backtracking(st_idx):
    if len(ans) == M:
        print(' '.join(map(str, ans)))
    else:
        for i in range(st_idx, N):
            ans.append(arr[i])
            backtracking(i)
            ans.pop()


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []
backtracking(0)
