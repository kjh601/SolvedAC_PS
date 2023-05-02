import sys
input = sys.stdin.readline
list = [0 for _ in range(31)]
for _ in range(28):
    list[int(input())] = 1

count = 0
for i in range(1, 31):
    if list[i] == 0:
        print(i)
        count += 1
    if count == 2:
        break
