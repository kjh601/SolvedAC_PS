def solution(bandage, health, attacks):
    
    roll_time, heal_per_second, add_heal = bandage
    cur_health = health
    left_count = roll_time
    
    nxt = 0
    for cur_time in range(attacks[-1][0]+1):
        if attacks[nxt][0] == cur_time:
            damage = attacks[nxt][1]
            nxt += 1
            cur_health -= damage
            left_count = roll_time
            if cur_health <=0:
                return -1
        
        else:
            cur_health = min(health, cur_health+heal_per_second)
            left_count -= 1
            if left_count == 0:
                cur_health = min(health, cur_health+add_heal)
                left_count = roll_time
        
        print(cur_health)
        
    return cur_health