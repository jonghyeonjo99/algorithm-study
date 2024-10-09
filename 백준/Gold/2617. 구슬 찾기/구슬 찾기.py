
n, m = map(int, input().split())

INF = float('inf')
gragh = [[float('inf') for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            gragh[i][j] = 0

for i in range(m):
    a, b = map(int, input().split())
    gragh[a-1][b-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            gragh[i][j] = min(gragh[i][j], (gragh[i][k] + gragh[k][j]))

# print(gragh)
answer = 0

for i in range(n):
    max_count = 0
    min_count = 0 
    for j in range(n):
        if gragh[i][j] < INF and i != j:
            max_count += 1
        if gragh[j][i] < INF and i != j:
            min_count += 1

    if max_count >= (n + 1) // 2 or min_count >= (n + 1) // 2:
        answer += 1


print(answer)
