from collections import  deque

for test_case in range(1, 11):
    t, n = map(int, input().split())
    road = list(map(int, input().split()))

    board = [[] for _ in range(100)]
    visited = [0 for _ in range(100)]
    for i in range(0, len(road)):
        if i % 2 == 0:
            board[road[i]].append(road[i + 1])

    # print(board)

    def bfs():
        queue = deque()
        queue.append(0)
        visited[0] = 1
        while queue:
            node = queue.popleft()
            if node == 99:
                return 1
            for n_node in board[node]:
                if visited[n_node] == 0:
                    queue.append(n_node)
                    visited[n_node] = 1

        return 0
    print("#%d %d" % (t, bfs()))