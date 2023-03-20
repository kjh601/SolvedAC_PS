string1 = input().rstrip()
string2 = input().rstrip()

dp = [[0 for _ in string2+' '] for _ in string1+' ']

for i, ch1 in enumerate(string1, 1):
    for j, ch2 in enumerate(string2, 1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif ch1 == ch2:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
