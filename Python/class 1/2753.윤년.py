year = int(input())
print(int((year%4==0 and not(year%100==0)) or year%400==0))