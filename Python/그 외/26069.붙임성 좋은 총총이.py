import sys
input = sys.stdin.readline

N = int(input())

rainbow_dance = set(["ChongChong"])

for _ in range(N):
    person1, person2 = input().split()
    if person1 in rainbow_dance:
        rainbow_dance.add(person2)
    elif person2 in rainbow_dance:
        rainbow_dance.add(person1)

print(len(rainbow_dance))
