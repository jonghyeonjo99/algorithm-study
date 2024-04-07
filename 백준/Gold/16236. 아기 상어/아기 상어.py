import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

board = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

x,y,size = 0,0,2
for i in range(n):
    for j in range(n):
        if(board[i][j] == 9):
            x = i
            y = j

def eatFish(x,y,shark_size):
    distance = [[0 for _ in range(n)] for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    eatableFish = []
    while queue:
        cur_x,cur_y = queue.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if(board[nx][ny] <= shark_size):
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[cur_x][cur_y] + 1
                    if(board[nx][ny] < shark_size and board[nx][ny] != 0):
                        eatableFish.append((nx,ny,distance[nx][ny]))

    return sorted(eatableFish, key=lambda x: (-x[2],-x[0],-x[1]))

cnt = 0
result = 0
while(True):
    fish_list = eatFish(x,y,size)

    if(len(fish_list) == 0):
        break

    nx,ny,dist = fish_list.pop()

    result += dist
    board[x][y], board[nx][ny] = 0,0
    x,y = nx,ny
    cnt += 1
    if(cnt == size):
        size += 1
        cnt = 0
print(result)
