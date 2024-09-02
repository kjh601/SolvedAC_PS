N = int(input())
DP = [0] + list(map(int,input().split()))

for i in range(N+1):
    for j in range(i+1):
        DP[i] = max(DP[i], DP[j]+DP[i-j])
print(DP[N])