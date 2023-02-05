"""최대공약수와 최소공배수"""
def euclidean(a, b) :
    """재귀함수로 구현한 유클리드 호제법으로 최대공약수 구하기"""
    r = b%a
    if r == 0 :
        return a
    return gcd(r, a)

arr = list(map(int,input().split()))
arr.sort()
b,a = arr

gcd = euclidean(a,b)
print(gcd)

lcd = a*b//gcd
print(lcd)