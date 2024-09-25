from collections import deque

def solution(cards):
    answer = 0
    
    visited = [0 for _ in range(len(cards))]
    result = []
    for i in range(len(cards)):
        count = 0
        queue = deque()
        if visited[i] == 0:
            visited[i] = 1
            count += 1
            queue.append(cards[i])
        while queue:
            card = queue.popleft()
            if visited[card - 1] == 0:
                queue.append(cards[card-1])
                visited[card-1] = 1
                count += 1
        result.append(count)
            
    result.sort(reverse = True)
    
    answer = result[0] * result[1]
    
    
    return answer