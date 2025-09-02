import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
dist = [INF] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        cost, now = heapq.heappop(q)
        if dist[now] < cost:
            continue

        for next_city, next_cost in graph[now]:
            total_cost = cost + next_cost
            if total_cost < dist[next_city]:
                dist[next_city] = total_cost
                heapq.heappush(q, (total_cost, next_city))

    return dist[end]



start, end = map(int, input().split())

print(dijkstra(start, end))