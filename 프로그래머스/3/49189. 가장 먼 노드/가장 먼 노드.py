from collections import deque

def solution(n, edge):
    answer = 0
    visited = [0 for _ in range(n)]
    gragh = [[] for _ in range(n)]
    for a, b in edge:
        gragh[a-1].append(b-1)
        gragh[b-1].append(a-1)
    
    # print(gragh)
    
    queue = deque()
    for i in gragh[0]:
        queue.append(i)
        visited[i] = 1
    # print(queue)
    
    while queue:
        node = queue.popleft()
        for i in gragh[node]:
            if visited[i] == 0 and i != 0:
                visited[i] += visited[node] + 1
                queue.append(i)
    
     # print(visited)
    max_num = max(visited)
    answer = visited.count(max_num)
                
    return answer