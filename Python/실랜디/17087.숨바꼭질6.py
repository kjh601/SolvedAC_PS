def gcd(a, b):
    while b!= 0:
        r = a%b
        a = b
        b = r
    return abs(a)

N, S = map(int,input().split())
arr = list(map(int,input().split()))

max_value = arr[0] - S
for num in arr[1:]:
    max_value = gcd(max_value, num - S)
print(max_value)