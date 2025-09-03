import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
reverse_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    reverse_graph[b].append((a, t))


def dijkstra(start, graph):
    dist = [INF] * (n + 1)
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
    return dist


dist_from_x = dijkstra(x, graph)
dist_to_x = dijkstra(x, reverse_graph)

answer = 0
for i in range(1, n + 1):
    temp = dist_to_x[i] + dist_from_x[i]
    answer = max(answer, temp)

print(answer)
