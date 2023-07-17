N = int(input())
prev = [1,0]
for i in range(1,N):
    curr = [0,0]
    curr[0] = (prev[0] + prev[1])%10
    curr[1] = prev[0]
    prev = curr
print(sum(prev)%10)