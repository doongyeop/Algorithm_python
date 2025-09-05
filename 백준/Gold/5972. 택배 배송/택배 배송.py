import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    dist[start] = 0
    q = [(0, start)]
    while q:
        cost, now = heapq.heappop(q)

        if dist[now] < cost: continue

        for next, next_cost in graph[now]:
            temp = cost + next_cost
            if temp < dist[next]:
                dist[next] = temp
                heapq.heappush(q, (temp, next))

dijkstra(1)
print(dist[n])
