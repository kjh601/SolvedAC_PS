N = int(input())

arr = sorted(list(map(int,input().split())))
sum = 0
for time in arr:
    sum += time*N
    N-=1
print(sum)