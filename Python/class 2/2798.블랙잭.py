"""블랙잭"""
N,M = map(int,input().split())
cards = list(map(int,input().split()))

ans = 0
for pre in range(N-2):
    for mid in range(pre+1,N-1):
        for post in range(mid+1,N):
            sum = cards[pre]+cards[mid]+cards[post]
            if ans < sum <= M :
                ans = sum

print(ans)
