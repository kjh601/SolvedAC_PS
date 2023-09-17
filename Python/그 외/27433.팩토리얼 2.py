def fac(N):
    if N == 0:
        return 1
    else:
        return N*fac(N-1)


print(fac(int(input())))
