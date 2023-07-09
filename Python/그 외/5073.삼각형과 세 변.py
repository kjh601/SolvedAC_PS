from sys import stdin

input = stdin.readline

result = []
while True:
    a, b, c = map(int, input().split())
    
    if a == 0 and b == 0 and c == 0:
        break
    
    if a >= b + c or b >= a + c or c >= a + b:
        result.append("Invalid\n")
    elif a == b and b == c:
        result.append("Equilateral\n")
    elif a == b or b == c or a == c:
        result.append("Isosceles\n")
    else:
        result.append("Scalene\n")

print("".join(result))
