from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    idxA, idxB = n-1, n-1
    count = 0
    while idxA>-1:
        target = b[idxB]
        while idxA>=0 and target < a[idxA]:
            idxA -= 1
            count += 1
        idxB -= 1
        idxA -= 1
        
    print(count)