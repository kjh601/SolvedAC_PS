import sys
input = sys.stdin.readline

def check_available(dist):
    last = arr[0]
    count = 1
    for i in range(1, N):
        if arr[i] >= last+dist:
            count += 1
            last = arr[i]
    if count < C:
        return False
    else :
        return True
        


def upper_bound():
    left = 1
    right = arr[-1] - arr[0]
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if check_available(mid):
            left = mid + 1
            result = mid
        else :
            right = mid - 1
    return result

N, C = map(int,input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
print(upper_bound())