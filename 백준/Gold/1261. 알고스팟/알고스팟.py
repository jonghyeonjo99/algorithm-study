import heapq

m, n = map(int, input().split())

board = []
for i in range(n):
    temp = []
    line = input()
    for j in line:
        temp.append(int(j))
    board.append(temp)


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
distance = [[int(1e9) for _ in range(m)] for _ in range(n)]
def dijkstra():
    queue = []
    heapq.heappush(queue, (0, 0, 0))
    distance[0][0] = 0

    while queue:
        cost, x, y = heapq.heappop(queue)

        if cost > distance[x][y]:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if cost + board[nx][ny] < distance[nx][ny]:
                    distance[nx][ny] = cost + board[nx][ny]
                    heapq.heappush(queue,(distance[nx][ny], nx, ny))


    return distance

dijkstra()
print(distance[n-1][m-1])
