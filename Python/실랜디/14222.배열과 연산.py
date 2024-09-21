N, K = map(int,input().split())
A = list(map(int,input().split()))
B = [0] * 100

for num in A:
    B[num] += 1

def solve(N,K,B):
    for i in range(1, N+1):
        if B[i] > 1:
            tmp = B[i]-1
            B[i+K] += tmp
            B[i] -= tmp
        elif B[i] > 0:
            continue
        else:
            return 0
    return 1

print(solve(N,K,B))