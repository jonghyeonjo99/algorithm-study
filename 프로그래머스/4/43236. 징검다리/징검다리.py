from collections import deque

def solution(distance, rocks, n):
    answer = 0
    start = 0
    end = 1000000001
    rocks.sort()
    queue = deque(rocks)
    queue.appendleft(0)
    queue.append(distance)
    # print(queue)
    while start <= end:
        # 지점 사이 거리
        mid = (start + end) // 2
        count = 0
        pre = queue[0]
        temp = 1000000001
        for i in range(1,len(queue)):
            cur = queue[i]
            if cur - pre < mid:
                count += 1
            elif cur - pre >= mid:
                temp = min(temp, cur-pre)
                pre = queue[i]
        if count > n:
            end = mid - 1
        elif count <= n:
            start = mid + 1
            answer = temp
            
    return answer