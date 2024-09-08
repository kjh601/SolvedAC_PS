def solve(N):
    mul = 1
    for i in range(1, N+1):
        mul*=i
        while mul%10 == 0:
            mul//=10
        mul%=1000000000000
    mul%=100000
    return mul

print('%05d'%solve(int(input())))