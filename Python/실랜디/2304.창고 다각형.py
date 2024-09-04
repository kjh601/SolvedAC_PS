from sys import stdin

input = stdin.readline
N = int(input())
sticks = [tuple(map(int,input().split())) for _ in range(N)]
sticks.sort(key=lambda x:x[0])
area = 0

i = 0
while i < N:
    flag = False
    for j in range(i+1,N):
        if sticks[i][1] < sticks[j][1]:
            width = sticks[j][0] - sticks[i][0]
            heigth = sticks[i][1]
            area += width*heigth
            i = j
            flag = True
            break
    if not flag:
        break
idx = i
sticks.reverse()        
i = 0
while i < N:
    flag = False
    for j in range(i+1,N):
        if sticks[i][1] < sticks[j][1]:
            width = sticks[i][0] - sticks[j][0]
            heigth = sticks[i][1]
            area += width*heigth
            i = j
            flag = True
            break
    if not flag:
        break
sticks.reverse()   
area += sticks[idx][1]*(sticks[N-i-1][0]-sticks[idx][0]+1)
print(area)
