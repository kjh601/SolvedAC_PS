N = int(input())


def generate_primes(n):
    primes = [False, False] + [True] * (n-1)
    for current in range(2, int(n**0.5) + 1):
        if primes[current]:
            for multiple in range(current*current, n+1, current):
                primes[multiple] = False
    return [x for x in range(2, n+1) if primes[x]]


prime_nums = generate_primes(N)
length = len(prime_nums)
ptr1 = ptr2 = 0
num = count = 0

while ptr2 < length:
    num += prime_nums[ptr2]
    while num > N:
        num -= prime_nums[ptr1]
        ptr1 += 1
    if num == N:
        count += 1
    ptr2 += 1

print(count)
