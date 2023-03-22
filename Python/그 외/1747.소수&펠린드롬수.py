N = int(input())

prime_nums = [2]


def is_prime_num(num):
    sqrt_num = num**0.5
    for prime_num in prime_nums:
        if prime_num > sqrt_num:
            return True
        if num % prime_num == 0:
            return False


def is_palindrome_num(num):
    string = str(num)
    length = len(string)//2
    for i in range(length):
        if string[i] != string[-1-i]:
            return False
    return True


for i in range(3, N, 2):
    if is_prime_num(i):
        prime_nums.append(i)

if N < 3:
    num = 2
else:
    if N % 2 == 0:
        num = N+1
    elif N == 1:
        num = 3
    else:
        num = N
    while True:
        if is_prime_num(num):
            if is_palindrome_num(num):
                break
            else:
                prime_nums.append(num)
        num += 2

print(num)
