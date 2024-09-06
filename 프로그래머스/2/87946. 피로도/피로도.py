from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    per_dungeons = permutations(dungeons, len(dungeons))
    
    for dungeon in per_dungeons:
        count = 0
        now_k = k
        #print(dungeon)
        for min_need, spend in dungeon:
            #print(now_k)
            if now_k >= min_need:
                count += 1
                now_k -= spend
            else:
                break
        answer = max(count, answer) 
                
    return answer