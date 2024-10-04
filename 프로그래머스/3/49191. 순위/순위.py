def solution(n, results):
    answer = 0
    gragh = [[0] * n for _ in range(n)]
    for winner, loser in results:
        gragh[winner-1][loser-1] = 1
        gragh[loser-1][winner-1] = -1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if gragh[i][k] == 1 and gragh[k][j] == 1:
                    gragh[i][j] = 1
                if gragh[i][k] == -1 and gragh[k][j] == -1:
                    gragh[i][j] = -1
    for i in range(n):
        if sum(1 for j in range(n) if gragh[i][j] != 0) == n-1:
            answer += 1
    return answer