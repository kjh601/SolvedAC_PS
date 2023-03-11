from collections import Counter
import sys
input = sys.stdin.readline

def backtracking():
    if len(arr) == M:
        sys.stdout.write(' '.join(map(str,arr))+'\n')
    else :
        for num in nums_keys:
            if nums[num] == 0:
                continue
            arr.append(num)
            nums[num] -= 1
            backtracking()
            nums[num] += 1
            arr.pop()
          

N, M = map(int,input().split())
nums = Counter(list(map(int,input().split())))
nums_keys = sorted(nums.keys())
arr = []
backtracking()
