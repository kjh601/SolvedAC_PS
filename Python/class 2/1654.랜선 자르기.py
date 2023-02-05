import sys
input = sys.stdin.readline

def count_LAN_lines(length):
    count = 0
    for line in lines:
        count += line//length
    return count
count = 0

def binary_search(head, rear, goal):
    mid = (head+rear)//2
    result = 0
    
    while head < mid:
        count = count_LAN_lines(mid)
        if goal > count:
            rear = mid
        else:
            result = max(result,mid)
            head = mid
        mid = (head+rear)//2
    return result


K, N = map(int,input().split())
lines = [int(input()) for _ in range(K)]
lines.sort()
print(binary_search(0,lines[-1]+1,N))