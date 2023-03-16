# print(pow(*map(int, input().split())))

def pow(base, exp, mod):
    num = base*base % mod
    if exp == 1:
        return base % mod
    elif exp % 2 == 0:
        return pow(num, exp//2, mod) % mod
    else:
        return pow(num, exp//2, mod)*base % mod


print(pow(*map(int, input().split())))
