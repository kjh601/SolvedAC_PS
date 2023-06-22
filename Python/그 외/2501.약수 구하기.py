N, K = map(int,input().split())

tmp = K
idx = 0 
while idx <= N and tmp:
    idx += 1
    if N%idx == 0:
        tmp -= 1
if tmp == 0:
    print(idx)
else :
    print(0)