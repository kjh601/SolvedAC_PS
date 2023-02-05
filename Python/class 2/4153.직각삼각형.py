"""직각삼각형"""
T = int(input())
for i in range(T):
    H,W,N = map(int,input().split())

    if N==H:
        num = H*100
        num += N//H+1
    else :
        num = (N%H)*100
        num += N//H

    print(num)
    