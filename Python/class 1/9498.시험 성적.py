grades = 'ABCDF'
score = int(input())

std = 89
for grade in grades:
    if grade == 'F':
        print('F')
        break
    if score>std:
        print(grade)
        break
    std-=10