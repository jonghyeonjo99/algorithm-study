import heapq

n, m, k = map(int, input().split())

cities = [[] for _ in range(n)]
for i in range(m):
    u, v, c = map(int, input().split())
    # cities[u - 1].append((v - 1, c))
    # 방향을 바꿈
    cities[v - 1].append((u - 1, c))

interview = list(map(int, input().split()))


def dijkstra():  # start는 면접장
    queue = []
    for j in interview:
        heapq.heappush(queue, (0, j-1))
        distance[j-1] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if dist > distance[now]:
            continue

        for next, cost in cities[now]:
            if distance[next] > dist + cost:
                distance[next] = dist + cost
                heapq.heappush(queue, (dist + cost, next))

distance = [int(1e11) for _ in range(n)]
dijkstra()

max_dist = 0
max_city = 0
for i, now_dist in enumerate(distance):
    if now_dist > max_dist and now_dist != int(1e11):
        max_dist = now_dist
        max_city = i + 1

print(max_city)
print(max_dist)