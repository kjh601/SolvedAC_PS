days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

week_days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

x, y = map(int, input().split())
total_days = sum(days_in_month[:x]) + y

day_of_week = week_days[total_days % 7]

print(day_of_week)
