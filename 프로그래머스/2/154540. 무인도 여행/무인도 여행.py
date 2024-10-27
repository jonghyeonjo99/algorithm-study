from collections import deque

def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    
    visited = [[0 for _ in range(m)] for _ in range(n)]
    
    def bfs(x, y, visited):
        food = 0
        
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        
        queue = deque()
        queue.append((x,y))
        visited[x][y] = 1
        while queue:
            x, y = queue.popleft()
            food += int(maps[x][y])
            # print(food)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X':
                    if visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        queue.append((nx,ny))
                        
        return food
    for i in range(n):
        for j in range(m):
            # print(maps[i][j])
            if visited[i][j] == 0 and maps[i][j] != 'X':
                temp = bfs(i, j, visited)
                # print(temp)
                answer.append(temp)
    
    if len(answer) > 0:
        answer.sort()
        return answer
    else:
        return [-1]
                    