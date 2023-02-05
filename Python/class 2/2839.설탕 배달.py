N = int(input())

def min(a,b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a < b :
        return a
    else:
        return b

arr = [0 for _ in range(N+6)]
arr[3] = 1
arr[5] = 1
for i in range(N-2):
    if arr[i]>0:
        arr[i+3] = min(arr[i+3],arr[i]+1)
        arr[i+5] = min(arr[i+5],arr[i]+1)
if arr[N]==0:
    print(-1)
else:
    print(arr[N])