import sys
input = sys.stdin.readline

N,M = map(int,input().split())
nums = list(map(int,input().split()))
for i in range(1,N):
    nums[i] += nums[i-1]
for _ in range(M):
    st, ed = map(int,input().split())
    if st==1:
        print(nums[ed-1])
    else :
        print(nums[ed-1]-nums[st-2])