def backtracking(st_idx):
    if len(ans) == M:
        print(' '.join(map(str, ans)))
    else:
        for i in range(N):
            if arr[i] not in ans:
                ans.append(arr[i])
                backtracking(i+1)
                ans.pop()


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []
backtracking(0)
