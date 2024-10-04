from collections import deque

INF = 1e9

def bfs(gragh, visited):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    queue = deque()
    queue.append((0,0))
    visited[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(gragh) and 0 <= ny < len(gragh[0]) and gragh[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))
    if visited[len(gragh)-1][len(gragh[0])-1] != 0:
        return visited[len(gragh)-1][len(gragh[0])-1]
    else:
        return -1

def solution(maps):
    answer = 0
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    answer = bfs(maps, visited)
    print(visited)

    return answer