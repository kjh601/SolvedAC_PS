E = 15
S = 28
M = 19

e, s, m = map(int, input().split())
year = 0
while year % E != e-1 or year % S != s-1 or year % M != m-1:
    year += 1
print(year+1)
