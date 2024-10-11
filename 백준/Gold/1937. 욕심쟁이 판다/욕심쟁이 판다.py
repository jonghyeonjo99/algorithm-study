n = int(input())

bamboo = []
for i in range(n):
    bamboo.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
steps = [[0 for _ in range(n)] for _ in range(n)]

def dfs(x, y):

    if steps[x][y]: return steps[x][y]
    steps[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or bamboo[nx][ny] <= bamboo[x][y]:
            continue
        else:
            steps[x][y] = max(steps[x][y], dfs(nx, ny) + 1)
    return steps[x][y]

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))

print(answer)