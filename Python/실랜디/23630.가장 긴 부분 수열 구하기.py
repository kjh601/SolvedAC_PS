from math import log2

def solution(N, A):
    max_num = max(A)
    dp = [0]*(max_num+1)
    for num in A:
        dp[num] += 1
    for i in range(max_num, 0, -1):
        base = 2**int(log2(i))
        dp[base] += dp[i]
        dp[i-base] += dp[i]
    return max(dp[1:])//2

N = int(input())
A = list(map(int,input().split()))
print(solution(N,A))
