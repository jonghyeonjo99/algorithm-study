from collections import deque

def bfs(x, y, land, visited, locate):
    m_list = set()
    queue = deque([(x,y)])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    count = 0
    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        m_list.add(y)
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(land) and 0 <= ny < len(land[0]):
                if land[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    m_list.add(ny)
                    queue.append((nx,ny))
                    
    m_list = list(m_list)
    for i in m_list:
        locate[i] += count
        
    return count
                    
def solution(land):
    answer = 0
    locate = [0 for _ in range(len(land[0]))]
    visited = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    for i in range(len(land[0])):
        for j in range(len(land)):
            if land[j][i] == 1 and visited[j][i] == 0:
                bfs(j, i, land, visited, locate)

    answer = max(locate)
    return answer