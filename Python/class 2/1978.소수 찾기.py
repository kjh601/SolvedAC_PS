import math
t = int(input())
nums = list(map(int,input().split()))

count = 0
for num in nums:
    if num == 1:
        count+=1
    elif num!=2 and num%2==0:
        count+=1
    else : 
        for i in range(3,int(math.sqrt(num))+1,2):
            if num%i==0:
                count+=1
                break

print(t-count)