# O(N^2)
N = int(input())
arr = list(map(int,input().split()))
for i in range(N):
    x = arr[i]
    arr[i] = [x, 1] # [현재 위치의 값, 나보다 작은 값 중에서 횟수가 가장 큰 값, 횟수]
for i in range(N):
    for j in range(i):
        if arr[i][0] <= arr[j][0]:
            continue
        if arr[i][1] > arr[j][1]:
            continue
        arr[i][1] = arr[j][1]+1
        
result = 0
for i in range(N):
    result = max(result, arr[i][1])
print(result)

# O(NlogN)
# 추후에...