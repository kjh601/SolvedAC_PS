N, K = map(int, input().split())
arr = list(map(int, input().split()))

curr_sum = sum(arr[:K])
max_sum = curr_sum
for i in range(N-K):
    curr_sum -= arr[i]
    curr_sum += arr[K+i]
    max_sum = max(max_sum, curr_sum)
print(max_sum)
