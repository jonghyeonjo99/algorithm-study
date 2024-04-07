import sys
from collections import deque
#90도 회전 코드
#자료구조 deque사용 중요!

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
apple = []
for i in range(k):
    apple.append(list(map(int, sys.stdin.readline().split())))
l = int(sys.stdin.readline())
turn_list = []
for i in range(l):
    turn_list.append(list(sys.stdin.readline().split())) # X초는 int형이 아님 주의

board = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i, j in apple:
    board[i][j] = 1

dx, dy = 0, 1
head_dir = 1
#turn_list를 만났을 때 방향전환 결과 함수
def turn_head(head_dir,n_dir):
    if(head_dir == 1):
        if(n_dir == 'D'):
            head_dir = 4
            dx, dy = 1, 0
        elif(n_dir == 'L'):
            head_dir = 3
            dx, dy = -1, 0
    elif(head_dir == 2):
        if(n_dir == 'D'):
            head_dir = 3
            dx, dy = -1, 0
        elif(n_dir == 'L'):
            head_dir = 4
            dx, dy = 1, 0
    elif (head_dir == 3):
        if (n_dir == 'D'):
            head_dir = 1
            dx, dy = 0, 1
        elif (n_dir == 'L'):
            head_dir = 2
            dx, dy = 0, -1
    elif (head_dir == 4):
        if (n_dir == 'D'):
            head_dir = 2
            dx, dy = 0, -1
        elif (n_dir == 'L'):
            head_dir = 1
            dx, dy = 0, 1
    return head_dir, dx, dy

time = 0
def move(board,x,y):
    global time, dx, dy, head_dir, flag
    snake = deque()
    board[x][y] = 2
    snake.append((x,y))
    while(True):
        time += 1
        nx = x + dx
        ny = y + dy
        x, y = nx, ny

        # 게임이 끝나는 조건
        if (nx < 1 or nx > n or ny < 1 or ny > n or board[nx][ny] == 2):
            break

        # 사과를 만났을 때
        if (board[nx][ny] == 0):
            del_x, del_y = snake.popleft()
            board[del_x][del_y] = 0
            snake.append((nx, ny))
            board[nx][ny] = 2
        elif (board[nx][ny] == 1):
            board[nx][ny] = 2
            snake.append((nx, ny))

        #방향전환이 이뤄지는 타이밍
        for t, c in turn_list:
            if(int(t) == time):
                n_dir = c
                head_dir, dx, dy = turn_head(head_dir,n_dir)

    return time

print(move(board,1,1))