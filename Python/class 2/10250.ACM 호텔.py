"""ACM 호텔"""
T = int(input())

for i in range(T):
    H,W,N = map(int, input().split())

    if N%H == 0 :
        floor = H*100
        house = N//H
    else :
        floor = N%H*100
        house = N//H+1

    print(floor+house)
