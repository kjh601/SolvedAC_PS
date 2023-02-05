"""수 정렬하기"""
import sys

arr = [0 for i in range(10001)]

for i in range(int(sys.stdin.buffer.readline())):
    arr[int(sys.stdin.buffer.readline())]+=1

for i in range(10001):
    for j in range(arr[i]):
        sys.stdout.write(str(i)+'\n')
