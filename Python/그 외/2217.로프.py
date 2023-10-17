import sys

N = int(input())
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort()

sys.stdout.write(str(max(arr[i]*(N-i) for i in range(N))))
