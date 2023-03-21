N = input()

for num in sorted(list(set(map(int, input().split())))):
    print(num, end=' ')
