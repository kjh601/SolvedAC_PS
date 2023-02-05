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
        if goal > count_LAN_lines(mid):
            rear = mid
        else:
            head = mid
        mid = (head+rear)//2
    return mid


K, N = map(int,input().split())
lines = [int(input()) for _ in range(K)]
print(binary_search(0,2**31,N))