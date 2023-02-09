X = int(input())

def min(a,b):
    if a==0: return b
    if b==0: return a
    if a<b : return a
    else : return b

dp = [0 for _ in range(X+1)]
for i in range(X,1,-1):
    dp[i-1] = min(dp[i-1],dp[i]+1)
    if i%3 == 0:
        dp[i//3] = min(dp[i//3],dp[i]+1)
    if i%2 == 0:
        dp[i//2] = min(dp[i//2],dp[i]+1)
print(dp[1])