def solution(n):
    answer = 1
    for i in range(2,n+1):
        if (n - (i * (i-1) / 2)) <= 0:
            break
        elif (n - (i * (i-1) / 2)) % i == 0:
            # print(i)
            answer += 1
    return answer