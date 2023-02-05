nums = map(int,input().split())

sum = 0
for num in nums:
    sum += num**2
print(sum%10)