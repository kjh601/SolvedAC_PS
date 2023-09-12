import sys
write = sys.stdout.write
N = int(input())
arr = list(map(int, input().split()))
nums = [(num+1, value) for num, value in enumerate(arr)]

idx = 0
value = 1
while nums:
    if value < 0:
        idx = (idx + value) % N
    else:
        idx = (idx + value - 1) % N

    num, value = nums.pop(idx)
    write(str(num)+' ')
    N -= 1
