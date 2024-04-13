import sys
import heapq

n = int(sys.stdin.readline().rstrip())

board = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

# visited = [[0 for _ in range(n)] for _ in range(n)]
dx = [1, 1]
dy = [-1, 1]

#x,y,d1,d2 구하기 함수
#(x,y,d1,d2) 리스트 리턴
def init(n):
    init_list = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    if(i + k + l > n-1):
                        continue
                    if(j + l > n-1):
                        continue
                    if(j - k < 0):
                        continue
                    # max_x = i + k + l
                    # max_y = j + l - k
                    # if(0 <= max_x < n and 0 <= max_y < n):
                    init_list.append((i,j,k,l))
    return init_list

#init_list를 돌면서 모든 선거구 나누기 경우의 수를 탐색
#하나의 x,y,d1,d2가 정해졌을 때,
#5번 구역이 그려진 visited 리턴
def section_5(x,y,d1,d2):
    visited[x][y] = 5
    temp_x, temp_y = x,y
    #1번 라인
    for i in range(d1):
        nx = x + dx[0]
        ny = y + dy[0]
        visited[nx][ny] = 5
        x,y = nx,ny
    #3번 라인
    for i in range(d2):
        nx = x + dx[1]
        ny = y + dy[1]
        visited[nx][ny] = 5
        x,y = nx,ny
    #2번 라인
    for i in range(d2):
        nx = temp_x + dx[1]
        ny = temp_y + dy[1]
        visited[nx][ny] = 5
        temp_x,temp_y = nx,ny
    #4번 라인
    for i in range(d1):
        nx = temp_x + dx[0]
        ny = temp_y + dy[0]
        visited[nx][ny] = 5
        temp_x,temp_y = nx,ny

    return visited

#전체 인구 수 세기
#전체 인구수 리턴
def all_population(board):
    all_count = 0
    for i in range(n):
        for j in range(n):
            all_count += board[i][j]
    return all_count

#구역별 인구수 세기
#구역별 인구수와 5번을 제외한 총인구수 리턴
def rest_section(x,y,d1,d2, visited):
    #구역 별 for문을 4개 만들어서 각각의 결과값을 저장(어디 구역의 인구수인지는 몰라도 됨)
    pop_list_min = []
    pop_list_max = []
    pop_count = 0
    all_pop_count = 0
    #1번 구역
    for i in range(x + d1):
        for j in range(y+1):
            if visited[i][j] == 5:
                break
            pop_count += board[i][j]
            all_pop_count += board[i][j]
    heapq.heappush(pop_list_min, pop_count)
    heapq.heappush(pop_list_max, -pop_count)
    # pop_list.append(pop_count)
    pop_count = 0
    #2번 구역 y 반대로
    for i in range(x+d2+1):
        for j in range(n-1,y,-1):
            if visited[i][j] == 5:
                break
            pop_count += board[i][j]
            all_pop_count += board[i][j]
    heapq.heappush(pop_list_min, pop_count)
    heapq.heappush(pop_list_max, -pop_count)
    # pop_list.append(pop_count)
    pop_count = 0
    #3번구역
    for i in range(x+d1,n):
        for j in range(y-d1+d2):
            if visited[i][j] == 5:
                break
            pop_count += board[i][j]
            all_pop_count += board[i][j]
    heapq.heappush(pop_list_min, pop_count)
    heapq.heappush(pop_list_max, -pop_count)
    # pop_list.append(pop_count)
    pop_count = 0
    #4번구역 y반대로
    for i in range(x+d2+1,n):
        for j in range(n-1, y-d1+d2-1, -1):
            if visited[i][j] == 5:
                break
            pop_count += board[i][j]
            all_pop_count += board[i][j]
    heapq.heappush(pop_list_min, pop_count)
    heapq.heappush(pop_list_max, -pop_count)
    # pop_list.append(pop_count)
    
    return pop_list_min, pop_list_max, all_pop_count

all_count = all_population(board)
init_list = init(n)
result = []
for x,y,d1,d2 in init_list:
    visited = [[0 for _ in range(n)] for _ in range(n)]

    section_5(x,y,d1,d2)
    pop_list_min, pop_list_max, all_pop_count = rest_section(x,y,d1,d2, visited)
    sec_5 = all_count - all_pop_count
    heapq.heappush(pop_list_min, sec_5)
    heapq.heappush(pop_list_max, -sec_5)

    min_pop = heapq.heappop(pop_list_min)
    max_pop = -(heapq.heappop(pop_list_max))
    heapq.heappush(result, (max_pop-min_pop))

print(heapq.heappop(result))