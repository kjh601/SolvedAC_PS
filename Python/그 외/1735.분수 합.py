prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
              79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173]


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a*b/gcd(a, b)


a, b = map(int, input().split())
c, d = map(int, input().split())

LCM = lcm(b, d)
numerator = a*(LCM/b) + c*(LCM/d)
print(int(numerator/gcd(LCM, numerator)), int(LCM/gcd(LCM, numerator)))
