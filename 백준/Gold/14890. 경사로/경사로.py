import sys
import copy

n,l = map(int,sys.stdin.readline().split())

board = []
for i in range(n):
    board.append(list(map(int,sys.stdin.readline().split())))

def cross_road(arr,l):
    length = 1
    load_info = []
    for i in range(1,len(arr)):
        if (abs(arr[i-1] - arr[i]) > 0):
            load_info.append((arr[i-1],length))
            length = 0
        length += 1
    load_info.append((arr[-1],length))

    visited = [0 for _ in range(len(load_info))]

    if(len(load_info)==1):
        return 1

    for i in range(len(load_info)-1):
        if(abs(load_info[i][0] - load_info[i+1][0]) >= 2):
            return 0
        if(load_info[i][0] - load_info[i+1][0] == -1):
            if(load_info[i][1] >= l):
                visited[i] += 1
            else:
                return 0
        elif(load_info[i][0] - load_info[i+1][0] == 1):
            if(load_info[i+1][1] >= l):
                visited[i+1] += 1
            else:
                return 0

    for i in range(len(visited)):
        if((visited[i] * l) > load_info[i][1]):
            return 0

    return 1


road = 0
for i in range(n):

    road_list = []
    for j in range(n):
        road_list.append(board[i][j])

    road += cross_road(road_list,l)

for i in range(n):
    road_list = []
    for j in range(n):
        road_list.append(board[j][i])
    road += cross_road(road_list,l)

print(road)