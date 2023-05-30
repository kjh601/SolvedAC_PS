import sys
input = sys.stdin.readline
grade_points = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

total_credits = 0.0
weighted_grade_points = 0.0

for _ in range(20):
    subject, credit, grade = input().split()
    credit = float(credit)

    if grade == 'P':
        continue

    total_credits += credit
    weighted_grade_points += grade_points[grade] * credit

if total_credits == 0.0:
    print('0.000000')
else:
    major_GPA = weighted_grade_points / total_credits
    print('{:.6f}'.format(major_GPA))
