import sys

# n, m = map(int, sys.stdin.readline().split())
#
# board = []
# for i in range(n):
#     board.append(list(map(int, sys.stdin.readline().split())))
#
# dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
#
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + board[i-1][j-1]
#
# for i in range(m):
#     x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
#     result = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
#     print(result)

n, m = map(int, sys.stdin.readline().split())

board = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    dp[i][0] = board[i][0]
    for j in range(1, n):
        dp[i][j] = dp[i][j - 1] + board[i][j]

for i in range(n):
    for j in range(1, n):
        dp[j][i] = dp[j - 1][i] + dp[j][i]

for i in range(m):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    if x1 != 1 and y1 != 1:
        result = dp[x2 - 1][y2 - 1] - dp[x2 - 1][y1 - 2] - dp[x1 - 2][y2 - 1] + dp[x1 - 2][y1 - 2]
    elif x1 == 1 and y1 != 1:
        result = dp[x2 - 1][y2 - 1] - dp[x2 - 1][y1 - 2]
    elif x1 != 1 and y1 == 1:
        result = dp[x2 - 1][y2 - 1] - dp[x1 - 2][y2 - 1]
    else:
        result = dp[x2 - 1][y2 - 1]
    print(result)