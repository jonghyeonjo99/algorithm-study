def solution(k, d):
    answer = 0
    
    for i in range(0,d+1,k):
        y = int((d**2 - i**2) ** 0.5)
        answer += y // k + 1
    
    return answer