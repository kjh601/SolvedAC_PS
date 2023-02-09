from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int,input().split()))
    documents = deque([(i,arr[i]) for i in range(N)])
    sorted_arr = sorted(arr)

    count = 0
    while True:
        document = documents.popleft()
        if sorted_arr[-1] == document[1]:
            count+=1
            sorted_arr.pop()
            if document[0] == M:
                print(count)
                break
        else :
            documents.append(document)