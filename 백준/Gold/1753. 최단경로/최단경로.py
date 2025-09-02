import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

V, e = map(int, input().split())
K = int(input()) # start

graph = [[] for _ in range(V + 1)]
dist = [INF] * (V + 1)

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue

        for i in graph[now]:
            cost = d + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(K)

for i in range(1, V + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])

