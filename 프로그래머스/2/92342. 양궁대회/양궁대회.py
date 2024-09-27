from itertools import combinations_with_replacement

def solution(n, info):
    
    max_result = [ -1 for _ in range(12)]
    for comb in combinations_with_replacement(range(11), n):
        cur = [0 for _ in range(12)]
        for c in comb:
            cur[10-c] += 1
        
        for i in range(11):
            # 라이언의 화살 수가 더 많을 때
            if cur[i] > info[i]:
                cur[-1] += 10 - i
            
            # 어피치의 화살 수가 더 많을 때
            elif info[i] != 0:
                cur[-1] -= 10 - i
        
        # 라이언의 점수가 어피치보다 낮다
        if cur[-1] <= 0:
            continue
        
        # 라이언의 점수가 더 높고, 점수 차이 최대값 갱신
        if cur[::-1] > max_result[::-1]:
            max_result = cur
            
    return [-1] if max_result[-1] <= 0 else max_result[:-1]