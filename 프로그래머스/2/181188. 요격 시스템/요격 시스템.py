def solution(targets):
    answer = 0
    targets = sorted(targets)
    # print(targets)
    count = 1
    temp = 10 ** 8
    for i in range(len(targets) - 1):
        s = targets[i][0]
        e = targets[i][1]
        temp = min(temp, e)
        if temp > targets[i+1][0]:
            temp = min(temp, targets[i+1][1])
        else:
            count += 1
            temp = targets[i+1][1]
    # print(count)
    answer = count     
    return answer