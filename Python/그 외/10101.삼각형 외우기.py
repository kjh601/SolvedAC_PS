angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

def triangle_type(a, b, c):
    if a + b + c != 180:
        return 'Error'
    elif a == b == c:
        return 'Equilateral'
    elif a == b or b == c or a == c:
        return 'Isosceles'
    else:
        return 'Scalene'

print(triangle_type(angle1, angle2, angle3))
