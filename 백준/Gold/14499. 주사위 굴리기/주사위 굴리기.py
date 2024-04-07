#주사위 굴리는게 아닌 굴리고나서 위치 변화를 리스트에 저장하는 로직 익히기

import sys

n,m,x,y,k = map(int,sys.stdin.readline().rstrip().split())
maps = []
for i in range(n):
    maps.append(list(map(int,sys.stdin.readline().rstrip().split())))
commands = list(map(int,sys.stdin.readline().rstrip().split()))

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

dice = [0 for _ in range(7)]

nx, ny = x,y
dice_surface_num = 1

#주사위 표면 번호 가져오기
def dice_surface(dice_surface_num,command):
    global dice
    if(dice_surface_num == 1):
        if(command == 1):
            dice_surface_num = 3
        elif(command == 2):
            dice_surface_num = 4
        elif(command == 3):
            dice_surface_num = 2
        elif(command == 4):
            dice_surface_num = 5
    elif(dice_surface_num == 2):
        if(command == 1):
            dice_surface_num = 3
        elif(command == 2):
            dice_surface_num = 4
        elif(command == 3):
            dice_surface_num = 6
        elif(command == 4):
            dice_surface_num = 1
    elif (dice_surface_num == 3):
        if (command == 1):
            dice_surface_num = 6
        elif (command == 2):
            dice_surface_num = 1
        elif (command == 3):
            dice_surface_num = 2
        elif (command == 4):
            dice_surface_num = 5
    elif (dice_surface_num == 4):
        if (command == 1):
            dice_surface_num = 1
        elif (command == 2):
            dice_surface_num = 6
        elif (command == 3):
            dice_surface_num = 2
        elif (command == 4):
            dice_surface_num = 5
    elif (dice_surface_num == 5):
        if (command == 1):
            dice_surface_num = 3
        elif (command == 2):
            dice_surface_num = 4
        elif (command == 3):
            dice_surface_num = 1
        elif (command == 4):
            dice_surface_num = 6
    elif (dice_surface_num == 6):
        if (command == 1):
            dice_surface_num = 3
        elif (command == 2):
            dice_surface_num = 4
        elif (command == 3):
            dice_surface_num = 5
        elif (command == 4):
            dice_surface_num = 2
    return dice_surface_num

#주사위 굴리기
def rolling_dice(command):
    global dice
    if(command == 1):
        dice[1],dice[2],dice[3],dice[4],dice[5],dice[6] = dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]
    elif(command == 2):
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]
    elif (command == 3):
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]
    elif (command == 4):
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]

#주사위 값과 지도 값 상호작용
def dice_maps_value(i,j,dice_surface_num):
    if(maps[i][j] == 0):
        maps[i][j] = dice[dice_surface_num]
    elif(maps[i][j] != 0):
        dice[dice_surface_num] = maps[i][j]
        maps[i][j] = 0

#주사위 윗면에 쓰여있는 수
def upper_dicenum(dice_surface_num):
    global dice
    result = 0
    if(dice_surface_num == 1):
        result = dice[6]
    elif(dice_surface_num == 2):
        result = dice[5]
    elif (dice_surface_num == 3):
        result = dice[4]
    elif (dice_surface_num == 4):
        result = dice[3]
    elif (dice_surface_num == 5):
        result = dice[2]
    elif (dice_surface_num == 6):
        result = dice[1]
    return result

for comand in commands:
    temp_x, temp_y = nx, ny
    nx = nx + dx[comand]
    ny = ny + dy[comand]
    if(0 <= nx < n and 0 <= ny < m):
        # next_dice_surface_num = dice_surface(dice_surface_num,comand)
        # dice_maps_value(nx,ny,next_dice_surface_num)
        # print(upper_dicenum(next_dice_surface_num))
        # dice_surface_num = next_dice_surface_num
        rolling_dice(comand)
        if(maps[nx][ny] == 0):
            maps[nx][ny] = dice[6]
        else:
            dice[6] = maps[nx][ny]
            maps[nx][ny] = 0
        print(dice[1])
    else:
        nx, ny = temp_x, temp_y
