N = int(input())

if N % 10:
    print(-1)
else:
    A = 300
    B = 60
    C = 10

    print(N//A, end=' ')
    N %= A
    print(N//B, end=' ')
    N %= B
    print(N//C)
