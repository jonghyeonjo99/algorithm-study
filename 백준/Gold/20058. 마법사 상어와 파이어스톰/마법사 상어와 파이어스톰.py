import sys
from collections import deque

n,q = map(int,sys.stdin.readline().split())

board = []
for i in range(2**n):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))

step = list(map(int,sys.stdin.readline().rstrip().split())) #l단계

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

#얼음판 90도 회전
def rotate_board(divided_board,l):
    temp_board = [[0 for _ in range(2**l)] for _ in range(2**l)]
    for i in range(2**l):
        for j in range(2**l -1,-1,-1):
            temp_board[i][2**l-1-j] = divided_board[j][i]

    #temp_board에 회전된 value값을 다시 원래 divided_board에 옮기기
    for i in range(2**l):
        for j in range(2**l):
            divided_board[i][j] = temp_board[i][j]

    return divided_board

#얼음 녹는거 확인
def check_board(x,y):
    count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if(0 <= nx < 2**n and 0 <= ny < 2**n):
            if(board[nx][ny] > 0):
                count += 1
    if(count < 3 and board[x][y] != 0):
        return [x,y]


#한꺼번에 얼음 녹이기
def melting_ice(board):
    melting_list = []
    for i in range(2**n):
        for j in range(2**n):
            if(check_board(i,j) != None):
                melting_list.append(check_board(i,j))

    for x,y in melting_list:
        board[x][y] -= 1

#격자 나눈 후 각각의 작은 board  90도 회전
def divide_board(n,l):
    start_list = []
    for i in range(0,2**n,2**l):
        for j in range(0,2**n,2**l):
            start_list.append((i,j))

    for i,j in start_list:
        divided_board = [[0 for _ in range(2**l)] for _ in range(2**l)]
        for x in range(2**l):
            for y in range(2**l):
                divided_board[x][y] = board[i + x][j + y]

        divided_board = rotate_board(divided_board,l)

        for x in range(2**l):
            for y in range(2**l):
                board[i + x][j + y] = divided_board[x][y]

    return board

#남아있는 얼음의 합
def sum_ice(board):
    total_ice = 0
    for i in range(2**n):
        for j in range(2**n):
            total_ice += board[i][j]

    return total_ice

#남아있는 얼음 중 가장 큰 덩어리 크기
ice_size_list = set()
def dfs(x,y,count):
    global ice_size_list
    #ice_size max값 가져오기
    ice_size_list.add(count)
    board[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if(0 <= nx < 2**n and 0 <= ny < 2**n):
            if(board[nx][ny] > 0):
                board[nx][ny] = 0
                dfs(nx,ny,count + 1)

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    count = 0
    while queue:
        x,y = queue.popleft()
        board[x][y] = 0
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0 <= nx < 2**n and 0 <= ny < 2**n):
                if(board[nx][ny] > 0):
                    queue.append((nx,ny))
                    board[nx][ny] = 0
    return count

#파이어스톰 횟수만큼 진행
for l in step:
    #2**l 크기로 얼음판 나누고 90도 회전
    board = divide_board(n,l)
    #얼음 녹이기
    melting_ice(board)

#최종 board의 얼음의 합
total_ice = sum_ice(board)

flag = 0
temp_list = []
for i in range(2**n):
    for j in range(2**n):
        if(board[i][j] > 0):
            flag = 1
            result = bfs(i,j)
            ice_size_list.add(result)
            temp_list.append(result)


# ice_size = max(ice_size_list)
temp_list.sort()
if(len(temp_list) != 0):
    ice_size = temp_list[-1]

if flag == 0:
    ice_size = 0

print(total_ice)
print(ice_size)
