N, M = map(int,input().split())
arr = list(map(int,input().split()))

count = 0
i = 0
j = 0
total = arr[0]
while True:
    if total == M:
        count += 1
        
    if i == j or total < M:
        j += 1
        if j >= N:
            break
        total += arr[j]
    else:
        total -= arr[i]
        i += 1
        

print(count)