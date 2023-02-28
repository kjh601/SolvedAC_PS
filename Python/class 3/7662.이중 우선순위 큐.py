from heapq import heappop, heappush
import sys
input = sys.stdin.readline
                
for _ in range(int(input())):
    max_heap = []
    min_heap = []
    max_visited = []
    min_visited = []
    for _ in range(int(input())):
        cmd, num = input().split()
        num = int(num)

        if cmd == 'I':
            heappush(min_heap, num)
            heappush(max_heap, -num)
        
        elif cmd=='D':
            if num == -1 and min_heap:
                result = heappop(min_heap)
                heappush(max_visited, -result)
            if num == 1 and max_heap:
                result = -heappop(max_heap)
                heappush(min_visited, result)
            while min_heap and min_visited:
                if min_heap[0] == min_visited[0]:
                    heappop(min_heap)
                    heappop(min_visited)
                else:
                    break
                    
            while max_heap and max_visited:
                if max_heap[0] == max_visited[0]:
                    heappop(max_heap)
                    heappop(max_visited)
                else :
                    break
    if min_heap:
        print(-max_heap[0], min_heap[0])
    else:
        print("EMPTY")