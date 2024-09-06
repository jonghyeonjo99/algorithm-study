def solution(brown, yellow):
    answer = []
    total = brown + yellow
    temp = (brown + 4) // 2
    
    for i in range(1,(temp // 2 + 1)):
        if (temp - i) * i == total:
            if (temp - i) >= i:
                answer.append(temp - i)
                answer.append(i)
            else:
                answer.append(i)
                answer.append(temp - i)
    return answer