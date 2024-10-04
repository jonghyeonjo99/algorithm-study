from collections import deque

dx = [1, 0]
dy = [0, 1]

def bfs(gragh, visited):
    queue = deque()
    queue.append((0,0))
    visited[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < len(gragh) and 0<= ny < len(gragh[0]):
                if visited[nx][ny] == 0 and gragh[nx][ny] == 0:
                    visited[nx][ny] = visited[nx][ny-1] + visited[nx-1][ny]
                    queue.append((nx, ny))

    print(visited)
            
    return visited[len(gragh)-1][len(gragh[0]) - 1]

def solution(m, n, puddles):
    answer = 0
    gragh = [[0 for _ in range(n)] for _ in range(m)]
    visited = [[0 for _ in range(n)] for _ in range(m)]
    for i, j in puddles:
        gragh[i-1][j-1] = 1
    answer = bfs(gragh, visited) % 1000000007
    return answer