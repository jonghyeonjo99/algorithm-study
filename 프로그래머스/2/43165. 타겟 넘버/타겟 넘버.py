result = []
def solution(numbers, target):
    answer = 0
    plus_dfs(answer, numbers, 0)
    sub_dfs(answer, numbers, 0)
    count = 0
    for i in result:
        if i == target:
            count += 1
    return count

def plus_dfs(temp,numbers, i):
    global result
    temp += numbers[i]
    i += 1
    if i < len(numbers):
        plus_dfs(temp, numbers, i)
        sub_dfs(temp,numbers,i)
    else:
        result.append(temp)
    

def sub_dfs(temp, numbers, i):
    global result
    temp -= numbers[i]
    i += 1
    if i < len(numbers):
        plus_dfs(temp, numbers, i)
        sub_dfs(temp,numbers,i)
    else:
        result.append(temp)