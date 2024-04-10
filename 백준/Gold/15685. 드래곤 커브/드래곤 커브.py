import sys

n = int(sys.stdin.readline().rstrip())

curves =[]
for i in range(n):
    curves.append(list(map(int, sys.stdin.readline().rstrip().split())))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
board = [[0 for _ in range(101)] for _ in range(101)]

#0세대 드래곤 커브
def init_curve(x,y,d):
    nx = x + dx[d]
    ny = y + dy[d]
    nd = (d+1) % 4
    return (nx, ny, nd)

#n세대 드래곤 커브
def draw_curve(curve_list):

    x, y = curve_list[-1][0], curve_list[-1][1]

    for i in range(len(curve_list)-1,0,-1):
        direction = curve_list[i][2]
        nx = x + dx[direction]
        ny = y + dy[direction]
        curve_list.append((nx,ny,(direction+1)%4))
        x,y = nx,ny

    return curve_list

#격자에 드래곤 커브 그리기
def draw_board(curve_list):
    for x,y,d in curve_list:
        board[x][y] += 1

#꼭짓점 모두 드래곤 커브의 일부인 개수세기
def check_board(board):
    result = 0
    for i in range(100):
        for j in range(100):
            count = 0
            for k in range(2):
                for l in range(2):
                    if board[i+k][j+l] > 0:
                        count += 1
            if(count == 4):
                result += 1
    return result

for x,y,d,g in curves:
    curve_list = [(x,y,d)]
    n_x, n_y, n_d = init_curve(x,y,d)
    curve_list.append((n_x,n_y,n_d))

    for i in range(g):
        curve_list = draw_curve(curve_list)

    draw_board(curve_list)

print(check_board(board))


