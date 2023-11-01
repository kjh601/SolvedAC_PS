from functools import cmp_to_key

N = int(input())
nums = sorted(input().split(), key=cmp_to_key(
    lambda x, y: int(y+x) - int(x+y)))
if int(nums[0]):
    print(''.join(nums))
else:
    print(0)
