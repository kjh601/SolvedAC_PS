"""분해합"""
N = int(input())
for i in range(N - 9*len(str(N)),N):
    tmp = i
    total = tmp
    while tmp>0:
        total += tmp%10
        tmp//=10
    if total == N:
        tmp = i
        break
print(tmp)
