def solution(s):
    answer = True
    
    start = 0
    end = 0
    for i in range(len(s)):
        if s[i] == "(":
            start += 1
        else:
            end += 1
        if end > start:
            return False
    if start != end:
        return False

    return True