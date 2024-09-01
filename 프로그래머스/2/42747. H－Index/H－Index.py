def solution(citations):
    answer = 0
    citations.sort()
    for i in range(1001):
        temp = 0
        for j in range(len(citations)):
            if i <= citations[j]:
                temp += 1
        if temp >= i:
            answer = max(answer, i)
    return answer