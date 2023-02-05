"""달팽이는 올라가고 싶다"""
A, B, V = map(int, input().split())

day = (V - A)//(A-B)
left_dist = A+(V - A)%(A-B)
if left_dist>A :
    day += 2
else :
    day += 1
print(day)
