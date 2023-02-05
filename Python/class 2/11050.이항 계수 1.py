"""이항 계수 1"""

N, K = map(int,input().split())
K = min(N-K, K)

tmp1 = 1
tmp2 = 1
for count in range(1,K+1):
    tmp1 *= N
    N -= 1
    tmp2 *= count

print(int(tmp1/tmp2))
