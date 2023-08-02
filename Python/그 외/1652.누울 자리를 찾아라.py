N = int(input())
nums = set(map(int,input().split()))

result = []

K = int(input())
for num in map(int,input().split()):
    if num in nums:
        result.append('1')
    else :
        result.append('0')

print(" ".join(result))