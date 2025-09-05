import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
dist = [INF] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

ans = []


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

dijkstra(X)

for idx, d in enumerate(dist):
    if d == K:
        ans.append(idx)

ans.sort()

if len(ans) == 0:
    print(-1)
else:
    print("\n".join(map(str, ans)))
