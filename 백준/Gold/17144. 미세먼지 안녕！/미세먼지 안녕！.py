import sys

r,c,t = map(int,sys.stdin.readline().split())

board = []
for i in range(r):
    board.append(list(map(int,sys.stdin.readline().split())))

#공기청정기 위치 저장
air_cleaner = []
for i in range(r):
    for j in range(c):
        if(board[i][j] == -1):
            air_cleaner.append([i,j])

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

#미세먼지 감소 함수
def microDust_reduce(x,y):
    count = 0
    reduce_value = board[x][y] // 5
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if(0<= nx < r and 0 <= ny < c):
            if(board[nx][ny] != -1):
                count += 1

    board[x][y] -= (reduce_value * count)
    reduce_spot_list.append((x,y))
    reduce_temp_list[x][y] = reduce_value

#미세먼지 확산 함수
def microDust_diffusion(x,y):
    diffusion_value = reduce_temp_list[x][y]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if( 0 <= nx < r and 0 <= ny < c):
            if(board[nx][ny] != -1):
                board[nx][ny] += diffusion_value

#공기청정기 시계방향 순환 함수
#공기청정기의 아래 좌표
def rotate_clockwise(x,y):
    dummy_1 = []
    dummy_2 = []
    dummy_3 = []
    dummy_4 = []

    #시계방향 value 저장
    for i in range(1,c-1):
        dummy_1.append(board[x][i])
    for i in range(x,r-1):
        dummy_2.append(board[i][c-1])
    for i in range(1,c):
        dummy_3.append(board[r-1][i])
    for i in range(x+2,r):
        dummy_4.append(board[i][0])

    #시계방향 value 입력
    board[x][y+1] = 0
    for i in range(2,c):
        board[x][i] = dummy_1[i-2]
    for i in range(x+1,r):
        board[i][c-1] = dummy_2[i-x-1]
    for i in range(c-1):
        board[r-1][i] = dummy_3[i]
    for i in range(x+1,r-1):
        board[i][0] = dummy_4[i-x-1]


#공기청정기 반시계방향 순환 함수
#공기청정기의 위 좌표
def rotate_counter_clockwise(x,y):
    dummy_1 = []
    dummy_2 = []
    dummy_3 = []
    dummy_4 = []
    #반시계방향 value 저장
    for i in range(x):
        dummy_1.append(board[i][0])
    for i in range(y + 1, c - 1):
        dummy_2.append(board[x][i])
    for i in range(1, x + 1):
        dummy_3.append(board[i][c - 1])
    for i in range(1, c):
        dummy_4.append(board[0][i])
    
    #반시계방향 value 입력
    board[x][y+1] = 0
    for i in range(2,c):
        board[x][i] = dummy_2[i-2]
    for i in range(x):
        board[i][c-1] = dummy_3[i]
    for i in range(c-1):
        board[0][i] = dummy_4[i]
    for i in range(1,x):
        board[i][0] = dummy_1[i-1]

for _ in range(t):
    # 매초가 지나고 초기화가 필요하다 reduce_temp_list
    reduce_temp_list = [[0 for _ in range(c)] for _ in range(r)]
    reduce_spot_list = []
    for i in range(r):
        for j in range(c):
            if(board[i][j] > 0):
                microDust_reduce(i,j)

    for i, j in reduce_spot_list:
        microDust_diffusion(i,j)

    up_x, up_y = air_cleaner[0][0],air_cleaner[0][1]
    down_x, down_y = air_cleaner[1][0],air_cleaner[1][1]

    rotate_clockwise(down_x,down_y)
    rotate_counter_clockwise(up_x,up_y)

result = 0
for i in range(r):
    for j in range(c):
        if(board[i][j] != -1):
            result += board[i][j]

print(result)