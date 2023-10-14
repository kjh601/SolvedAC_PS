x = int(input())
sticks = [64]
while sum(sticks) > x:
    smallest_stick = sticks.pop()
    half_stick = smallest_stick // 2
    sticks.append(half_stick)
    if sum(sticks) < x:
        sticks.append(half_stick)
print(len(sticks))
