N, M = map(int, input().split())
M = min(M, N-M)

tmp1 = 1
tmp2 = 1
for _ in range(M):
    tmp1 *= N
    N -= 1
    tmp2 *= M
    M -= 1
print(tmp1//tmp2)
