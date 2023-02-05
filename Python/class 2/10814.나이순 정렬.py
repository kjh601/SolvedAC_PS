import sys

N = int(sys.stdin.readline())
people = list()

for _ in range(N):
    age, name = sys.stdin.readline().split()
    people.append((int(age),name))

people.sort(key=lambda x : x[0])

for person in people:
    sys.stdout.write(str(person[0])+' '+person[1]+'\n')