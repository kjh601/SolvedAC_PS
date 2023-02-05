"""부녀회장이 될테야"""
T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())

    apartment = [[] for i in range(k+1)]
    apartment[0] = [x for x in range(0,n+1)]
    for floor in range(1,k+1):
        apartment[floor] = [sum(apartment[floor-1][1:i+1]) for i in range(n+1)]
    print(apartment[k][n])
