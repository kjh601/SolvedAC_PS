N = int(input())
arr = list(map(int, input().split()))
arr.sort()

arr_sum = [0]*N
arr_sum[0] = arr[0]
for i in range(1, N):
    arr_sum[i] = arr[i]+arr_sum[i-1]

result = 0

for i in range(N):
    result += (arr[i]*(arr_sum[-1]-arr_sum[i])) % 1000000007

print(result % 1000000007)
