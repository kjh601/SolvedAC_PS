import sys
input = sys.stdin.readline

N = int(input())

max_dp = [0,0,0]
min_dp = [0,0,0]

for i in range(N):
    x, y, z = list(map(int,input().split()))

    max_0 = x+max(max_dp[:2])
    max_1 = y+max(max_dp)
    max_2 = z+max(max_dp[1:])
    max_dp = [max_0, max_1, max_2]

    min_0 = x+min(min_dp[:2])
    min_1 = y+min(min_dp)
    min_2 = z+min(min_dp[1:])
    min_dp = [min_0, min_1, min_2]

print(max(max_dp), min(min_dp))
