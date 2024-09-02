from  heapq import heappush
string = input()
length = len(string)
arr = []
for i in range(1, length-1):
    for j in range(i+1, length):
        arr.append(''.join(reversed(string[0:i]))+''.join(reversed(string[i:j]))+''.join(reversed(string[j:length])))
        arr = sorted(arr)
print(arr[0])