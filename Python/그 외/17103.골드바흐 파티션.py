import sys
write = sys.stdout.write
input = sys.stdin.readline

MAX_NUM = 1000000
is_prime = [1]*(MAX_NUM+1)
is_prime[0] = 0
is_prime[1] = 0


is_prime[4::2] = [0]*((MAX_NUM-4)//2+1)
for i in range(3, int(MAX_NUM**0.5)+1, 2):
    is_prime[i*i::i*2] = [0]*((MAX_NUM-i*i)//(i*2)+1)

primes = [2] + [i for i in range(3, MAX_NUM, 2) if is_prime[i]]

T = int(input())
for _ in range(T):
    N = int(input())
    count = 0
    for prime in primes:
        if prime*2 > N:
            break
        if is_prime[N-prime]:
            count += 1
    write(str(count)+'\n')
