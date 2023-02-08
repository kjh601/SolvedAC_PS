import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)
count = 0
for coin in coins:
    if coin > K:
        continue
    count += K//coin
    K %= coin
    
print(count)