N = int(input())
arr = list(map(int,input().split()))
arr.sort()
num = arr[0]
diff = 0
for i in range(1,N):
    diff += abs(num-arr[i])
min_diff = diff
min_num = arr[0]
for i in range(1,N):
    diff += abs(arr[i-1]-arr[i])*(i-N+i)
    if min_diff > diff:
        min_diff = diff
        min_num = arr[i]
print(min_num)