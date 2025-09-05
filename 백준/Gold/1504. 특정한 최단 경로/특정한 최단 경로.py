import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
    dist = [INF] * (n + 1)
    dist[start] = 0
    q = [(0, start)]
    while q:
        cost, now = heapq.heappop(q)
        if dist[now] < cost:
            continue
        for nxt, nxt_cost in graph[now]:
            temp = cost + nxt_cost
            if temp < dist[nxt]:
                dist[nxt] = temp
                heapq.heappush(q, (temp, nxt))
    return dist

dist1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

path1 = dist1[v1] + dist_v1[v2] + dist_v2[n]
path2 = dist1[v2] + dist_v2[v1] + dist_v1[n]

ans = min(path1, path2)

print(ans if ans < INF else -1)
