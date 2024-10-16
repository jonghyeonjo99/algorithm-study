import heapq

n, m, k, x = map(int, input().split())

cities = [[] for _ in range(n + 1)]
distance = [int(1e10) for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    cities[a].append((b, 1))

def dijkstra(start):
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, city = heapq.heappop(queue)

        if distance[city] < dist:
            continue

        for next, cost in cities[city]:
            if distance[next] > dist + cost:
                distance[next] = dist + cost
                heapq.heappush(queue, (dist + cost, next))


result = []
dijkstra(x)

for i, d in enumerate(distance):
    if d == k:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    for i in result:
        print(i)
