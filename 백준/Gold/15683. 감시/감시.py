#함수 사이 리스트를 가져다 쓰는데,
#어떤 형식으로 넘어가는지 유심히 살펴볼 필요가 있다.

import copy
INF = int(1e9)

# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
direction = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[0, 2], [2, 1], [1, 3], [3, 0]],
             [[3, 0, 2], [1, 3, 0], [0, 2, 1], [2, 1, 3]], [[0, 1, 2, 3]]]

#여기서 direction에 들어가는 리스트는 cctv종류에 따른 한번에 볼 수 있는 방향이다.abs
#즉 위의 direction 2차배열의 안쪽 리스트라고 할 수 있다.  
def watch(y, x, direction, tmp):
    for d in direction:
        nx = x
        ny = y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx >= 0 and nx < m and ny >= 0 and ny < n and tmp[ny][nx] != 6:
                if tmp[ny][nx] == 0:
                    tmp[ny][nx] = '#'
            else:
                break

def dfs(office, cnt):
    global ans

    tmp = copy.deepcopy(office)
    #모든 cctv를 다 살펴봤다면, 최솟값을 업데이트
    if cnt == cctv_cnt:
        c = 0
        for i in tmp:
            c += i.count(0)
        ans = min(ans, c)
        return
    y, x, cctv = q[cnt]
    for i in direction[cctv]:
        watch(y, x, i, tmp)
        dfs(tmp, cnt + 1)
        tmp = copy.deepcopy(office)

n, m = map(int, input().split())
office = []
cctv_cnt = 0
q = []
ans = INF
for i in range(n):
    input_data = list(map(int, input().split()))
    office.append(input_data)
    for j in range(len(input_data)):
        if input_data[j] != 0 and input_data[j] != 6:
            cctv_cnt += 1
            #q에 cctv의 좌표와 번호(종류)를 저장한다.
            q.append([i, j, input_data[j]])

dfs(office, 0)
print(ans)