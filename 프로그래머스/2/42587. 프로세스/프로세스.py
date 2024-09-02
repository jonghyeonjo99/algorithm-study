from collections import deque


def solution(priorities, location):
    answer = 0
    queue = deque()
    for i in range(len(priorities)):
        queue.append((priorities[i], i))
    #print(queue)
    result = []
    while queue:
        pri, idx = queue.popleft()
        flag = True
        for i in range(len(queue)):
            if pri < queue[i][0]:
                queue.append((pri, idx))
                flag = False
                break
        if flag:
            result.append(idx)
    
    answer = result.index(location) + 1
            
    return answer