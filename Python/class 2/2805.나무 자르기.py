from collections import Counter

def sum_of_wood(length):
    sum = 0
    for height, num in trees.items():
        if height>length:
            sum+=(height-length)*num
    return sum

def binary_search(head, rear, goal):
    result = 0
    mid = (head+rear)//2

    while head < mid:
        if goal > sum_of_wood(mid):
            rear = mid
        else :
            head = mid
        mid = (head+rear)//2
    return mid
    
N,M = map(int,input().split())
trees = Counter(list(map(int,input().split())))
print(binary_search(0,10**9+1, M))