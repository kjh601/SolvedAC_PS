def gcd(a, b):
    while (b != 0):
        n = a % b
        a = b
        b = n
    return a


def lcm(a, b):
    return int(a*b/gcd(a, b))


print(lcm(*map(int, input().split())))
