S = input()

countK = 0
countP = 0

for ch in S:
    if ch == 'K':
        if countP>0:
            countP-=1
        countK+=1
        
    if ch == 'P':
        if countK>0:
            countK-=1
        countP+=1
            
print(countK+countP)