def solution(friends, gifts):
    
    #1. 2차 딕셔너리
    dictionary = {person : {friend : 0 for friend in friends}for person in friends}
    #2. 딕셔너리로 이름:인덱스 맵핑 테이블 / 준 선물 수는 이차원 배열로
    
    #선물지수
    giftScore = {person : 0 for person in friends}
    
    
    for gift in gifts:
        giver, reciever = gift.split()
        dictionary[giver][reciever] += 1
        giftScore[giver] += 1
        giftScore[reciever] -= 1
    
    
    next_gift = {person : 0 for person in friends}
    
    for personA in friends:
        for personB in friends:
            if personA == personB:
                continue
            if dictionary[personA][personB] > dictionary[personB][personA]:
                next_gift[personA] += 1
            elif dictionary[personA][personB] == dictionary[personB][personA] and giftScore[personA] > giftScore[personB]:
                next_gift[personA] += 1
                
    answer = sorted(next_gift.items(), key=lambda x:-x[1])[0][1]
            
    return answer