def solution(nums):
    answer = 0
    length = len(nums)
    type = set(nums)
    if len(type) >= length // 2:
        answer = length // 2
    else:
        answer = len(type)
    
    return answer